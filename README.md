# Fokon
Fokon discord bot source code



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

--ELECTRONICS--

/Current {voltage} {resistance}

/resistance_code n{color}   with n number of arguments , you input the color of the resistance in 
the correct order and the bot will help you knowing the resistance value


--GAMING--

/steam track
