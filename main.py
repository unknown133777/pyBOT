import json, os
import nextcord

from nextcord.ext import commands

JSON_PATH = str(os.getcwd()) + '\pyBOT\config.json'
with open(JSON_PATH, 'r') as file:
    data = json.load(file)

GUILD_ID = data['config']['guild_id']
TOKEN = data['config']['token']

intents = nextcord.Intents.default()
bot = commands.Bot()

bot.run(TOKEN)