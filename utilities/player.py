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
        print('\nMunny: ' + str(self.munny) + '🔸')
        print("Items in stock: ", self.stock)
        print(Fore.YELLOW + "---------------------------")
        print('To cast a magic spell just type \'cast [magic]\'')
        print('To use an item just type \'use [item]\'')
        print('To equip an equipment just type \'equipment\'')
        print('To open the map of the current World just type \'map\'')
        print('To get the treasure chest from the current room just type \'treasure\'')
        print(Fore.YELLOW + "---------------------------")

    def status(self):
        self.menu()
        print(Fore.GREEN + "---------------------------")
        print("Keyblade: " + self.keyblade)
        print("Keyblade List: ", *self.keyblades)
        print("Equipment: " + str(self.equipment))
        print("Number of equipable equipment: " + str(self.equipmentNumber))
        print("Equipment List: " + str(self.equipmentList))
        print("Exp: " + str(self.exp))
        print("Next level: " + str(levelUp[self.level]['next']-self.exp) + ' xp')
        print("Key items: ", self.keyItems)
        print(Fore.BLUE + "---------------------------")
        print("Spells learned: ", *self.magic)
        print("Abilities: ", self.abilities)
        print("Strength: ", self.STR)
        print("Defense: ", self.DEF)


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
                option=''

            elif option == '0':
                break

            elif option[0] == 'equip':
                if option[1] in self.equipmentList:
                    if len(self.equipment)<self.equipmentNumber:
                        self.equipment.append(option[1])
                        self.equipmentList.remove(option[1])
                        print(option[1] + ' equipped!\n')
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


    def tradeKeyblade(self):
        option = ''
        i=0
        while option == '':
            print('To equip a different keyblade use equip [keyblade] or navigate with \'next\' or \'previous\'. (0 to cancel)\n')
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
            if len(option)>2: option[1] = option[1] + ' ' + option[2]

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

            elif option == '0':
                break

            elif option[0] == 'equip':
                if option[1].capitalize() in self.keyblades:
                    self.keyblade = option[1].capitalize()
                    print(option[1].capitalize() + ' equipped!\n')
                    break
                else:
                    print(Fore.RED + 'Equipment not found')
                option=''
            
            else:
                print(Fore.RED + 'Command not found')
                option=''