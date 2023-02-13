import nextcord, requests
from nextcord.ext import commands

#from main import GUILD_ID

def log_embed(interaction: nextcord.Interaction, channel: nextcord.TextChannel, description: str):
    embed = nextcord.Embed(title=f"Save Log at {channel.name}", description=description, color=0x5947FF)
    embed.add_field(name="Selected channel ID", value=f"```diff\n+ {channel.id}```", inline=False)
    embed.set_footer(text=f"Request by {interaction.user} ・ Developed by 동건#2222", icon_url=interaction.user.display_avatar)
    return embed

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #Set Log Channel to show logs
    @nextcord.slash_command(description="You can choose channel that shows logs", name="Music")
    async def setMusic(self, interaction: nextcord.Interaction, channel: nextcord.TextChannel = nextcord.SlashOption(required=True)):
        print("music")
            
        
def setup(bot):
    bot.add_cog(Music(bot))