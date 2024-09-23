import requests
import os
from datetime import datetime, timedelta, timezone

STRATZ_API_KEY = os.getenv('STRATZ_API_KEY')
STRATZ_URL = "https://api.stratz.com/graphql"


def make_query(query):
    headers = {"Authorization": f"Bearer {STRATZ_API_KEY}"}
    payload = {"query": query}
    response = requests.post(STRATZ_URL, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API returned status code {response.status_code}")
    

def fetch_matches(account_id, is_victory, start_of_day, game_mode='ALL_PICK_RANKED'):
    query = f"""
    query {{
        player(steamAccountId: {account_id}) {{
            matches(request: {{isVictory: {str(is_victory).lower()}, startDateTime: {start_of_day}, take: 100}}) {{
                gameMode
                startDateTime
            }}  
        }}
    }}
    """
    data = make_query(query)
    return [
        match for match in data['data']['player']['matches']
        if match['startDateTime'] >= start_of_day and match['gameMode'] == game_mode
    ]


def get_player_win_loss(account_id, days=0):
    now_utc = datetime.now(timezone.utc)
    today_brt = now_utc.astimezone(timezone(timedelta(hours=-3)))

    delta_time = today_brt - timedelta(days=days)
    start_of_day = int(datetime(delta_time.year, delta_time.month, delta_time.day).timestamp())

    wins = len(fetch_matches(account_id, is_victory=True, start_of_day=start_of_day))
    losses = len(fetch_matches(account_id, is_victory=False, start_of_day=start_of_day))

    total_games = wins + losses
    win_rate = round((wins / total_games) * 100, 2) if total_games > 0 else 0.0

    if days != 0:
        return {'day': days, 'wins': wins, 'losses': losses, 'winrate': win_rate}

    return {
        'day': f'{today_brt.day}/{today_brt.month}/{today_brt.year}',
        'wins': wins,
        'losses': losses,
        'winrate': win_rate
    }