from discord.ext import commands
from utils.stratz_api import get_player_win_loss
from database import db

class WinLoss(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="wl")
    async def win_loss(self, ctx, days: int = 0):
        """Show win/loss stats for a given period (days) up to 30 days."""
        discord_id = str(ctx.author.id)

        account_id = db.get_dota_account(discord_id)
        
        if not account_id: 
            await ctx.send(f"{ctx.author.mention}\nYour account is not registered yet.\nUse `!register <account_id>` to register.")
            return

        days = max(0, min(days, 30))

        try:
            performance = get_player_win_loss(account_id, days)
            
            response = self.build_response(ctx.author.mention, performance, days)

            await ctx.send(response)

        except Exception as e:
            await ctx.send(f"Error retrieving data: {e}")

    def build_response(self, mention, performance, days):
        """Builds a formatted response based on player performance data."""
        wins = performance['wins']
        losses = performance['losses']
        win_rate = performance['winrate']
        day = performance['day']

        period_text = f"Last {days} days" if days else f"Day {day}"
        balance = wins - losses

        return (
            f"{mention}\n"
            f"{period_text}: {wins} Wins | {losses} Losses | WinRate: {win_rate}%\n"
            f"Balance: {balance}"
        )


async def setup(bot):
    await bot.add_cog(WinLoss(bot))