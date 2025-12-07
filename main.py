import discord 
from discord.ext import commands
import os
from dotenv_vault import load_dotenv
 
    #DEFINING INTENTS
bot_intents = discord.Intents.default()
bot_intents.message_content = True

 #Get the token from .env file
load_dotenv()
TOKEN = os.getenv("TOKEN")

client = commands.Bot(command_prefix= "/",intents=bot_intents)


#2 MAIN WAYS TO CREATE A DISCORD BOT:

# 1.FROM DISCORD.EXT USING COMMANDS
# 2.CREATING DIRECTLY A BOT OBJECT WITH:  DISCORD.CLIENT()


@client.event #
async def  on_ready():
    print(f"The bot is now ready for use as {client.user} ")

@client.command()
async def hello(ctx):
    await ctx.send("Hello, World!")


client.run(TOKEN)



