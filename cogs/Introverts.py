import discord
from discord.ext import commands
from apikeys import *
from cogs.Player import *
from cogs.PvPGame import *
from main import game


class Introverts(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(brief = 'Deal 15 damage, take 3 hp')
    @commands.has_role("Introvert")
    async def deafeningSilence(self, ctx):
        await ctx.send(f'{ctx.author.mention} looks at you with judgment and says nothing, taking damage themselves from the awkwardness')
        #await ctx.send('https://tenor.com/view/wtf-stranger-things-steve-gif-25802354')

        attacker = game.get_player(ctx.author)
        attacker.hp -= 3
        
        return [1, 15]

    @commands.command(brief = 'Heals 10 hp, deal 5 damage, up SB by 0.75')
    @commands.has_role("Introvert")
    async def slipAway(self, ctx):
        await ctx.send(f'{ctx.author.mention} slips away from all the people, regaining hp and some social battery (now at {self.buff})')
        #await ctx.send('https://tenor.com/view/the-simpsons-homer-simpson-bush-hide-bye-gif-16150806')

        attacker = game.get_player(ctx.author)
        attacker.buff += 0.75
        attacker.health += 10

        return [1, 5]
    
    @commands.command(brief = 'Deal 10 damage, up SB by 0.5 ')
    @commands.has_role('Introvert')
    async def annoyBestFriend(self, ctx):
        await ctx.send(f'{ctx.author.mention} finds their best friend!! Together their sheer weirdness alone damages any bystanders and recovers some social battery (now at GO FUCK YOURSELF)')
        #await ctx.send('https://tenor.com/view/good-times-and-crazy-friends-make-the-best-memories-gif-19669131')

        attacker = game.get_player(ctx.author)
        attacker.buff += 0.5
        return [1, 10]
    
    @commands.command(brief = '12.5 x SB damage, SB halfed')
    @commands.has_role('Introvert')
    async def socialize(self, ctx):
        baseDamage = 12.5
        await ctx.send(f'{ctx.author.mention} Gathers their courage and social battery to talk to... *people*. Their social battery is crushed')
        #await ctx.send('https://tenor.com/view/social-interaction-grinch-gif-25790026')
        attacker = game.get_player(ctx.author)
        
        finalDamage = baseDamage * attacker.buff
        attacker.buff = attacker.buff/2

        return[1, finalDamage]
    
    @commands.command(brief = 'Deal 20 x SB damage, set SB to 0')
    @commands.has_role('Introvert')
    async def breakingPoint(self, ctx):
        await ctx.send(f'{ctx.author.mention} has reached thier limit due to your bullshit and gives you a piece of their mind. They are done with people and their social battery is nonexistent (now at {self.buff})')
        #await ctx.send(f'https://tenor.com/view/spongebob-explode-gif-12811206')

        attacker = game.get_player(ctx.author)
        finalDamage = 20 * attacker.buff

        attacker.buff = 0
        return[1,finalDamage]
    
    @commands.command(brief='Deal 5 x SB damage, up SB by 0.25')
    @commands.has_role('Introvert')
    async def hyperfixation(self, ctx):
        baseDamage = 5
        await ctx.send(f'{ctx.author.mention} realized you like something they like. You sit through hours of detailed lore explanation while their social battery grows (now at {self.buff})')
        #await ctx.send(f'https://tenor.com/view/explaining-stressed-crazy-homework-music-gif-13036231')
        attacker = game.get_player(ctx.author)
        finalDamage = baseDamage * attacker.buff
        attacker.buff += 0.25
        return[1,finalDamage]
    


async def setup(client):
    await client.add_cog(Introverts(client))
