import discord
from discord.ext import commands

class avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.hybrid_command(name="avatar", description="Returns with the avatar of the user")
    async def ping(self, interaction: discord.Interaction, user: discord.Member = None):
        if user is None:
            user = interaction.author
        
        embed = discord.Embed(title=f"Avatar of {user.display_nams}" color=discord.Color.from_rgb(43, 45, 49))
        embed.set_image(url=user.display_avatar.url)
        await interaction.send(embed=embed)
        
    @commands.Cog.listener()
    async def on_ready(self):
        print('Avatar command is ready!')
        
async def setup(bot):
    await bot.add_cog(avatar(bot))