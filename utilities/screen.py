import ast
import sys
from utilities.player import *

def save(file, y, saves):
  print('Saving in file ' +  str(file)  +'...\n')

  saves[file] = {}
  x=saves[file]

  x['keyblade'] = y.keyblade
  x['HP'] = y.MaxHP
  x['STR'] = y.STR
  x['DEF'] = y.DEF
  x['MP'] = y.MaxMP
  x['magic'] = y.magic
  x['item'] = y.item
  x['itemPouch'] = y.itemPouch
  x['keyItems'] = y.keyItems
  x['equipment'] = y.equipment
  x['equipmentNumber'] = y.equipmentNumber
  x['equipmentList'] = y.equipmentList
  x['exp'] = y.exp
  x['level'] = y.level
  x['munny'] = y.munny
  x['stock'] = y.stock
  x['keyblades'] = y.keyblades
  x['abilities'] = y.abilities
  x['finishers'] = y.finishers
  x['world'] = y.world
  x['map'] = y.map
  x['tutorial'] = y.tutorial
  x['treasures'] = y.treasures
  x['restrictionLifted'] = y.restrictionLifted
  x['currentRoom'] = y.currentRoom
  x['story'] = y.story
  x['shipUnlocked'] = y.shipUnlocked
  x['unlockedWorlds'] = y.unlockedWorlds
  x['unlockedArenas'] = y.unlockedArenas
  x['arenaRecords'] = y.arenaRecords
  y.saveFile = file

  saves[file]=x

  with open('utilities/saveFile.txt', 'w') as file:
    file.write(str(saves))

  print('Save complete!\n')


def load(file, y, saves):
  print('Loading save file...\n')
  x=saves[file]

  y.keyblade = x['keyblade']
  y.MaxHP = x['HP']
  y.MaxMP = x['MP']
  y.STR = x['STR']
  y.DEF = x['DEF']
  y.magic = x['magic']
  y.item = x['item']
  y.itemPouch = x['itemPouch']
  y.keyItems = x['keyItems']
  y.equipment = x['equipment']
  y.equipmentNumber = x['equipmentNumber']
  y.equipmentList = x['equipmentList']
  y.exp = x['exp']
  y.level = x['level']
  y.munny = x['munny']
  y.stock = x['stock']
  y.keyblades = x['keyblades']
  y.abilities = x['abilities']
  y.finishers = x['finishers']
  y.world = x['world']
  y.map = x['map']
  y.tutorial = x['tutorial']
  y.treasures = x['treasures']
  y.restrictionLifted = x['restrictionLifted']
  y.currentRoom = x['currentRoom']
  y.story = x['story']
  y.shipUnlocked = x['shipUnlocked']
  y.unlockedWorlds = x['unlockedWorlds']
  y.unlockedArenas = x['unlockedArenas']
  y.arenaRecords = x['arenaRecords']
  y.saveFile = file
  y.HP = y.MaxHP
  y.MP = y.MaxMP

def loadScreen(player, saves):
  option = ''
  i=1
  while option == '':
    if player.HPBKP == 0:
      print('Select a save file or navigate with \'next\' or \'previous\'. (0 to cancel)\n')
    else:
      print('Select a save file or navigate with \'next\' or \'previous\'.\n')
    if 2 in saves:
      if 3 in saves:
        print(Fore.BLUE + '''
    Save ''' + str(i) + '''   \t\t\t\tSave ''' + str(i+1) + '''   \t\t\t\tSave ''' + str(i+2) + Fore.WHITE + '''

    Lvl: ''' + str(saves[i]['level']) + '''   \t\t\t\tLvl: ''' + str(saves[i+1]['level']) + '''   \t\t\t\tLvl: ''' + str(saves[i+2]['level']) + '''
    World: ''' + str(saves[i]['world']) + '''   \t\tWorld: ''' + str(saves[i+1]['world']) + '''   \t\tWorld: ''' + str(saves[i+2]['world']) + '''
        ''')
      else:
        print(Fore.BLUE + '''
    Save ''' + str(i) + '''   \t\t\t\tSave ''' + str(i+1) + Fore.WHITE + '''

    Lvl: ''' + str(saves[i]['level']) + '''   \t\t\t\tLvl: ''' + str(saves[i+1]['level']) + '''
    World: ''' + str(saves[i]['world']) + '''   \t\tWorld: ''' + str(saves[i+1]['world']) + '''
        ''')
    else:
      print(Fore.BLUE + '''
    Save ''' + str(i) + Fore.WHITE + '''

    Lvl: ''' + str(saves[i]['level']) + '''
    World: ''' + str(saves[i]['world']) + '''
        ''')
    option = input('>')
    if str(option).lower() == 'next':
      if (i+3) in saves:
        i+=1
      else:
        print(Fore.RED + 'No save file after this!')
      option=''
    elif str(option).lower() == 'previous':
      if i>1:
        i-=1
      else:
        print(Fore.RED + 'No save file previous to this!')
      option=''
    elif option == '0' and player.HPBKP == 0:
      titleScreen(player, saves)
    elif option.isnumeric():
        if int(option) in saves:
            load(int(option), player, saves)
            break
        else:
            print(Fore.RED + 'Save file not found')
            option=''
    else:
      print(Fore.RED + 'Save file not found')
      option=''



def editSaveFile(player):
  if 'edit' in sys.argv or (input('To write the save file from the \'saves\' dict inside \"utilities\\save.py\" to the saveFile.txt write \'save\'.')) == 'save':
    with open('utilities/saveFile.txt', 'w') as file:
      file.write(str(player.editedSaves))
    with open('utilities/saveFile.txt', 'r') as f:
      saves = ast.literal_eval(f.read())
    print('saveFile.txt overwritten!')
    return saves

def titleScreen(player, saves):

  while True:
    print('\n\n---------------------------')
    print('''
KINGDOM HEARTS🤍

Text-Based RPG

New Game
Load Game
  ''')
    print('---------------------------')

    if 'edit' in sys.argv:
      saves = editSaveFile(player)

    option = ''
    while option == '':  
      option = input('>')
    option = option.lower()

    if 'new' in option or 'New' in option:
      print('\n\n\nNew game starting')
      break

    elif 'load' in option or 'Load' in option:
      if 1 in saves:
        saves = loadScreen(player, saves)
      break
    
    elif 'edit save' in option:
      saves = editSaveFile(player)

    else:
      print('Command not foud')


def saveScreen(y, saves):
    if y.saveFile !=0:
        answer = input('You wish to overwrite the save file ' + str(y.saveFile) + ' ? (yes/no)\n>')
        if answer.lower() == 'yes':
            save(int(y.saveFile), y, saves)
            return
        elif answer.lower() == 'no':
            pass
        else:
            print('Save canceled')
            return
    
    option = ''
    i=1
    while option == '':
        print('Select a save file or navigate with \'next\' or \'previous\'. (0 to cancel)\n')
        if 2 in saves:
            if 3 in saves:
                print(Fore.BLUE + '''
Save ''' + str(i) + '''   \t\t\t\tSave ''' + str(i+1) + '''   \t\t\t\tSave ''' + str(i+2) + Fore.WHITE + '''

Lvl: ''' + str(saves[i]['level']) + '''   \t\t\t\tLvl: ''' + str(saves[i+1]['level']) + '''   \t\t\t\tLvl: ''' + str(saves[i+2]['level']) + '''
World: ''' + str(saves[i]['world']) + '''   \t\tWorld: ''' + str(saves[i+1]['world']) + '''   \t\t\tWorld: ''' + str(saves[i+2]['world']) + '''
        ''')
            else:
                print(Fore.BLUE + '''
Save ''' + str(i) + '''   \t\t\t\tSave ''' + str(i+1) + Fore.WHITE + '''

Lvl: ''' + str(saves[i]['level']) + '''   \t\t\t\tLvl: ''' + str(saves[i+1]['level']) + '''
World: ''' + str(saves[i]['world']) + '''   \t\tWorld: ''' + str(saves[i+1]['world']) + '''
        ''')
        else:
            print(Fore.BLUE + '''
Save ''' + str(i) + Fore.WHITE + '''

Lvl: ''' + str(saves[i]['level']) + '''
World: ''' + str(saves[i]['world']) + '''
        ''')

        option = input('>')
        if str(option).lower() == 'next':
            if (i+3) in saves:
                i+=1
            else:
                print(Fore.RED + 'No save file after these!')
            option=''
        elif str(option).lower() == 'previous':
            if i>1:
                i-=1
            else:
                print(Fore.RED + 'No save file previous to these!')
            option=''
        elif option == '0':
          print('Save canceled')
          return
        elif option.isnumeric():
            if int(option) in saves:
                answer = input('You wish to overwrite the save file ' + option + ' ? (yes/no)')
                if answer.lower() == 'yes':
                    save(int(option), y, saves)
                    return
                else:
                    print('Save canceled')
            else:
                if (int(option)-1) in saves:
                  save(int(option), y, saves)
                else:
                  print("Save file too far! Saving in new file...")
                  save(len(saves)+1, y, saves)
                return
        else:
            print(Fore.RED + 'Save file not found')
            option=''