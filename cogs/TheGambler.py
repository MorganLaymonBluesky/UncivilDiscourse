import discord
from discord.ext import commands
from apikeys import *
import random

class Gambler(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    @commands.has_role("Gambler")
    async def Welcome(self, ctx):
        await ctx.send(f'Welcome to the table, {ctx.author.mention}!')

    @commands.command()
    @commands.has_role("Gambler")
    async def SeeSkills(self, ctx):
        await ctx.send(f'Welcome to the big house, {ctx.author.mention}!')

    #Special Attack Buff(One Turn)
    @commands.command()
    @commands.has_role("Gambler")
    async def UseRoll(self, ctx):
        multiplier = random.randrange(1, 20)
        # Bad Roll
        if multiplier < 6:
            self.buff = 1.75

        # Successful Roll
        elif multiplier >= 6 and multiplier < 11:
            self.buff = 2.25

        # Bad Roll
        elif multiplier >= 11 and multiplier < 16 :
            self.buff = 2.5

        # High Roll
        elif multiplier >= 16 and multiplier <= 20:
            self.buff = 2.75
            

        await ctx.send('Time to let the good times rollllllll,' + ctx.author.mention + '!')
        await ctx.send('https://tenor.com/view/xqc-gambling-gamble-gambler-gambling-addiction-gif-25801242')
        await ctx.send(f"Your buff for the next turn is {self.buff}")
        

    #Medium Attack
    @commands.command()
    @commands.has_role("Gambler")
    async def UseBottleSmash(self, ctx):
        baseDamage = 20
        finalDamage = [1, 0]
        multiplier = random.randrange(1, 20)

        # Bad Roll
        if multiplier < 3:
            baseDamage = 0
            await ctx.send("https://tenor.com/view/twenty-century-fox-meme-gfy-go-fuck-yourself-meme-get-lost-gif-26260205")

        # Successful Roll
        elif multiplier >= 3 and multiplier < 18:
            finalDamage[1] = baseDamage + round(((((multiplier - 3)/100) * baseDamage) * self.buff), 2)
            await ctx.send(f"Ouch, {ctx.author.mention}, Alcohol is bad for who? Cause you damaged your opponent! {(multiplier - 3)}%! (Rolled a {multiplier})")
            

        # High Roll
        elif multiplier > 18 and multiplier <= 20:
            baseDamage = 14
            finalDamage[1] = baseDamage + round(((((multiplier - 3)/100) * baseDamage) * self.buff), 2)
            await ctx.send(f'{ctx.author.mention} Your supposed to hit them with the bottle, not make a molotov out of it... Base damage increased to {baseDamage} and has a damage bonus of {(multiplier - 3)}%! (Rolled a {multiplier})')
            

        await ctx.send(f'{finalDamage[1]} Damage Dealt!')
        self.buff = 1
        return finalDamage[1]
        

    #Small Attack
    @commands.command()
    @commands.has_role("Gambler")
    async def SoreLoser(self, ctx):
        baseDamage = 10
        finalDamage = [1, 0]
        multiplier = random.randrange(1, 20)

        # Bad Roll
        if multiplier < 3:
            baseDamage = 0
            await ctx.send("https://tenor.com/view/twenty-century-fox-meme-gfy-go-fuck-yourself-meme-get-lost-gif-26260205")

        # Successful Roll
        elif multiplier >= 3 and multiplier < 18:
            finalDamage[1] = baseDamage + round(((((multiplier - 3)/100) * baseDamage) * self.buff), 2)
            await ctx.send(f"{ctx.author.mention} It seems like the rage pulled off in the Gambler's favor... {(multiplier - 3)}%! (Rolled a {multiplier})")  
            

        # High Roll
        elif multiplier > 18 and multiplier <= 20:
            baseDamage = 14
            finalDamage[1] = baseDamage + round(((((multiplier - 3)/100) * baseDamage) * self.buff), 2)
            await ctx.send(f'{ctx.author.mention} THE HOUSE WAS WRONG! Base damage increased to {baseDamage} and has a damage bonus of {(multiplier - 3)}%! (Rolled a {multiplier})')

        await ctx.send(f'{finalDamage[1]} Damage Dealt!')
        self.buff = 1
        return finalDamage[1]
    

    #Big Attack
    @commands.command()
    @commands.has_role("Gambler")
    async def BigWin(self, ctx):
        baseDamage = 30
        finalDamage = [1, 0]
        multiplier = random.randrange(1, 20)

        # Bad Roll
        if multiplier < 3:
            baseDamage = 0
            await ctx.send("https://tenor.com/view/twenty-century-fox-meme-gfy-go-fuck-yourself-meme-get-lost-gif-26260205")

        # Successful Roll
        elif multiplier >= 3 and multiplier < 18:
            finalDamage[1] = baseDamage + round(((((multiplier - 3)/100) * baseDamage) * self.buff), 2)
            await ctx.send(f"Ouch, {ctx.author.mention} wins big!! Your opponent should've bet on black... {(multiplier - 3)}%! (Rolled a {multiplier})")
            await ctx.send("https://tenor.com/view/bruno-mars-throw-swag-photo-shoot-playing-cards-gif-8593407")

        # High Roll
        elif multiplier > 18 and multiplier <= 20:
            baseDamage = 14
            finalDamage[1] = baseDamage + round(((((multiplier - 3)/100) * baseDamage) * self.buff), 2)
            await ctx.send(f'{ctx.author.mention} HOLY SMOKES YOU GOT THE MILLION DOLLAR JACKPOT!!!! Too bad the money just so happened to fall on your opponent...')
            await ctx.send(f'Base damage increased to {baseDamage} and has a damage bonus of {(multiplier - 3)}%! (Rolled a {multiplier})')
            await ctx.send('https://tenor.com/view/money-cash-dollars-raining-money-gif-7741653S')

        await ctx.send(f'{finalDamage[1]} Damage Dealt!')
        self.buff = 1
        return finalDamage[1]
        
        

    @commands.command()
    @commands.has_role("Gambler")
    async def Love(self, ctx):
        await ctx.send('https://tenor.com/view/foxy-freddy-fnaf-gay-kissing-gif-25767212')

    @commands.command()
    @commands.has_role("Gambler")
    async def Laugh(self, ctx):
        await ctx.send('https://cdn.discordapp.com/attachments/605408294458097664/1158188393868566548/CANDACE.mp4?ex=653eeeff&is=652c79ff&hm=82229bdd440035bf21c56c6611ef8eae2b7581bafe84c854c5a81253dae098c6&')

    @commands.command()
    @commands.has_role("Gambler")
    async def ISeeYou(self, ctx):
        await ctx.send('https://tenor.com/view/thomas-train-choo-cursed-gif-26158193')

    @commands.command()
    @commands.has_role("Gambler")
    async def Dies(self, ctx):
        await ctx.send('https://tenor.com/view/daeth-funi-periflight-dies-from-gif-22212023')

    @commands.command()
    @commands.has_role("Gambler")
    async def Dance(self, ctx):
        await ctx.send('https://tenor.com/view/pikmin-dumpy-purple-pikmin-gif-24432434')

    @commands.command()
    @commands.has_role("Gambler")
    async def Happy(self, ctx):
        await ctx.send('https://tenor.com/view/smile-bigsmile-cats-creepy-bigteeth-gif-599187008962754459')

    #HP Gain Move
    @commands.command()
    @commands.has_role("Gambler")
    async def UseGambleHP(self, ctx):
        heal = [2, 0]
        multiplier = random.randrange(1, 20)
        # Bad Roll
        if multiplier < 6:
            heal[1] = 5 * self.buff

        # Successful Roll
        elif multiplier >= 6 and multiplier < 11:
            heal[1] = 10 * self.buff

        # Bad Roll
        elif multiplier >= 11 and multiplier < 16 :
            heal[1] = 15 * self.buff

        # High Roll
        elif multiplier >= 16 and multiplier <= 20:
            heal[1] = 20 * self.buff

        await ctx.send(f"{ctx.author.mention} is wanting to gamble for some health, and wins {heal[1]}HP!")
        self.buff = 1

    #Small Attack 2
    @commands.command()
    @commands.has_role("Gambler")
    async def OldPersonStampede(self, ctx):
        baseDamage = 10
        finalDamage = [1, 0]
        multiplier = random.randrange(1, 20)

        # Bad Roll
        if multiplier < 3:
            baseDamage = 0
            await ctx.send("https://tenor.com/view/twenty-century-fox-meme-gfy-go-fuck-yourself-meme-get-lost-gif-26260205")

        # Successful Roll
        elif multiplier >= 3 and multiplier < 18:
            finalDamage[1] = baseDamage + round(((((multiplier - 3)/100) * baseDamage) * self.buff), 2)
            await ctx.send(f"{ctx.author.mention} Wow! The slots are half off! Too bad for your opponent... {(multiplier - 3)}%! (Rolled a {multiplier})")
            await ctx.send("https://tenor.com/view/casino-oldpeople-oldpeopleonslots-slots-vegas-gif-27586086")

        # High Roll
        elif multiplier > 18 and multiplier <= 20:
            baseDamage = 14
            finalDamage[1] = baseDamage + round(((((multiplier - 3)/100) * baseDamage) * self.buff), 2)
            await ctx.send(f'{ctx.author.mention} BINGO AND SLOTS!?! NOW WE ARE TALKING!!! Base damage increased to {baseDamage} and has a damage bonus of {(multiplier - 3)}%! (Rolled a {multiplier})')

        await ctx.send(f'{finalDamage[1]} Damage Dealt!')
        self.buff = 1
        return finalDamage[1]
    

async def setup(client):
    await client.add_cog(Gambler(client))