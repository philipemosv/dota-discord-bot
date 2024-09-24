from discord.ext import commands
from utils.stratz_api import get_player_heroes_win_loss
from commands.register import user_dota_accounts


class Stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="stats")
    async def stats(self, ctx, days: int = 0):
        discord_id = str(ctx.author.id)

        if discord_id not in user_dota_accounts:
            await ctx.send(f"{ctx.author.mention}\nYour account is not registered yet.\nUse `!register <account_id>` to register.")
            return

        account_id = user_dota_accounts[discord_id]

        days = max(0, min(days, 30))

        try:
            heroes_summary = get_player_heroes_win_loss(account_id, days)

            response = self.build_response_message(ctx.author.mention, heroes_summary, days)

            await ctx.send(response)
        
        except Exception as e:
            await ctx.send(f"Error retrieving data: {e}")

    def build_response_message(self, mention, heroes_summary, days):
        """Builds the response message with hero stats."""
        if not heroes_summary:
            return f"{mention}\nNo stats available for this period!"

        period_text = f"{days} days" if days else "Today"

        response = f"{mention}```markdown\n"
        response += f"# Stats ({period_text})\n"
        response += f"Heroes: {len(heroes_summary)}\n\n"
        response += "| Hero               | TM | W  | L  |   WR    |\n"
        response += "|--------------------|----|----|----|---------|\n"

        sorted_heroes = sorted(heroes_summary.items(), key=lambda item: item[1]['Total Matches'], reverse=True)

        for hero, stats in sorted_heroes:
            response += f"| {hero:<18} | {stats['Total Matches']:>2} | {stats['Wins']:>2} | {stats['Losses']:>2} | {stats['Winrate']:>6.2f}% |\n"

        response += "```"
        return response


async def setup(bot):
    await bot.add_cog(Stats(bot))