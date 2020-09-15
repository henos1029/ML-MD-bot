import os
from discord.ext import commands, tasks
import discord
from dotenv import load_dotenv
import logging
import json
import typing
client = commands.Bot(command_prefix = 'mlmd: ')
red = discord.Colour.red()

os.chdir('C:\\Users\\SPI0003\\OneDrive - boxhillhs.vic.edu.au\\Home\\Coding\\discord bot\\ml md bot')

# logging.basicConfig(level=logging.INFO)

# logger = logging.getLogger('discord')
# logger.setLevel(logging.DEBUG)
# handler = logging.FileHandler(filename='errors.log', encoding='utf-8', mode='w')
# handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
# logger.addHandler(handler)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

@client.command()
async def new(ctx, thing, *, monster=None):
    with open('score.json', 'r') as rf:
        score = json.load(rf)
    if str(ctx.author.id) not in score:
        score[str(ctx.author.id)]={'score': 0, 'dc': 0}
        with open("score.json", "w") as wf:
            json.dump(score, wf)    
    score[str(ctx.author.id)]['score'] = score[str(ctx.author.id)]['score'] + 10
    score[str(ctx.author.id)]['dc'] = score[str(ctx.author.id)]['dc'] + 1
    with open("score.json", "w") as wf:
            json.dump(score, wf)
    embed=discord.Embed(
        title=f'{ctx.author.name} has posted a new {thing}',
        description=f'Here it is:\n{monster}',
        colour=red
    )
    embed.set_footer(text='Do you like it? 🤔')
    await ctx.send(f'{thing} submitted succesfully')
    channel = 747144603077050498
    channel = client.get_channel(channel)
    await channel.send('<@&747148925219111002>', embed=embed)
    
@client.command()
async def score(ctx, user : discord.Member = None):
    if user == None:
        with open('score.json', 'r') as rf:
            score = json.load(rf)
        if str(ctx.author.id) not in score:
            score[str(ctx.author.id)]={'score': 0, 'dc': 0}
            with open("score.json", "w") as wf:
                json.dump(score, wf)
        score1 = score[str(ctx.author.id)]['score']
        dc = score[str(ctx.author.id)]['dc']
        await ctx.send(f'__Score:__ {score1}\n__Design Count:__ {dc}')
    else:
        with open('score.json', 'r') as rf:
            score = json.load(rf)
        if str(user.id) not in score:
            score[str(user.id)]={'score': 0, 'dc': 0}
            with open("score.json", "w") as wf:
                json.dump(score, wf)
        score1 = score[str(user.id)]['score']
        dc = score[str(user.id)]['dc']
        await ctx.send(f'__Score:__ {score1}\n__Design Count:__ {dc}')

@client.event
async def on_ready():
    user_count = len(client.users)
    status = f'{user_count} members in ML:  Monster Designers'
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status))
    print(f'{client.user} is online!')

@client.event
async def on_member_join(member):
    channel = 747144549226381382
    channel = client.get_channel(channel)
    await member.send(
        f'Hi {member.name}, welcome to {member.guild.name}!, use `:commands` to get a list of the commands'
    )
    await channel.send(
        f'Hi {member.name}, welcome to {member.guild.name}!, use `:commands` to get a list of the commands'
    )

@client.command()
async def ping(ctx):
    embed = discord.Embed(
    title="__Pong__",
    description=f'{round(client.latency * 1000)} ms',
    colour=red
        )
    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=1000):
    await ctx.channel.purge(limit=amount)
    embed=discord.Embed(    
    title='__Clear!__',
    description=f'{ctx.author.mention}, I have cleared some messages for you',
    footer=f'Deleting in 30 seconds',
    colour=red
    )
    await ctx.send(embed=embed, delete_after=30)

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    embed=discord.Embed(
    title='__Ban!__',
    description=f'{member.name}#{member.discriminator} was banned from {member.guild.name}',
    footer=f'Reason: {reason}',
    colour=red
    )
    await ctx.send(embed=embed)
    
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    embed=discord.Embed(
    title='__Kick!__',
    description=f'{member.name}#{member.discriminator} was kicked from {member.guild.name}',
    footer=f'Reason: {reason}',
    colour=red
    )
    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *,member):
    unbanned_member = discord.Object(id=int(member.id))
    await member.unban(unbanned_member)
    embed=discord.Embed(
    title='__Unban!__',
    description='{member.name}#{member.discriminator} was unbaned from {member.guild.name}',
    footer='they can now rejoin',
    colour=red
    )
    await ctx.send(embed=embed)

client.run(TOKEN)