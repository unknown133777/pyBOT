import nextcord, os
import utils.utils as utils
from nextcord.ext import commands

#Read json(config.json)
data = utils.read_json()
GUILD_ID = int(data[0])
TOKEN = data[1]

intents = nextcord.Intents.default()
intents.message_content = True
intents.members = True
intents.voice_states = True
intents.reactions = True

bot = commands.Bot(intents=intents)
#Cogs load
for file in os.listdir('cogs'):
    if file.endswith('.py'):
        bot.load_extension(f'cogs.{file[:-3]}')

bot.run(TOKEN)