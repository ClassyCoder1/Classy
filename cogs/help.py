import discord
from discord.ext import commands

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.hybrid_command(name="hell", description="Get a list of commands the bot have")
    async def ping(self, interaction: discord.Interaction):
        description = f"Hello {interaction.author.mention}! All the commands are listed below.\n\n**/avatar:** Gives you the profile picture of a user.\n**/ping:** Returns with the ping of the bot.\n**/report <user> <reason>:** Using this command you can report a user for violating rules.\n**/serverinfo:** Gives you information about the discord server. (Not added yet!)\n**/info:** Gives you information about the Minecraft Server and some usefull links as well.\n\nThanks for being a member in our Discord Server!"
        embed = discord.Embed(title="HELP", description=description, color=discord.Color.from_rgb(43, 45, 49))
        await interaction.send(embed=embed)
        
    @commands.Cog.listener()
    async def on_ready(self):
        print('Help command is ready!')
        
async def setup(bot):
    await bot.add_cog(help(bot))