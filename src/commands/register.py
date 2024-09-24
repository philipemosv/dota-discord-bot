import json
import os
from discord.ext import commands

MAPPINGS_FILE = 'mappings.json'

def load_mappings(file_path):
    """Load mappings from a JSON file."""
    if os.path.isfile(file_path):
        try:
            with open(file_path, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}
    return {}

def save_mappings(file_path, mappings):
    """Save mappings to a JSON file."""
    with open(file_path, 'w') as f:
        json.dump(mappings, f, indent=4)

user_dota_accounts = load_mappings(MAPPINGS_FILE)

class Register(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="register")
    async def register(self, ctx, account_id: int):
        """Register the user's Dota 2 account ID."""
        discord_id = str(ctx.author.id)

        user_dota_accounts[discord_id] = account_id
        save_mappings(MAPPINGS_FILE, user_dota_accounts)

        await ctx.send(f"{ctx.author.mention}, your Dota 2 account with ID: {account_id} has been registered.")

async def setup(bot):
    await bot.add_cog(Register(bot))