import discord
from discord.ext import commands
from apikeys import *
from cogs.Player import *

from KissAss import kissass_Check

class PvPGame(commands.Cog):
    def __init__(self):
        self.players = {}
    
    def add_player(self, player):
        self.players[player.user.id] = player

    def remove_players(self):
        self.players.clear()
        
    def get_player(self, user):
        return self.players.get(user.id)

    def attack(self, attacker, target, moveAttack):
        if attacker.hp <= 0:
            return 'You are dead, not big suprise. Type !leave'
        else:
            moveAttack = kissass_Check(self, attacker, target, moveAttack)
            target.take_damage(moveAttack)
        
            if target.hp <= 0:
                return f'{target.user} has dies LMAO get rekt'

            else:
                return f'{str(attacker.user)} hit {str(target.user)}, who now has {target.hp} health remaining'
        
    def heal(self,attacker, moveHeal):
        if attacker.hp <= 0:
            return 'You are dead, not big suprise. Type !leave'
        else:
            attacker.hp += moveHeal
            return f'{attacker.user} healed for {moveHeal}'
    
    def damageSelf(self, attacker, selfDamage):
        if attacker.hp <= 0:
            return 'You are dead, not big suprise. Type !leave'
        else:
            attacker.take_damage(selfDamage)
            return attacker.hp
            
    def changeBuff(self, attacker, buffIncrease):
        attacker.change_Buff(buffIncrease)
        
        return attacker.buff

async def setup(client):
    await client.add_cog(PvPGame())