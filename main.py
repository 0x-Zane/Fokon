import discord 
from discord.ext import commands
from discord import app_commands
import os
from dotenv_vault import load_dotenv
import random as ra
import json


#-----------------Commands Sources -----------------

#---------------------------------------------------

with open('Fokon/quizz.json', 'r') as quizzes:
    quizz_data = json.load(quizzes)
with open('Fokon/periodic.json', 'r') as periodic:
    periodic_data = json.load(periodic)



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


@client.event 
async def  on_ready():
    print(f"The bot is now ready for use as {client.user} ")
    try:
        synced = await client.tree.sync() #Synchronize slash commands from the bot with discord
        print(f"Successfully synced {len(synced)} commands as !")
    except Exception as e:
        print(e)



@client.tree.command(name = "quizz")
@app_commands.describe(category = "Choose a category")
async def quizz(interaction: discord.Interaction,category:str): # will add the argument to get a quizz from a certain niche
            
            await interaction.response.send_message(quizz_data[category][ra.randint(0,len(quizz_data["quizz_cybersecurity"])-1)])


@client.tree.command(name="nohello")
async def nohello(interaction : discord.Interaction):
    await interaction.response.send_message("https://nohello.net/en/")



@client.tree.command(name = "random")
@app_commands.describe(min = "Choose a minimum number", max  = "Choose a maximum number")
async def quizz(interaction: discord.Interaction,min:int,max:int):
    await interaction.response.send_message(ra.randint(min,max))


@client.tree.command(name = "periodic")
@app_commands.describe(element = "")
async def quizz(interaction: discord.Interaction,element:str):
    await interaction.response.send_message("In developpement")    


client.run(TOKEN)



