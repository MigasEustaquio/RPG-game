from colorama import Fore, Style
from colorama import init as colorama_init
import math

import copy

from dictionaries.itemsNmagic import *
from dictionaries.shopDetails import *
from dictionaries.exp import *
from dictionaries.maps import *
from dictionaries.save import *
from dictionaries.tutorials import *
from dictionaries.treasuresNrestrictions import *
from dictionaries.abilities import *
from dictionaries.arenas import *
from dictionaries.enemies import *

class player:
    def __init__(self):

        self.keyblade = 'Wooden Sword'

        self.MaxHP = 5
        self.TotalHP = self.MaxHP
        self.HP = self.TotalHP  ## full: ♥,  empty: ♡
        self.MaxMP = 1
        self.TotalMP = self.MaxMP
        self.MP = self.MaxMP  ## full: ●,  empty: ○

        self.STR = 1
        self.DEF = 0
        self.magicPower = 0

        self.equipment = []
        self.equipmentNumber = 1
        self.equipmentList = []

        self.magic = []
        self.item = []
        self.itemPouch = 3
        self.keyItems = []
        self.exp = 0
        self.level = 1
        self.munny = 0
        self.stock = []

        self.keyblades = ['Wooden Sword']

        self.MaxAP = 3
        self.TotalAP = self.MaxAP
        self.AP = self.TotalAP

        self.abilities = [] #All unlocked abilities
        self.finishers = [] #Only equipped finishers
        self.comboModifiers = [] #Only equipped combo modifiers
        self.activeAbilities = [] #Only equipped active abilities
        self.combo = [] #Avaliable combo modifiers for current combo

        #STORY RELATED
        self.path = 'none'
        self.world = 'DestinyIslands'
        self.allies = []
        self.map = worldMaps
        self.shipUnlocked = True
        self.unlockedWorlds = ['DestinyIslands']
        self.story = {'DestinyIslands' : 0, 'TraverseTown' : 0, 'Wonderland' : 0, 'DeepJungle' : 0,
        'Atlantica' : 0, 'OlympusColiseum' : 0, 'Agrabah' : 0, 'Monstro' : 0, '100AcreWood' : 0,
        'HalloweenTown' : 0, 'Neverland' : 0, 'HollowBastion' : 0, 'EndOfTheWorld' : 0}

        self.unlockedArenas = []
        self.arenaRecords = {}

        self.tutorial = tutorials
        self.treasures = treasureList
        self.restrictionLifted = restrictionLiftedList
        self.visitedRooms = worlds

        self.enemiesList = {}

        self.saveFile = 0
        self.editedSaves = saves
        self.currentRoom = 'Dive to the Heart'

        self.HPBKP = 0
        self.MPBKP = 0
        self.itemBKP = []

        self.ArenaHPBKP = 0
        self.ArenaMPBKP = 0
        self.ArenaitemBKP = []

        self.ignoreBlock = False
        self.blocked = False

        colorama_init(autoreset=True)
        self.colors = dict(Fore.__dict__.items())

        self.HPBarColour = 'GREEN'

    def createBKP(self):
        self.HPBKP = self.HP
        self.MPBKP = self.MP
        self.itemBKP = []
    def restoreBKP(self):
        self.HP = self.HPBKP
        self.MP = self.MPBKP
        self.item = self.item + self.itemBKP
    def createArenaBKP(self):
        self.HP=self.TotalHP
        self.MP=self.TotalMP
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

        if self.HP<= math.ceil(0.25*self.TotalHP):
            self.HPBarColour = 'RED'
        elif self.HP<= math.ceil(0.5*self.TotalHP):
            self.HPBarColour = 'YELLOW'
        else: self.HPBarColour = 'GREEN'

    def sortItem(self):
        self.item.sort(key=lambda val: list(items.keys()).index(val))
    def sortStock(self):
        self.stock.sort(key=lambda val: list(items.keys()).index(val))
    def sortKeyItem(self):
        self.keyItems.sort(key=lambda val: keyItems.index(val))
    def sortMagic(self):
        self.magic.sort(key=lambda val: list(magics.keys()).index(val))
    def sortEquipment(self):
        self.equipment.sort(key=lambda val: list(equipments.keys()).index(val))
    def sortEquipmentList(self):
        self.equipmentList.sort(key=lambda val: list(equipments.keys()).index(val))
    def sortKeyblades(self):
        self.keyblades.sort(key=lambda val: list(keybladeStatus.keys()).index(val))
    def sortAbilities(self):
        self.abilities.sort(key=lambda val: list(abilityList.keys()).index(val))

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
    def buildItemDisplay(self, item):
        itemRepeat = {}
        for individualItem in item:
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

    def showEquipments(self):
        print('\nEquipment Slots: ' + str(len(self.equipment)) + '\\' + str(self.equipmentNumber) + '\n')
        for equipment in self.equipmentList: #● ○
            tab=''
            for _ in range(30-len(equipment)):  tab=tab+'-'
            tab = equipment + tab + 'HP: ' + str(equipments[equipment]['HP']) + '  MP: ' + str(equipments[equipment]['MP']) + '  STR: ' + str(equipments[equipment]['STR']) + '  DEF: ' + str(equipments[equipment]['DEF'])
            if ' -' in tab: tab=tab.replace(' -', '-')
            if equipment in self.equipment: print(Fore.YELLOW + '● ' + Fore.WHITE + tab)
            else: print(Fore.YELLOW + '○ ' + Fore.WHITE + tab)
    def showKeyblades(self):
        for keyblade in self.keyblades: #● ○
            tab=''
            for _ in range(30-len(keyblade)):   tab=tab+'-'
            tab = keyblade + tab + 'Damage: ' + str(keybladeStatus[keyblade]['damage']) + '   MP: ' + str(keybladeStatus[keyblade]['MP'])
            if keybladeStatus[keyblade]['damage'] > 9: tab=tab.replace('  MP:', ' MP:')
            if ' -' in tab: tab=tab.replace(' -', '-')
            if keyblade == self.keyblade: print(Fore.BLUE + '● ' + Fore.WHITE + tab)
            else: print(Fore.BLUE + '○ ' + Fore.WHITE + tab)
    def showAbilities(self):
        print('\nAP: ' + str(self.AP) + '\\' + str(self.TotalAP) + '\n')
        for ability in self.abilities: #● ○
            name=ability[0]
            if ability[0] in self.finishers: name=name+' (F)'
            for _ in range(30-len(name)):   name=name+' '
            if ability[1]: print(Fore.YELLOW + '● ' + Fore.WHITE + name + 'cost: ' + str(abilityList[ability[0]][1]))
            else: print('○ ' + name + 'cost: ' + str(abilityList[ability[0]][1]))
    def showSpells(self):
        i=-1
        previousSpell='aaa'
        spellList = []
        for spell in self.magic:
            if previousSpell in spell:  spellList[i].append(spell)
            else:
                i+=1
                spellList.append([spell])
                previousSpell=spell[:3]

        for line in spellList:
            print(self.colors[magics[line[0]]['speech'][4]] + ', '.join(line))

    def startingGame(self):
        self.calculateHealth()
        self.HP = self.TotalHP
        self.MP = self.TotalMP
        if self.tutorial == {}: self.tutorial = tutorials

    def showBattleStatus(self):
        #print the player's current battle status

        self.calculateHealth()

        currentHP, currentMP = self.buildHPMPDisplay()
        itemsDisplay = self.buildItemDisplay(self.item)        

        print(Fore.YELLOW + '\n---------------------------')
        print("HP : " + self.colors[self.HPBarColour] + str(currentHP))
        if self.MP==0:
            print(Fore.WHITE + "MP : " + Fore.RED + str(currentMP))
        else: print(Fore.WHITE + "MP : " + Fore.BLUE + str(currentMP))
        print(Fore.WHITE + "Items :", itemsDisplay)
        print(Fore.YELLOW + "---------------------------")

    def menu(self):
        
        itemsDisplay = self.buildItemDisplay(self.stock) 

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
        print("\nStrength: ", self.STR)
        print("Defense: ", self.DEF)
        print("Total Strength: ", damage)
        print("Total Defense: ", defense)
        print("\nExp: " + str(self.exp))
        print("Next level: " + str(levelUpExp[self.level+1]-self.exp) + ' xp')
        print(Fore.GREEN + "---------------------------\n"+Fore.WHITE+"Keyblades:")
        self.showKeyblades()
        if any(self.equipmentList):
            print(Fore.BLUE + "---------------------------\n"+Fore.WHITE+"Equipment")
            self.showEquipments()
        if any(self.magic):
            print(Fore.GREEN + "---------------------------\n"+Fore.WHITE+"Spells:")
            self.showSpells()
        if any(self.abilities):
            print(Fore.BLUE + "---------------------------\n"+Fore.WHITE+"Abilities")
            self.showAbilities()
        if any(self.keyItems):
            print("\nKey items: " + ', '.join(self.keyItems))

    def showTutorials(self):
        for text in self.tutorial:
            if self.tutorial[text] == 1:    print(tutorialSpeech[text])

    def treasureJournal(self):
        print('\nTreasures opened/total:\n')
        for world in self.treasures:
            total=0
            opened=0
            print(worldDisplayName[world])
            for room in self.treasures[world]:
                for number in self.treasures[world][room]:
                    total+=1
                    if self.treasures[world][room][number]['status']=='opened':
                        opened+=1
            print(str(opened)+'/'+str(total)+'\n')

    def mapJournal(self):
        print('\nMaps owned\n')
        for world in self.map:
            print(worldDisplayName[world])
            for mapNumber in self.map[world]:
                print('Map '+mapNumber+': '+self.map[world][mapNumber])

    def enemyDetails(self, enemyName):
        enemy=heartless[enemyName]

        try:
            if enemy['magicImmunity'] == True: magicResistance='Immune'
            else: magicResistance = str(enemy['magic resistance'])
        except:
            try: magicResistance = str(enemy['magic resistance'])
            except: magicResistance='0'

        text=Fore.YELLOW + 'HP: ' + Fore.WHITE + str(enemy['HP']) + Fore.YELLOW + '   damage: ' + Fore.WHITE + str(enemy['damage']) + Fore.YELLOW + '   defense: ' + Fore.WHITE + str(enemy['defense']) + Fore.YELLOW + '   magic resistance: ' + Fore.WHITE + magicResistance

        if enemy['HP']>9:text=text.replace('   damage:','  damage:')
        if enemy['damage']>9:text=text.replace('   defense:','  defense:')
        if enemy['defense']>9:text=text.replace('   magic:','  magic:')

        print(text)

    def enemyDeepDetails(self, enemyName):
        enemy=heartless[enemyName]
        drops=list(enemy['drop'].values())

        text=Fore.YELLOW + 'Munny: ' + Fore.WHITE + str(3*enemy['munny'][0]) + '-' + str(3*enemy['munny'][1]) + Fore.YELLOW + '    Exp: ' + Fore.WHITE + str(enemy['exp']) + Fore.YELLOW + '    Drops: ' + Fore.WHITE + ', '.join(drops)

        if (3*enemy['munny'][0])>9:text=text.replace('   Exp','  Exp')
        if (3*enemy['munny'][0])>99:text=text.replace('   Exp','  Exp')
        if (3*enemy['munny'][0])>99:text=text.replace('   Exp','  Exp')
        if enemy['exp']>99:text=text.replace('   Drops','  Drops')
        if enemy['exp']>999:text=text.replace('  Drops',' Drops')
        if not drops: text=text+'Nothing'

        print(text)

    def enemiesJournal(self):
        print('Enemy List')
        for enemy in self.enemiesList:
            tab=''
            for _ in range(30-len(enemy)):   tab=tab+' '
            print('\n' + Fore.LIGHTRED_EX + enemy.capitalize() + Fore.WHITE + tab + 'Defeated: ', self.enemiesList[enemy])
            if self.enemiesList[enemy]>=10: self.enemyDetails(enemy)
            if self.enemiesList[enemy]>=20: self.enemyDeepDetails(enemy)

#####TRADE EQUIPMENTS
    def tradeEquipment(self):
        option = ''
        while option == '':
            self.equipmentList=sorted(self.equipmentList, key=lambda x: x[0])
            print('To equip or unequip use equip/unequip [equipment]. (0 to cancel)')

            self.showEquipments()

            option = input('>')
            option = option.lower().split()
            if len(option)>2: option[1] = option[1] + ' ' + option[2]

            if option == '0' or option[0] == '0':   break

            elif option[0] == 'equip':
                if option[1] in self.equipmentList:
                    if len(self.equipment)<self.equipmentNumber:
                        self.equipment.append(option[1])
                        self.sortEquipment()
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
        while option == '':
            self.keyblades=sorted(self.keyblades, key=lambda x: x[0])
            print('To equip a different keyblade use \'equip [keyblade]\'. (0 to cancel)\n')

            self.showKeyblades()

            option = input('>')
            option = option.lower().split()
            if len(option)>3: option[1] = option[1].capitalize() + ' ' + option[2].capitalize() + ' ' + option[3].capitalize()
            elif len(option)>2: option[1] = option[1].capitalize() + ' ' + option[2].capitalize()
            elif len(option)>1: option[1] = option[1].capitalize()

            if option == '0' or option[0] == '0':
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

            print('\nTo equip an ability use \'equip [ability]\', to unequip use \'unequip [ability]\'. If you want to see an ability description use \'see [ability]\'. (0 to cancel)')
            self.showAbilities()

            option = input('>')
            option = option.lower().split()
            if len(option)>2: option[1] = option[1].capitalize() + ' ' + option[2].capitalize()
            elif len(option)>1: option[1] = option[1].capitalize()

            if option == '0' or option[0] == '0':   break

            elif option[0] == 'equip':
                if [option[1], False] in self.abilities:
                    if self.AP >= abilityList[option[1]][1]:
                        self.abilities[self.abilities.index([option[1], False])][1]=True
                        self.AP=self.AP-abilityList[option[1]][1]
                        print(Fore.GREEN + option[1] + ' equipped!\n')
                        if option[1] in finishersList: self.finishers.append(option[1])
                        if option[1] in comboModifiersList: self.comboModifiers.append(option[1])
                        if option[1] in activeAbilitiesList: self.activeAbilities.append(option[1])
                    else: print(Fore.RED + 'Not enought AP!')
                elif [option[1], True] in self.abilities: print(Fore.RED + 'This ability is already equipped!')
                else:   print(Fore.RED + 'Ability not found!')
                option=''

            elif option[0] == 'unequip':
                if [option[1], True] in self.abilities:
                    self.abilities[self.abilities.index([option[1], True])][1]=False
                    self.AP+=abilityList[option[1]][1]
                    print(Fore.CYAN + option[1] + ' unequipped!\n')
                    if option[1] in finishersList: del(self.finishers[self.finishers.index(option[1])])
                    if option[1] in comboModifiersList: del(self.comboModifiers[self.comboModifiers.index(option[1])])
                    if option[1] in activeAbilitiesList: del(self.activeAbilities[self.activeAbilities.index(option[1])])
                elif [option[1], False] in self.abilities: print(Fore.RED + 'This ability is already unequipped!')
                else:   print(Fore.RED + 'Ability not found')
                option=''

            elif option[0] == 'see':
                if [option[1], True] in self.abilities or [option[1], False] in self.abilities: print('\n' + Fore.YELLOW + option[1] + Fore.WHITE + ': ' + abilityList[option[1]][0])
                option=''
            
            else:
                print(Fore.RED + 'Command not found')
                option=''

        self.calculateHealth()
