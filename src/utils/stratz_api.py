import requests
import os
from datetime import datetime, timedelta, timezone
from collections import Counter

STRATZ_API_KEY = os.getenv('STRATZ_API_KEY')
STRATZ_URL = "https://api.stratz.com/graphql"


def make_query(query):
    """Send a GraphQL query to the Stratz API and return the response data."""
    headers = {"Authorization": f"Bearer {STRATZ_API_KEY}"}
    payload = {"query": query}
    response = requests.post(STRATZ_URL, json=payload, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API returned status code {response.status_code}")

def get_start_of_day(days=0):
    """Calculate the start of the day in Unix timestamp."""
    now_utc = datetime.now(timezone.utc)
    today_brt = now_utc.astimezone(timezone(timedelta(hours=-3)))
    delta_time = today_brt - timedelta(days=days)
    return int(datetime(delta_time.year, delta_time.month, delta_time.day, tzinfo=timezone(timedelta(hours=-3))).timestamp())

def fetch_matches(account_id, is_victory, start_of_day, game_mode='ALL_PICK_RANKED'):
    """Fetch matches for a given player based on victory status and date."""
    query = f"""
    query {{
        player(steamAccountId: {account_id}) {{
            matches(request: {{isVictory: {str(is_victory).lower()}, startDateTime: {start_of_day}, take: 100}}) {{
                gameMode
                startDateTime
            }}  
        }}
    }}"""
    
    data = make_query(query)
    return [
        match for match in data['data']['player']['matches']
        if match['startDateTime'] >= start_of_day and match['gameMode'] == game_mode
    ]

def calculate_win_loss(wins, losses):
    """Calculate win rate from win and loss counts."""
    total_games = wins + losses
    return round((wins / total_games) * 100, 2) if total_games > 0 else 0.0

def get_player_win_loss(account_id, days=0):
    """Get win/loss statistics for a player over a specified number of days."""
    start_of_day = get_start_of_day(days)
    wins = len(fetch_matches(account_id, is_victory=True, start_of_day=start_of_day))
    losses = len(fetch_matches(account_id, is_victory=False, start_of_day=start_of_day))
    win_rate = calculate_win_loss(wins, losses)

    if days != 0:
        return {'day': days, 'wins': wins, 'losses': losses, 'winrate': win_rate}

    now_utc = datetime.now(timezone.utc)
    today_brt = now_utc.astimezone(timezone(timedelta(hours=-3)))
    return {
        'day': f'{today_brt.day}/{today_brt.month}/{today_brt.year}',
        'wins': wins,
        'losses': losses,
        'winrate': win_rate
    }

def fetch_heroes_matches(account_id, is_victory, start_of_day, game_mode='ALL_PICK_RANKED'):
    """Fetch matches with hero details for a player."""
    query = f"""
    query {{
        player(steamAccountId: {account_id}) {{
            matches(request: {{isVictory: {str(is_victory).lower()}, startDateTime: {start_of_day}, take: 100}}) {{
                gameMode
                startDateTime
                players(steamAccountId: {account_id}) {{
                    hero {{
                        id
                        displayName
                    }}
                }}
            }}  
        }}
    }}"""
    
    data = make_query(query)
    return [
        match for match in data['data']['player']['matches']
        if match['startDateTime'] >= start_of_day and match['gameMode'] == game_mode
    ]

def get_player_heroes_win_loss(account_id, days=0):
    """Get win/loss statistics for heroes used by a player over a specified number of days."""
    start_of_day = get_start_of_day(days)
    heroes_win = fetch_heroes_matches(account_id, is_victory=True, start_of_day=start_of_day)
    heroes_losses = fetch_heroes_matches(account_id, is_victory=False, start_of_day=start_of_day)
    
    heroes_win_count = Counter()
    heroes_losses_count = Counter()

    for game in heroes_win:
        for player in game['players']:
            heroes_win_count[player['hero']['displayName']] += 1

    for game in heroes_losses:
        for player in game['players']:
            heroes_losses_count[player['hero']['displayName']] += 1

    heroes_summary = {}
    all_heroes = set(heroes_win_count.keys()).union(set(heroes_losses_count.keys()))

    for hero in all_heroes:
        wins = heroes_win_count[hero]
        losses = heroes_losses_count[hero]
        total_matches = wins + losses
        winrate = (wins / total_matches * 100) if total_matches > 0 else 0

        heroes_summary[hero] = {
            'Total Matches': total_matches,
            'Wins': wins,
            'Losses': losses,
            'Winrate': winrate
        }

    return heroes_summary

def get_top_heroes_by_matches(position):
    query = f"""
    {{
      heroStats {{
        winWeek(
          {"" if position == 0 else "positionIds: [POSITION_" + str(position) + "]"}
          bracketIds: IMMORTAL
          gameModeIds: [ALL_PICK_RANKED]
          take: 1
        ) {{
          heroId
          winCount
          matchCount
          durationMinute
        }}
      }}
    }}
    """
    
    data = make_query(query)
    
    heroes = data['data']['heroStats']['winWeek']
       
    sorted_heroes = sorted(heroes, key=lambda x: x['matchCount'], reverse=True)[:5]
    return sorted_heroes