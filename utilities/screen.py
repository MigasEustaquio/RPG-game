import ast
from utilities.player import *

def save(file, y, saves):
  print('Saving file...\n')
  x=saves[file]

  x['keyblade'] = y.keyblade
  x['HP'] = y.MaxHP
  x['MP'] = y.MaxMP
  x['magic'] = y.magic
  x['item'] = y.item
  x['itemPouch'] = y.itemPouch
  x['keyItems'] = y.keyItems
  x['exp'] = y.exp
  x['level'] = y.level
  x['munny'] = y.munny
  x['stock'] = y.stock
  x['keyblades'] = y.keyblades
  x['abilities'] = y.abilities
  x['world'] = y.world
  x['map'] = y.map
  x['story'] = y.story
  y.saveFile = file

  with open('saveFile.txt', 'w') as file:
    file.write(str(saves))

  print('Save complete\n')


def load(file, y, saves):
  print('Loading save file...\n')
  x=saves[file]

  y.keyblade = x['keyblade']
  y.MaxHP = x['HP']
  y.MaxMP = x['MP']
  y.magic = x['magic']
  y.item = x['item']
  y.itemPouch = x['itemPouch']
  y.keyItems = x['keyItems']
  y.exp = x['exp']
  y.level = x['level']
  y.munny = x['munny']
  y.stock = x['stock']
  y.keyblades = x['keyblades']
  y.abilities = x['abilities']
  y.world = x['world']
  y.map = x['map']
  y.story = x['story']
  y.saveFile = file
  y.HP = y.MaxHP
  y.MP = y.MaxMP

def loadScreen(player, saves):
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
        print(Fore.RED + 'No save file after this!')
      option=''
    elif str(option).lower() == 'previous':
      if i>1:
        i-=1
      else:
        print(Fore.RED + 'No save file previous to this!')
      option=''
    elif option == '0':
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
  if (input('To write the save file from the \'saves\' dict inside \"utilities\\save.py\" to the saveFile.txt write \'save\'.')) == 'save':
    with open('utilities/saveFile.txt', 'w') as file:
      file.write(str(player.editedSaves))
    with open('utilities/saveFile.txt', 'r') as f:
      saves = ast.literal_eval(f.read())
    print('saveFile.txt overwritten!')
    return saves

def titleScreen(player, saves):

  while True:
    print('---------------------------')
    print('''
KINGDOM HEARTS🤍

Text-Based RPG

New Game
Load Game
  ''')
    print('---------------------------')

    option = ''
    while option == '':  
      option = input('>')
    option = option.lower()

    if 'new' in option or 'New' in option:
      print('New game starting')
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
            print()
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
                print(Fore.RED + 'No save file after this!')
            option=''
        elif str(option).lower() == 'previous':
            if i>1:
                i-=1
            else:
                print(Fore.RED + 'No save file previous to this!')
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
                save(int(option), y, saves)
                return
        else:
            print(Fore.RED + 'Save file not found')
            option=''