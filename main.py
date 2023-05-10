import discord
import os
import logging
from discord.ext import commands
from dotenv import load_dotenv
import json
from rhyme import Rhyme

# Create a log
logging.basicConfig(level=logging.INFO) 

# Load the .env
load_dotenv()

# Load the token from .env
token = os.environ.get('TOKEN')

# Create a bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='ai ', intents=intents)

# load all the rhymes from rhymes.json

with open("rhymes.json", "r", encoding="utf-8") as rhymesjson:
    content = rhymesjson.read()

loadedData = json.loads(content)
rhymes = [] 

for data in loadedData:
    triggers = data["triggers"]
    ignore = data["ignore"]
    answer = data["answer"]
    
    rhyme = Rhyme(triggers, ignore, answer)
    rhymes.append(rhyme)

@bot.event
async def on_ready():
    logging.info(f'We have logged in as {bot.user}')


# Answer the messages of the discord server
@bot.event
async def on_message(message):

    # get the last word of the message if it has text
    last_word = ""
    if message.content:
        last_word = message.content.split()[-1].lower()
    else:
        return
    
    # Remove all the '!', '.' and '?' characters
    charactersToRemove = "!?."
    last_word = last_word.rstrip(charactersToRemove)

    # Check if the author of the message is the bot itself to avoid loops
    if message.author == bot.user:
        return
    
    #Check if the last word rhymes with the rhymes in the json
    for rhyme in rhymes:
        if rhyme.rhymeswith(last_word) or rhyme.resultrhymeswith(last_word):                
        # Answer the message with the rhyme
            response = rhyme.answer
            await message.channel.send(response, reference=message, mention_author=True)
            logging.info(f'Answered to {message.author.name}:{message.author} in {message.guild.name}/{message.channel.name}: {response}')


bot.run(token)
