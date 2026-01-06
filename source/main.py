import discord 
from discord.ext import commands
from discord import app_commands
import os
from dotenv import load_dotenv
import random as ra
import json
import requests
from datetime import datetime


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

@client.tree.command(name="info")
async def info(interaction : discord.Interaction):
    await interaction.response.send_message("GET ALL THE INFORMATIONS [HERE](https://github.com/0Zane/Fokon/blob/main/README.md)")


@client.tree.command(name = "quizz")
@app_commands.describe(category = "Choose a category".lower())
@app_commands.choices( category=[
    
    app_commands.Choice(name="cybersecurity",value="cybersecurity"),
    app_commands.Choice(name="hardware",value="hardware"),
    app_commands.Choice(name="software",value="software"),
    app_commands.Choice(name="networking",value="networking"),
    app_commands.Choice(name="3dmodeling",value="3dmodeling"),
    app_commands.Choice(name="webdevelopment",value="webdevelopment"),
    app_commands.Choice(name="electronics",value="electronics"),

                                 ])
async def quizz(interaction: discord.Interaction,category:str): # will add the argument to get a quizz from a certain niche
    try:
        embed = discord.Embed(title=category.upper(),description="",color=yellow,url=f'https://en.wikipedia.org/wiki/{category}')  
        #embed.set_thumbnail(url="")   
        
        embed.add_field(name="",value=quizz_data[category][ra.randint(0,len(quizz_data[category])-1)])   
        await interaction.response.send_message(embed=embed)
        

            # await interaction.response.send_message(quizz_data[category][ra.randint(0,len(quizz_data["quizz_cybersecurity"])-1)]) --> DEBUG

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
    if max > min:
        try:
            await interaction.response.send_message(ra.randint(min,max))
        except:
            await interaction.response.send_message(f"Fokon cannot generate a random number between {min} and {max}")
    else:
        await interaction.response.send_message(f"Min argument needs to be superior to Max argument, please try with valid values.")


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
@app_commands.checks.cooldown(1, 15.0, key=lambda i: (i.guild_id, i.user.id))
@app_commands.describe(repo = "Please insert the link of the repository in this format : username/repositoryname")
async def github(interaction: discord.Interaction, repo: str):

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
                "License": repo_info["license"]["name"] if repo_info["license"] else "None",
                "Watchers": repo_info["watchers"],
                "Creation": repo_info["created_at"],

             
            }


            
            

            return data
        else:
            pass
    
    try:
        repo_result  = get_repo_data(repo)
        languages = ", ".join(repo_result["Programming languages used"]) or "Not specified"
        issues_count = len(repo_result["Open issues"])

        created_at = datetime.fromisoformat(repo_result["Creation"].replace("Z", "")).strftime("%d %B %Y")
        updated_at = datetime.fromisoformat(repo_result["Last maintained"].replace("Z", "")).strftime("%d %B %Y")
        
        embed = discord.Embed(
            title=f"{repo_result['Project name']}",
            description=repo_result["Description"] or "No description provided.",
            color=discord.Color.blue(),
            url=f"https://github.com/{repo}"
        )

        embed.set_thumbnail(url=repo_result["Avatar"])

        embed.add_field(name="Owner",value=repo_result["Project owner"],inline=True)

        embed.add_field(name="watchers",value=str(repo_result["Watchers"]),inline=True)

        embed.add_field(name="Languages",value=languages,inline=False)

        embed.add_field(name="Open issues",value=str(issues_count),inline=True)

        embed.add_field(name="License",value=repo_result["License"] or "None",inline=True)

        embed.add_field(name="Timeline",value=f"Created: **{created_at}**\nLast update: **{updated_at}**",inline=False)

        embed.set_footer(text="Using github API")
        await interaction.response.send_message(embed=embed)

    except:
        await interaction.response.send_message(f"Could not find {repo}")

@github.error
async def on_github_error(interaction: discord.Interaction, error: app_commands.AppCommandError):
    if isinstance(error, app_commands.CommandOnCooldown):
        await interaction.response.send_message(str(error), ephemeral=True)



@client.tree.command(name="resistance") 
@app_commands.describe(v="Insert voltage here",i="Insert current here")
async def resistance(interaction: discord.Interaction, v:float, i:float):
    try:
        await interaction.response.send_message(f"With V = {v}, I = {i}         -->     R = {v/i}")
    
    except Exception as e:
        await interaction.response.send_message(f"Could not determine resistance, error : {e}")


@client.tree.command(name="resistance_color")
@app_commands.describe(number_of_lines="Please select the number of lines on your THT Resistor (4 or 5)", color1="Insert the color of the first line",color2="Insert the color of the 2nd resistor",color3="ONLY USEFUL FOR 5 LINES RESISTORS",color4="Insert the color of the 4th line",color5="Insert the color of the 5th line")
@app_commands.choices(

    number_of_lines=[
        app_commands.Choice(name="4 lines",value=4),
        app_commands.Choice(name="5 lines",value=5)
    ],

    color1=[
        app_commands.Choice(name="Black", value=0),
        app_commands.Choice(name="Brown", value=1),
        app_commands.Choice(name="Red", value=2),
        app_commands.Choice(name="Orange", value=3),
        app_commands.Choice(name="Yellow", value=4),
        app_commands.Choice(name="Green", value=5),
        app_commands.Choice(name="Blue", value=6),
        app_commands.Choice(name="Purple", value=7),
        app_commands.Choice(name="Grey", value=8),
        app_commands.Choice(name="White", value=9),
    ],
    color2=[
        app_commands.Choice(name="Black", value=0),
        app_commands.Choice(name="Brown", value=1),
        app_commands.Choice(name="Red", value=2),
        app_commands.Choice(name="Orange", value=3),
        app_commands.Choice(name="Yellow", value=4),
        app_commands.Choice(name="Green", value=5),
        app_commands.Choice(name="Blue", value=6),
        app_commands.Choice(name="Purple", value=7),
        app_commands.Choice(name="Grey", value=8),
        app_commands.Choice(name="White", value=9),
    ],
    color3=[
        app_commands.Choice(name="CHOOSE THIS IF YOU HAVE 4 LINES RESISTOR", value=67),
        app_commands.Choice(name="Black", value=0),
        app_commands.Choice(name="Brown", value=1),
        app_commands.Choice(name="Red", value=2),
        app_commands.Choice(name="Orange", value=3),
        app_commands.Choice(name="Yellow", value=4),
        app_commands.Choice(name="Green", value=5),
        app_commands.Choice(name="Blue", value=6),
        app_commands.Choice(name="Purple", value=7),
        app_commands.Choice(name="Grey", value=8),
        app_commands.Choice(name="White", value=9),
    ],
    color4=[
        app_commands.Choice(name="Black", value=0),
        app_commands.Choice(name="Brown", value=1),
        app_commands.Choice(name="Red", value=2),
        app_commands.Choice(name="Orange", value=3),
        app_commands.Choice(name="Yellow", value=4),
        app_commands.Choice(name="Green", value=5),
        app_commands.Choice(name="Blue", value=6),
        app_commands.Choice(name="Purple", value=7),
        app_commands.Choice(name="Grey", value=8),
        app_commands.Choice(name="White", value=9),
    ],
    color5=[


        app_commands.Choice(name="black", value=0),
        app_commands.Choice(name="brown", value=1),
        app_commands.Choice(name="red", value=2),
        app_commands.Choice(name="orange", value=3),
        app_commands.Choice(name="yellow", value=4),
        app_commands.Choice(name="green", value=5),
        app_commands.Choice(name="blue", value=6),
        app_commands.Choice(name="purple", value=7),
        app_commands.Choice(name="grey", value=8),
        app_commands.Choice(name="white", value=9),
        app_commands.Choice(name="gold", value=10),
        app_commands.Choice(name="silver", value=11),
    ]

)

async def resistance_color(interaction: discord.Interaction,number_of_lines:int, color1: int,color2:int,color3:int,color4:int,color5:int):
    colors= [
    "⬛",
    "🟫",
    "🟥",
    "🟧",
    "🟨",
    "🟩",
    "🟦",
    "🟪",
    "⬜",
    "🌫️",
    "🟨✨",
    "⬜✨"
    ]
    tolerances= [
        None,
        1.00,
        2.00,
        None,
        None,
        0.50,
        0.25,
        0.10,
        0.05,
        5.00,
        10.0,
        ]


    if number_of_lines == 4: #IN this case , the resistance has 4 lines

        try:
            digits = int(str(color1)+str(color2))
            factor = 10**color4
            embed = discord.Embed(
                title = f"Resistance selected : |{colors[color1]}|{colors[color2]}|{colors[color4]}|{colors[color5]}|",
                description = "" ,
                color=discord.Color.yellow(),
                )
            embed.add_field(name="Resistance value : ", value= f"{digits*factor} ohms")
            embed.add_field(name="Tolerance : ", value= f"{tolerances[color5]}%" if tolerances[color5] else "not defined")

            await interaction.response.send_message(embed=embed)


        except Exception as e:
            await interaction.response.send_message(f"Error : {e}")


    elif number_of_lines == 5: #IN this case , the resistance has 5 lines    
        try:
            digits = int(str(color1)+str(color2)+str(color3))
            factor = 10**color4
            embed = discord.Embed(
                title = f"Resistance selected : |{colors[color1]}|{colors[color2]}|{colors[color3]}|{colors[color4]}|{colors[color5]}|",
                description = "" ,
                color=discord.Color.yellow(),
                )
            embed.add_field(name="Resistance value : ", value= f"{digits*factor} ohms")
            embed.add_field(name="Tolerance : ", value= f"{tolerances[color5]}%" if tolerances[color5] else "not defined")

            await interaction.response.send_message(embed=embed)

            

        
        except Exception as e:
            await interaction.response.send_message(f"Error : {e}")

    else:
        await interaction.response.send_message("The number of lines is incorrect")


client.run(TOKEN)



