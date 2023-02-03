import nextcord, utils.utils as utils
from nextcord.ext import commands

from main import GUILD_ID

class game1(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_raw_message_delete(self, payload): #When message is deleted
        message = payload.cached_message
        if message.author.bot: #Ignore bot messages
            return
        embed = nextcord.Embed(description=f"Message deleted in {message.channel.mention} by {message.author.mention}", color=0x5947FF)
        embed.set_author(name=message.author, icon_url=message.author.display_avatar)
        embed.add_field(name="Content", value=message.content, inline=False)
        embed.add_field(name="ID", value=f"```yaml\n{payload.message_id} (Message ID)\n{payload.channel_id} (Channel ID)```", inline=False)
        embed.set_footer(text=f"github.com/Lee-d-g2222/pyBOT ・ Developed by 동건#2222")
        await self.bot.get_channel(utils.get_channel_id(str(payload.guild_id))).send(embed=embed)
        
    @commands.Cog.listener()
    async def on_message_edit(self, before, after): #When message is edited
        if before.author.bot: #Ignore bot messages
            return
        message_jump_url = f"https://discord.com/channels/{before.guild.id}/{before.channel.id}/{before.id}"
        embed = nextcord.Embed(description=f"Message edited!  →  [Go to Message]({message_jump_url})", color=0x5947FF)
        embed.set_author(name=before.author, icon_url=before.author.display_avatar)
        embed.add_field(name="Before", value=before.content, inline=True)
        embed.add_field(name="After", value=after.content, inline=True)
        embed.add_field(name="ID", value=f"```yaml\n{before.id} (Message ID)\n{before.channel.id} (Channel ID)```", inline=False)
        embed.set_footer(text=f"github.com/Lee-d-g2222/pyBOT ・ Developed by 동건#2222")
        await self.bot.get_channel(utils.get_channel_id(str(before.guild.id))).send(embed=embed)
        
    @commands.Cog.listener()
    async def on_guild_update(self, before, after): #When guild(server) was updated
        embed = nextcord.Embed(description="Server was updated", color=0x59AEEE)
        # Get user who updated the server
        async for entry in after.audit_logs(limit=1, action=nextcord.AuditLogAction.guild_update):
            if entry.user.bot: # Ignore bot
                return
            embed.set_author(name=entry.user, icon_url=entry.user.display_avatar)
        
        Status = False
        
        if before.name != after.name: # Server name changed
            embed.add_field(name="Server name changed", value=f"Before: **{before.name}**\nAfter: **{after.name}**", inline=False)
            Status = True
            
        if before.region != after.region: # Server region changed (VoiceChannel)
            embed.add_field(name="Server region changed", value=f"Before: **{before.region}**\nAfter: **{after.region}**", inline=False)
            Status = True
                        
        if before.afk_channel != after.afk_channel: # AFK Channel changed
            if before.afk_channel == None:
                embed.add_field(name="AFK Channel changed", value=f"Before: **None**\nAfter: <#{after.afk_channel.id}>", inline=False)
            elif after.afk_channel == None:
                embed.add_field(name="AFK Channel changed", value=f"Before: <#{before.afk_channel.id}>\nAfter: **None**", inline=False)
            else:
                embed.add_field(name="AFK Channel changed", value=f"Before: <#{before.afk_channel.id}>\nAfter: <#{after.afk_channel.id}>", inline=False)
            Status = True
            
        if before.afk_timeout != after.afk_timeout: # AFK Timeout changed
            embed.add_field(name="AFK Timeout changed", value=f"Before: **{(round(int(before.afk_timeout)/60))}** minutes\nAfter: **{(round(int(after.afk_timeout)/60))}** minutes", inline=False)
            Status = True
            
        if before.description != after.description: # Server's description changed
            embed.add_feild(name="Server description changed", value=f"Before: **{before.description}**\nAfter: **{after.description}**", inline=False)
            Status = True
        
        if before.mfa_level != after.mfa_level: # Server MFA Level changed
            embed.add_field(name="Server MFA Level changed", value=f"Before: **{before.mfa_level}**\nAfter: **{after.mfa_level}**", inline=False)
            Status = True
        
        if before.verification_level != after.verification_level: # Server Verification Level changed
            embed.add_field(name="Server Verification Level changed", value=f"Before: **{before.verification_level}**\nAfter: **{after.verification_level}**", inline=False)
            Status = True

        if before.explicit_content_filter != after.explicit_content_filter: # Server Explicit Content Filter changed
            embed.add_field(name="Server Explicit Content Filter changed", value=f"Before: **{before.explicit_content_filter}**\nAfter: **{after.explicit_content_filter}**", inline=False)
            Status = True
            
        if before.default_notifications != after.default_notifications: # Server Default Notifications changed
            embed.add_field(name="Server Default Notifications changed", value=f"Before: **{before.default_notifications}**\nAfter: **{after.default_notifications}**", inline=False)
            Status = True
            
        if before.premium_tier != after.premium_tier: # Server Boost Tier changed
            embed.add_field(name="Server Boost Tier changed", value=f"Before: **{before.premium_tier}**nAfter: **{after.premium_tier}**", inline=False)
            Status = True
        
        if before.premium_subscription_count != after.premium_subscription_count: # Server Boost Count changed
            embed.add_field(name="Server Boost Count changed", value=f"Before: **{before.premium_subscription_count}**\nAfter: **{after.premium_subscription_count}**", inline=False)
            Status = True
        
        if before.nsfw_level != after.nsfw_level: # Server NSFW Level changed
            embed.add_field(name="Server NSFW Level changed", value=f"Before: **{before.nsfw_level}**\nAfter: **{after.nsfw_level}**", inline=False)
            Status = True
            
        embed.add_field(name="ID", value=f"```yaml\n{before.id} (Server ID)```", inline=False)
        embed.set_footer(text=f"github.com/Lee-d-g2222/pyBOT ・ Developed by 동건#2222")
        if Status == True: # If there is a change
            await self.bot.get_channel(utils.get_channel_id(str(before.id))).send(embed=embed)
            
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload): # When a reaction(emoji) is added
        if payload.member.bot: # Ignore bot
            return
        message_jump_url = f"https://discord.com/channels/{payload.guild_id}/{payload.channel_id}/{payload.message_id}"
        embed = nextcord.Embed(description=f"Emoji added!  →  [Go to Message]({message_jump_url})", color=0x5947FF)
        embed.set_author(name=payload.member, icon_url=payload.member.display_avatar)
        embed.add_field(name="Reaction", value=payload.emoji, inline=False)
        embed.add_field(name="ID", value=f"```yaml\n{payload.message_id} (Message ID)\n{payload.channel_id} (Channel ID)```", inline=False)
        embed.set_footer(text=f"github.com/Lee-d-g2222/pyBOT ・ Developed by 동건#2222")
        await self.bot.get_channel(utils.get_channel_id(str(payload.guild_id))).send(embed=embed)
            
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload): # When a reaction(emoji) is removed
        # if payload.member.bot: # Ignore bot
        #     return
        message_jump_url = f"https://discord.com/channels/{payload.guild_id}/{payload.channel_id}/{payload.message_id}"
        embed = nextcord.Embed(description=f"Emoji removed!  →  [Go to Message]({message_jump_url})", color=0x5947FF)
        # embed.set_author(name=payload.member, icon_url=payload.member.display_avatar)
        embed.add_field(name="Reaction", value=f"{payload.emoji} / {payload.member}", inline=False)
        embed.add_field(name="ID", value=f"```yaml\n{payload.message_id} (Message ID)\n{payload.channel_id} (Channel ID)```", inline=False)
        embed.set_footer(text=f"github.com/Lee-d-g2222/pyBOT ・ Developed by 동건#2222")
        await self.bot.get_channel(utils.get_channel_id(str(payload.guild_id))).send(embed=embed)
        
        
    
def setup(bot):
    bot.add_cog(game1(bot))