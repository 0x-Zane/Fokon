import discord 
from dotenv_vault import load_dotenv
import os
from discord.ext import commands
load_dotenv()

TOKEN = os.getenv("TOKEN")
intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix="/", intents=intents)

bot.run(TOKEN)