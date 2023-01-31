import nextcord
from nextcord.ext import commands

from main import GUILD_ID

class game1(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
            
def setup(bot):
    bot.add_cog(game1(bot))