from random import randint
from colorama import Fore
from colorama import init as colorama_init
from matplotlib.style import available

from utilities.player import *

from dictionaries.allies import *
from dictionaries.itemsNmagic import *
from dictionaries.exp import *
from dictionaries.maps import *
from dictionaries.save import *
from dictionaries.tutorials import *
from dictionaries.abilities import *
from dictionaries.enemies import *
class Ally:
    def __init__(self, name, player, mode=2):

        self.name=name
        self.name1=name
        self.name2=name

        
        self.TotalMP=player.TotalMP
        self.MP=self.TotalMP

        if self.name=='Donald&Goofy':
            self.name1='Donald'
            self.name2='Goofy'

        self.mode=mode
        #modes: 0->conservative
        #       1->moderate
        #       2->go wild


        # self.commandTurn = 0   #commands that require multiple rounds
        # self.commandName = ''

        colorama_init(autoreset=True)
        self.colors = dict(Fore.__dict__.items())


    def changeMode(self, mode):  #Upgrade this method later
        self.mode=mode

    def useCommand(self, command, helpType):

        if command in magics:
            text=magics[command]['speech']
            if helpType == 'damage':
                print(self.name1 + " casts " + self.colors[text[-1]] + command.capitalize() + Fore.WHITE + " and it deals " + Fore.RED + text[1] + Fore.WHITE + text[2] + self.colors[text[-1]] + text[3])
                helpStatus=command
            else:
                print(self.name1 + " casts " + Fore.GREEN + command.capitalize() + Fore.WHITE + " and it restores " + Fore.RED + text[1] + Fore.WHITE + text[2])
                helpStatus=''
            self.MP = self.MP-magics[command]['MP']
            helpValue=magics[command][helpType]

            return helpType, helpValue, helpStatus
        else:
            text=alliesAbilities[command]['speech']
            if helpType == 'damage':
                print(self.name2 + " uses " + self.colors[text[-1]] + command.capitalize() + Fore.WHITE + " and it deals " + Fore.RED + text[1] + Fore.WHITE + text[2])
            else:
                print(self.name2 + " uses " + Fore.GREEN + command.capitalize() + Fore.WHITE + " and it restores " + Fore.RED + text[1] + Fore.WHITE + text[2])
            helpStatus=''
            self.MP = self.MP-alliesAbilities[command]['MP']
            helpValue=alliesAbilities[command][helpType]

            return helpType, helpValue, helpStatus

    def selectCommand(self, player):     ###SELECT COMMAND
    #   if self.commandTurn == 0:
        if self.MP<self.TotalMP and randint(0, 100) >= 40: self.MP+=1 #RECOVER MP
        commandNumber=randint(0, 100)
        healORdamage=randint(1, 3)
        availableCommands = []
        if commandNumber <= (25+10*self.mode):
            if player.HP == player.TotalHP: helpType = 'damage'
            elif player.HP <= player.TotalHP*(30+10*self.mode)/100:
                if healORdamage==3: helpType='damage'
                else: helpType='heal'
            else:
                if healORdamage==3: helpType='heal'
                else: helpType='damage'
            for number in allies[self.name][helpType]:
                if number > player.level: break
                for command in allies[self.name][helpType][number]:
                    for _ in range(number):
                        if command in magics:
                            if self.MP >= magics[command]['MP']: availableCommands.append(command)
                        else:
                            if self.MP >= alliesAbilities[command]['MP']: availableCommands.append(command)
            # print(availableCommands) #####
            if availableCommands: return self.useCommand(availableCommands[randint(0, len(availableCommands)-1)], helpType)
            else: return '', 0, ''
        else: return '', 0, ''
