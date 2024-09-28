from discord.ext import commands
from database import db

class Register(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="register")
    async def register(self, ctx, account_id: int):
        """Register the user's Dota 2 account ID."""
        discord_id = str(ctx.author.id)

        db.register_dota_account(discord_id, account_id)

        await ctx.send(f"{ctx.author.mention}, your Dota 2 account with ID: {account_id} has been registered.")


async def setup(bot):
    await bot.add_cog(Register(bot))