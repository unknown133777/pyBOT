import nextcord, requests
from nextcord.ext import commands

from main import GUILD_ID

def log_embed(interaction: nextcord.Interaction, channel: nextcord.TextChannel, description: str):
    embed = nextcord.Embed(title=f"Save Log at {channel.name}", description=description, color=0x5947FF)
    embed.add_field(name="Selected channel ID", value=f"```diff\n+ {channel.id}```", inline=False)
    embed.set_footer(text=f"Request by {interaction.user} ・ Developed by 동건#2222", icon_url=interaction.user.display_avatar)
    return embed

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #Set Log Channel to show logs
    @nextcord.slash_command(description="You can choose channel that shows logs", name="play", guild_ids=[GUILD_ID])
    async def join(self, interaction: nextcord.Interaction):
        if interaction.user.voice:
            if interaction.guild.voice_client:
                await interaction.response.send_message("Moved to the voice channel.")
                return await interaction.guild.voice_client.move_to(interaction.user.voice.channel)
            else: 
                await interaction.user.voice.channel.connect()
                await interaction.response.send_message("Joined the voice channel.")
        else:
            await interaction.response.send_message("You are not in the voice channel. Please join the voice channel and try again.")
            
    
        
def setup(bot):
    bot.add_cog(Music(bot))