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
  x['MaxAP'] = y.MaxAP
  x['AP'] = y.AP
  x['magicPower'] = y.magicPower
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
  x['comboModifiers'] = y.comboModifiers
  x['activeAbilities'] = y.activeAbilities
  x['path'] = y.path
  x['world'] = y.world
  x['map'] = y.map
  x['tutorial'] = y.tutorial
  x['treasures'] = y.treasures
  x['restrictionLifted'] = y.restrictionLifted
  x['visitedRooms'] = y.visitedRooms
  x['enemiesList'] = y.enemiesList
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
  y.MaxAP = x['MaxAP']
  y.AP = x['AP']
  y.STR = x['STR']
  y.DEF = x['DEF']
  y.magicPower = x['magicPower']
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
  y.comboModifiers = x['comboModifiers']
  y.activeAbilities = x['activeAbilities']
  y.path = x['path']
  y.world = x['world']
  y.map = x['map']
  y.tutorial = x['tutorial']
  y.treasures = x['treasures']
  y.restrictionLifted = x['restrictionLifted']
  y.visitedRooms = x['visitedRooms']
  y.enemiesList = x['enemiesList']
  y.currentRoom = x['currentRoom']
  y.story = x['story']
  y.shipUnlocked = x['shipUnlocked']
  y.unlockedWorlds = x['unlockedWorlds']
  y.unlockedArenas = x['unlockedArenas']
  y.arenaRecords = x['arenaRecords']
  y.saveFile = file
  y.HP = y.MaxHP
  y.MP = y.MaxMP

def deleteFile(file, saves):
  saves.pop(file)
  with open('utilities/saveFile.txt', 'w') as file:
    file.write(str(saves))
  print('\nDelete complete!\n')

def loadScreen(player, saves):
  option = ''
  while option == '':
    if player.HPBKP == 0:
      print('Select a save file. (0 to cancel) (\'delete\' [file] to permanently delete a save file)\n')
    else:
      print('Select a save file.\n')

    for save in saves:
        tab = 'Save ' + str(save) +'\tLvl: ' + str(saves[save]['level']) + '   World: ' + str(saves[save]['world'])
        if saves[save]['level'] > 9: tab=tab.replace('   World:', '  World:')
        print(tab)

    option = input('\n>')

    if option == '0' and player.HPBKP == 0:
      titleScreen(player, saves)

    elif option.isnumeric():
        if int(option) in saves:
            load(int(option), player, saves)
            break
        else: print(Fore.RED + 'Save file not found')
        option=''

    elif 'delete' in option:
      try:
        option=option.split(' ')
        fileNumber=int(option[1])
        if fileNumber in saves:
          answer = input('\nAre you sure you want to permanently delete the save file ' + option[1] + '? (yes/no)\n>')
          if answer.lower() == 'yes': deleteFile(fileNumber, saves)
          else: print('\nDelete canceled\n')
        else: print(Fore.RED + 'Save file not found')
      except: print(Fore.RED + 'Please select a file. (\'delete\' [file])\n')
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
    while option == '':
      print('Select a save file or create a new one. (0 to cancel)\n')

      for file in saves:
        tab = 'Save ' + str(file) +'\tLvl: ' + str(saves[file]['level']) + '   World: ' + str(saves[file]['world'])
        if saves[file]['level'] > 9: tab=tab.replace('   World:', '  World:')
        print(tab)

      option = input('>')

      # if str(option).lower() == 'next':
      #     if (i+3) in saves:
      #         i+=1
      #     else:
      #         print(Fore.RED + 'No save file after these!')
      #     option=''
      # elif str(option).lower() == 'previous':
      #     if i>1:
      #         i-=1
      #     else:
      #         print(Fore.RED + 'No save file previous to these!')
      #     option=''

      if option == '0':
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