# Dota 2 Discord Bot using STRATZ GraphQL API

This Discord bot allows Dota 2 players to get a quick summary of their win/loss performance and win rate over a specific period using the [STRATZ GraphQL API](https://stratz.com/graphql). Players can request their performance statistics from the last few days directly within a Discord server, helping them track their recent progress.

## Features:
- **Win/Loss Tracking**: Get the number of wins, losses, and overall win rate for a specified number of days (up to 30 days).
- **Simple Command**: The bot offers a user-friendly command to retrieve your Dota 2 statistics quickly.

## Technologies:
- **Discord.py**: For interacting with Discord and managing bot commands.
- **STRATZ GraphQL API**: To query Dota 2 match statistics.
- **Python**: The core language used to build the bot.

## Setup:

1. Clone the repository:
   ```bash
   git clone https://github.com/philipemosv/dota-discord-bot

2. Install dependencies:
    pip install -r requirements.txt

3. Create a .env file with the following:
    DISCORD_TOKEN=your-discord-bot-token
    STRATZ_API_KEY=your-stratz-api-key

4. Run the bot
    python bot.py


Commands:
!wl [days]: This command returns the number of wins, losses, and win rate over the past
[days] days (up to a maximum of 30 days). For example:
!wl 7
This command will retrieve the win/loss record and win rate for the last 7 days.


Future Features:
More advanced stats like hero performance, specific match details, and rankings.
Additional commands for querying match history or hero performance.