import discord
from discord.ext import commands
from apikeys import *

intents = discord.Intents.all()
intents.members = True
intents.messages = True

client = commands.Bot(command_prefix = '!', intents=intents)

@client.event
async def on_ready():
    print('Uncivil Discourse is ready to commence.')
    print('---------------------------------------')

@client.command()
async def hello(ctx):
    await ctx.send(f'Hello, {ctx.author.mention}!')

@client.command()
async def dumbass(ctx):
    await ctx.send(f'The dumbass is {client.get_user(882613199466278953).display_name}!')

@client.event
async def on_member_join(member):
    channel = client.get_channel(GENERALID)
    await channel.send('Message')

client.run(DISCORDTOKEN)