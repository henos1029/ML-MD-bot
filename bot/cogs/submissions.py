import discord
from discord.ext import commands
import functions
from replit import db

red = discord.Colour.red()

class submissions(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def new(self, ctx, thing, *, monster=None):
        await functions.open_account(ctx.author.id)
        await functions.save(user=ctx.author.id, amount=10)
        embed=discord.Embed(
            title=f'{ctx.author.name} has posted a new {thing}',
            description=f'Here it is:\n{monster}',
            colour=red
        )
        embed.set_footer(text='Do you like it? 🤔')
        await ctx.send(f'{thing} submitted succesfully')
        channel = 747144603077050498
        channel = ctx.guild.get_channel(channel)
        await channel.send('<@&747148925219111002>', embed=embed)
        
    @commands.command()
    async def score(self, ctx, user : discord.Member = None):
        if user == None:
            await functions.open_account(ctx.author.id)
            score, dc = db[ctx.author.id].split(',')
            await ctx.send(f'__Score:__ {score}\n__Design Count:__ {dc}')
        else:
            await functions.open_account(user.id)
            score, dc = db[user.id].split(',')
            await ctx.send(f'__Score:__ {score}\n__Design Count:__ {dc}')

def setup(bot):
    bot.add_cog(submissions(bot))
