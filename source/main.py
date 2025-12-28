import discord 
from discord.ext import commands
from discord import app_commands
import os
from dotenv import load_dotenv
import random as ra
import json
import requests


#-----------------Commands Sources-----------------
red = discord.Color.red()
blue = discord.Color.blue()
yellow = discord.Color.yellow()
#------------------Loading Json data------------------

with open('assets/text_sources/quizz.json', 'r',encoding="utf-8") as quizzes:
    quizz_data = json.load(quizzes)
with open('assets/text_sources/periodic.json', 'r',encoding="utf-8") as periodic:
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
        print(f"Successfully synced {len(synced)} commands.")
    except Exception as e:
        print(e)



@client.tree.command(name = "quizz")
@app_commands.describe(category = "Choose a category".lower())
async def quizz(interaction: discord.Interaction,category:str): # will add the argument to get a quizz from a certain niche
    try:
        embed = discord.Embed(title=category.upper(),description="",color=yellow,url=f'https://en.wikipedia.org/wiki/{category}')  
        #embed.set_thumbnail(url="")   
        
        embed.add_field(name="",value=quizz_data[category][ra.randint(0,len(quizz_data[category])-1)])   
        await interaction.response.send_message(embed=embed)
        

            # await interaction.response.send_message(quizz_data[category][ra.randint(0,len(quizz_data["quizz_cybersecurity"])-1)])

    except:
        await interaction.response.send_message(f"{category} is not an available category. ")
        
@client.tree.command(name="nohello")
async def nohello(interaction : discord.Interaction):
    await interaction.response.send_message("https://nohello.net/en/")


@client.tree.command(name="dontasktoask")
async def dontasktoask(interaction : discord.Interaction):
    await interaction.response.send_message("https://dontasktoask.com")


@client.tree.command(name = "random")
@app_commands.describe(min = "Choose a minimum number", max  = "Choose a maximum number")
async def random(interaction: discord.Interaction,min:int,max:int):
    await interaction.response.send_message(ra.randint(min,max))


@client.tree.command(name = "periodic")
@app_commands.describe(element = "Please provide the atomic number/symbol/name of the wanted element.")
async def periodic(interaction: discord.Interaction,element:str):




    if element.isdigit(): # Checking if the argument is the atomic number 
        element = int(element)
      
        try:
            name = periodic_data["elements"][element-1]["name"]
            symbol= periodic_data["elements"][element-1]["symbol"]
            mass = periodic_data["elements"][element-1]["atomic_mass"]
            category = periodic_data["elements"][element-1]["category"]
            density = periodic_data["elements"][element-1]["density"]
            boil = periodic_data["elements"][element-1]["boil"]
            phase = periodic_data["elements"][element-1]["phase"]
            melt = periodic_data["elements"][element-1]["melt"]
            shells = periodic_data["elements"][element-1]["shells"]
            electronic_configuration = periodic_data["elements"][element-1]["electronic_configuration"]
            try:
                discovered_by = periodic_data["elements"][element-1]["discovered_by"]
            except:
                discovered_by = "Unknown"

            embed = discord.Embed(title=name,description="",color=blue,url=f'https://en.wikipedia.org/wiki/{name}')  
             
            
            embed.add_field(name="symbol",value=symbol)   
            embed.add_field(name="atomic_mass",value=mass)  
            embed.add_field(name="category",value=category)  
            embed.add_field(name="density",value=density)  
            embed.add_field(name="boil",value=boil)  
            embed.add_field(name="phase",value=phase)
            if melt != None:  
                embed.add_field(name="melt",value=str(melt)+"K")  
            else:
                embed.add_field(name="melt",value="Unavailable")  

            embed.add_field(name="shells",value=shells)  
            embed.add_field(name="electronic_configuration",value=electronic_configuration)  
            embed.add_field(name="discovered_by",value=discovered_by)  
            embed.add_field(name="WARNING",value=" ⚠️ Fokon sometimes makes mistakes, if you spot one , please create a pull request with needed modifications on periodic.json file  .")
            embed.set_thumbnail(url=f"https://images-of-elements.com/s/{name.lower()}.jpg")  

            await interaction.response.send_message(embed=embed)




            
        except Exception as e:
            await interaction.response.send_message(f"{element} is not in the periodic table, don't forget that the periodic table starts at 1 and ends at 118.")



    elif len(element) == 2 or len(element) == 1: #checking if the argument is the symbol
        element = element.lower().title()
        try:
            found = False
            i = 0
            while not found and i <= len(periodic_data["elements"]):
                if periodic_data["elements"][i]["symbol"] == element:
                    found = True

                    name = periodic_data["elements"][i]["name"]
                    symbol= periodic_data["elements"][i]["symbol"]
                    mass = periodic_data["elements"][i]["atomic_mass"]
                    category = periodic_data["elements"][i]["category"]
                    density = periodic_data["elements"][i]["density"]
                    boil = periodic_data["elements"][i]["boil"]
                    phase = periodic_data["elements"][i]["phase"]
                    melt = periodic_data["elements"][i]["melt"]
                    shells = periodic_data["elements"][i]["shells"]
                    electronic_configuration = periodic_data["elements"][i]["electronic_configuration"]
                    try:
                        discovered_by = periodic_data["elements"][i-1]["discovered_by"]
                    except:
                        discovered_by = "Unknown"

                    embed = discord.Embed(title=name,description="",color=discord.Color.blue(),url=f'https://en.wikipedia.org/wiki/{name}')  
                    
                    
                    embed.add_field(name="symbol",value=symbol)   
                    embed.add_field(name="atomic_mass",value=mass)  
                    embed.add_field(name="category",value=category)  
                    embed.add_field(name="density",value=density)  
                    embed.add_field(name="boil",value=boil)  
                    embed.add_field(name="phase",value=phase)
                    if melt != None:  
                        embed.add_field(name="melt",value=str(melt)+"K")  
                    else:
                        embed.add_field(name="melt",value="Unavailable")  

                    embed.add_field(name="shells",value=shells)  
                    embed.add_field(name="electronic_configuration",value=electronic_configuration)  
                    embed.add_field(name="discovered_by",value= discovered_by)  
                    embed.add_field(name="WARNING",value=" ⚠️ Fokon sometimes makes mistakes, if you spot one , please create a pull request with needed modifications on periodic.json file  .")
                    embed.set_thumbnail(url=f"https://images-of-elements.com/s/{name.lower()}.jpg")  

                    await interaction.response.send_message(embed=embed)
                    



                else :
                    i+=1
        except :
            await interaction.response.send_message(f"{element} is not available in periodic table")


    else: #Otherwise, assuming that it's the english name of the element
        
    
        element = element.lower().title()
        try:
            found = False
            i = 0
            while not found and i <= len(periodic_data["elements"]):
                if periodic_data["elements"][i]["name"] == element:
                    found = True

                    name = periodic_data["elements"][i]["name"]
                    symbol= periodic_data["elements"][i]["symbol"]
                    mass = periodic_data["elements"][i]["atomic_mass"]
                    category = periodic_data["elements"][i]["category"]
                    density = periodic_data["elements"][i]["density"]
                    boil = periodic_data["elements"][i]["boil"]
                    phase = periodic_data["elements"][i]["phase"]
                    melt = periodic_data["elements"][i]["melt"]
                    shells = periodic_data["elements"][i]["shells"]
                    electronic_configuration = periodic_data["elements"][i]["electronic_configuration"]
                    try:
                        discovered_by = periodic_data["elements"][i-1]["discovered_by"]
                    except:
                        discovered_by = "Unknown"

                    embed = discord.Embed(title=name,description="",color=discord.Color.blue(),url=f'https://en.wikipedia.org/wiki/{name}')  
                    
                    
                    embed.add_field(name="symbol",value=symbol)   
                    embed.add_field(name="atomic_mass",value=mass)  
                    embed.add_field(name="category",value=category)  
                    embed.add_field(name="density",value=density)  
                    embed.add_field(name="boil",value=boil)  
                    embed.add_field(name="phase",value=phase)
                    if melt != None:  
                        embed.add_field(name="melt",value=str(melt)+"K")  
                    else:
                        embed.add_field(name="melt",value="Unavailable")  

                    embed.add_field(name="shells",value=shells)  
                    embed.add_field(name="electronic_configuration",value=electronic_configuration)  
                    embed.add_field(name="discovered_by",value=discovered_by)  
                    embed.add_field(name="WARNING",value=" ⚠️ Fokon sometimes makes mistakes, if you spot one , please create a pull request with needed modifications on periodic.json file  .")
                    embed.set_thumbnail(url=f"https://images-of-elements.com/s/{name.lower()}.jpg")  

                    await interaction.response.send_message(embed=embed)
                    



                else :
                    i+=1
        except:
            await interaction.response.send_message(f"{element} is not available in periodic table")


@client.tree.command(name="github")
@app_commands.describe(repo = "Please insert the link of the repository in this format : username/repositoryname")
async def github(interaction: discord.Integration, repo: str):

    def get_repo_info(owner, repo):
        url = f"https://api.github.com/repos/{owner}/{repo}"
        headers = {"Accept": "application/vnd.github+json"}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            return None

    def get_collaborators(collaborators_url):
        response = requests.get(collaborators_url)
        if response.status_code == 200:
            return [collaborator["login"] for collaborator in response.json()]
        else:
            return []

    def get_languages(languages_url):
        response = requests.get(languages_url)
        if response.status_code == 200:
            return list(response.json().keys())
        else:
            return []

    def get_open_issues(owner, repo):
        url = f"https://api.github.com/repos/{owner}/{repo}/issues?state=open"
        headers = {"Accept": "application/vnd.github+json"}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            return []

    def get_repo_data(repo_url):
        owner, repo = repo_url.split("/")[-2:]
        repo_info = get_repo_info(owner, repo)

        if repo_info:
            data = {
                "Github URL": repo_url,
                "Project name": repo_info["name"],
                "Project owner": repo_info["owner"]["login"],
                "Programming languages used": get_languages(repo_info["languages_url"]),
                "Description": repo_info["description"],
                "Last maintained": repo_info["pushed_at"],
                "Open issues": get_open_issues(owner, repo),
                "Avatar" : repo_info["owner"]["avatar_url"],
                "License": repo_info["license"]["name"],
                "Watchers": repo_info["watchers"],
                "Creation": repo_info["created_at"],

             
            }


            
            

            return data
        else:
            pass
    
    #try:
    repo_result  = get_repo_data(repo)
    
    embed = discord.Embed(title=repo_result["Project name"],description=repo_result["Description"],color=blue,url=f"https://github.com/{repo}") 
    embed.add_field(name="Owner", value=repo_result["Project owner"]) 
    embed.add_field(name="Programming languages used", value=repo_result["Programming languages used"]) 
    embed.add_field(name=" ",value=f"Created on {repo_result["Creation"]} and last updated on {repo_result["Last maintained"]}")
    embed.add_field(name="Issues",value=repo_result["Open issues"])
    embed.add_field(name="Watchers",value=repo_result["Watchers"])
    embed.add_field(name="LICENSE", value=repo_result['License'])
    embed.set_thumbnail(url=repo_result["Avatar"])
    await interaction.response.send_message(embed=embed)

"""    except:
        await interaction.response.send_message(f"Could not find {repo}")"""




client.run(TOKEN)



