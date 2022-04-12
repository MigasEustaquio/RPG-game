from random import randint
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
    def __init__(self, name, bossBattle):

        self.name = name
        self.bossBattle = bossBattle

        if bossBattle == False: self.MaxHP = heartless[name]['HP']
        else: self.MaxHP = bosses[name]['HP']
        self.HP = self.MaxHP  ## full: ♥,  empty: ♡

        if bossBattle == False: self.totalDamage = heartless[name]['damage']
        else: self.totalDamage = bosses[name]['damage']
        
        if not bossBattle:
          try:
              self.totalDefense = heartless[name]['defense']
          except:
              self.totalDefense = 0
        else: self.totalDefense = bosses[name]['defense']

        self.damage = self.totalDamage
        self.defense = self.totalDefense

        self.commandTurn = 0
        self.commandName = ''

        self.statusEffect = 'none'
        self.statusDuration = 99

        if bossBattle == False:
          self.exp = heartless[name]['exp']
          self.munny = heartless[name]['munny']
          self.drop = heartless[name]['drop']
          self.luckyDrop = {(x+20):heartless[name]['drop'][x] for x in heartless[name]['drop']}
        else:
          self.exp = bosses[name]['exp']
          self.munny = bosses[name]['munny']
          self.drop = bosses[name]['drop']
          self.luckyDrop = {(x+20):bosses[name]['drop'][x] for x in bosses[name]['drop']}


        colorama_init(autoreset=True)
        self.colors = dict(Fore.__dict__.items())


    def statusEffectEnd(self):                    ###STATUS EFFECT END
      if self.statusDuration == 0 and self.statusEffect != 'none':
        print('\nThe ' + self.colors[magics[self.statusEffect]['speech'][4]] + magics[self.statusEffect]['status']['name'] + Fore.WHITE + ' effect has passed\n')
        self.statusEffect = 'none'
        self.statusDuration = 99
      print("---------------------------")

    def statusEffectDuration(self):               ###STATUS EFFECT DURATION
      if 'blizza' in self.statusEffect or 'thund' in self.statusEffect:
        self.damage = self.damage - magics[self.statusEffect]['status']['reduction']
        self.statusDuration = self.statusDuration - 1
      print("---------------------------")

    def statusEffectDamage(self):                 ###STATUS EFFECT DAMAGE
      print(magics[self.statusEffect]['status']['speech'][0] + self.colors[magics[self.statusEffect]['speech'][4]] + magics[self.statusEffect]['status']['speech'][1] + Fore.WHITE + magics[self.statusEffect]['status']['speech'][2] + Fore.RED + magics[self.statusEffect]['status']['speech'][3] + Fore.WHITE + magics[self.statusEffect]['status']['speech'][4])
      if 'fir' in self.statusEffect:
        self.HP = self.HP - magics[self.statusEffect]['status']['damage']
        self.statusDuration = self.statusDuration - 1
      
    def unpenetrableBlock(self):
      self.totalDefense=99

    def block(self, player):
      if player.ignoreBlock:
        print('The enemy tries to block all incoming phisical attacks!')
        self.defense=99
      else:
        print('The enemy blocks all incoming phisical attacks!')
        self.defense=99
        player.blocked=True

    def calculateDamage(self, player, defense):   ###CALCULATE DAMAGE DEALT
      damageDealt = self.damage-defense
      if damageDealt < 0: damageDealt = 0
      if self.commandTurn == 0:
        if self.bossBattle == False: print("The Heartless attacks you!\nYou lost " + Fore.RED + str(damageDealt) + ' ♥ ' + Fore.WHITE + '!')
        else: print(self.name + " attacks you!\nYou lost " + Fore.RED + str(damageDealt) + ' ♥ ' + Fore.WHITE + '!')
      else:
        if 'unpenetrableBlock'in commands[self.commandName][self.commandTurn]:
          self.unpenetrableBlock()
          print(commands[self.commandName][self.commandTurn]['speech'])
        else:  
          if self.bossBattle == False: print("The Heartless used " + self.commandName.capitalize() + "!\nYou lost " + Fore.RED + str(damageDealt) + ' ♥ ' + Fore.WHITE + '!')
          else: print(self.name + " used " + self.commandName.capitalize() + "!\nYou lost " + Fore.RED + str(damageDealt) + ' ♥ ' + Fore.WHITE + '!')
      oldHP = player.HP
      player.HP = player.HP - damageDealt
      if 'Second Chance' in player.abilities:                ###SECOND CHANCE
        if player.HP < 1 and oldHP > 1:
          player.HP = 1
          print('Second Chance')

    def useCommand(self, player, defense):        ###CALCULATE COMMAND DETAILS
      self.calculateDamage(player, defense)
      self.defense = commands[self.commandName][self.commandTurn]['defense']
      self.totalDamage = commands[self.commandName][self.commandTurn]['damage']
      self.commandTurn = self.commandTurn-1

    def selectCommand(self, player, defense):     ###SELECT COMMAND
      if not self.bossBattle:
        try:
            self.totalDefense = heartless[self.name]['defense']
        except:
            self.totalDefense = 0
      else: self.totalDefense = bosses[self.name]['defense']
      
      self.damage = self.totalDamage
      self.defense = self.totalDefense
      if self.commandTurn == 0:
        number=randint(1, 100)
        if heartless[self.name]['commands'] != 'attack':
          if number <= 30:
            self.commandName = heartless[self.name]['commands'][1]
            self.commandTurn = commands[self.commandName]['turns']
            self.useCommand(player, defense)
          elif number <= 50: self.block(player)
          else: self.calculateDamage(player, defense)
        else:
          if number<=40: self.calculateDamage(player, defense)
          else: self.block(player)
      else: self.useCommand(player, defense)


    def selectCommandBoss(self, player, defense):     ###SELECT COMMAND BOSS
      self.damage = self.totalDamage
      self.defense = self.totalDefense
      if self.commandTurn == 0:
        commandNumber=randint(0, len(bosses[self.name]['commands']))
        if commandNumber == 0 or commandNumber == len(bosses[self.name]['commands']):
          self.calculateDamage(player, defense)
        else:
          self.commandName = bosses[self.name]['commands'][commandNumber]
          self.commandTurn = commands[self.commandName]['turns']
          self.useCommand(player, defense)
      else: self.useCommand(player, defense)



###USE COMMAND AND SELECT COMMAND DIFFERENT FOR BOSSES (if else in the game to call different method)