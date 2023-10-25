import discord
from discord.ext import commands
from apikeys import *

class Player(commands.Cog):
    def __init__(self, user):
        self.user = user
        self.hp = 200
        self.buff = 1
        self.mattBuff = 10
        self.willBuff = 10
        self.benBuff = 10
        self.melissaBuff = 10
        self.bradBuff = 10

    def take_damage(self, damage):
        self.hp = round((self.hp - damage), 2)
    
    def regain_Hp(self, heal):
        self.hp = round((self.hp + heal), 2)

    def change_Buff(self, increase):
        self.buff = round((increase), 2)

    def return_Buff(self):
        return self.buff

async def setup(client):
    await client.add_cog(Player(discord.Member))