import os
os.system('pip install --upgrade pip')
os.system('pip install python-dotenv')
os.system('pip install hoster')
os.system('pip install discord.py')
os.system('pip install hcolours')
os.system('pip install henostools')
os.system('clear')
import discord
from discord.ext import commands#, tasks
from dotenv import load_dotenv
import hoster
import functions
from replit import db
import hcolours
import henostools

intents = discord.Intents.all()
status = 'ML:  Monster Designers'
mlmd = commands.Bot(command_prefix = commands.when_mentioned_or('mlmd: ', 'mlmd:', 'Mlmd:', 'Mlmd: ', 'MLMD:', 'MLMD: '), intents=intents, activity=discord.Activity(type=discord.ActivityType.watching, name=status))
red = discord.Colour.red()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

@mlmd.event
async def on_command_error(ctx, error):
    if not isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(
              title='Oh no!',
              description=f'There was a error with the {ctx.command.name} command\n\nError: {error}',
              colour=red
            )
        await ctx.send(embed=embed)
    else:
        await ctx.send('Command not found')

@mlmd.event
async def on_message(message):
    await functions.open_account(message.author.id)
    reason = 'score autorole'
    score, dc = db[message.author.id].split(',')
    score = int(score)
    if score >= 500:
        cmdid = message.guild.get_role(736919708179234867)
        if not cmdid in message.author.roles:
            await message.author.add_roles(cmdid, reason=reason)
            embed = discord.Embed(
              title='Level Up!!',
              description=f'{message.author.mention} leveled up to {cmdid.mention}!!',
              colour=red
            )
            embed.set_footer(text='Well Done!')
            channel = message.guild.get_channel(772925251889135627)
            await channel.send(embed=embed)
    if score >= 400:
        mmdid = message.guild.get_role(738488304948871309)
        if not mmdid in message.author.roles:
            await message.author.add_roles(mmdid, reason=reason)
            embed = discord.Embed(
              title='Level Up!!',
              description=f'{message.author.mention} leveled up to {mmdid.mention}!!',
              colour=red
            )
            embed.set_footer(text='Well Done!')
            channel = message.guild.get_channel(772925251889135627)
            await channel.send(embed=embed)
    if score >= 300:
        fmdid = message.guild.get_role(738488456220639312)
        if not fmdid in message.author.roles:
            await message.author.add_roles(fmdid, reason=reason)
            embed = discord.Embed(
              title='Level Up!!',
              description=f'{message.author.mention} leveled up to {fmdid.mention}!!',
              colour=red
            )
            embed.set_footer(text='Well Done!')
            channel = message.guild.get_channel(772925251889135627)
            await channel.send(embed=embed)
    if score >= 200:
        elmdid = message.guild.get_role(736919360047677450)
        if not elmdid in message.author.roles:
            await message.author.add_roles(elmdid, reason=reason)
            embed = discord.Embed(
              title='Level Up!!',
              description=f'{message.author.mention} leveled up to {elmdid.mention}!!',
              colour=red
            )
            embed.set_footer(text='Well Done!')
            channel = message.guild.get_channel(772925251889135627)
            await channel.send(embed=embed)
    if score >= 150:
        nmdid = message.guild.get_role(738488670344052798)
        if not nmdid in message.author.roles:
            await message.author.add_roles(nmdid, reason=reason)
            embed = discord.Embed(
              title='Level Up!!', 
              description=f'{message.author.mention} leveled up to {nmdid.mention}!!',
              colour=red
            )
            embed.set_footer(text='Well Done!')
            channel = message.guild.get_channel(772925251889135627)
            await channel.send(embed=embed)
    if score >= 100:
        lmdid = message.guild.get_role(738488853110849566)
        if not lmdid in message.author.roles:
            await message.author.add_roles(lmdid, reason=reason)
            embed = discord.Embed(
              title='Level Up!!',
              description=f'{message.author.mention} leveled up to {lmdid.mention}!!',
              colour=red
            )
            embed.set_footer(text='Well Done!')
            channel = message.guild.get_channel(772925251889135627)
            await channel.send(embed=embed)
    if score >= 75:
        emdid = message.guild.get_role(738488995927031898)
        if not emdid in message.author.roles:
            await message.author.add_roles(emdid, reason=reason)
            embed = discord.Embed(
              title='Level Up!!',
              description=f'{message.author.mention} leveled up to {emdid.mention}!!',
              colour=red
            )
            embed.set_footer(text='Well Done!')
            channel = message.guild.get_channel(772925251889135627)
            await channel.send(embed=embed)
    if score >= 50:
        rmdid = message.guild.get_role(738489190450331799)
        if not rmdid in message.author.roles:
            await message.author.add_roles(rmdid, reason=reason)
            embed = discord.Embed(
              title='Level Up!!',
              description=f'{message.author.mention} leveled up to {rmdid.mention}!!',
              colour=red
            )
            embed.set_footer(text='Well Done!')
            channel = message.guild.get_channel(772925251889135627)
            await channel.send(embed=embed)
    if score >= 25:
        umdid = message.guild.get_role(738489281647214612)
        if not umdid in message.author.roles:
            await message.author.add_roles(umdid, reason=reason)
            embed = discord.Embed(
              title='Level Up!!',
              description=f'{message.author.mention} leveled up to {umdid.mention}!!',
              colour=red
            )
            embed.set_footer(text='Well Done!')
            channel = message.guild.get_channel(772925251889135627)
            await channel.send(embed=embed)
    if score >= 10:
        cmdid = message.guild.get_role(736919165704863755)
        if not cmdid in message.author.roles:
            await message.author.add_roles(cmdid, reason=reason)
            embed = discord.Embed(
              title='Level Up!!',
              description=f'{message.author.mention} leveled up to {cmdid.mention}!!',
              colour=red
            )
            embed.set_footer(text='Well Done!')
            channel = message.guild.get_channel(772925251889135627)
            await channel.send(embed=embed)
    await mlmd.process_commands(message)

# @mlmd.command()
# async def transfer(ctx, user : discord.Member = None):
#     await functions.open_account(user.id)
#     with open('score.json', 'r') as rf:
#         score = json.load(rf)
#     score1 = score[str(user.id)]['score']
#     dc = score[str(user.id)]['dc']
#     db[str(user.id)] = f'{score1},{dc}'
#     await ctx.send('Done!')

@mlmd.event
async def on_ready():
    print(f'{mlmd.user} is online!')
    await henostools.sleep('5s')
    print(f'{hcolours.colour.red}Guild Count:{hcolours.reset} {len(mlmd.guilds)}')
    print(f'{hcolours.colour.red}Member Count:{hcolours.reset} {len(mlmd.users)}')

extentions = [
  'cogs.henostools',
  'cogs.other',
  'cogs.submissions'
]
for extention in extentions:
    mlmd.load_extension(extention)

@mlmd.event
async def on_member_join(member):
    channel = 747144549226381382
    channel = mlmd.get_channel(channel)
    await member.send(
        f'Hi {member.name}, welcome to {member.guild.name}!, use `mlmd: help` to get a list of the commands'
    )
    await channel.send(
        f'Hi {member.name}, welcome to {member.guild.name}!, use `mlmd: help` to get a list of the commands'
    )

# @mlmd.event
# async def on_member_update(before, after):
#     channel = mlmd.get_channel('mod-log')
#     embed = discord.Embed(
#       title='Member Update',
#     )
#     await channel.send(embed=embed)

hoster.start(ip='0.0.0.0', port=8080)
mlmd.run(TOKEN)
