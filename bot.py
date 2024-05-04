import discord
from discord.ext import commands
import os
import dotenv
from dotenv import load_dotenv
import re
import asyncio

load_dotenv()

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.all()
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents, activity=discord.Game(name='Activity'))

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    print(f'ID: {bot.user.id}')
    await bot.tree.sync()
    print('Bot is ready! All commands are synced.')

async def load_cogs():
    async with bot:
        cog_modules = ['cogs.ping', 'cogs.avatar', 'cogs.report', 'cogs.help', 'cogs.serverinfo']
        for cog in cog_modules:
            await bot.load_extension(cog)
         await bot.start(TOKEN)
         
async def main():
    await load_cogs()
    
asyncio.run(main())