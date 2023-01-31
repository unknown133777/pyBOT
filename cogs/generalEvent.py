import nextcord
from nextcord.ext import commands

class mainEvent(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self): 
        print(f'on_ready() executed {self.bot.user}')

def setup(bot):
    bot.add_cog(mainEvent(bot))