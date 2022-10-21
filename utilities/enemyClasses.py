from random import randint
from colorama import Fore
from colorama import init as colorama_init

# from utilities.player import *

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

        if bossBattle:  enemy=bosses[name]
        else: enemy=heartless[name]

        self.MaxHP = enemy['HP']
        self.totalDamage = enemy['damage']
        self.totalDefense = enemy['defense']
        self.totalMagicResistance = enemy['magic resistance']

        self.HP = self.MaxHP  ## full: ♥,  empty: ♡

        self.damage = self.totalDamage
        self.defense = self.totalDefense
        self.magicResistance = self.totalMagicResistance
        self.magicImmunity=enemy['magicImmunity']

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
      if 'blizza' in self.statusEffect or 'thund' in self.statusEffect or 'gravi' in self.statusEffect:
        self.statusDuration = self.statusDuration - 1
      print("\n---------------------------")

    def statusEffectDamageReduction(self, speech, damageDealt, mPower):
      reduction = magics[self.statusEffect]['status']['reduction']+mPower-self.magicResistance
      if reduction<0: reduction=0
      newDamage = damageDealt - reduction
      if newDamage<0: newDamage=0
      speech=speech.replace(str(damageDealt) + ' ♥',Fore.RED + str(newDamage) + ' ♥' + Fore.WHITE)
      return speech, newDamage

    def statusEffectDamage(self):                 ###STATUS EFFECT DAMAGE
      reduction = magics[self.statusEffect]['status']['damage']-self.magicResistance
      if reduction<0: reduction=0
      print(magics[self.statusEffect]['status']['speech'][0] + self.colors[magics[self.statusEffect]['speech'][4]] + magics[self.statusEffect]['status']['speech'][1] + Fore.WHITE + magics[self.statusEffect]['status']['speech'][2] + Fore.RED + str(reduction) + ' ♥' + Fore.WHITE + magics[self.statusEffect]['status']['speech'][4])
      if 'fir' in self.statusEffect:
        self.HP = self.HP - reduction
        self.statusDuration = self.statusDuration - 1
      
    def unpenetrableBlock(self):
      self.totalDefense=99
      self.magicResistance=99

    def block(self):
      self.defense=99
      return 'The enemy tries to block all incoming phisical attacks!', 0

    def calculateDamage(self, defense):   ###CALCULATE DAMAGE DEALT
      damageDealt = self.damage-defense
      if damageDealt < 0: damageDealt = 0
      if self.commandTurn == 0:
        if self.bossBattle == False: speech = "The Heartless attacks you!\nYou lost " + Fore.RED + str(damageDealt) + ' ♥' + Fore.WHITE + '!'
        else: speech = self.name + " attacks you!\nYou lost " + Fore.RED + str(damageDealt) + ' ♥' + Fore.WHITE + '!'
      else:
        if 'unpenetrableBlock'in commands[self.commandName][self.commandTurn]:
          self.unpenetrableBlock()
          speech = commands[self.commandName][self.commandTurn]['speech']
        else:  
          if self.bossBattle == False: speech = "The Heartless used " + self.commandName.capitalize() + "!\nYou lost " + Fore.RED + str(damageDealt) + ' ♥' + Fore.WHITE + '!'
          else: speech = self.name + " used " + self.commandName.capitalize() + "!\nYou lost " + Fore.RED + str(damageDealt) + ' ♥' + Fore.WHITE + '!'

      return speech, damageDealt

    def useCommand(self, defense):        ###CALCULATE COMMAND DETAILS
      self.defense = commands[self.commandName][self.commandTurn]['defense']
      self.damage = commands[self.commandName][self.commandTurn]['damage']
      if 'magic immunity' in commands[self.commandName][self.commandTurn]: self.magicImmunity=commands[self.commandName][self.commandTurn]['magic immunity']
      speech, damageDealt = self.calculateDamage(defense)
      self.commandTurn = self.commandTurn-1
      return speech, damageDealt

    def selectCommand(self, defense):     ###SELECT COMMAND
      if not self.bossBattle:
        try:
            self.totalDefense = heartless[self.name]['defense']
        except:
            self.totalDefense = 0
      else: self.totalDefense = bosses[self.name]['defense']
      
      self.damage = self.totalDamage
      self.defense = self.totalDefense
      self.magicResistance = self.totalMagicResistance
      if self.commandTurn == 0:
        number=randint(1, 100)
        if heartless[self.name]['commands'] != 'attack':
          if number <= 30:
            self.commandName = heartless[self.name]['commands'][1]
            self.commandTurn = commands[self.commandName]['turns']
            speech, damageDealt = self.useCommand(defense)
          elif number <= 50: speech, damageDealt = self.block()
          else: speech, damageDealt = self.calculateDamage(defense)
        else:
          if number<=80: speech, damageDealt = self.calculateDamage(defense)
          else: speech, damageDealt = self.block()
      else: speech, damageDealt = self.useCommand(defense)

      return speech, damageDealt

    def selectCommandBoss(self, defense):     ###SELECT COMMAND BOSS
      self.damage = self.totalDamage
      self.defense = self.totalDefense
      if self.commandTurn == 0:
        commandNumber=randint(0, len(bosses[self.name]['commands']))
        if commandNumber == 0 or commandNumber == len(bosses[self.name]['commands']):
          speech, damageDealt = self.calculateDamage(defense)
        else:
          self.commandName = bosses[self.name]['commands'][commandNumber]
          self.commandTurn = commands[self.commandName]['turns']
          speech, damageDealt = self.useCommand(defense)
      else: speech, damageDealt = self.useCommand(defense)

      return speech, damageDealt

###USE COMMAND AND SELECT COMMAND DIFFERENT FOR BOSSES (if else in the game to call different method)