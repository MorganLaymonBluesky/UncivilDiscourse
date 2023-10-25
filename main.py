import os
import discord
from discord.ext import commands
from discord.utils import get
import asyncio

from cogs.PvPGame import *
from apikeys import *

intents = discord.Intents.all()
intents.members = True
intents.messages = True

client = commands.Bot(command_prefix = '!', intents=intents)
client.add_cog(client)

initial_extensions = []

@client.event
async def on_ready():
    print('Uncivil Discourse is ready to commence.')
    print('---------------------------------------')

async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            initial_extensions.append('cogs.' + filename[:-3])

    for extension in initial_extensions:
        await client.load_extension(extension)

    print(initial_extensions)

async def main():
    await load()
    await client.start(DISCORDTOKEN)
    contestant = get(client.guild.roles, name="Contestants")
    for member in contestant.members:
        await member.kick()

game = PvPGame()

@client.command()
async def initiateFight(ctx, target:discord.Member):
    await ctx.send(f'{ctx.author.name} wants to fight {target.name}! {target.name}, enter ***!deny @{ctx.author.name}*** to decline this invitation, or enter the arena to begin your battle!')
    channel = client.get_channel(ARENA)
    player1 = Player(ctx.author)
    player2 = Player(target)
    game.add_player(player1)
    game.add_player(player2)
    cont1 = ctx.message.author
    cont2 = target
    contestant = get(ctx.guild.roles, name="Contestants")
    await cont1.add_roles(contestant)
    await cont2.add_roles(contestant)

@client.command()
async def deny(ctx, target:discord.Member):
    contestant = get(ctx.guild.roles, name="Contestants")
    user = ctx.author
    if contestant in ctx.author.roles:
        await user.remove_roles(contestant)
        await target.remove_roles(contestant)
        game.remove_players()
        await ctx.send(f'{user} has declined the invitation to battle {target.name}.')
    else:
        await ctx.send(f'{user} has no invites to decline.')

@client.command()
async def leave(ctx):
    channel = client.get_channel(ARENA)
    player = game.get_player(ctx.author)
    if player:
        game.remove_players()
        await ctx.send(f'{ctx.author.name} has ran away, coward')
        await channel.set_permissions(ctx.author, send_messages=False)
    else:
        await ctx.send('You are not in a fight. You can not escape yourself')



@client.command()
async def attack(ctx, target:discord.Member, move):
    attacker = game.get_player(ctx.author)
    target_player = game.get_player(target)
    
    if attacker and target_player:
        Moveresult = await ctx.invoke(client.get_command(move))
        print(Moveresult)

        if Moveresult is not None:
            if Moveresult[0] == 1:
                result = game.attack(attacker, target_player, Moveresult[1])
                print(result)
                await ctx.send(result)

            elif Moveresult[0] == 2:
                result = game.heal(attacker, Moveresult[1])
                print(result)
                await ctx.send(result)
            
            elif Moveresult[0] == 3:
                resultY = game.damageSelf(attacker, Moveresult[2])
                resultX = game.attack(attacker, target_player, Moveresult[1])
                await ctx.send(resultY)
                await ctx.send(resultX)
                
            elif Moveresult[0] == 4:
                result = game.changeBuff(attacker, Moveresult[1])
                await ctx.send(result)

            else:
                await ctx.send('Zach fucked up, point and laugh')
        else:
            await ctx.send('Failed to find the move you were looking for')
    else:
        await ctx.send('Either you or your target are not in the battle')

asyncio.run(main())