#!/bin/python3
import random

from dictionaries.location import *
from dictionaries.dictionaries import *
from player import *

def showInstructions():
    #print a main menu and the commands
    print('''
RPG Game v 0.2
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

def showStatus():
  #print the player's current status
  print('\n---------------------------')
  print('You are in the ' + currentRoom)
  if "person" in rooms[currentRoom]:
    print('You see ' + rooms[currentRoom]['person'])
    if rooms[currentRoom]['person'].lower() not in player.map:
      player.map = player.map + people[rooms[currentRoom]['person']]['mapUpdate']
  if "shop" in rooms[currentRoom] and (currentRoom+' Shop location') in player.keyItems:
    print('You see the ' + rooms[currentRoom]['shop'] + ', try: \'enter shop\'')
  if "Shop" in currentRoom:
      player.HP = player.MaxHP
      player.MP = player.MaxMP
      print('\nYou see a Save point, HP and MP restored!\nTo get out of the shop type: \'go back\'')
  print("---------------------------")

def shop(currentRoom):
    for item in shops[currentRoom]:
        print(item, '   \tcost:', shops[currentRoom][item], 'munny!')


def battle(enemy):
    print("---------------------------")
    print('You see a Heartless! It\'s a '+ enemy + '!')
    print('commands: \n\nattack \nmagic [magic name] \nitem [item name] \nrun')
    
    heartlessHealth = int(heartless[enemy]['HP'])
    statusEffect = 'none'
    statusDuration = 99
    command = ''
    while True:
        player.showBattleStatus()
        while command == '':
            command = input('>')
        command = command.lower()

        heartlessDamage = int(heartless[enemy]['damage'])

        if statusDuration == 0:
          print('\nThe ' + statusEffect + ' effect has passed\n')
          statusEffect = 'none'
          statusDuration = 99

        if statusEffect == 'blizzard':
          heartlessDamage = heartlessDamage -1

        print("---------------------------")

        if command == 'attack':
            command = ''
            print('You and the heartless attack each other!')
            print('You caused 1 ♥  of damage!')

            if statusEffect != 'none':
              print(magics[statusEffect]['status']['speech'])
              heartlessHealth = heartlessHealth-magics[statusEffect]['status']['damage']
              statusDuration = statusDuration - 1

            heartlessHealth = heartlessHealth-1
            
            print("You lost "+ str(heartlessDamage) + ' ♥ !')
            player.HP = player.HP - heartlessDamage

        if "magic" in command:
          command = command.lower().split()
          if not player.magic:
            print('Magic is still a mystery to you!')

          else:
            if command[1] in player.magic:
              if player.MP >= magics[command[1]]['MP']:

                print(magics[command[1]]['speech'])
                player.MP = player.MP - magics[command[1]]['MP']

                print("The heartless attacks you!")
                print("You lost "+ str(heartlessDamage) + ' ♥ !')

                if statusEffect != 'none':
                  print(magics[statusEffect]['status']['speech'])
                  heartlessHealth = heartlessHealth-magics[statusEffect]['status']['damage']
                  statusDuration = statusDuration - 1

                heartlessHealth = heartlessHealth-magics[command[1]]['damage']
                player.HP = player.HP + magics[command[1]]['heal'] - heartlessDamage

                if command[1] != 'cure':
                  statusEffect = command[1]
                  statusDuration = magics[statusEffect]['status']['duration']

              else:
                print('Not enough MP!')

          command = ''

        if "item" in command:
          command = command.lower().split()
          if not player.item:
            print('You have no items!')
          else:
            try:
              if command[1] in player.item:
                del player.item[player.item.index(command[1])]

                print("The heartless attacks you!")
                print("You lost "+ str(heartlessDamage) + ' ♥ !')

                print('Used a ' + str(command[1]))
                print(items[command[1]]['speech'])

                if statusEffect != 'none':
                  print(magics[statusEffect]['status']['speech'])
                  heartlessHealth = heartlessHealth-magics[statusEffect]['status']['damage']
                  statusDuration = statusDuration - 1


                player.HP = player.HP + items[command[1]]['HP']  - heartlessDamage
                player.MP = player.MP + items[command[1]]['MP']

              else:
                print("You don\'t have any ", command[1])
            except IndexError:
                print('try: item [item name]')
          command = ''

        if "run" in command:
            command = ''
            print('You got away successfully!')
            return 'run'

        if player.HP == 0:
            return 'defeat'

        if heartlessHealth <= 0:

            munny = 3 * random.randint(heartless[enemy]['munny'][0], heartless[enemy]['munny'][1])
            print('\nYou defeated the Heartless!\nCONGRATULATIONS!')
            print('You obtained ' + str(munny) + ' munny!')
            player.munny += munny
            # print('You gained xp!')
            return 'victory'

#start the player in the First District
currentRoom = 'First District'
previusRoom = 'First District'

player = player()

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

  if move == 'map':        ##### OPEN MAP
    print('Opening map...\n')
    from PIL import Image
    img = Image.open('images/' + player.world + '/Map' + str(maps[player.world][player.map]) + '.jpg')
    img.show()
    
  move = move.lower().split()

  if 'menu' in move:        ##### SHOW MENU
      player.menu()

  if move[0] == 'buy':        ##### BUY IN SHOP
      if move[1] in shops[currentRoom]:
        if player.munny >= shops[currentRoom][move[1]]:
            print('\nMoogle: Thanks for shopping here, Kupo!!\nObtained a ' + move[1] + '!')
            player.munny = player.munny - shops[currentRoom][move[1]]
            player.item.append(move[1])
        else:
            print('\nMoogle: You don\'t have enough munny for this item, Kupo!!')
      else:
          print('\nMoogle: I\'m sorry, I don\'t have this item, Kupo!')


  if move[0] == 'use':        ##### USE ITEM
    if not player.item:
        print('You have no items!')
    else:
        try:
            if move[1] in player.item:
                del player.item[player.item.index(move[1])]
                print('Used a ' + str(move[1]))
                print(items[move[1]]['speech'])
                player.HP = player.HP + items[move[1]]['HP']
                player.MP = player.MP + items[move[1]]['MP']
            else:
                print("You don\'t have any ", move[1])
        except IndexError:
            print('try: use [item]')
        command = ''

  #if they type 'go' first
  if move[0] == 'go' or move[0] == 'enter':        ##### MOVE
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      previusRoom = currentRoom
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    elif move[1] == 'back':
        temp = currentRoom
        currentRoom = previusRoom
        previusRoom = temp
    else:
      print('You can\'t go that way!')

  #if they type 'talk' first
  if move[0] == 'talk' :        ##### TALK WITH PERSON
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
        player.item.append(people[rooms[currentRoom]['person']]['item'])
        print('You got a "' + people[rooms[currentRoom]['person']]['item'] + '"!')
      people[rooms[currentRoom]['person']]['reward'] = 'no'
      if rooms[currentRoom]['person'].lower() == 'moogle':
          shop(currentRoom)
    else:
      #tell them they can't talk
      print('Can\'t talk to ' + move[1] + '!')



  if 'heartless' in rooms[currentRoom]:           ###### BATTLE
    result = battle(rooms[currentRoom]['heartless'])  
    if result == 'victory':
        del rooms[currentRoom]['heartless']
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
  
