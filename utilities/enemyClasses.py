from colorama import Fore
from colorama import init as colorama_init

from utilities.player import *

from dictionaries.itemsNmagic import *
from dictionaries.exp import *
from dictionaries.maps import *
from dictionaries.save import *
from dictionaries.tutorials import *
from dictionaries.abilities import *
from dictionaries.enemies import *
class Heartless:
    def __init__(self, name):

        self.name = name

        self.MaxHP = heartless[name]['HP']
        self.HP = self.MaxHP  ## full: ♥,  empty: ♡
        # self.MaxMP = heartless[name]['MP']
        # self.MP = self.MaxMP  ## full: ●,  empty: ○

        self.totalDamage = heartless[name]['damage']
        self.damage = self.totalDamage
        try:
            self.defense = heartless[name]['defense']
        except:
            self.defense = 0

        self.statusEffect = 'none'
        self.statusDuration = 99


        self.exp = heartless[name]['exp']
        self.munny = heartless[name]['munny']
        self.drop = heartless[name]['drop']


        colorama_init(autoreset=True)
        self.colors = dict(Fore.__dict__.items())



    def statusEffectDuration(self):               ###STATUS EFFECT DURATION
        if self.statusDuration == 0 and self.statusEffect != 'none':
          print('\nThe ' + self.colors[magics[self.statusEffect]['speech'][4]] + magics[self.statusEffect]['status']['name'] + Fore.WHITE + ' effect has passed\n')
          self.statusEffect = 'none'
          self.statusDuration = 99

        if 'blizza' in self.statusEffect or 'thund' in self.statusEffect:
          self.damage = self.damage - magics[self.statusEffect]['status']['reduction']
          self.statusDuration = self.statusDuration - 1

        print("---------------------------")

    
    def statusEffectDamage(self):                 ###STATUS EFFECT DAMAGE
      print(magics[self.statusEffect]['status']['speech'][0] + self.colors[magics[self.statusEffect]['speech'][4]] + magics[self.statusEffect]['status']['speech'][1] + Fore.WHITE + magics[self.statusEffect]['status']['speech'][2] + Fore.RED + magics[self.statusEffect]['status']['speech'][3] + Fore.WHITE + magics[self.statusEffect]['status']['speech'][4])
      self.HP = self.HP - magics[self.statusEffect]['status']['damage']
      self.statusDuration = self.statusDuration - 1


    def calculateDamage(self, player, defense):   ###CALCULATE DAMAGE DEALT
      damageDealt = self.damage-defense
      if damageDealt < 0: damageDealt = 0
      print("The Heartless attacks you!\nYou lost " + Fore.RED + str(damageDealt) + ' ♥ ' + Fore.WHITE + '!')
      oldHP = player.HP
      player.HP = player.HP - damageDealt
      if 'Second Chance' in player.abilities:                ###SECOND CHANCE
        if player.HP < 1 and oldHP > 1:
          player.HP = 1
          print('Second Chance')


    def selectCommand(self, player, defense):     ###JUST ATTACK FOR NOW

      self.calculateDamage(player, defense)