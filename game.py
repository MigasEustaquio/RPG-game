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
  print('You are in the ' + currentRoom)
  print("Health : " + str(Health))
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
  print("Health : " + str(Health))
  #print an item if there is one
  print("---------------------------")



#an inventory, which is initially empty
Health = ["❤","❤","❤"]

#a dictionary linking a room to other room positions
rooms = {

            'First District' : { 'south' : 'Second District',
                  'east'  : 'Third District',
                  'person'  : 'Leon'
                },        

            'Second District' : { 'north' : 'First District',
                  'heartless'  : 'shadow'
                },
                
            'Third District' : { 'west'  : 'First District',
                  'south' : 'Fourth District',
                  'person'  : 'Yuffie'
              
                },
                
            'Fourth District' : { 'north' : 'Third District',
                    'person' : 'Donald & Goofy'
             }

         }

people = {

            'Leon' : 'Leon: Donald & Goofy are in the Fourth District!',
            'Yuffie' : 'Yuffie: Hi there, Sora!'

}

heartless = {

            'shadow' : {'commands' : 'attack', 
                    'health': 1 ,
                    'damage': 1
            }

}

#start the player in the First District
currentRoom = 'First District'

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
      print(people[rooms[currentRoom]['person']])
      #delete the item from the room
      #del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t talk to ' + move[1] + '!')

  # player loses if they enter a room with a monster
  if 'heartless' in rooms[currentRoom]:
    showStatus()
    print("---------------------------")
    print('You see a Heartless! It\'s a '+ rooms[currentRoom]['heartless'] + '!')
    print('commands: [attack], [magic], [item], [run]')
    
    heartlessHealth = int(heartless[rooms[currentRoom]['heartless']]['health'])
    heartlessDamage = int(heartless[rooms[currentRoom]['heartless']]['damage'])
    command = ''
    while True:
        while command == '':
            command = input('>')
        command = command.lower()

        print("---------------------------")

        if command == 'attack':
            print('You and the heartless attack each other!')
            print('You caused 1 ❤  of damage!')
            heartlessHealth = heartlessHealth-1
            print("You lost "+ str(heartlessDamage) + ' ❤ !')
            del Health[-1]

        if Health == []:
            break

        if heartlessHealth <= 0:
            print('You defeated the Heartless!\nCONGRATULATIONS!')
            # print('You gained xp!')
            break
    

  if Health == []:
    print("---------------------------")
    print('Your health has dropped to zero!\nGAME OVER')
    break
  # player wins if they get to the Fourth District
  if currentRoom == 'Fourth District':
    print('You found Donald & Goofy... YOU WIN!')
    break
  
