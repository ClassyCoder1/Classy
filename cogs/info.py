import discord
from discord.ext import commands

class info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.hybrid_command(name="info", description="Gives you information about the minecraft server.")
    async def info(self, interaction: discord.Interaction):
        description = f"Support: https://support.hypixel.net\nMinecraft Server IP: **mc.hypixel.net**\nWebsite: https://hypixel.net/\nServer Invite Link: https://discord.gg/hypixel\n\n**Store**: https://store.hypixel.net/"
        embed = discord.Embed(title="Useful Links", description=description, color=discord.Color.from_rgb(43, 45, 49))
        await interaction.send(embed=embed)
        
    @commands.Cog.listener()
    async def on_ready(self):
        print('Info command is ready!')
        
async def setup(bot):
    await bot.add_cog(info(bot))