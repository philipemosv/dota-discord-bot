from discord.ext import commands
from utils.stratz_api import get_player_win_loss
from commands.register import user_dota_accounts


class WinLoss(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="wl")
    async def win_loss(self, ctx, days: int = 0):
        discord_id = str(ctx.author.id)

        if discord_id not in user_dota_accounts:
            await ctx.send(f"{ctx.author.mention}\nYour account is not registered yet.\nUse !register <account_id> to register.")
            return
        
        account_id = user_dota_accounts[discord_id]

        days = max(0, min(days, 30))

        try:
            performance = get_player_win_loss(account_id, days)
            wins = performance['wins']
            losses = performance['losses']
            win_rate = performance['winrate']
            day = performance['day']

            period_text = f"Last {day} days" if days else f"Day {day}"
            balance = wins - losses
            response = (
                f"{ctx.author.mention}\n"
                f"{period_text}: {wins} Wins | {losses} Losses | WinRate: {win_rate}%\n"
                f"Balance: {balance}"
            )
            await ctx.send(response)
            
        except Exception as e:
            await ctx.send(f"Erro ao retornar dados: {e}")


async def setup(bot):
    await bot.add_cog(WinLoss(bot))