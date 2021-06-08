#!/bin/python3

def showInstructions():
    #print a main menu and the commands
    print('''
RPG Game v 0.1
Traverse Town
========

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
  # print(keyItems)
  # print(item)
  print('You are in the ' + currentRoom)
  print("HP : " + str(HP))
  print("MP : " + str(MP))
  #print the current inventory
  #print("inventory : " + str(inventory))
  #print an item if there is one
  if "person" in rooms[currentRoom]:
    print('You see ' + rooms[currentRoom]['person'])
  print("---------------------------")


def showBattleStatus():
  #print the player's current battle status
  print('\n---------------------------')
  #print the current inventory
  print("HP : " + str(HP))
  print("MP : " + str(MP))
  print("Items :",item)
  #print an item if there is one
  print("---------------------------")



#an inventory, which is initially empty
HP = ["❤","❤","❤"]
MP = ['●']  ## full: ●,  empty: ○

magic = []
item = []
keyItems = []

#a dictionary linking a room to other room positions
rooms = {

            'First District' : { 'north' : 'Second District',
                  'shop' : ''                                           ##### Para implementar
            },        

            'Second District' : { 'south' : 'First District',
                  'east' : 'Third District',
                  'west' : 'Hotel',
                  'heartless'  : 'shadow'
                },
                
            'Third District' : { 'west'  : 'Second District',              
                },
                
            'Hotel' : { 'east' : 'Second District',
                    'west' : 'Green Room',
                    'north' : 'Red Room',
                    'heartless'  : 'shadow'
                    
             },

             'Green Room' : { 'east' : 'Hotel',
                  'north' : 'Alleyway',
                  'person'  : 'Leon'
                },

              'Red Room' : { 'south' : 'Hotel',
                  'west' : 'Alleyway',
                  'person'  : 'Yuffie'
                },

              'Alleyway' : { 'south' : 'Green Room',
                  'east' : 'Red Room',
                  'heartless'  : 'shadow'
                },

         }

people = {

            'Leon' : {'speech' : 'Leon: Donald & Goofy are in the Third District!',
                      'reward' : 'key item',
                      'key item': 'Leon\'s tip'
            },
            'Yuffie' : {'speech' : 'Yuffie: Hi there, Sora!',
                        'reward' : 'item',
                        'item' : 'potion'
            }

}

heartless = {

            'shadow' : {'commands' : 'attack', 
                    'HP': 1 ,
                    'damage': 1
            }

}

#start the player in the First District
currentRoom = 'First District'
previusRoom = 'First District'

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
        keyItems.append(people[rooms[currentRoom]['person']]['key item'])
        print('You got the "' + people[rooms[currentRoom]['person']]['key item'] + '" key item!')
      elif reward == 'item':
        item.append(people[rooms[currentRoom]['person']]['item'])
        print('You got a "' + people[rooms[currentRoom]['person']]['item'] + '"!')

      people[rooms[currentRoom]['person']]['reward'] = 'no'
      #delete the item from the room
      #del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t talk to ' + move[1] + '!')

  # player loses if they enter a room with a monster
  if 'heartless' in rooms[currentRoom]:           ###### BATTLE
    showBattleStatus()
    print("---------------------------")
    print('You see a Heartless! It\'s a '+ rooms[currentRoom]['heartless'] + '!')
    print('commands: [attack], [magic], [item], [run]')
    
    heartlessHealth = int(heartless[rooms[currentRoom]['heartless']]['HP'])
    heartlessDamage = int(heartless[rooms[currentRoom]['heartless']]['damage'])
    command = ''
    while True:
        while command == '':
            command = input('>')
        command = command.lower()

        print("---------------------------")

        if command == 'attack':
            command = ''
            print('You and the heartless attack each other!')
            print('You caused 1 ❤  of damage!')
            heartlessHealth = heartlessHealth-1
            print("You lost "+ str(heartlessDamage) + ' ❤ !')
            i=0
            while i<heartlessDamage:
              del HP[-1]
              i+=1

        if "magic" in command:
          
          if not magic:
            print('Magic is still a mystery to you!')
          command = ''

        if "item" in command:
          command = command.lower().split()
          if not item:
            print('You have no items!')
          else:
            try:
              if command[1] in item:
                print('Used', command[1])
                del item[item.index(command[1])]

                print("The heartless attacks you!")
                print("You lost "+ str(heartlessDamage) + ' ❤ !')
                i=0
                while i<heartlessDamage:
                  del HP[-1]
                  i+=1

              else:
                print("You don\'t have any ", command[1])
            except IndexError:
                print('try: item [item name]')
          command = ''


        if "run" in command:
            command = ''
            currentRoom = previusRoom
            print('You got away successfully!')
            break

        if HP == []:
            break

        if heartlessHealth <= 0:
            print('You defeated the Heartless!\nCONGRATULATIONS!')
            # print('You gained xp!')
            del rooms[currentRoom]['heartless']
            break
    

  if HP == []:
    print("---------------------------")
    print('Your HP has dropped to zero!\nGAME OVER')
    break
  # player wins if they get to the Fourth District
  if currentRoom == 'Third District' and 'Leon\'s tip' in keyItems:
    print('You found Donald & Goofy... YOU WIN!')
    break
  
