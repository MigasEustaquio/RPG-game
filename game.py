#!/bin/python3
import random

from dictionaries.people import *
from dictionaries.location import *
from dictionaries.enemies import *
from utilities.screen import *


def showInstructions():
    #print a main menu and the commands
    print('''
Traverse Town
========
Talk to Leon!
Find Donald and Goofy!
Survive the heartless!

Commands:
  go [direction]/[back]
  enter [location]
  talk [person]
  menu
''')

def showStatus():                ###SHOW STATUS
  #print the player's current status
  print(Fore.RED + '\n---------------------------')
  print(Fore.WHITE + 'You are in the ' + currentRoom)
  if "person" in rooms[currentRoom]:
    print('You see ' + rooms[currentRoom]['person'])
    if rooms[currentRoom]['person'].lower() not in player.map:
      player.map = player.map + people[rooms[currentRoom]['person']]['mapUpdate']
  if "shop" in rooms[currentRoom] and (currentRoom+' Shop location') in player.keyItems:
    print('You see the ' + rooms[currentRoom]['shop'] + ', try: \'enter shop\'')
  if "Shop" in currentRoom:
      player.HP = player.MaxHP
      player.MP = player.MaxMP
      print('\nYou see a Save point, HP and MP restored!\nTo open the save menu just type \'save\'\nTo get out of the shop type: \'go back\'')
  if 'treasure' in rooms[currentRoom]:
    print('You see a treasure chest!')
  print(Fore.RED + "---------------------------")

def shop(currentRoom):                    ###SHOP
    for item in shops[currentRoom]:
        print(item, '   \tcost:', shops[currentRoom][item], 'munny!')

def levelUP():                                   ###LEVEL UP
  if levelUp[player.level]['ability'] != 'none':
    player.abilities.append(levelUp[player.level]['ability'])
    print('\nObtained ' + levelUp[player.level]['ability'] + '!')
  if levelUp[player.level]['HP'] != 0:
    player.MaxHP += levelUp[player.level]['HP']
    player.HP += levelUp[player.level]['HP']
    print('Maximum HP increased')
  if levelUp[player.level]['MP'] != 0:
    player.MaxMP += levelUp[player.level]['MP']
    player.MP += levelUp[player.level]['MP']
    print('Maximum MP increased')

def useItem(item):                          ###USE ITEM
  del player.item[player.item.index(item)]

  if str(item) == 'ether' or str(item) == 'elixir':
    print('\nUsed an ' + green + str(item))
  else:
    print('\nUsed a ' + green + str(item))

  if 'potion' in item:
    print(items[item]['speech'][0] + red + items[item]['speech'][1] + white + items[item]['speech'][2])
  elif 'ether' in item:
    print(items[item]['speech'][0] + blue + items[item]['speech'][1] + white + items[item]['speech'][2])
  else:
    print(items[item]['speech'][0] + red + items[item]['speech'][1] + white + items[item]['speech'][2] +  blue + items[item]['speech'][3] + white + items[item]['speech'][4])

  player.HP = player.HP + items[item]['HP']
  if player.HP > player.MaxHP: player.HP = player.MaxHP
  player.MP = player.MP + items[item]['MP']
  if player.MP > player.MaxMP: player.MP = player.MaxMP


def scan(enemy, heartlessHealth):              ###SCAN
  heartlessHealthDisplay = ''
  i=0
  while i<heartless[enemy]['HP']:
    if i<heartlessHealth:
      heartlessHealthDisplay += '♥'
    else:
      heartlessHealthDisplay += '♡'
    i+=1

  print(Fore.MAGENTA + '\n---------------------------')
  print("Scan : " + enemy)
  print("HP : " + red + heartlessHealthDisplay)
  print(Fore.MAGENTA + "---------------------------")


def statusEffectDamage(statusEffect, heartlessHealth, statusDuration):         ###STATUS EFFECT DAMAGE
  print(magics[statusEffect]['status']['speech'][0] + player.colors[magics[statusEffect]['speech'][4]] + magics[statusEffect]['status']['speech'][1] + white + magics[statusEffect]['status']['speech'][2] + red + magics[statusEffect]['status']['speech'][3] + white + magics[statusEffect]['status']['speech'][4])
  return heartlessHealth-magics[statusEffect]['status']['damage'], statusDuration - 1

def calculateDamage (heartlessHealth, heartlessDamage, damage):         ###CALCULATE DAMAGE
  print("You lost " + red + str(heartlessDamage) + ' ♥ ' + white + '!')
  oldHP = player.HP
  player.HP = player.HP - heartlessDamage
  if 'second chance' in player.abilities:
    if player.HP < 1 and oldHP > 1:
      player.HP = 1
      print('Second Chance')
  return heartlessHealth-damage

def battle(enemy):                 ###BATTLE

    print("---------------------------")
    print('You see a ' + red + 'Heartless' + white +'! It\'s a '+ red + enemy + white + '!')
    print('commands: \n\nattack \nmagic [magic name] \nitem [item name] \nrun')
    
    heartlessHealth = int(heartless[enemy]['HP'])
    statusEffect = 'none'
    statusDuration = 99
    command = ''

    while True:
        player.showBattleStatus()

        if 'scan' in player.abilities:
          scan(enemy, heartlessHealth)

        while command == '':
            command = input('>')
        command = command.lower()

        heartlessDamage = int(heartless[enemy]['damage'])
        damage = keybladeStatus[player.keyblade]['damage']

### Status effect duration
        if statusDuration == 0:
          print('\nThe ' + player.colors[magics[statusEffect]['speech'][4]] + magics[statusEffect]['status']['name'] + white + ' effect has passed\n')
          statusEffect = 'none'
          statusDuration = 99

        if 'blizza' in statusEffect:
          heartlessDamage = heartlessDamage - magics[statusEffect]['status']['reduction']
###
        print("---------------------------")

        if command == 'attack':       ###ATTACK
            command = ''
            print('You and the heartless attack each other!')
            print('You caused ' + red + str(damage) + ' ♥ ' + white + 'of damage!')
### Status effect
            if statusEffect != 'none':
              heartlessHealth, statusDuration = statusEffectDamage(statusEffect, heartlessHealth, statusDuration)
### Calculate damage
            heartlessHealth = calculateDamage(heartlessHealth, heartlessDamage, damage)

        elif "magic" in command:       ###MAGIC
          command = command.lower().split()
          if not player.magic:
            print('Magic is still a mystery to you!')

          else:
            if command[1] in player.magic:
              if player.MP >= magics[command[1]]['MP']:

                magicText = magics[command[1]]['speech']
###COLOR SPEECH
                print('You used ' + blue + str(magics[command[1]]['MP']) +' ● ' + white + '!')
                if command[1] != 'cure':
                  print(magicText[0] + red + magicText[1] + white + magicText[2] + player.colors[magicText[4]] + magicText[3])
                else:
                  print(magicText[0] + red + magicText[1] + white + magicText[2])
                player.MP = player.MP - magics[command[1]]['MP']
### Status effect
                if statusEffect != 'none':
                  heartlessHealth, statusDuration = statusEffectDamage(statusEffect, heartlessHealth, statusDuration)
###Calculate damage
                print("The heartless attacks you!")
                player.HP = player.HP + magics[command[1]]['heal']
                if player.HP > player.MaxHP: player.HP = player.MaxHP
                heartlessHealth = calculateDamage(heartlessHealth, heartlessDamage, magics[command[1]]['damage'])
### Start status effect
                if command[1] != 'cure':
                  statusEffect = command[1]
                  statusDuration = magics[statusEffect]['status']['duration']
###
              else:
                print('Not enough MP!')

          command = ''

        elif "item" in command:       ###ITEM
          command = command.lower().split()
          if not player.item:
            print('You have no items!')
          else:
            try:
              if command[1] in player.item:
                useItem(command[1])
### Status effect
                if statusEffect != 'none':
                  heartlessHealth, statusDuration = statusEffectDamage(statusEffect, heartlessHealth, statusDuration)
###Calculate damage
                print("The heartless attacks you!")
                heartlessHealth = calculateDamage(heartlessHealth, heartlessDamage, 0)

              else:
                print("You don\'t have any ", command[1])
            except IndexError:
                print('try: item [item name]')
          command = ''

        elif "run" in command:       ###RUN
            command = ''
            print('You got away successfully!')
            return 'run'

        else:       ###ERROR
          command = ''
          print('Command not found!')

        if player.HP < 1:       ###DEFEAT
            return 'defeat'

        if heartlessHealth <= 0:       ###VICTORY

            munny = 3 * random.randint(heartless[enemy]['munny'][0], heartless[enemy]['munny'][1])
            print('\nYou defeated the Heartless!\nCONGRATULATIONS!')
            print('\nYou obtained ' + yellow + str(munny) + '🔸 munny!')
            player.munny += munny
            print('You gained ' + str(heartless[enemy]['exp']) + ' exp!')
            player.exp += heartless[enemy]['exp']

            if player.exp >= levelUp[player.level]['next']:
              player.level+=1
              print('Level Up!\nLevel: ' + str(player.level))
              levelUP()

            return 'victory'

#################       MAIN

player = player()

with open('utilities/saveFile.txt', 'r') as f:
  saves = ast.literal_eval(f.read())

#start the player in the First District
currentRoom = 'First District'
previusRoom = 'First District'

#COLOR
colorama_init(autoreset=True)
colors = dict(Fore.__dict__.items())
red = player.colors['RED']
white = player.colors['WHITE']
blue = player.colors['BLUE']
yellow = player.colors['YELLOW']
green = player.colors['GREEN']

alreadyBattled = 0
firstTimeMap = 0

titleScreen(player, saves)

showInstructions()

while True:
  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go up' would give the list:
  #['go','up']

  move = ''
  while move == '':  
    move = input('>')

  move = move.lower().split()

  if 'map' in move:        ##### OPEN MAP
    if firstTimeMap == 0:
      print('The first time opening a map may glitch and refuse to open, just close the map and open it again!')
      firstTimeMap = 1
    
    print('Opening map...\n')
    from PIL import Image
    img = Image.open('images/' + player.world + '/Map' + str(maps[player.world][player.map]) + '.jpg')
    img.show()
  
  elif 'treasure' in move:        ##### TREASURE
    if 'treasure' in rooms[currentRoom]:
      if rooms[currentRoom]['treasure']['treasure'] == 'item':
        print('You got a "' + rooms[currentRoom]['treasure']['item'] + '"!')
        if len(player.item) < player.itemPouch:
          player.item.append(rooms[currentRoom]['treasure']['item'])
        else:
          player.stock.append(rooms[currentRoom]['treasure']['item'])
          print('Your item pouch is full, item send to stock!!')

      if rooms[currentRoom]['treasure']['treasure'] == 'key item':
        print('You got the "' + rooms[currentRoom]['treasure']['key item'] + '" key item!')
        player.keyItems.append(rooms[currentRoom]['treasure']['key item'])

      if rooms[currentRoom]['treasure']['treasure'] == 'mapUpdate':
        player.map = player.map + rooms[currentRoom]['treasure']['mapUpdate']
        print(player.world + ' map updated!')

      del rooms[currentRoom]['treasure']
    else:
      print('There\'s no treasure chest in this room!')

  elif 'menu' in move:        ##### SHOW MENU
      player.menu()

  elif 'save' in move:
    if 'Shop' in currentRoom:
      saveScreen(player, saves)
    else:
      print('There is no save point here!')

  elif move[0] == 'buy':        ##### BUY IN SHOP
    if 'Shop' in currentRoom:
      if move[1] in shops[currentRoom]:
        if player.munny >= shops[currentRoom][move[1]]:
            print('\nMoogle: Thanks for shopping here, Kupo!!\nObtained a ' + move[1] + '!')
            player.munny = player.munny - shops[currentRoom][move[1]]
            if len(player.item) < player.itemPouch:
              player.item.append(move[1])
            else:
              player.stock.append(move[1])
              print('Your item pouch is full, item send to stock!!')
        else:
            print('\nMoogle: You don\'t have enough munny for this item, Kupo!!')
      else:
          print('\nMoogle: I\'m sorry, I don\'t have this item, Kupo!')
    else:
      print('You are not in a shop!')


  elif move[0] == 'use':        ##### USE ITEM
    if not player.item:
        print('You have no items!')
    else:
        try:
            if move[1] in player.item:
                useItem(move[1])
            else:
                print("You don\'t have any ", move[1])
        except IndexError:
            print('try: use [item]')
        command = ''


  elif move[0] == 'cast':        ##### MAGIC
    if not player.magic:
        print('Magic is still a mystery to you!')

    else:
      if move[1] in player.magic:
        if move[1] != 'cure':
          print('You can\'t cast that now!')
        else:
          if player.MP >= magics[move[1]]['MP']:
            print('You used ' + blue + str(magics[move[1]]['MP']) +' ● ' + white + '!')
            print(magics[move[1]]['speech'][0] + red + magics[move[1]]['speech'][1] + white + magics[move[1]]['speech'][2])
            player.MP = player.MP - magics[move[1]]['MP']
            player.HP = player.HP + magics[move[1]]['heal']
            if player.HP > player.MaxHP: player.HP = player.MaxHP
          else:
            print('Not enough MP!')


  #if they type 'go' first
  elif move[0] == 'go' or move[0] == 'enter':        ##### MOVE
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      alreadyBattled = 0
      previusRoom = currentRoom
      currentRoom = rooms[currentRoom][move[1]]
      for room in rooms[currentRoom]['resetHeartless']:
        if rooms[room]['heartless']['status'] == 0:
          rooms[room]['heartless']['status'] = rooms[room]['heartless']['waves']
    #there is no door (link) to the new room
    elif move[1] == 'back':
        alreadyBattled = 0
        temp = currentRoom
        currentRoom = previusRoom
        previusRoom = temp
        for room in rooms[currentRoom]['resetHeartless']:
          if rooms[room]['heartless']['status'] == 0:
            rooms[room]['heartless']['status'] = rooms[room]['heartless']['waves']
    else:
      print('You can\'t go that way!')

  #if they type 'talk' first
  elif move[0] == 'talk' :        ##### TALK WITH PERSON
    #if the room contains an person
    if 'person' in rooms[currentRoom] and move[1] in rooms[currentRoom]['person'].lower():
      #falar com a pessoa
      print(people[rooms[currentRoom]['person']]['speech'])
      reward = people[rooms[currentRoom]['person']]['reward']
      if reward == 'story':
        if player.story == (people[rooms[currentRoom]['person']]['story']-1):
          player.story += 1
          print()

      elif reward == 'key item':
        player.keyItems.append(people[rooms[currentRoom]['person']]['key item'])
        print('You got the "' + people[rooms[currentRoom]['person']]['key item'] + '" key item!')

      elif reward == 'item':
        print('You got a "' + people[rooms[currentRoom]['person']]['item'] + '"!')
        if len(player.item) < player.itemPouch:
          player.item.append(people[rooms[currentRoom]['person']]['item'])
        else:
          player.stock.append(people[rooms[currentRoom]['person']]['item'])
          print('Your item pouch is full, item send to stock!!')
      people[rooms[currentRoom]['person']]['reward'] = 'no'
      if rooms[currentRoom]['person'].lower() == 'moogle':
          shop(currentRoom)

    else:
      #tell them they can't talk
      print('Can\'t talk to ' + move[1] + '!')


  if 'heartless' in rooms[currentRoom] and alreadyBattled == 0:           ###### BATTLE
    status = rooms[currentRoom]['heartless']['status']
    if status > 0:
      result = battle(rooms[currentRoom]['heartless']['wave'][status])  
      if result == 'victory':
        alreadyBattled = 1
        rooms[currentRoom]['heartless']['status'] = (status - 1)
      elif result == 'run':
          temp = currentRoom
          currentRoom = previusRoom
          previusRoom = temp
      elif result == 'defeat':
          print("---------------------------")
          print('Your HP has dropped to zero!\nGAME OVER')
          break


  # player wins if they get to the Third District
  if currentRoom == 'Third District' and  player.story == 1:
    print('You found Donald & Goofy... YOU WIN!')
    break
