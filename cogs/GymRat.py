import discord
from discord.ext import commands
from apikeys import *
import random

from cogs.Player import *
from cogs.PvPGame import *
from main import game


class GymRat(commands.Cog):
    def __init__(self, client):
        self.client = client
    

    #### LOW MOVE ####
    @commands.command(brief="By using the magical elixir(TREN), you use your new gains to punch the opponent.", description="full desc")
    @commands.has_role("Gym Rat")
    async def trenythingIsPossible(self, ctx):
        baseDamage = 10
        finalDamage = 0
        multiplier = random.randrange(1, 20)
        attacker = game.get_player(ctx.author)
        sb = attacker.buff

        # Bad Roll
        if multiplier < 3:
            baseDamage = 0
            await ctx.send(f'The TREN you bought was secretly toilet water from your local Food City, {ctx.author.mention} got no gains. (Rolled a {multiplier})')

        # Successful Roll
        elif multiplier >= 3 and multiplier < 18:
            finalDamage = baseDamage + round(((((multiplier - 3)/100) * baseDamage) * sb), 2)
            await ctx.send(f'{ctx.author.mention} your gains are showing, you recieve a damage bonus of {(multiplier - 3)}%! (Rolled a {multiplier})')

        # High Roll
        elif multiplier > 18 and multiplier <= 20:
            baseDamage = 15
            if sb == 2:
                finalDamage = 50
                await ctx.send(f'WOW {ctx.author.mention}! Your opponent was not ready for you level 15 skills paired with you GOD COMPLEX!')
                await ctx.send('https://tenor.com/view/zyzz-gif-24316331')
            else:
                finalDamage = baseDamage + round(((((multiplier - 3)/100) * baseDamage) * sb), 2)
                await ctx.send(f'WOW {ctx.author.mention}! Your opponent was not ready for you level 15 skills. Base damage increased to {baseDamage} and has a damage bonus of {(multiplier - 3)}%! (Rolled a {multiplier})')
                await ctx.send('https://tenor.com/view/zyzz-gif-24316331')

        await ctx.send(f'{round(finalDamage, 2)} Damage Dealt!')
        attacker.buff = 1
        return [1, finalDamage]


    ####### DONE #######
    #### LOW MOVE ####
    @commands.command()
    @commands.has_role("Gym Rat")
    async def stairStomper(self, ctx):
        baseDamage = 10
        finalDamage = 0
        multiplier = random.randrange(1, 20)
        attacker = game.get_player(ctx.author)
        sb = attacker.buff

        # Bad Roll
        if multiplier < 3:
            baseDamage = 0
            await ctx.send(f'You trip! {ctx.author.mention} you stomp nothing, but thank you for checking gravity. (Rolled a {multiplier})')

        # Successful Roll
        elif multiplier >= 3 and multiplier < 18:
            finalDamage = baseDamage + round(((((multiplier - 3)/100) * baseDamage) * sb), 2)
            await ctx.send(f'{ctx.author.mention} you stomp the competition with a damage bonus of {(multiplier - 3)}%! (Rolled a {multiplier})')

        # High Roll
        elif multiplier > 18 and multiplier <= 20:
            baseDamage = 15
            if sb == 2:
                finalDamage = 25
                await ctx.send(f'WOW {ctx.author.mention}! Your opponent was not ready for you level 15 skills paired with you GOD COMPLEX!')
                await ctx.send('https://tenor.com/view/zyzz-gif-24316331')
            else:
                finalDamage = baseDamage + round(((((multiplier - 3)/100) * baseDamage) * sb), 2)
                await ctx.send(f'WOW {ctx.author.mention}! Your opponent was not ready for you level 15 skills. Base damage increased to {baseDamage} and has a damage bonus of {(multiplier - 3)}%! (Rolled a {multiplier})')
                await ctx.send('https://tenor.com/view/zyzz-gif-24316331')

        await ctx.send(f'{round(finalDamage, 2)} Damage Dealt!')
        attacker.buff = 1
        return [1, finalDamage]
        


    @commands.command()
    @commands.has_role("Gym Rat")
    async def thighsOfThunder(self, ctx):
        baseDamage = 10
        finalDamage = 0
        multiplier = random.randrange(1, 20)
        attacker = game.get_player(ctx.author)
        sb = attacker.buff

        # Bad Roll
        if multiplier < 3:
            baseDamage = 0
            await ctx.send(f'You trip! {ctx.author.mention} you stomp nothing, but thank you for checking gravity. (Rolled a {multiplier})')

        # Successful Roll
        elif multiplier >= 3 and multiplier < 18:
            finalDamage = baseDamage + round(((((multiplier - 3)/100) * baseDamage) * sb), 2)
            await ctx.send(f'{ctx.author.mention} you stomp the competition with a damage bonus of {(multiplier - 3)}%! (Rolled a {multiplier})')

        # High Roll
        elif multiplier > 18 and multiplier <= 20:
            baseDamage = 14
            if sb == 2:
                finalDamage = 50
                await ctx.send(f'WOW {ctx.author.mention}! Your opponent was not ready for you level 15 skills paired with you GOD COMPLEX!')
                await ctx.send('https://tenor.com/view/zyzz-gif-24316331')
            else:
                finalDamage = baseDamage + round(((((multiplier - 3)/100) * baseDamage) * sb), 2)
                await ctx.send(f'WOW {ctx.author.mention}! Your opponent was not ready for you level 15 skills. Base damage increased to {baseDamage} and has a damage bonus of {(multiplier - 3)}%! (Rolled a {multiplier})')
                await ctx.send('https://tenor.com/view/zyzz-gif-24316331')

        await ctx.send(f'{round(finalDamage, 2)} Damage Dealt!')
        attacker.buff = 1
        return [1, finalDamage]
    

    @commands.command()
    @commands.has_role("Gym Rat")
    async def roidRage(self, ctx):
        baseDamage = 10
        finalDamage = 0
        multiplier = random.randrange(1, 20)
        attacker = game.get_player(ctx.author)
        sb = attacker.buff

        # Bad Roll
        if multiplier < 3:
            baseDamage = 0
            await ctx.send(f'You trip! {ctx.author.mention} you stomp nothing, but thank you for checking gravity. (Rolled a {multiplier})')

        # Successful Roll
        elif multiplier >= 3 and multiplier < 18:
            finalDamage = baseDamage + round(((((multiplier - 3)/100) * baseDamage) * sb), 2)
            await ctx.send(f'{ctx.author.mention} you stomp the competition with a damage bonus of {(multiplier - 3)}%! (Rolled a {multiplier})')

        # High Roll
        elif multiplier > 18 and multiplier <= 20:
            baseDamage = 14
            if sb == 2:
                finalDamage = 40
                await ctx.send(f'WOW {ctx.author.mention}! Your opponent was not ready for you level 15 skills paired with you GOD COMPLEX!')
                await ctx.send('https://tenor.com/view/zyzz-gif-24316331')
            else:
                finalDamage = baseDamage + round(((((multiplier - 3)/100) * baseDamage) * sb), 2)
                await ctx.send(f'WOW {ctx.author.mention}! Your opponent was not ready for you level 15 skills. Base damage increased to {baseDamage} and has a damage bonus of {(multiplier - 3)}%! (Rolled a {multiplier})')
                await ctx.send('https://tenor.com/view/zyzz-gif-24316331')

        await ctx.send(f'{round(finalDamage, 2)} Damage Dealt!')
        attacker.buff = 1
        return [1, finalDamage]
    
    #### HIGHEST MOVE ####
    @commands.command()
    @commands.has_role("Gym Rat")
    async def goForPR(self, ctx):
        baseDamage = 20
        finalDamage = 0
        multiplier = random.randrange(1, 20)
        attacker = game.get_player(ctx.author)
        sb = attacker.buff

        # Bad Roll
        if multiplier < 8:
            baseDamage = 0
            await ctx.send(f'You failed...and you gym crush was watching...{ctx.author.mention} you are a disgrace. (Rolled a {multiplier})')

        # Successful Roll
        elif multiplier >= 8 and multiplier < 18:
            finalDamage = baseDamage + round(((((multiplier - 8)/100) * baseDamage) * sb), 2)
            await ctx.send(f'{ctx.author.mention} you got a new PR! You use your addrenalin boost to increase your attack by {(multiplier - 3)}%! (Rolled a {multiplier})')

        # High Roll
        elif multiplier > 18 and multiplier <= 20:
            baseDamage = 25
            if sb == 2:
                finalDamage = 40
                await ctx.send(f'YOUR GOD COMPLEX IS SHOWING! YOUR PR HAS INCREASED BY OVER 20LBS {ctx.author.mention}! AFTER YOUR SUCCESS YOU JAZALYN THROW YOUR BAR WITH THE WEIGHTS STILL ON AT YOUR OPPONENT!')
                await ctx.send('https://tenor.com/view/personal-record-mindovermatterfitness-fitness-gym-lifting-gif-18357628')
            else:
                finalDamage = baseDamage + round(((((multiplier - 8)/100) * baseDamage) * sb), 2)
                await ctx.send(f'YOUR PR HAS INCREASED BY OVER 20LBS {ctx.author.mention}! AFTER YOUR SUCCESS YOU JAZALYN THROW YOUR BAR WITH THE WEIGHTS STILL ON AT YOUR OPPONENT WITH A BASE DAMAGE OF {baseDamage} AND DAMAGE BONUS OF {(multiplier - 3)}%! (Rolled a {multiplier})')
                await ctx.send('https://tenor.com/view/personal-record-mindovermatterfitness-fitness-gym-lifting-gif-18357628')

        await ctx.send(f'{round(finalDamage, 2)} Damage Dealt!')
        attacker.buff = 1
        return [1, finalDamage]

    ####### DONE #######
    @commands.command()
    @commands.has_role("Gym Rat")
    async def MirrorCheck(self, ctx):
        multiplier = random.randrange(1, 20)
        
        # Bad Roll
        if multiplier < 10:
            sb = 0.5 
            await ctx.send('You checked the mirror and recieved crippling body dysmorphia ' + ctx.author.mention + '! Your next move will only do half damage.')
            await ctx.send('https://tenor.com/view/personal-record-mindovermatterfitness-fitness-gym-lifting-gif-18357628')


        # High Roll
        elif multiplier >= 10 and multiplier <= 20:
            sb = 2
            await ctx.send('YOU HAVE THE PHYSIQUE OF A GREEK GOD ' + ctx.author.mention + '! WITH YOUR NEW FOUND GOD COMPLEX YOUR NEXT MOVE DOES DOUBLE DAMAGE!')
            await ctx.send('https://tenor.com/view/borderlands-anarchy-gaige-borderlands2-gif-25398053')


        return[4, sb]

async def setup(client):
    await client.add_cog(GymRat(client))