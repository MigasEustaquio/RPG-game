#!/bin/python3
import random

from dictionaries.people import *
from dictionaries.location import *
from dictionaries.enemies import *
from utilities.screen import *


def showInstructions():
    #print a main menu and the commands
    print('''
Tutorial:
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
  if "person" in rooms[player.world][currentRoom]:
    print('You see ' + rooms[player.world][currentRoom]['person'])
    if rooms[player.world][currentRoom]['person'].lower() not in player.map:
      player.map = player.map + people[rooms[player.world][currentRoom]['person']]['mapUpdate']
  if "shop" in rooms[player.world][currentRoom] and (currentRoom+' Shop location') in player.keyItems:
    print('You see the ' + rooms[player.world][currentRoom]['shop'] + ', try: \'enter shop\'')
  if "Shop" in currentRoom:
      player.HP = player.TotalHP
      player.MP = player.TotalMP
      print('\nYou see a Save point, HP and MP restored!')
      if player.tutorial['save'] == 0:
        print(Fore.YELLOW + "tutorial: " + Fore.WHITE + tutorialSpeech['save'])
        player.tutorial['save'] = 1
      print('To get out of the shop type: \'go back\'')
  if 'treasure' in rooms[player.world][currentRoom]:
    print('You see a treasure chest!')
    if player.tutorial['treasure chest'] == 0:
      print(Fore.YELLOW + "tutorial: " + Fore.WHITE + tutorialSpeech['treasure chest'])
      player.tutorial['treasure chest'] = 1
  print(Fore.RED + "---------------------------")

def shop(currentRoom):                    ###SHOP
    for item in shops[currentRoom]:
        print(item, '   \tcost:', shops[currentRoom][item], 'munny!')

def levelUP():                                   ###LEVEL UP
  if levelUp[player.level]['ability'] != 'none':
    player.abilities.append(levelUp[player.level]['ability'])
    print('\nObtained ' + levelUp[player.level]['ability'] + '!')
    if levelUp[player.level]['ability'] in finishersList:
      player.finishers.append(levelUp[player.level]['ability'])
  if levelUp[player.level]['HP'] != 0:
    player.MaxHP += levelUp[player.level]['HP']
    player.HP += levelUp[player.level]['HP']
    print('Maximum HP increased!')
  if levelUp[player.level]['MP'] != 0:
    player.MaxMP += levelUp[player.level]['MP']
    player.MP += levelUp[player.level]['MP']
    print('Maximum MP increased!')
  if 'STR' in levelUp[player.level]:
    player.STR += levelUp[player.level]['STR']
    print('Strength increased!')
  if 'DEF' in levelUp[player.level]:
    player.DEF += levelUp[player.level]['DEF']
    print('Defense increased!')

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
  if player.HP > player.TotalHP: player.HP = player.TotalHP
  player.MP = player.MP + items[item]['MP']
  if player.MP > player.TotalMP: player.MP = player.TotalMP


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


def statusEffectDamage(statusEffect, heartlessHealth, statusDuration):           ###STATUS EFFECT DAMAGE
  print(magics[statusEffect]['status']['speech'][0] + player.colors[magics[statusEffect]['speech'][4]] + magics[statusEffect]['status']['speech'][1] + white + magics[statusEffect]['status']['speech'][2] + red + magics[statusEffect]['status']['speech'][3] + white + magics[statusEffect]['status']['speech'][4])
  return heartlessHealth-magics[statusEffect]['status']['damage'], statusDuration - 1

def calculateDamage (heartlessHealth, heartlessDamage, damage, defense):         ###CALCULATE DAMAGE TAKEN
  damageTaken = heartlessDamage-defense
  if damageTaken < 0: damageTaken = 0
  print("You lost " + red + str(damageTaken) + ' ♥ ' + white + '!')
  oldHP = player.HP
  player.HP = player.HP - damageTaken
  if 'Second Chance' in player.abilities:                                    ###SECOND CHANCE
    if player.HP < 1 and oldHP > 1:
      player.HP = 1
      print('Second Chance')
  return heartlessHealth-damage

def finishAttack(heartlessHealth, damage):

  finish = player.finishers[random.randint(0, (len(player.finishers)-1))]
  if finish == 'Blitz':
    print("You used Blitz and dealt " + yellow + "double" + white + " damage!" + ' You caused ' + red + str(2*damage) + ' ♥ ' + white + 'of damage!')
    return heartlessHealth - damage
  elif finish == 'Gravity Break':
    # print("You used Gravity Break and dealt " + yellow + "triple" + white + " damage!" + ' You caused ' + red + str(3*damage) + ' ♥ ' + white + 'of damage!')
    print('Gravity Break (not implemented)')
    return heartlessHealth
  elif finish == 'Hurricane Blast':
    # print("You used Zantetsuken and dealt " + yellow + "triple" + white + " damage!" + ' You caused ' + red + str(3*damage) + ' ♥ ' + white + 'of damage!')
    print('Hurricane Blast (not implemented)')
    return heartlessHealth
  elif finish == 'Ripple Drive':
    # print("You used Zantetsuken and dealt " + yellow + "triple" + white + " damage!" + ' You caused ' + red + str(3*damage) + ' ♥ ' + white + 'of damage!')
    print('Ripple Drive (not implemented)')
    return heartlessHealth
  elif finish == 'Stun Impact':
    # print("You used Zantetsuken and dealt " + yellow + "triple" + white + " damage!" + ' You caused ' + red + str(3*damage) + ' ♥ ' + white + 'of damage!')
    print('Stun Impact (not implemented)')
    return heartlessHealth
  elif finish == 'Zantetsuken':
    print("You used Zantetsuken and dealt " + yellow + "triple" + white + " damage!" + ' You caused ' + red + str(3*damage) + ' ♥ ' + white + 'of damage!')
    return heartlessHealth - 2*damage


def battle(enemy):                 ###BATTLE

    heartlessDamage = int(heartless[enemy]['damage'])
    damage = keybladeStatus[player.keyblade]['damage'] + player.STR
    defense = player.DEF

    for accessory in player.equipment:
      damage += equipments[accessory]['STR']
      defense += equipments[accessory]['DEF']

    print("---------------------------")
    print('You see a ' + red + 'Heartless' + white +'! It\'s a '+ red + enemy + white + '!')
    print('commands: \n\nattack \nmagic [magic name] \nitem [item name] \nrun')
    
    heartlessHealth = int(heartless[enemy]['HP'])
    statusEffect = 'none'
    statusDuration = 99
    finishCount = 0
    command = ''

    while True:
        player.showBattleStatus()

        if 'Scan' in player.abilities:
          scan(enemy, heartlessHealth)

        while command == '':
            command = input('>')
        command = command.lower()
### Status effect duration
        if statusDuration == 0:
          print('\nThe ' + player.colors[magics[statusEffect]['speech'][4]] + magics[statusEffect]['status']['name'] + white + ' effect has passed\n')
          statusEffect = 'none'
          statusDuration = 99

        if 'blizza' in statusEffect or 'thund' in statusEffect:
          heartlessDamage = heartlessDamage - magics[statusEffect]['status']['reduction']
###
        print("---------------------------")

        if command == 'attack':       ###ATTACK
            command = ''
            if any(item in player.abilities for item in finishersList) and finishCount == 3:
              heartlessHealth = finishAttack(heartlessHealth, damage)
              finishCount = 0
            elif any(item in player.abilities for item in finishersList) and 'Negative Combo' in player.abilities and finishCount == 2:
              heartlessHealth = finishAttack(heartlessHealth, damage)
              finishCount = 0
            else:
              finishCount += 1
              print('You and the heartless attack each other!')
              print('You caused ' + red + str(damage) + ' ♥ ' + white + 'of damage!')
### Status effect
            if statusEffect != 'none':
              heartlessHealth, statusDuration = statusEffectDamage(statusEffect, heartlessHealth, statusDuration)
### Calculate damage
            heartlessHealth = calculateDamage(heartlessHealth, heartlessDamage, damage, defense)

        elif "magic" in command:       ###MAGIC
          command = command.lower().split()
          if 'Combo Master' not in player.abilities or finishCount == 3:
            finishCount = 0
          if not player.magic:
            print('Magic is still a mystery to you!')

          else:
            if command[1] in player.magic:
              if player.MP >= magics[command[1]]['MP']:

                magicText = magics[command[1]]['speech']
###COLOR SPEECH
                print('You used ' + blue + str(magics[command[1]]['MP']) +' ● ' + white + '!')
                if 'cur' not in command[1]:
                  print("You cast " + player.colors[magicText[4]] + command[1].capitalize() + white + " and deal " + red + magicText[1] + white + magicText[2] + player.colors[magicText[4]] + magicText[3])
                else:
                  print("You cast " + green + command[1].capitalize() + white + " and restore " + red + magicText[1] + white + magicText[2])
                player.MP = player.MP - magics[command[1]]['MP']
### Status effect
                if statusEffect != 'none':
                  heartlessHealth, statusDuration = statusEffectDamage(statusEffect, heartlessHealth, statusDuration)
###Calculate damage
                print("The heartless attacks you!")
                player.HP = player.HP + magics[command[1]]['heal']
                if player.HP > player.TotalHP: player.HP = player.TotalHP
                if 'Leaf Bracer' in player.abilities and 'cur' in command[1]:
                  print(green + 'Leaf Bracer' + white +' protects you from damage while casting a Cure spell!')
                  heartlessHealth = calculateDamage(heartlessHealth, 0, magics[command[1]]['damage'], defense)
                else:
                  heartlessHealth = calculateDamage(heartlessHealth, heartlessDamage, magics[command[1]]['damage'], defense)
### Start status effect
                if 'cur' not in command[1]:
                  statusEffect = command[1]
                  statusDuration = magics[statusEffect]['status']['duration']
###
              else:
                print('Not enough MP!')

          command = ''

        elif "item" in command:       ###ITEM
          command = command.lower().split()
          finishCount = 0
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
                heartlessHealth = calculateDamage(heartlessHealth, heartlessDamage, 0, defense)

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

            dropNumber = random.randint(1, 100)
            for drop in heartless[enemy]['drop']:
              if dropNumber <= drop:
                print("Obtained a " + green + heartless[enemy]['drop'][drop] + white + "!")
                if len(player.item) < player.itemPouch:
                  player.item.append(heartless[enemy]['drop'][drop])
                else:
                  player.stock.append(heartless[enemy]['drop'][drop])
                  print('Your item pouch is full, item send to stock!!')
                break
            

            return 'victory'

#################       MAIN

player = player()

with open('utilities/saveFile.txt', 'r') as f:
  saves = ast.literal_eval(f.read())

#COLOR
colorama_init(autoreset=True)
colors = dict(Fore.__dict__.items())
red = player.colors['RED']
white = player.colors['WHITE']
blue = player.colors['BLUE']
yellow = player.colors['YELLOW']
green = player.colors['GREEN']

alreadyBattled = 0

titleScreen(player, saves)

player.calculateHealth()
player.HP = player.TotalHP
player.MP = player.TotalMP

if player.tutorial == {}:
  player.tutorial = tutorials

currentRoom = rooms[player.world][0]
previusRoom = currentRoom

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
    if player.tutorial['open map'] == 0:
      print('The first time opening a map may glitch out and refuse to open, just close the map and open it again!')
      player.tutorial['open map'] = 1
    
    print('Opening map...\n')
    from PIL import Image
    img = Image.open('images/' + player.world + '/Map' + str(maps[player.world][player.map]) + '.jpg')
    img.show()


  elif 'test' in move:        ##### TEST

    if any(item in player.abilities for item in finishersList):
      print('\ntested!\n')

  
  elif 'treasure' in move:        ##### TREASURE
    if 'treasure' in rooms[player.world][currentRoom]:
      if rooms[player.world][currentRoom]['treasure']['treasure'] == 'item':
        print('Obtained a "' + rooms[player.world][currentRoom]['treasure']['item'] + '"!')
        if len(player.item) < player.itemPouch:
          player.item.append(rooms[player.world][currentRoom]['treasure']['item'])
        else:
          player.stock.append(rooms[player.world][currentRoom]['treasure']['item'])
          print('Your item pouch is full, item send to stock!!')

      if rooms[player.world][currentRoom]['treasure']['treasure'] == 'key item':
        print('Obtained the "' + rooms[player.world][currentRoom]['treasure']['key item'] + '" key item!')
        player.keyItems.append(rooms[player.world][currentRoom]['treasure']['key item'])

      if rooms[player.world][currentRoom]['treasure']['treasure'] == 'mapUpdate':
        player.map = player.map + rooms[player.world][currentRoom]['treasure']['mapUpdate']
        print(player.world + ' map updated!')
        if player.tutorial['open map'] == 0:
          print(Fore.YELLOW + "tutorial: " + Fore.WHITE + tutorialSpeech['open map'])
          player.tutorial['open map'] = 1

      del rooms[player.world][currentRoom]['treasure']
    else:
      print('There\'s no treasure chest in this room!')

  elif 'menu' in move:        ##### SHOW MENU
      player.menu()

  elif 'equipment' in move:    ##### TRADE EQUIPMENT
      player.tradeEquipment()

  elif 'keyblade' in move:    ##### TRADE KEYBLADE
      player.tradeKeyblade()

  elif 'status' in move:        ##### SHOW MENU
      player.status()

  elif 'tutorials' in move:        ##### SHOW TUTORIALS
      player.showTutorials()

  elif 'save' in move:
    if 'Shop' in currentRoom:
      saveScreen(player, saves)
    else:
      print('There is no save point here!')

  elif move[0] == 'buy':        ##### BUY IN SHOP
    if len(move)>2: move[1]=move[1]+' '+move[2]
    print(move[1])
    if 'Shop' in currentRoom:
      if move[1] in shops[currentRoom]:
        if player.munny >= shops[currentRoom][move[1]]:
            print('\nMoogle: Thanks for shopping here, Kupo!!\nObtained a ' + move[1] + '!')
            player.munny = player.munny - shops[currentRoom][move[1]]
            if move[1] in items:
              if len(player.item) < player.itemPouch:
                player.item.append(move[1])
              else:
                player.stock.append(move[1])
                print('Your item pouch is full, item send to stock!!')
            else:
              player.equipmentList.append(move[1])
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
        if 'cur' not in move[1]:
          print('You can\'t cast that now!')
        else:
          if player.MP >= magics[move[1]]['MP']:
            print('You used ' + blue + str(magics[move[1]]['MP']) +' ● ' + white + '!')
            print("You cast " + green + move[1].capitalize() + white + " and restore " + red + magics[move[1]]['speech'][1] + white + magics[move[1]]['speech'][2])
            player.MP = player.MP - magics[move[1]]['MP']
            player.HP = player.HP + magics[move[1]]['heal']
            if player.HP > player.TotalHP: player.HP = player.TotalHP
          else:
            print('Not enough MP!')


  #if they type 'go' first
  elif move[0] == 'go' or move[0] == 'enter':        ##### MOVE
    #check that they are allowed wherever they want to go
    if move[1] in rooms[player.world][currentRoom]:
      #set the current room to the new room
      alreadyBattled = 0
      previusRoom = currentRoom
      currentRoom = rooms[player.world][currentRoom][move[1]]
      for room in rooms[player.world][currentRoom]['resetHeartless']:
        if rooms[player.world][room]['heartless']['status'] == 0:
          rooms[player.world][room]['heartless']['status'] = rooms[player.world][room]['heartless']['waves']
    #there is no door (link) to the new room
    elif move[1] == 'back':
        alreadyBattled = 0
        temp = currentRoom
        currentRoom = previusRoom
        previusRoom = temp
        for room in rooms[player.world][currentRoom]['resetHeartless']:
          if rooms[player.world][room]['heartless']['status'] == 0:
            rooms[player.world][room]['heartless']['status'] = rooms[player.world][room]['heartless']['waves']
    else:
      print('You can\'t go that way!')

  #if they type 'talk' first
  elif move[0] == 'talk' :        ##### TALK WITH PERSON
    #if the room contains an person
    if 'person' in rooms[player.world][currentRoom] and move[1] in rooms[player.world][currentRoom]['person'].lower():
      #falar com a pessoa
      print(people[rooms[player.world][currentRoom]['person']]['speech'])
      reward = people[rooms[player.world][currentRoom]['person']]['reward']
      if reward == 'story':
        if player.story == (people[rooms[player.world][currentRoom]['person']]['story']-1):
          player.story += 1
          print()

      elif reward == 'key item':
        player.keyItems.append(people[rooms[player.world][currentRoom]['person']]['key item'])
        print('You got the "' + people[rooms[player.world][currentRoom]['person']]['key item'] + '" key item!')

      elif reward == 'item':
        print('You got a "' + people[rooms[player.world][currentRoom]['person']]['item'] + '"!')
        if len(player.item) < player.itemPouch:
          player.item.append(people[rooms[player.world][currentRoom]['person']]['item'])
        else:
          player.stock.append(people[rooms[player.world][currentRoom]['person']]['item'])
          print('Your item pouch is full, item send to stock!!')
      people[rooms[player.world][currentRoom]['person']]['reward'] = 'no'
      if rooms[player.world][currentRoom]['person'].lower() == 'moogle':
          shop(currentRoom)

    else:
      #tell them they can't talk
      print('Can\'t talk to ' + move[1] + '!')


  if 'heartless' in rooms[player.world][currentRoom] and alreadyBattled == 0:           ###### BATTLE
    status = rooms[player.world][currentRoom]['heartless']['status']
    if status > 0:
      result = battle(rooms[player.world][currentRoom]['heartless']['wave'][status])  
      if result == 'victory':
        alreadyBattled = 1
        rooms[player.world][currentRoom]['heartless']['status'] = (status - 1)
      elif result == 'run':
          temp = currentRoom
          currentRoom = previusRoom
          previusRoom = temp
      elif result == 'defeat':
          print("---------------------------")
          print('Your HP has dropped to zero!\nGAME OVER')
          break
    player.calculateHealth()


  # player wins if they get to the Third District
  if currentRoom == 'Third District' and  player.story == 1:
    print('You found Donald & Goofy... YOU WIN!')
    break
