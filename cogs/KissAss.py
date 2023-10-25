import discord
import random
from discord.ext import commands
from discord.utils import get
from cogs.Player import *
from cogs.PvPGame import *
from main import game

from apikeys import *

class KissAss(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(brief="The teacher forgot to assign their homework, so you're gonna help the class out by reminding them.")
    @commands.has_role("Kiss-Ass")
    async def askAboutHomework(self, ctx):
        contestant = get(ctx.guild.roles, name="Contestants")
        if contestant in ctx.author.roles and ctx.channel.id == ARENA:
            baseDamage = 10
            finalDamage = 0
            multiplier = random.randrange(1, 20)

            # Bad Roll
            if multiplier < 3:
                baseDamage = 0
                await ctx.send(f'The class all turns in their chairs as {ctx.author.mention} reminds Matt that he forgot to assign the 22 hour long SAP assignment for the week. Tomatoes and chairs are subsequently thrown at their head. **No Damage Dealt. (Rolled a {multiplier})**')

            # Successful Roll
            elif multiplier >= 3 and multiplier < 18:
                finalDamage = baseDamage + round((((multiplier - 2)/100) * baseDamage), 2)
                await ctx.send(f'{ctx.author.mention} asks Matt about the homework he forgot to assign, but luckily he does not hear you. The students around them quickly subdue the threat and tapes their mouth shut, saving them from the class beating. **Base Damage ({baseDamage}) increased by {(multiplier - 5)}%! (Rolled a {multiplier})**')

            # High Roll
            elif multiplier > 18 and multiplier <= 20:
                baseDamage = 14
                finalDamage = baseDamage + round((((multiplier)/100) * baseDamage), 2)
                await ctx.send(f'{ctx.author.mention} asks about potentially postponing the 22 hour SAP Assignment due to the overwhelming class hatred that is had for the assignments. Matt says fuck it and proceeds to cancel the course as a whole. Screams and cheers erupt from the class, and {ctx.author.username} is praised as a hero. **Base damage increased to {baseDamage} and has a damage bonus of {(multiplier)}%! (Rolled a {multiplier})**')

            await ctx.send(f'{finalDamage} Damage Dealt!')
            return [1, finalDamage]
        elif contestant not in ctx.author.roles and ctx.channel.id != ARENA:
            await ctx.send(f'{ctx.author.mention} is not a contestant and is not in the Arena channel. Type ***!initiateFight @username*** to initiate a battle!')
        elif contestant not in ctx.author.roles and ctx.channel.id == ARENA:
            await ctx.send(f'{ctx.author.mention} is not a contestant.')
        elif contestant in ctx.author.roles and ctx.channel.id != ARENA:
            await ctx.send(f'{ctx.author.mention} is not in the Arena channel. Get back in the fight!')

    @commands.command(brief="You think students seem to lack understanding in a particular subject (*they understand the subject completely*) so you need to explain the concept to them in a way that you understand it.")
    @commands.has_role("Kiss-Ass")
    async def needlesslyExplain(self, ctx):
        contestant = get(ctx.guild.roles, name="Contestants")
        if contestant in ctx.author.roles and ctx.channel.id == ARENA:
            baseDamage = 8
            finalDamage = 0
            multiplier = random.randrange(1, 15)
            user = game.get_player(ctx.author)

            # Bad Roll
            if multiplier < 15:
                baseDamage = 0
                user.hp -= 12
                await ctx.send(f'The students did not need {ctx.author.mention} to explain shit to them so they, understandably, beat your ass. **(12 HP lost. HP: {user.hp}) (Rolled a {multiplier})**')

            # Successful Roll
            elif multiplier >= 15 and multiplier < 25:
                finalDamage = baseDamage + round((((multiplier - 5)/100) * baseDamage), 2)
                await ctx.send(f'{ctx.author.mention} needlessly explained several concepts, which the students barely listened to and will not remember. At least you can think you accomplished something? **Base Damage ({baseDamage}) increased by {(multiplier - 5)}%! (Rolled a {multiplier})**')

            # High Roll
            elif multiplier >= 25 and multiplier <= 45:
                baseDamage = 10
                finalDamage = baseDamage + round((((multiplier + 2)/100) * baseDamage), 2)
                await ctx.send(f'The students think {ctx.author.mention} is dumb as hell so, out of pity, they pay attention to the bullshit that they are spewing. You think they have paid attention to said bullshit, so you feel incredibly accomplished. **Base damage increased to {baseDamage} and has a damage bonus of {(multiplier + 2)}%! (Rolled a {multiplier})**')

            # Highest Roll
            elif multiplier >= 46 and multiplier <= 50:
                baseDamage = 14
                finalDamage = baseDamage + round((((multiplier + 5)/100) * baseDamage), 2)
                await ctx.send(f'{ctx.author.mention} just so happened to intelligently explain something to some people who need it. It is a fucking miracle. **Base damage increased to {baseDamage} and has a damage bonus of {(multiplier + 5)}%! (Rolled a {multiplier})**')
            
            finalDamage = summon_Check(ctx, finalDamage, user.MattBuff, user.willBuff, user.benBuff, user.melissaBuff, user.bradBuff)

            await ctx.send(f'{finalDamage} Damage Dealt!')
            return [1, finalDamage]
        
        elif contestant not in ctx.author.roles and ctx.channel.id != ARENA:
            await ctx.send(f'{ctx.author.mention} is not a contestant and is not in the Arena channel. Type ***!initiateFight @username*** to initiate a battle!')
        elif contestant not in ctx.author.roles and ctx.channel.id == ARENA:
            await ctx.send(f'{ctx.author.mention} is not a contestant.')
        elif contestant in ctx.author.roles and ctx.channel.id != ARENA:
            await ctx.send(f'{ctx.author.mention} is not in the Arena channel. Get back in the fight!')

    @commands.command(brief="High chance to summon Matt for damage increase on next three turns.")
    @commands.has_role("Kiss-Ass")
    async def divineDesjardins(self, ctx):
        await ctx.send(f'{ctx.author.mention} has gotten divine intervention from Melissa!')

    @commands.command(brief="Low chance to summon Brad for 10 extra damage on next three turns.")
    @commands.has_role("Kiss-Ass")
    async def bjjBrad(self, ctx):
        await ctx.send(f'{ctx.author.mention} has gotten divine intervention from Melissa!')

    @commands.command(brief="Medium chance to summon Melissa for 50% damage reduction on next two turns.")
    @commands.has_role("Kiss-Ass")
    async def minderMelissa(self, ctx):
        await ctx.send(f'{ctx.author.mention} has gotten divine intervention from Melissa!')

    @commands.command(brief="Medium chance to summon Will to return 33% damage taken on next three turns.")
    @commands.has_role("Kiss-Ass")
    async def willOfWill(self, ctx):
        await ctx.send(f'{ctx.author.mention} has gotten divine intervention from Melissa!')

    @commands.command(brief="High chance to summon Ben to heal 20 HP over the next two turns.")
    @commands.has_role("Kiss-Ass")
    async def bigBen(self, ctx):
        await ctx.send(f'{ctx.author.mention} has gotten divine intervention from Melissa!')

    @commands.command()
    @commands.has_role("Kiss-Ass")
    async def chimken(self, ctx):
        await ctx.send('https://tenor.com/bFuYJ.gif')

    @commands.command()
    @commands.has_role("Kiss-Ass")
    async def barmey(self, ctx):
        await ctx.send('https://tenor.com/bprDm.gif')

    @commands.command()
    @commands.has_role("Kiss-Ass")
    async def unless(self, ctx):
        await ctx.send('https://tenor.com/bzrXE.gif')

async def summon_Check(user, atkDmg, mattBuff, willBuff, benBuff, melissaBuff, bradBuff):
    if (mattBuff > 0 or willBuff > 0 or benBuff > 0 or melissaBuff > 0 or bradBuff > 0):
            if (mattBuff > 0):
                atkDmg = atkDmg * 1.2
                user.send(f'The deity Matt has blessed the attack with **15% extra damage**!')
            if (benBuff > 0):
                user.hp = user.hp + 10
                user.send(f'Ben the magical fairy has healed you for 10 HP! **(Current HP: {user.hp})**')
            if (bradBuff > 0):
                atkDmg = atkDmg + 20
                user.send(f'Black Belt Brad has joined you on your attack, and has hit the opponent with **20 extra damage**!')
            if (willBuff > 0):
                atkDmg = atkDmg * 1.2
                user.send(f'The Wizard Will has returned 33% of your damage taken onto them!')
            if (melissaBuff > 0):
                user.hp = user.hp + 10
                user.send(f'Mother Melissa has reduced your damage taken by 50%!')
            return atkDmg
    
def kissass_Check(self, attacker, target, returnDmg):
    if (target.willBuff > 0):
        atkDmg = returnDmg / 3
        attacker.hp = attacker.hp - atkDmg
        game.attack(self, attacker, target, atkDmg)

    if (target.melissaBuff > 0):
        resDmg = returnDmg * .5
        return resDmg
    else:
        return returnDmg

async def setup(client):
    await client.add_cog(KissAss(client))