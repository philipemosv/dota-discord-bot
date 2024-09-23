from discord.ext import commands

class Bagre(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="bagre")
    async def register(self, ctx):
        await ctx.send(f"Davi")

async def setup(bot):
    await bot.add_cog(Bagre(bot))