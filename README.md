# Fokon
Fokon discord bot source code

The official documentation of discord.ext commands that are used is available in this link:
https://discordpy.readthedocs.io/en/stable/ext/commands/api.html#discord.ext.commands.Context

First of all to use the bot you will need to install the dependencies with 

pip install -r requirements.txt

You Will also need to create a .env file and create a variable like this:
TOKEN = ""

This variable will be used to run the bot


The bot will handle these commands:

--GENERAL TECH--
/poll {message} n{option(n)} #Creates a poll with n custom options

/random {x} {y}  #Generates a random number between x and y 

/github {repository_link} #Get the informations of a repository

/quizz #Get a random developper question to answer

/nohello #Sends the nohello.net link
/sleep_calculator {wake_up} {wanted_cycle(default:190min)}  # returns the next best sleep hours
--ELECTRONICS--

/Current {voltage} {resistance}

/resistance_code n{color}   with n number of arguments , you input the color of the resistance in 
the correct order and the bot will help you knowing the resistance value

--SCIENCE--

/periodic {element} # we take element.lower and get from a dictionnary or small db the information of the element
--GAMING--

/steam track
