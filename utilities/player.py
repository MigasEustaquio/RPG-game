from colorama import Fore, Style
from colorama import init as colorama_init

from dictionaries.itemsNmagic import *
from dictionaries.exp import *
from dictionaries.maps import *
from dictionaries.save import *
class player:
    def __init__(self):

        self.keyblade = 'Kingdom Key'

        self.MaxHP = 5
        self.HP = self.MaxHP  ## full: ♥,  empty: ♡
        self.MaxMP = 1+keybladeStatus[self.keyblade]['MP']
        self.MP = self.MaxMP  ## full: ●,  empty: ○
        
        self.magic = []
        self.item = ['potion']
        self.itemPouch = 3
        self.keyItems = []
        self.exp = 0
        self.level = 1
        self.munny = 0
        self.stock = []

        self.keyblades = ['Kingdom Key']

        self.abilities = []

        #STORY RELATED
        self.world = 'TraverseTown'
        self.map = str(worldMaps[self.world])   ############### WHEN CHANGE WORLDS HAVE TO UPDATE THE worldMaps DICTIONARY
        self.story = 0

        self.saveFile = 0
        self.editedSaves = saves

        colorama_init(autoreset=True)
        self.colors = dict(Fore.__dict__.items())

    def showBattleStatus(self):
        #print the player's current battle status
        currentHP = ''
        currentMP = ''
        i=0
        while i<self.MaxHP:
            if i<self.HP:
                currentHP += '♥'
            else:
                currentHP += '♡'
            i+=1
        i=0
        while i<self.MaxMP:
            if i<self.MP:
                currentMP += '●'
            else:
                currentMP += '○'
            i+=1
        
        print(Fore.GREEN + '\n---------------------------')
        print("HP : " + Fore.RED + str(currentHP))
        print(Fore.WHITE + "MP : " + Fore.BLUE + str(currentMP))
        print(Fore.WHITE + "Items :", *self.item)
        print(Fore.GREEN + "---------------------------")

    def menu(self):
        self.showBattleStatus()

        print("Level: " + str(self.level))
        print("Exp: " + str(self.exp))
        print("Next level: " + str(levelUp[self.level]['next']-self.exp) + ' xp')
        print('\nMunny: ' + str(self.munny) + '🔸')
        print("Items in stock: ", self.stock)
        print("Key items: ", self.keyItems)
        print(Fore.BLUE + "---------------------------")
        print("Spells learned: ", *self.magic)
        print("Abilities: ", self.abilities)
        print(Fore.YELLOW + "---------------------------")
        print('To cast a magic spell just type \'cast [magic]\'')
        print('To use an item just type \'use [item]\'')
        print('To open the map of the current World just type \'map\'')
        print('To get the treasure chest from the current room just type \'treasure\'')
        print(Fore.YELLOW + "---------------------------")