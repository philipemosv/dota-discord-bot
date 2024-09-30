# Dota 2 Discord Bot

This Discord bot allows Dota 2 players to get a quick summary of their performance, hero stats, and meta trends using the [STRATZ GraphQL API](https://stratz.com/graphql). Players can track their progress and hero usage directly within Discord.

## Features:
- **Win/Loss Tracking**: Retrieve the number of wins, losses, and win rate for a specified number of days (up to 30).
- **Hero Stats**: Display win/loss statistics for all heroes over a given period.
- **Meta Trends**: Show the 5 most picked heroes by position, or across all positions if no position is provided.
- **Database Integration**: Store player and match data for historical tracking.
- **Docker Support**: Easily deploy and run the bot in a Docker container.

## Technologies:
- **STRATZ GraphQL API**: Used to fetch Dota 2 match statistics.
- **Python**: The core language for the bot.
- **Discord.py**: For managing bot commands and interaction with Discord.
- **SQLite3**: Lightweight database used to store player and match data.
- **Docker**: Containerization for easy deployment and environment management.

## Setup:

1. Clone the repository:
   ```bash
   git clone https://github.com/philipemosv/dota-discord-bot.git

2. Install dependencies:
    ```bash
    pip install -r requirements.txt

3. Create a .env file with the following:
    ```bash
    DISCORD_TOKEN=your-discord-bot-token
    STRATZ_API_KEY=your-stratz-api-key

4. Run the bot
    ```bash
    python bot.py

5. Alternatively, build and run the bot using Docker:
    ```bash
    docker build -t dota-discord-bot .
    docker run --env-file .env dota-discord-bot

## Commands:
- `!commands`: List all the available commands for the bot.
- `!wl [days]`: Returns the number of wins, losses, and win rate over the last [days] days (up to a maximum of 30 days).
- `!stats [days]`: Displays win/loss statistics for all heroes played over the specified number of days.
- `!meta [position]`: Shows the 5 most picked heroes for the given position in the immortal rank over the last 7 days.
  


[![image](https://github.com/user-attachments/assets/8c70c598-84b0-4f59-9240-0ccd473026af)](https://stratz.com/)
