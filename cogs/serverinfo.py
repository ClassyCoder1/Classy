import discord
from discord.ext import commands
import datetime

class serverinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.hybrid_command(name="server-info", description="Gives information about the Discord Server.")
    async def server_info(self, interaction: discord.Interaction):
        
        server = interaction.guild
        
        boost_level = str(server.premium_tier)
        if boost_level == '0':
            boost_level = 'No level'
         
         nsfw_level = str(server.explicit_content_filter)
         if nsfw_level == '0':
             nsfw_label = 'Undefined'
         else:
             nsfw_label = 'Defined'
              
          verification_level = server.verification_level.name
          
          creation_time = server.created_at.strftime("%l:%M %p %B %d, %Y")
          creation_time_ago = (discord.utils.utcnow() - server.created_at).days // 30
          creation_time_ago_str = f"{creation_time_ago} months ago"
          
          num_roles = len(server.roles)
          num_emojis = len(server.emojis)
          num_static_emojis = sum(1 for emoji in server.emojis if not emoji.animated)
          num_animated_emojis = num_emojis - num_static_emojis
          num_members = server.member_count
          num_online = sum(1 for member in server.members if member.status != discord.Status.offline)
          num_idle = sum(1 for member in server.members if member.status == discord.Status.idle)
          num_dnd = sum(1 for member in server.members if member.status == discord.Status.dnd)
          num_text_channels = len(server.text_channels)
          num_voice_channels = len(server.voice_channels)
          
          description = (
              f"**Server Name:** {server.name}\n"
              f"**Server ID:** {server.id}\n"
              f"**Server Boost Level:** {boost_level}\n"
              f"**Server NSFW Label:** {nsfw_label}\n"
              f"**Server Verification Level:** {verification_level}\n"
              f"**Server Creation Time:** {creation_time} [{creation_time_ago_str}]\n\n"
              f"**Number of Roles:** {num_roles}\n"
              f"**Number of Emojis:** {num_emojis}\n"
              f"**Of them the usual ones:** {num_static_emojis}\n"
              f"**Of them animated:** {num_animated_emojis}\n\n"
              f"**Number of Members:** {num_members}\n"
              f"**Of them online:** {num_online}\n"
              f"**Of them, they really require calm:** {num_idle}\n"
              f"**Of these, they eat in the crib:** {num_dnd}\n\n"
              f"**Text Channels:** {num_text_channels}\n"
              f"**Voice Channels:** {num_voice_channels}"
          )
          
          embed = discord.Embed(title="Server Information", description=description, color=discord.Color.from_rgb(43, 45, 49))
          
          await interaction.send(embed=embed)
        
    @commands.Cog.listener()
    async def on_ready(self):
        print('Server-Info command is ready!')
        
async def setup(bot):
    await bot.add_cog(serverinfo(bot))