from colorama import Fore, Style
from colorama import init as colorama_init

import copy

from dictionaries.itemsNmagic import *
from dictionaries.exp import *
from dictionaries.maps import *
from dictionaries.save import *
from dictionaries.tutorials import *
from dictionaries.treasuresNrestrictions import *
from dictionaries.abilities import *
from dictionaries.arenas import *

class player:
    def __init__(self):

        self.keyblade = 'Kingdom Key'

        self.MaxHP = 5
        self.TotalHP = self.MaxHP
        self.HP = self.TotalHP  ## full: ♥,  empty: ♡
        self.MaxMP = 1
        self.TotalMP = self.MaxMP
        self.MP = self.MaxMP  ## full: ●,  empty: ○

        self.STR = 0
        self.DEF = 0

        self.equipment = []
        self.equipmentNumber = 1
        self.equipmentList = []

        self.magic = []
        self.item = ['potion']
        self.itemPouch = 3
        self.keyItems = []
        self.exp = 0
        self.level = 1
        self.munny = 0
        self.stock = []

        self.keyblades = ['Kingdom Key']

        self.MaxAP = 1
        self.TotalAP = self.MaxAP
        self.AP = self.TotalAP

        self.abilities = [] #All unlocked abilities
        self.finishers = [] #Only equipped finishers

        #STORY RELATED
        self.world = 'TraverseTown'
        self.allies = []
        self.map = worldMaps
        self.shipUnlocked = True
        self.unlockedWorlds = ['TraverseTown']
        self.story = {'DestinyIslands' : 0, 'TraverseTown' : 0, 'Wonderland' : 0, 'DeepJungle' : 0,
        'Atlantica' : 0, 'OlympusColiseum' : 0, 'Agrabah' : 0, 'Monstro' : 0, '100AcreWood' : 0,
        'HalloweenTown' : 0, 'Neverland' : 0, 'HollowBastion' : 0, 'EndOfTheWorld' : 0}

        self.unlockedArenas = []
        self.arenaRecords = {}

        self.tutorial = tutorials
        self.treasures = treasureList
        self.restrictionLifted = restrictionLiftedList

        self.saveFile = 0
        self.editedSaves = saves
        self.currentRoom = 'First District'

        self.HPBKP = 0
        self.MPBKP = 0
        self.itemBKP = []

        self.ArenaHPBKP = 0
        self.ArenaMPBKP = 0
        self.ArenaitemBKP = []


        colorama_init(autoreset=True)
        self.colors = dict(Fore.__dict__.items())

    def createBKP(self):
        self.HPBKP = self.HP
        self.MPBKP = self.MP
        self.itemBKP = []
    def restoreBKP(self):
        self.HP = self.HPBKP
        self.MP = self.MPBKP
        self.item = self.item + self.itemBKP
    def createArenaBKP(self):
        self.ArenaHPBKP = self.HP
        self.ArenaMPBKP = self.MP
        self.ArenaitemBKP = []
    def restoreArenaBKP(self):
        self.HP = self.TotalHP
        self.MP = self.TotalMP
        self.item = self.item + self.ArenaitemBKP
    def calculateHealth(self):
        self.TotalHP = self.MaxHP
        self.TotalMP = self.MaxMP
        self.TotalAP = self.MaxAP

        self.TotalMP += keybladeStatus[self.keyblade]['MP']

        for accessory in self.equipment:
            self.TotalHP += equipments[accessory]['HP']
            self.TotalMP += equipments[accessory]['MP']
            self.TotalAP += equipments[accessory]['AP']

        if self.HP > self.TotalHP: self.HP = self.TotalHP
        if self.MP > self.TotalMP: self.MP = self.TotalMP
    def buildHPMPDisplay(self):
        currentHP = ''
        currentMP = ''
        i=0
        while i<self.TotalHP:
            if i<self.HP:
                currentHP += '♥'
            else:
                currentHP += '♡'
            i+=1
        i=0
        while i<self.TotalMP:
            if i<self.MP:
                currentMP += '●'
            else:
                currentMP += '○'
            i+=1
        return currentHP, currentMP
    def buildItemDisplay(self):
        itemRepeat = {}
        for individualItem in self.item:
            if individualItem in itemRepeat:
                itemRepeat[individualItem] += 1
            else:
                itemRepeat[individualItem] = 1
        itemsDisplay = ''
        for individualItem in itemRepeat:
            if itemRepeat[individualItem] == 1:
                itemsDisplay = itemsDisplay + Fore.GREEN + individualItem + Fore.WHITE + ', '
            else:
                itemsDisplay = itemsDisplay + Fore.GREEN + individualItem + Fore.WHITE + 'x' + str(itemRepeat[individualItem]) + ', '
        return itemsDisplay[:-2]
    def buildStockDisplay(self):
        itemRepeat = {}
        for individualItem in self.stock:
            if individualItem in itemRepeat:
                itemRepeat[individualItem] += 1
            else:
                itemRepeat[individualItem] = 1
        itemsDisplay = ''
        for individualItem in itemRepeat:
            if itemRepeat[individualItem] == 1:
                itemsDisplay = itemsDisplay + Fore.GREEN + individualItem + Fore.WHITE + ', '
            else:
                itemsDisplay = itemsDisplay + Fore.GREEN + individualItem + Fore.WHITE + 'x' + str(itemRepeat[individualItem]) + ', '
        return itemsDisplay[:-2]
    def buildSTRDEFDisplay(self):
        damage = self.STR
        defense = self.DEF
        damage += keybladeStatus[self.keyblade]['damage']
        for accessory in self.equipment:
            damage += equipments[accessory]['STR']
            defense += equipments[accessory]['DEF']
        return damage, defense

    def startingGame(self):
        self.calculateHealth()
        self.HP = self.TotalHP
        self.MP = self.TotalMP
        if self.tutorial == {}: self.tutorial = tutorials

    def showBattleStatus(self):
        #print the player's current battle status

        self.calculateHealth()
        currentHP, currentMP = self.buildHPMPDisplay()
        itemsDisplay = self.buildItemDisplay()        

        print(Fore.YELLOW + '\n---------------------------')
        print("HP : " + Fore.RED + str(currentHP))
        print(Fore.WHITE + "MP : " + Fore.BLUE + str(currentMP))
        print(Fore.WHITE + "Items :", itemsDisplay)
        print(Fore.YELLOW + "---------------------------")

    def menu(self):
        
        itemsDisplay = self.buildStockDisplay()

        self.showBattleStatus()
        print("Keyblade: " + Fore.CYAN +  self.keyblade + Fore.WHITE)
        print("Level: " + str(self.level))
        print('\nMunny: ' + str(self.munny) + '🔸')
        print("Items in stock: ", itemsDisplay)
        print("To see the complete status just type \'status\'")
        if self.tutorial['equipment'] == 0:
          print(Fore.YELLOW + "tutorial: " + Fore.WHITE + tutorialSpeech['equipment'])
          self.tutorial['equipment'] = 1
        if self.tutorial['keyblade'] == 0:
          print(Fore.YELLOW + "tutorial: " + Fore.WHITE + tutorialSpeech['keyblade'])
          self.tutorial['keyblade'] = 1
        print("\nTo see the tutorials just type \'" + Fore.YELLOW + "tutorials" + Fore.WHITE + "\'")

    def status(self):
        
        damage, defense = self.buildSTRDEFDisplay()

        self.menu()
        print(Fore.GREEN + "---------------------------")
        print("Keyblade List: ", *self.keyblades)
        print("\nEquipment: " + str(self.equipment))
        print("Number of equipable equipment: " + str(self.equipmentNumber))
        print("Equipment List: " + str(self.equipmentList))
        print("\nExp: " + str(self.exp))
        print("Next level: " + str(levelUp[self.level]['next']-self.exp) + ' xp')
        print("\nKey items: ", self.keyItems)
        print(Fore.BLUE + "---------------------------")
        print("Spells learned: ", *self.magic)
        print("Abilities: ", self.abilities)
        print("\nStrength: ", self.STR)
        print("Defense: ", self.DEF)
        print("Total Strength: ", damage)
        print("Total Defense: ", defense)

    def showTutorials(self):
        for text in self.tutorial:
            if self.tutorial[text] == 1:
                print(tutorialSpeech[text])

    def tradeEquipment(self):
        option = ''
        i=0
        j=0
        while option == '':
            print('To equip or unequip use equip/unequip [equipment] or navigate with \'next equipped/unequipped\' or \'previous equipped/unequipped\'. (0 to cancel)\n')
            print(Fore.YELLOW + 'Equipped:\n')
            if len(self.equipment) > 1:
                if len(self.equipment) > 2:
                    print(Fore.BLUE +
                self.equipment[i] + '''   \t\t\t''' + self.equipment[i+1] + '''   \t\t\t''' + self.equipment[i+2] + Fore.WHITE + '''

HP: ''' + str(equipments[self.equipment[i]]['HP']) + '''   \t\t\tHP: ''' + str(equipments[self.equipment[i+1]]['HP']) + '''   \t\t\t\tHP: ''' + str(equipments[self.equipment[i+2]]['HP']) + '''
MP: ''' + str(equipments[self.equipment[i]]['MP']) + '''   \t\t\tMP: ''' + str(equipments[self.equipment[i+1]]['MP']) + '''   \t\t\t\tMP: ''' + str(equipments[self.equipment[i+2]]['MP']) + '''
STR: ''' + str(equipments[self.equipment[i]]['STR']) + ''' \t\t\t\tSTR: ''' + str(equipments[self.equipment[i+1]]['STR']) + '''\t\t\t\t\tSTR: ''' + str(equipments[self.equipment[i+2]]['STR']) + '''
DEF: ''' + str(equipments[self.equipment[i]]['DEF']) + ''' \t\t\t\tDEF: ''' + str(equipments[self.equipment[i+1]]['DEF']) + '''\t\t\t\t\tDEF: ''' + str(equipments[self.equipment[i+2]]['DEF']) + '''
                    ''')
                else:
                    print(Fore.BLUE +
                self.equipment[i] + '''   \t\t\t''' + self.equipment[i+1] + Fore.WHITE + '''

HP: ''' + str(equipments[self.equipment[i]]['HP']) + '''   \t\t\tHP: ''' + str(equipments[self.equipment[i+1]]['HP']) + '''
MP: ''' + str(equipments[self.equipment[i]]['MP']) + '''   \t\t\tMP: ''' + str(equipments[self.equipment[i+1]]['MP']) + '''
STR: ''' + str(equipments[self.equipment[i]]['STR']) + ''' \t\t\t\tSTR: ''' + str(equipments[self.equipment[i+1]]['STR']) + '''
DEF: ''' + str(equipments[self.equipment[i]]['DEF']) + ''' \t\t\t\tDEF: ''' + str(equipments[self.equipment[i+1]]['DEF']) + '''
                    ''')
            elif len(self.equipment) == 1:
                print(Fore.BLUE +
                self.equipment[i] +  Fore.WHITE +  '''

HP: ''' + str(equipments[self.equipment[i]]['HP']) + '''
MP: ''' + str(equipments[self.equipment[i]]['MP']) + '''
STR: ''' + str(equipments[self.equipment[i]]['STR']) + '''
DEF: ''' + str(equipments[self.equipment[i]]['DEF']) + '''
                    ''')
            else:
                print('You have nothing equipped!\n')


            print(Fore.YELLOW + 'Unequipped:\n')
            if len(self.equipmentList) > 1:
                if len(self.equipmentList) > 2:
                    print(Fore.BLUE +
                self.equipmentList[j] + '''   \t\t\t''' + self.equipmentList[j+1] + '''   \t\t\t\t''' + self.equipmentList[j+2] + Fore.WHITE + '''

HP: ''' + str(equipments[self.equipmentList[j]]['HP']) + '''   \t\t\tHP: ''' + str(equipments[self.equipmentList[j+1]]['HP']) + '''   \t\t\t\tHP: ''' + str(equipments[self.equipmentList[j+2]]['HP']) + '''
MP: ''' + str(equipments[self.equipmentList[j]]['MP']) + '''   \t\t\tMP: ''' + str(equipments[self.equipmentList[j+1]]['MP']) + '''   \t\t\t\tMP: ''' + str(equipments[self.equipmentList[j+2]]['MP']) + '''
STR: ''' + str(equipments[self.equipmentList[j]]['STR']) + ''' \t\t\t\tSTR: ''' + str(equipments[self.equipmentList[j+1]]['STR']) + '''\t\t\t\t\tSTR: ''' + str(equipments[self.equipmentList[j+2]]['STR']) + '''
DEF: ''' + str(equipments[self.equipmentList[j]]['DEF']) + ''' \t\t\t\tDEF: ''' + str(equipments[self.equipmentList[j+1]]['DEF']) + '''\t\t\t\t\tDEF: ''' + str(equipments[self.equipmentList[j+2]]['DEF']) + '''
                    ''')
                else:
                    print(Fore.BLUE +
                self.equipmentList[j] + '''   \t\t\t''' + self.equipmentList[j+1] + Fore.WHITE + '''

HP: ''' + str(equipments[self.equipmentList[j]]['HP']) + '''   \t\t\tHP: ''' + str(equipments[self.equipmentList[j+1]]['HP']) + '''
MP: ''' + str(equipments[self.equipmentList[j]]['MP']) + '''   \t\t\tMP: ''' + str(equipments[self.equipmentList[j+1]]['MP']) + '''
STR: ''' + str(equipments[self.equipmentList[j]]['STR']) + ''' \t\t\t\tSTR: ''' + str(equipments[self.equipmentList[j+1]]['STR']) + '''
DEF: ''' + str(equipments[self.equipmentList[j]]['DEF']) + ''' \t\t\t\tDEF: ''' + str(equipments[self.equipmentList[j+1]]['DEF']) + '''
                    ''')
            elif len(self.equipmentList) == 1:
                print(Fore.BLUE +
                self.equipmentList[j] + Fore.WHITE + '''

HP: ''' + str(equipments[self.equipmentList[j]]['HP']) + '''
MP: ''' + str(equipments[self.equipmentList[j]]['MP']) + '''
STR: ''' + str(equipments[self.equipmentList[j]]['STR']) + '''
DEF: ''' + str(equipments[self.equipmentList[j]]['DEF']) + '''
                    ''')
            else:
                print('You have nothing unequipped!\n')

            option = input('>')
            option = option.lower().split()
            if len(option)>2: option[1] = option[1] + ' ' + option[2]

            if option[0] == 'next':
                if option[1] == 'equipped':
                    if len(self.equipment) > (i+3):
                        i+=1
                    else:
                        print(Fore.RED + 'No more equipments after these!')
                elif option[1] == 'unequipped':
                    if len(self.equipmentList) > (j+3):
                        j+=1
                    else:
                        print(Fore.RED + 'No more equipments after these!')
                else:
                    print('usage: next [equipped/unequipped]!')
                option=''

            elif option[0] == 'previous':
                if option[1] == 'equipped':
                    if i>0:
                        i-=1
                    else:
                        print(Fore.RED + 'No more equipments previous to these!')
                elif option[1] == 'unequipped':
                    if j>0:
                        j-=1
                    else:
                        print(Fore.RED + 'No more equipments previous to these!')
                else:
                    print('usage: previous [equipped/unequipped]!')
                option=''

            elif option == '0' or option[0] == '0':
                break

            elif option[0] == 'equip':
                if option[1] in self.equipmentList:
                    if len(self.equipment)<self.equipmentNumber:
                        self.equipment.append(option[1])
                        self.equipmentList.remove(option[1])
                        print(option[1] + ' equipped!\n')
                        self.TotalHP += equipments[option[1]]['HP']
                        self.HP += equipments[option[1]]['HP']
                        self.TotalMP += equipments[option[1]]['MP']
                        self.MP += equipments[option[1]]['MP']
                        if (input('Do you want to keep equipping? (yes/no)\n') == 'yes'):
                            pass
                        else:
                            break
                    else:
                        print(Fore.RED + 'You can\' equip any more items!\n')
                else:
                    print(Fore.RED + 'Equipment not found')
                option=''
            
            elif option[0] == 'unequip':
                if option[1] in self.equipment:
                    self.equipmentList.append(option[1])
                    self.equipment.remove(option[1])
                    print(option[1] + ' unequipped!\n')
                    self.TotalHP = self.TotalHP - equipments[option[1]]['HP']
                    self.HP = self.HP - equipments[option[1]]['HP']
                    self.TotalMP = self.TotalMP - equipments[option[1]]['MP']
                    self.MP = self.MP - equipments[option[1]]['MP']
                    if (input('Do you want to keep equipping? (yes/no)\n') == 'yes'):
                        pass
                    else:
                        break
                else:
                    print(Fore.RED + 'Equipment not found')
                option=''

            else:
                print(Fore.RED + 'Command not found')
                option=''

        self.calculateHealth()

#####TRADE KEYBLADES 
    def tradeKeyblade(self):
        option = ''
        i=0
        while option == '':
            print('To equip a different keyblade use \'equip [keyblade]\' or navigate with \'next\' or \'previous\'. (0 to cancel)\n')
            print(Fore.YELLOW + 'Equipped:\n')

            print(Fore.BLUE +
                self.keyblade +  Fore.WHITE +  '''

Damage: ''' + str(keybladeStatus[self.keyblade]['damage']) + '''
MP: ''' + str(keybladeStatus[self.keyblade]['MP']) + '''
                    ''')

            print(Fore.YELLOW + 'Unquipped:\n')
            if len(self.keyblades) > 1:
                if len(self.keyblades) > 2:
                    print(Fore.BLUE +
                self.keyblades[i] + '''   \t\t\t''' + self.keyblades[i+1] + '''   \t\t\t''' + self.keyblades[i+2] + Fore.WHITE + '''

Damage: ''' + str(keybladeStatus[self.keyblades[i]]['damage']) + ''' \t\t\tDamage: ''' + str(keybladeStatus[self.keyblades[i+1]]['damage']) + '''\t\t\tDamage: ''' + str(keybladeStatus[self.keyblades[i+2]]['damage']) + '''
MP: ''' + str(keybladeStatus[self.keyblades[i]]['MP']) + '''   \t\t\tMP: ''' + str(keybladeStatus[self.keyblades[i+1]]['MP']) + '''   \t\t\tMP: ''' + str(keybladeStatus[self.keyblades[i+2]]['MP']) + '''
                    ''')
                else:
                    print(Fore.BLUE +
                self.keyblades[i] + '''   \t\t\t''' + self.keyblades[i+1] + Fore.WHITE + '''

Damage: ''' + str(keybladeStatus[self.keyblades[i]]['damage']) + ''' \t\t\tDamage: ''' + str(keybladeStatus[self.keyblades[i+1]]['damage']) + '''
MP: ''' + str(keybladeStatus[self.keyblades[i]]['MP']) + '''   \t\t\tMP: ''' + str(keybladeStatus[self.keyblades[i+1]]['MP']) + '''
                    ''')
            elif len(self.keyblades) == 1:
                print(Fore.BLUE +
                self.keyblades[i] +  Fore.WHITE +  '''

Damage: ''' + str(keybladeStatus[self.keyblades[i]]['damage']) + '''
MP: ''' + str(keybladeStatus[self.keyblades[i]]['MP']) + '''
                    ''')
            else:
                print('You don\' have other keyblades!\n')

            option = input('>')
            option = option.lower().split()
            if len(option)>3: option[1] = option[1].capitalize() + ' ' + option[2].capitalize() + ' ' + option[3].capitalize()
            elif len(option)>2: option[1] = option[1].capitalize() + ' ' + option[2].capitalize()
            elif len(option)>1: option[1] = option[1].capitalize()

            if 'next' in option:
                if len(self.keyblades) > (i+3):
                    i+=1
                else:
                    print(Fore.RED + 'No more keyblades after these!')
                option=''

            elif 'previus' in option:
                if i>0:
                    i-=1
                else:
                    print(Fore.RED + 'No more equipments previous to these!')
                option=''

            elif option == '0' or option[0] == '0':
                break

            elif option[0] == 'equip':
                if option[1] in self.keyblades:
                    self.TotalMP = self.TotalMP + keybladeStatus[option[1]]['MP'] - keybladeStatus[self.keyblade]['MP']
                    self.MP = self.MP + keybladeStatus[option[1]]['MP'] - keybladeStatus[self.keyblade]['MP']
                    self.keyblade = option[1]
                    print(option[1] + ' equipped!\n')
                    break
                else:
                    print(Fore.RED + 'Equipment not found')
                option=''
            
            else:
                print(Fore.RED + 'Command not found')
                option=''

        self.calculateHealth()

#####EQUIP ABILITIES
    def equipAbilities(self):
        option = ''
        while option == '':
            self.abilities=sorted(self.abilities, key=lambda x: x[0])

            print('\nTo equip an ability use \'equip [ability]\', to unequip use \'unequip [ability]\'. If you want to see an ability description use \'see [ability]\'. (0 to cancel)\n')

            print('\nAP: ' + str(self.AP) + '\\' + str(self.TotalAP) + '\n')
            for ability in self.abilities: #● ○
                tab='\t'
                name=ability[0]
                if ability[0] in self.finishers: name=name+' (F)'
                if len(name)<=8: tab=tab+tab+tab+tab
                elif len(name)<=12: tab=tab+tab+tab
                elif len(name)<=16: tab=tab+tab
                if ability[1]: print(Fore.YELLOW + '● ' + Fore.WHITE + name + tab + 'cost: ' + str(abilityList[ability[0]][1]))
                else: print('○ ' + name + tab + 'cost: ' + str(abilityList[ability[0]][1]))

            option = input('>')
            option = option.lower().split()
            if len(option)>2: option[1] = option[1].capitalize() + ' ' + option[2].capitalize()
            elif len(option)>1: option[1] = option[1].capitalize()


            if option == '0' or option[0] == '0':
                break

            elif option[0] == 'equip':
                if [option[1], True] in self.abilities: print(Fore.RED + 'This ability is already equipped!')
                elif [option[1], False] in self.abilities:
                    if self.AP >= abilityList[option[1]][1]:
                        self.abilities[self.abilities.index([option[1], False])][1]=True
                        self.AP=self.AP-abilityList[option[1]][1]
                        print(Fore.GREEN + option[1] + ' equipped!\n')
                        if option[1] in finishersList: self.finishers.append(option[1])
                    else: print(Fore.RED + 'Not enought AP!')
                else:
                    print(Fore.RED + 'Ability not found!')
                option=''

            elif option[0] == 'unequip':
                if [option[1], False] in self.abilities: print(Fore.RED + 'This ability is already unequipped!')
                elif [option[1], True] in self.abilities:
                    self.abilities[self.abilities.index([option[1], True])][1]=False
                    self.AP+=abilityList[option[1]][1]
                    print(Fore.CYAN + option[1] + ' unequipped!\n')
                    if option[1] in finishersList: del(self.finishers[self.finishers.index(option[1])])
                else:
                    print(Fore.RED + 'Ability not found')
                option=''
            
            else:
                print(Fore.RED + 'Command not found')
                option=''

        self.calculateHealth()