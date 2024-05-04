import discord
from discord.ext import commands

class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.hybrid_command(name="ping", description="Returns the latency (Ping) of the bot")
    async def ping(self, interaction: discord.Interaction):
        ping = round(self.bot.latency * 1000)
        description = f"Hello {interaction.author.mention}!\n\nMy ping is **{ping}** milliseconds."
        embed = discord.Embed(title="PING, PONG!", description=description, color=discord.Color.from_rgb(43, 45, 49))
        await interaction.send(embed=embed)
        
    @commands.Cog.listener()
    async def on_ready(self):
        print('Ping command is ready!')
        
async def setup(bot):
    await bot.add_cog(ping(bot))