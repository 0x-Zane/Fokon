import discord 
from discord.ext import commands
import os
from dotenv_vault import load_dotenv
import random as ra

#-----------------Commands Sources -----------------
quizz_cybersecurity = [
    # ----------------------------------------------------
    # CYBERSECURITY
    # ----------------------------------------------------
    "What is the name of the technique where an attacker impersonates a trusted entity to obtain sensitive information? ||Phishing||",
    "Which secure network protocol uses port 443 to encrypt web communications? ||HTTPS (HyperText Transfer Protocol Secure)||" ,
    "What does the acronym 'DDoS' stand for in the context of network attacks? ||Distributed Denial of Service||",
    "What term describes malware that encrypts a user's data and demands a ransom to unlock it? ||Ransomware||",
    "What is the main function of a 'firewall'? ||To filter and control incoming and outgoing network traffic based on established security rules.||",
    "What type of web vulnerability allows an attacker to inject SQL commands into a database? ||SQL Injection||",
    "In cryptography, what is the term for converting plaintext into an unreadable format? ||Encryption||"]
quizz_hardware = [
    # ----------------------------------------------------
    # HARDWARE & ELECTRONICS
    # ----------------------------------------------------
    "Which unit of measurement expresses the clock speed of a processor? ||Hertz (Hz) or Gigahertz (GHz)||" ,
    "In an electronic circuit, which component is capable of storing an electrical charge and is measured in Farads? ||The Capacitor||",
    "Which component is considered the basic building block of digital electronics, acting as a controlled switch? ||The Transistor||",
    "What is the role of 'RAM' (Random Access Memory) in a computer? ||To temporarily store data and programs currently being executed for the processor.||",
    "What fundamental law relates Voltage (U), Current (I), and Resistance (R) in electronics? ||Ohm's Law (U = R × I)||" ,
    "Which type of integrated circuit is at the heart of a computer and executes program instructions? ||The CPU (Central Processing Unit) or Processor||",
    "Which serial communication bus is commonly used to connect external peripherals like mice, keyboards, and external hard drives? ||USB (Universal Serial Bus)||" ]
quizz_software = [
    # ----------------------------------------------------
    # SOFTWARE & CODE
    # ----------------------------------------------------
    "Which data structure uses the 'LIFO' (Last-In, First-Out) principle? ||The Stack||",
    "In Object-Oriented Programming (OOP), what does 'Inheritance' mean? ||The mechanism by which one class acquires the properties and methods of another class (its parent class).||",
    "What is the primary role of a 'compiler'? ||To translate source code written in a high-level language into machine language (binary code) executable by the processor.||",
    "What is an 'infinite loop' in programming? ||A sequence of instructions that repeats indefinitely without a termination condition.||",
    "What does the acronym 'API' stand for? ||Application Programming Interface||",
    "In Python, what is the standard method for adding an item to the end of a list? ||.append()||",
    "Name the three pillars of Object-Oriented Programming (OOP). ||Encapsulation, Inheritance, Polymorphism.||",
    "What is the standard text-based markup language used to structure content on the World Wide Web? ||HTML (HyperText Markup Language)||" ]
quizz_networking = [
    # ----------------------------------------------------
    # INTERNET & NETWORKS
    # ----------------------------------------------------
    "What is the most common layered model used to describe network communications? ||TCP/IP Model||",
    "What does an 'IP address' represent? ||A unique identifier assigned to every device connected to a network that uses the Internet Protocol.||",
    "What is the role of 'DNS' (Domain Name System)? ||To translate human-readable domain names (e.g., google.com) into numerical IP addresses.||",
    "Which simple messaging protocol is commonly used for sending emails? ||SMTP (Simple Mail Transfer Protocol)||" ,
    "What is the fundamental difference between HTTP and HTTPS? ||HTTPS uses encryption (TLS/SSL) to secure communication, unlike HTTP.||",
    "Which network device has the primary function of connecting multiple networks together and directing data packets? ||The Router||"]
quizz_blockchain = [
    # ----------------------------------------------------
    # CRYPTO & BLOCKCHAIN
    # ----------------------------------------------------
    "What is a 'hash' in cryptography? ||The output of a mathematical function (hashing function) that produces a fixed-size, unique fingerprint for any input data.||",
    "What is the main technical characteristic of a 'blockchain'? ||An immutable, secure chain of data blocks, validated by a peer network and secured by cryptography.||",
    "Which mechanism guarantees both the authenticity and non-repudiation of a digital document? ||Digital signature||",
    "What is the name of the hashing algorithm used by Bitcoin? ||SHA-256||",
    "In the context of blockchains, what does 'PoW' stand for? ||Proof of Work||"]
quizz_general = [
    # ----------------------------------------------------
    # DIVERSE & TECH CULTURE
    # ----------------------------------------------------
    "What is the programming language most often used to style the look and feel of web pages (colors, fonts, layout)? ||CSS (Cascading Style Sheets)||" ,
    "Who invented the World Wide Web (WWW)? ||Tim Berners-Lee||",
    "Which operating system is based on the Linux kernel and is very popular among developers? ||GNU/Linux (e.g., Ubuntu or Debian)||" ,
    "What concept describes the practice of entrusting the hosting and execution of applications to remote servers via the Internet? ||Cloud Computing||",
    "Which software development methodology emphasizes rapid delivery and adaptation to change through short, iterative cycles (sprints)? ||Agile Methodology (e.g., Scrum)||",
    "Which software tool allows managing code versions and is essential for teamwork (e.g., commit, push, pull)? ||Git||",
    "What is the fundamental difference between Direct Current (DC) and Alternating Current (AC)? ||DC flows in one direction only, while AC periodically reverses direction.||",
    "What acronym represents a virtualization technology for packaging an application and its dependencies to ensure it runs reliably in any environment? ||Docker (or Conteneurization)||"
]

#---------------------------------------------------
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
        synced = await client.tree.sync()
        print(f"Successfully synced {len(synced)} commands  !")
    except Exception as e:
        print(e)
@client.command()
async def hello(ctx):
    await ctx.send(f"Hello, {ctx.author} !")
@client.command()
async def quizz(ctx,category): # will add the argument to get a quizz from a certain niche
    match category:
        case "cybersecurity":
            await ctx.send(quizz_cybersecurity[ra.randint(0,len(quizz_cybersecurity)-1)])

        case "blockchain":
            await ctx.send(quizz_blockchain[ra.randint(0,len(quizz_blockchain)-1)])

        case "":
            await ctx.send(ra.choice(quizz_blockchain[ra.randint(0,len(quizz_blockchain)-1)],quizz_cybersecurity[ra.randint(0,len(quizz_cybersecurity)-1)]))
@client.command()
async def nohello(ctx):
    await ctx.send("https://nohello.net/en/")

@client.command()
async def info(ctx):
    await ctx.send(f"All the code is open source in this repository : https://github.com/0x-Zane/Fokon")

@client.command()
async def whereami(ctx):
    await ctx.reply(f"Hello {ctx.author}, you are in {ctx.guild} in the channel {ctx.channel}, i am {ctx.me} AKA FOKON .")

@client.tree.command(name="hello")
async def hello(interaction : discord.Interaction):
    await interaction.response.send_message(f"Hey {interaction.user.mention}")
client.run(TOKEN)



