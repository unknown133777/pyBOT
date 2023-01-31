import nextcord, requests
from nextcord.ext import commands

from main import GUILD_ID

def log_embed(interaction: nextcord.Interaction, channel: nextcord.TextChannel, description: str):
    embed = nextcord.Embed(title=f"Save Log at {channel.name}", description=description, color=0x5947FF)
    embed.add_field(name="Selected channel ID", value=f"```diff\n+ {channel.id}```", inline=False)
    embed.set_footer(text=f"Request by {interaction.user} ・ Developed by 동건#2222", icon_url=interaction.user.display_avatar)
    return embed

class LogChannel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #Set Log Channel to show logs
    @nextcord.slash_command(guild_ids=[GUILD_ID], description="You can choose channel that shows logs", name="log_channel")
    async def setLogChannelA(self, interaction: nextcord.Interaction, channel: nextcord.TextChannel = nextcord.SlashOption(required=True)):
        
        #REST API TO POST
        url = "http://ubuntu.donggeon.xyz:8000/setlogchannel/"
        headers = {"Content-Type": "application/json"}
        jSON = {"channel_id": f"{channel.id}", "guild_id": f"{channel.guild.id}"}
        http_post = requests.post(url, json=jSON, headers=headers)
            
        if http_post.status_code == 201:
            if http_post.json()["detail"] == "dbCreateSuccess":
                embed = log_embed(interaction, channel, f"Log Channel has been set! [{channel.mention}]")
                await interaction.response.send_message(embed=embed)
            elif http_post.json()["detail"] == "dbUpdateSuccess":
                embed = log_embed(interaction, channel, f"Log Channel has been updated! [{channel.mention}]")
                await interaction.response.send_message(embed=embed)

        elif http_post.status_code == 409:
            if http_post.json()["detail"] == "dbCreateFail":
                embed = log_embed(interaction, channel, f"Error! [Log channel NOT SET]")
                await interaction.response.send_message(embed=embed)
            elif http_post.json()["detail"] == "dbUpdateFail":
                embed = log_embed(interaction, channel, f"Error! [Log channel NOT UPDATED]")
                await interaction.response.send_message(embed=embed)
            else:
                embed = log_embed(interaction, channel, f"Log Channel is already set to [{channel.mention}]")
                await interaction.response.send_message(embed=embed)
            
        
def setup(bot):
    bot.add_cog(LogChannel(bot))