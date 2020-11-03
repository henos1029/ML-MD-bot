import discord
from discord.ext import commands
import functions
from replit import db

red = discord.Colour.red()

class henostools(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def add(ctx, user : discord.Member, amount : int):
        await functions.open_account(user.id)
        await functions.save(user=user.id, amount=amount)
        await ctx.send(f"Added {amount} to {user.mention}'s score and {round(amount / 10)} to their dc!")

    @commands.command()
    @commands.is_owner()
    async def remove(ctx, user : discord.Member, amount : int):
        await functions.open_account(user.id)
        score, dc = db[user.id].split(',')
        score2 = int(score) - amount
        amount2 = round(amount / 10)
        dc2 = int(dc) - amount2
        db[user.id] = f'{score2},{dc2}'
        await ctx.send(f"Removed {amount} from {user.mention}'s score and {amount2} from their dc!")

    @commands.command()
    @commands.is_owner()
    async def set(ctx, user : discord.Member, amount : int):
        await functions.open_account(user.id)
        score, dc = db[user.id].split(',')
        score2 = amount
        amount2 = round(amount / 10)
        dc2 = amount2
        db[user.id] = f'{score2},{dc2}'
        await ctx.send(f"Set {user.mention}'s score as {amount} and {amount2} as their dc!")

def setup(bot):
    bot.add_cog(henostools(bot))
