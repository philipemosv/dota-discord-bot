import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


async def load_extensions():
    await bot.load_extension('commands.win_loss')
    await bot.load_extension('commands.register')
    await bot.load_extension('commands.bagre')

async def main():
    async with bot:
        await load_extensions()
        await bot.start(os.getenv('DISCORD_TOKEN'))


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())