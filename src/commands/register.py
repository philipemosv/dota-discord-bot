import json
import os
from discord.ext import commands

MAPPINGS_FILE = 'mappings.json'

def load_mappings():
    if os.path.isfile(MAPPINGS_FILE):
        with open(MAPPINGS_FILE, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {} 
    return {}

def save_mappings(mappings):
    with open(MAPPINGS_FILE, 'w') as f:
        json.dump(mappings, f, indent=4)

user_dota_accounts = load_mappings()

class Register(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="register")
    async def register(self, ctx, account_id: int):
        discord_id = str(ctx.author.id)
        
        user_dota_accounts[discord_id] = account_id
        save_mappings(user_dota_accounts)
        
        await ctx.send(f"Registrada sua conta do Dota 2 com id: {account_id}")

async def setup(bot):
    await bot.add_cog(Register(bot))