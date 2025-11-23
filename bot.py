import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Define bot intents
intents = discord.Intents.default()
intents.message_content = True  # Required to read message content for commands

# Initialize the bot with a command prefix and intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f'Bot is ready! Logged in as {bot.user}')
    print(f'User ID: {bot.user.id}')
    print('------')

# Command: Hello
@bot.command(name='hello')
async def hello(ctx):
    """Responds with a friendly greeting."""
    await ctx.send(f'Hello, {ctx.author.mention}!')

# Run the bot with the token from environment variables
bot.run(os.getenv('DISCORD_TOKEN'))