from discord.ext import commands
from utils.stratz_api import get_top_heroes_by_matches
from utils.heroes import heroes

class Meta(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="meta")
    async def top_heroes(self, ctx, position: int = 0):
        """Show top 5 heroes with the most matches for a specified position (1-5)."""
        if position < 1 or position > 5:
            await ctx.send(f"{ctx.author.mention}\nPlease provide a valid position number (1-5).")
            return

        try:
            performance = get_top_heroes_by_matches(position)
            
            response = self.build_response(ctx.author.mention, performance, position)

            await ctx.send(response)

        except Exception as e:
            await ctx.send(f"Error retrieving data: {e}")

    def build_response(self, mention, performance, position):
        """Builds a formatted response based on top hero performance data."""
        if not performance:
            return f"{mention}\nNo data available for the requested position."

        response = f"{mention}```markdown\n"
        response += f"# META Position {position} (Last 7 days)\n"
        response += "| Hero               | Matches |   WR  |\n"
        response += "|--------------------|---------|-------|\n"
    
        for stat in performance:
            hero_name = self.get_hero_name(stat['heroId'])
            matches = stat['matchCount']
            wins = stat['winCount']
            win_rate = self.calculate_win_rate(wins, matches)

            response += f"| {hero_name:<18} | {matches:<7} | {win_rate:<3.1f}% |\n"

        response += "```"
        return response
        
    def get_hero_name(self, hero_id):
        for hero in heroes:
            if hero['id'] == hero_id:
                return hero['name']
        return 'Unknown'
        
    def calculate_win_rate(self, wins, matches):
        """Calculates win rate as a percentage."""
        if matches == 0:
            return 0
        return round((wins / matches) * 100, 1)


async def setup(bot):
    await bot.add_cog(Meta(bot))