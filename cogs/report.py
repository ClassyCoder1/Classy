import discord
from discord.ext import commands

class report(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.hybrid_command(name="report", description="Report a user for violating servef rules")
    async def report(self, interaction: discord.Interaction, user: discord.Member, reason: str):
        
        REPORT_CHANNEL_ID = your_report_channel_id
        
        report_channel = interaction.guild.get_channel(REPORT_CHANNEL_ID)
        if report_channel is None:
            return await interaction.send("Report channel not found. Please contact a server administrator.", ephemeral=True)
        embed_dm = discord.Embed(title="REPORT", description=f"Your report has been successfully submitted. Please wait for a staff member to check it. You will receive a direct message from a staff member shortly. We appreciate you for reporting a rule breaker!", color=discord.Color_from_rgb(43, 45, 49))
        await interaction.author.send(embed=embed_dm)
        
        embed_report_channel = discord.Embed(title="REPORT", description=f"Hello! :wave: Someone just reported a user.\n\nReporter: {interaction.author.mention}\nReported: {user.menrion}\nReason: **{reason}**", color=discord.Color.from_rgb(43, 45,49))
        await report_channel.send(embed=embed_report_channel)
        
        await interaction.send("Report has been submitted successfully", ephemeral=True)
        
    @commands.Cog.listener()
    async def on_ready(self):
        print('Report command is ready!')
        
async def setup(bot):
    await bot.add_cog(report(bot))