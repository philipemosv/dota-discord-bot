from discord.ext import commands

class Miscellaneous(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="commands")
    async def show_commands(self, ctx):
        response = """
### Available commands:
- **!wl [days]**: Show the wins and losses in a given period (days), up to a maximum of 30 days.
  - If no days are given, shows the wins and losses for today.
- **!stats [days]**: Show the statistics of win and losses of all your heroes played in a given period (days) up to a maximum of 30 days.
  - If no days are given, shows the wins and losses for today.
- **!commands**: List all the available commands for the bot.
- **!code**: Show the bot's repository link.
- **!bagre**: Show the name of the most 'bagre' player in Brazil.
"""
        await ctx.send(response)


    @commands.command(name="code")
    async def show_code(self, ctx):
        await ctx.send(f"https://github.com/philipemosv/dota-discord-bot")


    @commands.command(name="bagre")
    async def show_bagre(self, ctx):
        await ctx.send(f"Davi")


async def setup(bot):
    await bot.add_cog(Miscellaneous(bot))