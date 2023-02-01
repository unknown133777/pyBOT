import nextcord, utils.utils as utils
from nextcord.ext import commands

from main import GUILD_ID


class game1(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_raw_message_delete(self, payload):
        message = payload.cached_message
        if message.author.bot:
            return
        embed = nextcord.Embed(description=f"Message deleted in {message.channel.mention} by {message.author.mention}", color=0x5947FF)
        embed.set_author(name=message.author, icon_url=message.author.display_avatar)
        #Content
        embed.add_field(name="Content", value=message.content, inline=False)
        embed.add_field(name="ID", value=f"```yaml\n{payload.message_id} (Message ID)\n{payload.channel_id} (Channel ID)```", inline=False)
        embed.set_footer(text=f"github.com/Lee-d-g2222/pyBOT ・ Developed by 동건#2222")
        await self.bot.get_channel(utils.get_channel_id(str(payload.guild_id))).send(embed=embed)
        
            
def setup(bot):
    bot.add_cog(game1(bot))