#!/bin/python3

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
  go [direction]
  talk [person]
  command [command]
''')

def showStatus():
  #print the player's current status
  print('\n---------------------------')
  print('You are in the ' + currentRoom)
  if "person" in rooms[currentRoom]:
    print('You see ' + rooms[currentRoom]['person'])
  print("---------------------------")

def battle(enemy):
    print("---------------------------")
    print('You see a Heartless! It\'s a '+ enemy + '!')
    print('commands: [attack], [magic], [item], [run]')
    
    heartlessHealth = int(heartless[enemy]['HP'])
    heartlessDamage = int(heartless[enemy]['damage'])
    command = ''
    while True:
        player.showBattleStatus()
        while command == '':
            command = input('>')
        command = command.lower()

        print("---------------------------")

        if command == 'attack':
            command = ''
            print('You and the heartless attack each other!')
            print('You caused 1 ♥  of damage!')
            heartlessHealth = heartlessHealth-1
            print("You lost "+ str(heartlessDamage) + ' ♥ !')
            player.HP = player.HP - heartlessDamage

        if "magic" in command:
          
          if not player.magic:
            print('Magic is still a mystery to you!')
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

                player.HP = player.HP + items[command[1]]['HP']  - heartlessDamage

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
            print('You defeated the Heartless!\nCONGRATULATIONS!')
            # print('You gained xp!')
            return 'victory'

#start the player in the First District
currentRoom = 'First District'
previusRoom = 'First District'

player = player()

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':  
    move = input('>')
    
  move = move.lower().split()

  if 'status' in move:
      player.showBattleStatus()

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      previusRoom = currentRoom
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
      print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'talk' :
    #if the room contains an item, and the item is the one they want to get
    if 'person' in rooms[currentRoom] and move[1] in rooms[currentRoom]['person'].lower():
      #add the item to their inventory
      #falar com a pessoa
      print(people[rooms[currentRoom]['person']]['speech'])
      reward = people[rooms[currentRoom]['person']]['reward']
      if reward == 'key item':
        player.keyItems.append(people[rooms[currentRoom]['person']]['key item'])
        print('You got the "' + people[rooms[currentRoom]['person']]['key item'] + '" key item!')
      elif reward == 'item':
        player.item.append(people[rooms[currentRoom]['person']]['item'])
        print('You got a "' + people[rooms[currentRoom]['person']]['item'] + '"!')

      people[rooms[currentRoom]['person']]['reward'] = 'no'
      #delete the item from the room
      #del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t talk to ' + move[1] + '!')


  if 'heartless' in rooms[currentRoom]:           ###### BATTLE

    result = battle(rooms[currentRoom]['heartless'])  
    if result == 'victory':
        del rooms[currentRoom]['heartless']
    elif result == 'run':
        currentRoom = previusRoom
    elif result == 'defeat':
        print("---------------------------")
        print('Your HP has dropped to zero!\nGAME OVER')
        break

  # player wins if they get to the Third District
  if currentRoom == 'Third District' and 'Leon\'s tip' in player.keyItems:
    print('You found Donald & Goofy... YOU WIN!')
    break
  
