from discord.ext import commands

class Miscellaneous(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def format_commands_list(self):
        """Return the formatted list of available commands."""
        return """
### Available commands:
- **!wl [days]**: Show the wins and losses in a given period (days), up to a maximum of 30 days.
  - If no days are given, shows the wins and losses for today.
- **!stats [days]**: Show the statistics of win and losses of all your heroes played in a given period (days), up to a maximum of 30 days.
  - If no days are given, shows the wins and losses for today.
- **!meta [position]**: Show the 5 most picked heroes for the given position (1-5) in the immortal rank over the last 7 days.
  - If no position or `0` is given, shows the 5 most picked heroes across all positions.
- **!commands**: List all the available commands for the bot.
- **!code**: Show the bot's repository link.
"""

    @commands.command(name="commands")
    async def show_commands(self, ctx):
        """Show the list of available commands."""
        response = self.format_commands_list()
        await ctx.send(response)

    @commands.command(name="code")
    async def show_code(self, ctx):
        """Show the bot's repository link."""
        await ctx.send("https://github.com/philipemosv/dota-discord-bot")


async def setup(bot):
    await bot.add_cog(Miscellaneous(bot))