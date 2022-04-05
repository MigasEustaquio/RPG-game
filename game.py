#!/bin/python3
# from os import X_OK
import random
import math
import time
from utilities.enemyClasses import *
from utilities.screen import *
from dictionaries.people import *
from dictionaries.location import *
from dictionaries.enemies import *
from dictionaries.scenes import *

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


def verifyPersonStory(peolpeInRoom):  ###Check person's speech and reward based on story
  peopleToTalk = []
  storyToTalk = []
  for person in peolpeInRoom:
      if player.story > list(people[currentRoom][person])[-1]:
        if people[currentRoom][person][list(people[currentRoom][person])[-1]]['present'] == 'yes':
          peopleToTalk.append(person)
          storyToTalk.append(list(people[currentRoom][person])[-1])
      elif player.story < list(people[currentRoom][person])[0]:
        pass
      else:
        for story in people[currentRoom][person]:
          if story == player.story:
            if people[currentRoom][person][story]['present'] == 'yes':
              peopleToTalk.append(person)
              storyToTalk.append(story)
            break
          else:
            if story > player.story:
              if people[currentRoom][person][previusStory]['present'] == 'yes':
                peopleToTalk.append(person)
                storyToTalk.append(previusStory)
              break
            else:
              previusStory = story
  return peopleToTalk, storyToTalk

def bossScene(enemyName):             ###Print Scenes
  skip = input('Skip scene?(yes/no)\n>')
  print()
  if skip.lower() == 'yes':
    pass
  else:
    for phrase in bossScenes[enemyName]:
     print(phrase)
     time.sleep(3)
    print()

def showStatus():                     ###SHOW STATUS
  #print the player's current status
  print(Fore.RED + '\n---------------------------')
  print(Fore.WHITE + 'You are in the ' + currentRoom)
  if "person" in rooms[player.world][currentRoom]:
    peopleToTalk, storyToTalk = verifyPersonStory(rooms[player.world][currentRoom]['person'])
    for person in peopleToTalk:
      print('You see ' + person)
  if "shop" in rooms[player.world][currentRoom] and (currentRoom+' Shop location') in player.keyItems:
    print('You see the ' + rooms[player.world][currentRoom]['shop'] + ', try: \'enter shop\'')
  if "Shop" in currentRoom or "Save" in rooms[player.world][currentRoom]:
      player.HP = player.TotalHP
      player.MP = player.TotalMP
      print('\nYou see a Save point, HP and MP restored!')
      if player.tutorial['save'] == 0:
        print(Fore.YELLOW + "tutorial: " + Fore.WHITE + tutorialSpeech['save'])
        print(Fore.YELLOW + "tutorial: " + Fore.WHITE + tutorialSpeech['quit'])
        player.tutorial['save'] = 1
        player.tutorial['quit'] = 1
      if "Shop" in currentRoom:
        print('To get out of the shop type: \'leave\'')
  if 'treasure' in rooms[player.world][currentRoom] and player.treasures[player.world][currentRoom]['status']=='closed':
    print('You see a treasure chest!')
    if player.tutorial['treasure chest'] == 0:
      print(Fore.YELLOW + "tutorial: " + Fore.WHITE + tutorialSpeech['treasure chest'])
      player.tutorial['treasure chest'] = 1
  print(Fore.RED + "---------------------------")

def shop(currentRoom):                ###SHOP
    for item in shops[currentRoom]:
        print(item, '   \tcost:', shops[currentRoom][item], 'munny!')

def levelUP():                        ###LEVEL UP
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

def useItem(item):                    ###USE ITEM
  del player.item[player.item.index(item)]
  player.itemBKP.append(item)

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

def scan(enemy):                      ###SCAN
  heartlessHealthDisplay = ''
  i=0
  while i< enemy.MaxHP:
    if i<enemy.HP:
      heartlessHealthDisplay += '♥'
    else:
      heartlessHealthDisplay += '♡'
    i+=1

  print(Fore.MAGENTA + '\n---------------------------')
  print("Scan : " + enemy.name)
  print("HP : " + red + heartlessHealthDisplay)
  print(Fore.MAGENTA + "---------------------------")

def finishAttack(enemy, damage):      ###FINISHERS
  finish = player.finishers[random.randint(0, (len(player.finishers)-1))]
  if finish == 'Blitz':
    print("You used " + yellow + "Blitz" + white + " and dealt " + yellow + "critical" + white + " damage!")
    damageDealt = math.ceil(1.5*damage)-enemy.defense
  elif finish == 'Gravity Break':
    print("You used " + blue + "Gravity Break" + white + " and the gravity pull stunned the enemy!")
    enemy.damage = 0
    damageDealt = damage-enemy.defense
  elif finish == 'Hurricane Blast':   ##NOT IMPLEMENTED
    # print("You used Zantetsuken and dealt " + yellow + "triple" + white + " damage!" + ' You caused ' + red + str(3*damage) + ' ♥ ' + white + 'of damage!')
    print('Hurricane Blast (not implemented)')
  elif finish == 'Ripple Drive':   ##HALF IMPLEMENTED
    if 'Kingdom' in player.keyblade:
      print("You used " + blue + "Ripple Drive" + white + " and activated the " + blue + "Defender" + white + " ability!")
      enemy.damage = enemy.damage-1
      damageDealt = damage-enemy.defense
    elif 'Oathkeeper' in player.keyblade:
      print("You used " + green + "Ripple Drive" + white + " and restore " + red + str(math.ceil(player.TotalMP/4)) + ' ♥'+ white + " !")
      player.HP += math.ceil(player.TotalMP/4)
      damageDealt = damage-enemy.defense
    else:
      print('Not implemented')
      damageDealt = damage-enemy.defense
  elif finish == 'Stun Impact':   ##NOT IMPLEMENTED
    # print("You used Zantetsuken and dealt " + yellow + "triple" + white + " damage!" + ' You caused ' + red + str(3*damage) + ' ♥ ' + white + 'of damage!')
    print('Stun Impact (not implemented)')
  elif finish == 'Zantetsuken':
    print("You used " + yellow + "Zantetsuken" + white + " and dealt " + yellow + "double" + white + " damage!")
    damageDealt = 2*damage-enemy.defense
  if damageDealt<0: damageDealt=0
  print('You caused ' + red + str(damageDealt) + ' ♥ ' + white + 'of damage!')
  enemy.HP = enemy.HP - damageDealt

def battle(enemyName):                ###BATTLE
  ###
    player.createBKP()
    if enemyName in bosses:
      bossBattle = True
    elif enemyName in heartless:
      bossBattle = False

    damage = keybladeStatus[player.keyblade]['damage'] + player.STR
    defense = player.DEF

    for accessory in player.equipment:
      damage += equipments[accessory]['STR']
      defense += equipments[accessory]['DEF']

    print("---------------------------")
    if bossBattle == False:
      print('You see a ' + red + 'Heartless' + white +'! It\'s a '+ red + enemyName + white + '!')
    else:
      print('Boss Battle! ' + enemyName  + '!')
    print('commands: \n\nattack \nmagic [magic name] \nitem [item name] \nrun')
    
    enemy = Heartless(enemyName, bossBattle)

    finishCount = 0
    command = ''

    while True:
        player.showBattleStatus()
        enemy.damage = enemy.totalDamage

        if 'Scan' in player.abilities:
          scan(enemy)

        while command == '':
            command = input('>')
        command = command.lower()
  ###Status effect duration      #INCLUDE BLIZZARD AND THUNDER
        enemy.statusEffectDuration()
  ###PassTurn
        if command == 'pass':
          command = ''
          print('Turn passed!\n')
          if enemy.statusEffect != 'none':
            enemy.statusEffectDamage()
    ### Calculate damage
          if bossBattle == False: enemy.selectCommand(player, defense)
          else: enemy.selectCommandBoss(player, defense)
  ###ATTACK
    ###
        if command == 'attack':       ###ATTACK
            command = ''
    ### Finishers
            if any(item in player.abilities for item in finishersList) and finishCount == 3:
              finishAttack(enemy, damage)
              finishCount = 0
            elif any(item in player.abilities for item in finishersList) and 'Negative Combo' in player.abilities and finishCount == 2:
              finishAttack(enemy, damage)
              finishCount = 0
            else:
              finishCount += 1
              damageDealt = (damage-enemy.defense)
              if damageDealt < 0: damageDealt=0
              print('You attacked and caused ' + red + str(damageDealt) + ' ♥ ' + white + 'of damage!')
              enemy.HP = enemy.HP - damageDealt
    ### Status effect
            if enemy.statusEffect != 'none':
              enemy.statusEffectDamage()
    ### Calculate damage
            if bossBattle == False: enemy.selectCommand(player, defense)
            else: enemy.selectCommandBoss(player, defense)
  ###MAGIC
    ###
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
                if 'fir' in enemy.statusEffect:
                  enemy.statusEffectDamage()
    ###Calculate damage
                if player.HP > player.TotalHP: player.HP = player.TotalHP
                if 'Leaf Bracer' in player.abilities and 'cur' in command[1]:
                  print(green + 'Leaf Bracer' + white +' protects you from damage while casting a Cure spell!')
                  enemy.damage = 0
                else:
                  enemy.HP = enemy.HP - magics[command[1]]['damage']
                player.HP = player.HP + magics[command[1]]['heal']
                if bossBattle == False: enemy.selectCommand(player, defense)
                else: enemy.selectCommandBoss(player, defense)
    ### Start status effect
                if 'cur' not in command[1]:
                  enemy.statusEffect = command[1]
                  enemy.statusDuration = magics[command[1]]['status']['duration']
    ###
              else:
                print('Not enough MP!')

          command = ''
  ###ITEM
    ###
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
                if 'fir' in enemy.statusEffect:
                  enemy.statusEffectDamage()
    ###Calculate damage
                if bossBattle == False: enemy.selectCommand(player, defense)
                else: enemy.selectCommandBoss(player, defense)
              else:
                print("You don\'t have any ", command[1])
            except IndexError:
                print('try: item [item name]')
          command = ''
  ###RUN
        elif "run" in command:       ###RUN
          if bossBattle == False:
            command = ''
            print('You got away successfully!')
            return 'run'
          else:
            print('You can\'t run from a boss battle!')
            command = ''
  ###ERROR
        else:       ###ERROR
          command = ''
          print('Command not found!')
  ###DEFEAT
        if player.HP < 1:       ###DEFEAT
            return 'defeat'
  ###VICTORY
        if enemy.HP <= 0:       ###VICTORY
    ###MUNNY
            munny = 3 * random.randint(enemy.munny[0], enemy.munny[1])
            print('\nYou defeated the Heartless!\nCONGRATULATIONS!')
            print('\nYou obtained ' + yellow + str(munny) + '🔸 munny!')
            player.munny += munny
    ###EXP
            print('You gained ' + str(enemy.exp) + ' exp!')
            player.exp += enemy.exp
            while player.exp >= levelUp[player.level]['next']:
              player.level+=1
              print('\nLevel Up!\nLevel: ' + str(player.level))
              levelUP()
    ###DROP
            dropNumber = random.randint(1, 100)
            for drop in enemy.drop:
              if dropNumber <= drop:
                if enemy.drop[drop] in items:
                  print("\nObtained a " + green + enemy.drop[drop] + white + "!")
                  if len(player.item) < player.itemPouch:
                    player.item.append(enemy.drop[drop])
                  else:
                    player.stock.append(enemy.drop[drop])
                    print('Your item pouch is full, item send to stock!!')
                elif enemy.drop[drop] in keybladeStatus:
                  player.keyblades.append(enemy.drop[drop])
                  print('\nObtained the ' + cyan + enemy.drop[drop] + white + ' Keyblade!')
                break
    ###MP RECOVER
            recoverMPNumber = random.randint(1, 100)
            if 'MP Haste' in player.abilities: recoverMPNumberNeeded = 55
            else: recoverMPNumberNeeded = 75
            if 'MP Rage' in player.abilities: recoverMP = math.ceil(player.TotalMP/4) + math.ceil((player.TotalMP-player.MP)/4)
            else: recoverMP = math.ceil(player.TotalMP/4)

            if recoverMPNumber > recoverMPNumberNeeded:
              print('\nYou recovered ' + blue + str(recoverMP) + ' ● ' + white + '!')
              player.MP += recoverMP
              if player.MP > player.TotalMP: player.MP = player.TotalMP

            return 'victory'
        enemy.statusEffectEnd()

def gameOver():                       ###GAME OVER
  print('\n\nKINGDOM HEARTS🤍\n\nretry?\ncontinue?\nload game?\n\n')
  command = ''
  while True:
    command = input('>').lower()
    if 'retry' in command:
      player.restoreBKP()
      return ''
    elif 'continue' in command:
      player.restoreBKP()
      return 'run'
    elif 'load' in command:
      with open('utilities/saveFile.txt', 'r') as f:
        saves = ast.literal_eval(f.read())
      loadScreen(player, saves)
      return 'load'
    else:
      print('Command not found!\n')
      command = ''

def determineBattle(story, currentRoom, previusRoom):   ###DETERMINE ENEMY TO BATTLE
    status = rooms[player.world][currentRoom]['heartless'][story]['status']
    if status > 0:
      while True:
        result = battle(rooms[player.world][currentRoom]['heartless'][story]['wave'][status])
        if result == 'victory':
          rooms[player.world][currentRoom]['heartless'][story]['status'] = (status - 1)
          player.calculateHealth()
          return 1, currentRoom, previusRoom
        if result == 'defeat':
          print("---------------------------")
          print('Your HP has dropped to zero!\nGAME OVER')
          result = gameOver()
        if result == 'run':
          temp = currentRoom
          currentRoom = previusRoom
          previusRoom = temp
          player.calculateHealth()
          return 0, currentRoom, previusRoom
        if result == 'load':
          player.HP = player.TotalHP
          player.MP = player.TotalMP
          return 0, rooms[player.world][0], rooms[player.world][0]
    else: return 0, currentRoom, previusRoom
  
def unrestrict(currentRoom):          ###UNRESTRICT AREAS

  if len(rooms[player.world][currentRoom]['unlock'][x])>2:
    del rooms[player.world][rooms[player.world][currentRoom]['unlock'][x][2]]['restricted'][rooms[player.world][currentRoom]['unlock'][x][3]]
    if rooms[player.world][currentRoom]['unlock'][x][2] in player.restrictionLifted[player.world]:
      player.restrictionLifted[player.world][rooms[player.world][currentRoom]['unlock'][x][2]].append(rooms[player.world][currentRoom]['unlock'][x][3])
    else:
      player.restrictionLifted[player.world][rooms[player.world][currentRoom]['unlock'][x][2]]=[rooms[player.world][currentRoom]['unlock'][x][3]]
  del rooms[player.world][currentRoom]['restricted'][rooms[player.world][currentRoom]['unlock'][x][0]]

  if currentRoom in player.restrictionLifted[player.world]:
    player.restrictionLifted[player.world][currentRoom].append(rooms[player.world][currentRoom]['unlock'][x][0])
  else:
    player.restrictionLifted[player.world][currentRoom]=[rooms[player.world][currentRoom]['unlock'][x][0]]

def worldMap():                       ###WORLD MAP
  while True:
    # showStatus()        #### MAKE A WORLD MAP SHOW STATUS
    print('\nWorld Map\n')
    move = ''
    world = ''
    worldFound = False
    while move == '':  
      move = input('>')
    move = move.lower()
    
    for world in worldNames:
      if move in worldNames[world]:
        if world not in player.unlockedWorlds:
          print('We can\'t travel to ' + worldDisplayName[world])
        else:
          worldFound = True
          break

    if worldFound:
      answer = input('Do you want to land in ' + worldDisplayName[world] + '?\n')
      if 'yes' in answer.lower() :
        player.world=world
        return rooms[world][0]  ###############################

    # if 'save' in move:
    #   print()

  
def selectArena():
  while True:
    print('\nPhil: What arena do you wish to enter?\n(type the number or the name of the arena you wish to enter. 0 or \'nevermind\' to leave)')
    #Print unlocked arenas
    
    answer = input('>')
    answer = str(answer).lower()

    if answer == '0' or answer == 'nevermind':
      print('\nPhil: Okay kid, talk to me if you wish to become a hero!')
      break
    elif answer == '1':
      print('\nEntering Arena 1')
      #create arena fights function
    elif answer == '2':
      print('\nEntering Arena 2')
    else:
      print('\nArena not found!')




#################
player = player()
while True:                        ###MAIN
  with open('utilities/saveFile.txt', 'r') as f:
    saves = ast.literal_eval(f.read())
#COLOR
  colorama_init(autoreset=True)
  colors = dict(Fore.__dict__.items())
  red = player.colors['RED']
  white = player.colors['WHITE']
  blue = player.colors['BLUE']
  cyan = player.colors['CYAN']
  yellow = player.colors['YELLOW']
  green = player.colors['GREEN']
#CONFIGURE PARAMETERS
  titleScreen(player, saves)      ### NEW/LOAD GAME
  player.startingGame()
  roomsbk=copy.deepcopy(rooms)
  peoplebk=copy.copy(people)

  for world in player.restrictionLifted:
    for room in player.restrictionLifted[world]:
      for direction in player.restrictionLifted[world][room]:
        del rooms[world][room]['restricted'][direction]
#INITIALIZE VARIABLES
  alreadyBattled = 0
  retryBoss = False
  previusStory = 0
  currentRoom = player.currentRoom
  previusRoom = currentRoom
#
  showInstructions()
  while True:
    showStatus()

    if retryBoss == False:                              ##### INPUT READER
      move = ''
      while move == '':  
        move = input('>')
      move = move.lower().split()

    if 'map' in move and 'world' not in move:           ##### OPEN MAP
      if player.tutorial['open map'] == 0:
        print('The first time opening a map may glitch out and refuse to open, just close the map and open it again!')
        player.tutorial['open map'] = 1
      
      print('Opening map...\n')
      from PIL import Image
      mapNumber = rooms[player.world][currentRoom]['map number']
      if player.map[player.world][mapNumber] == 'no':
        print(red +'You have no map of this area!' + white)
      else:
        img = Image.open('images/' + player.world + '/Map' + maps[player.world][mapNumber][player.map[player.world][mapNumber]] + '.jpg')
        img.show()

    elif 'test' in move:                                ##### TEST

      print(player.restrictionLifted)
      print()
      print(rooms['TraverseTown']['First District'])
      print('\ntested!\n')
    
    elif 'upgrade' in move:                             ##### TEST 2

      player.story += 1
      print('Story: ' + str(player.story))
      # print(list(rooms[player.world]['2nd Floor']['heartless']))
      print('\ntested!\n')
    
    elif 'treasure' in move:                            ##### TREASURE
      if 'treasure' in rooms[player.world][currentRoom] and player.treasures[player.world][currentRoom]['status']=='closed':
        if rooms[player.world][currentRoom]['treasure']['treasure'] == 'item':
          print('Obtained a "' + rooms[player.world][currentRoom]['treasure']['item'] + '"!')
          if len(player.item) < player.itemPouch:
            player.item.append(rooms[player.world][currentRoom]['treasure']['item'])
          else:
            player.stock.append(rooms[player.world][currentRoom]['treasure']['item'])
            print('Your item pouch is full, item send to stock!!')

        elif rooms[player.world][currentRoom]['treasure']['treasure'] == 'key item':
          print('Obtained the "' + rooms[player.world][currentRoom]['treasure']['key item'] + '" key item!')
          player.keyItems.append(rooms[player.world][currentRoom]['treasure']['key item'])

        elif rooms[player.world][currentRoom]['treasure']['treasure'] == 'mapUpdate':
          if player.map[player.world][rooms[player.world][currentRoom]['treasure']['mapUpdate']] == 'no':
            player.map[player.world][rooms[player.world][currentRoom]['treasure']['mapUpdate']] = 'incomplete'
            print('Obtained ' + player.world + ' ' + rooms[player.world][currentRoom]['treasure']['mapUpdate'] + ' map!')
          elif player.map[player.world][rooms[player.world][currentRoom]['treasure']['mapUpdate']] == 'incomplete':
            player.map[player.world][rooms[player.world][currentRoom]['treasure']['mapUpdate']] = 'complete'
            print(player.world + ' ' + rooms[player.world][currentRoom]['treasure']['mapUpdate'] + ' map updated!')
          if player.tutorial['open map'] == 0:
            print(Fore.YELLOW + "tutorial: " + Fore.WHITE + tutorialSpeech['open map'])
            player.tutorial['open map'] = 1

        elif rooms[player.world][currentRoom]['treasure']['treasure'] == 'keyblade':
          print('Obtained the ' + cyan + rooms[player.world][currentRoom]['treasure']['keyblade'] + white + ' Keyblade!')
          player.keyblades.append(rooms[player.world][currentRoom]['treasure']['keyblade'])

        del rooms[player.world][currentRoom]['treasure']
        player.treasures[player.world][currentRoom]['status']='opened'
      else:
        print('There\'s no treasure chest in this room!')

    elif 'menu' in move:                                ##### SHOW MENU
        player.menu()

    elif 'equipment' in move:                           ##### TRADE EQUIPMENT
        player.tradeEquipment()

    elif 'keyblade' in move:                            ##### TRADE KEYBLADE
        player.tradeKeyblade()

    elif 'status' in move:                              ##### SHOW MENU
        player.status()

    elif 'tutorials' in move:                           ##### SHOW TUTORIALS
        player.showTutorials()

    elif 'save' in move:                                ##### SAVE
      if 'Shop' in currentRoom or 'Save' in rooms[player.world][currentRoom]:
        player.currentRoom = currentRoom
        with open('utilities/saveFile.txt', 'r') as f:
          saves = ast.literal_eval(f.read())
        saveScreen(player, saves)
      else:
        print('There is no save point here!')

    elif 'world' in move:                                ##### SAVE
      if 'Shop' in currentRoom or 'Save' in rooms[player.world][currentRoom]:
        previusRoom = currentRoom = worldMap()
      else:
        print('There is no save point here!')

    elif 'quit' in move:                                ##### QUIT
      answer = input('Are you sure you want to quit the game and return to the Title Screen? (All unsaved progress will be lost)\n')
      if 'yes' in answer.lower() :
        player.__init__()
        rooms=copy.deepcopy(roomsbk)
        people=copy.copy(peoplebk)
        print('\n\n\n')
        break

    elif move[0] == 'buy':                              ##### BUY IN SHOP
      if len(move)>2: move[1]=move[1]+' '+move[2]
      print(move[1])
      if 'Shop' in currentRoom:
        if move[1] in shops[currentRoom]:
          if player.munny >= shops[currentRoom][move[1]]:
              print('\nMoogle: Thanks for shopping here, Kupo!!\nObtained a ' + green + move[1] + white + '!')
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

    elif move[0] == 'use':                              ##### USE ITEM
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

    elif move[0] == 'cast':                             ##### MAGIC
      if not player.magic:
          print('Magic is still a mystery to you!')

      else:
        if move[1] in player.magic:

          if 'unlock' in rooms[player.world][currentRoom]:
            unlockCast='no'
            for x in rooms[player.world][currentRoom]['unlock']:
              if x in move[1]:
                unlockCast = 'yes'
                if player.MP >= magics[move[1]]['MP']:
                  magicText = magics[move[1]]['speech']
                  print('You used ' + blue + str(magics[move[1]]['MP']) +' ● ' + white + '!')

                  if 'cur' not in move[1]:
                    print("You cast " + player.colors[magicText[4]] + move[1].capitalize() + white + rooms[player.world][currentRoom]['unlock'][x][1])
                  else:
                    print("You cast " + green + move[1].capitalize() + white + rooms[player.world][currentRoom]['unlock'][x][1])
                  
                  player.MP = player.MP - magics[move[1]]['MP']
                  player.HP = player.HP + magics[move[1]]['heal']
                  if player.HP > player.TotalHP: player.HP = player.TotalHP

                  unrestrict(currentRoom)

                else:
                  print('Not enough MP!')

            if unlockCast == 'no':
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

          elif 'cur' not in move[1]:
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

    elif move[0] == 'go' or move[0] == 'enter' or 'leave' in move:         ##### MOVE
      if 'leave' in move:
        move = "leave leave"
        move=move.lower().split()
      #check that they are allowed wherever they want to go
      if move[1] in rooms[player.world][currentRoom]['restricted']:
        print(rooms[player.world][currentRoom]['restricted'][move[1]])
      else:
        if move[1] in rooms[player.world][currentRoom]:
          #set the current room to the new room
          alreadyBattled = 0
          previusRoom = currentRoom
          currentRoom = rooms[player.world][currentRoom][move[1]]
          for room in rooms[player.world][currentRoom]['resetHeartless']:
              if player.story in rooms[player.world][room]['heartless']:
                if rooms[player.world][room]['heartless'][player.story]['status'] == 0:
                  rooms[player.world][room]['heartless'][player.story]['status'] = rooms[player.world][room]['heartless'][player.story]['waves']
              else:
                if player.story > list(rooms[player.world][room]['heartless'])[-1]:
                  rooms[player.world][room]['heartless'][list(rooms[player.world][room]['heartless'])[-1]]['status'] = rooms[player.world][room]['heartless'][list(rooms[player.world][room]['heartless'])[-1]]['waves']
                elif player.story < list(rooms[player.world][room]['heartless'])[0]:
                  pass
                else:
                  for story in rooms[player.world][room]['heartless']:
                    if story > player.story:
                      rooms[player.world][room]['heartless'][previusStory]['status'] = rooms[player.world][room]['heartless'][previusStory]['waves']
                      break
                    else:
                      previusStory = story
        #there is no door (link) to the new room
        elif move[1] == 'back':
            alreadyBattled = 0
            temp = currentRoom
            currentRoom = previusRoom
            previusRoom = temp
            for room in rooms[player.world][currentRoom]['resetHeartless']:
              if player.story in rooms[player.world][room]['heartless']:
                if rooms[player.world][room]['heartless'][player.story]['status'] == 0:
                  rooms[player.world][room]['heartless'][player.story]['status'] = rooms[player.world][room]['heartless'][player.story]['waves']
              else:
                if player.story > list(rooms[player.world][room]['heartless'])[-1]:
                  rooms[player.world][room]['heartless'][list(rooms[player.world][room]['heartless'])[-1]]['status'] = rooms[player.world][room]['heartless'][list(rooms[player.world][room]['heartless'])[-1]]['waves']
                elif player.story < list(rooms[player.world][room]['heartless'])[0]:
                  pass
                else:
                  for story in rooms[player.world][room]['heartless']:
                    if story > player.story:
                      rooms[player.world][room]['heartless'][previusStory]['status'] = rooms[player.world][room]['heartless'][previusStory]['waves']
                      break
                    else:
                      previusStory = story

        else:
          if retryBoss == False:
            print('You can\'t go that way!')

    elif move[0] == 'talk' :                            ##### TALK WITH PERSON
      #if the room contains an person
      peopleToTalk, storyToTalk = verifyPersonStory(rooms[player.world][currentRoom]['person'])

      if 'person' in rooms[player.world][currentRoom] and move[1].capitalize() in peopleToTalk:
        i=0
        for person in peopleToTalk:
          if move[1].capitalize() == person:
            #falar com a pessoa
            print(people[currentRoom][person][storyToTalk[i]]['speech'])
            event = people[currentRoom][person][storyToTalk[i]]
            reward = event['reward']
            if reward == 'story':
              if player.story == (people[currentRoom][person][storyToTalk[i]]['story']-1):
                player.story += 1
                print()
            elif reward == 'mapUpdate':
              if player.map[player.world][event['mapUpdate']] == 'no':
                player.map[player.world][event['mapUpdate']] = 'incomplete'
                print('Obtained ' + player.world + ' ' + event['mapUpdate'] + ' map!')
              elif player.map[player.world][event['mapUpdate']] == 'incomplete':
                player.map[player.world][event['mapUpdate']] = 'complete'
                print(player.world + ' ' + event['mapUpdate'] + ' map updated!')
              if player.tutorial['open map'] == 0:
                print(Fore.YELLOW + "tutorial: " + Fore.WHITE + tutorialSpeech['open map'])
                player.tutorial['open map'] = 1
            elif reward == 'keyblade':
              player.keyblades.append(people[currentRoom][person][storyToTalk[i]]['keyblade'])
              print('You got the ' + cyan + people[currentRoom][person][storyToTalk[i]]['keyblade'] + white + ' Keyblade!')
            elif reward == 'key item':
              player.keyItems.append(people[currentRoom][person][storyToTalk[i]]['key item'])
              print('You got the "' + people[currentRoom][person][storyToTalk[i]]['key item'] + '" key item!')
            elif reward == 'item':
              print('You got a ' + green + people[currentRoom][person][storyToTalk[i]]['item'] + white + '!')
              if len(player.item) < player.itemPouch:
                player.item.append(people[currentRoom][person][storyToTalk[i]]['item'])
              else:
                player.stock.append(people[currentRoom][person][storyToTalk[i]]['item'])
                print('Your item pouch is full, item send to stock!!')
            elif reward == 'arena':
              selectArena()
            # elif reward == 'transport':
            #   print(event['transport speech'])

            if reward != 'arena':
              people[currentRoom][person][storyToTalk[i]]['reward'] = 'no'

            if 'Moogle' in rooms[player.world][currentRoom]['person']:
                shop(currentRoom)

          i+=1

      else:
        #tell them they can't talk
        print('Can\'t talk to ' + move[1] + '!')


    if 'boss' in rooms[player.world][currentRoom] and player.story == (bosses[rooms[player.world][currentRoom]['boss']]['story']-1):           ###### BOSS BATTLE
      retryBoss = False
      bossScene(rooms[player.world][currentRoom]['boss'])
      result = battle(rooms[player.world][currentRoom]['boss'])
      if result == 'victory':
        player.story = bosses[rooms[player.world][currentRoom]['boss']]['story']
      ###RESET HEARTLESS STATUS SO PLAYER WON'T FIGHT RIGHT AWAY
        if 'heartless' in rooms[player.world][currentRoom]:
          if player.story > list(rooms[player.world][currentRoom]['heartless'])[-1]:
            rooms[player.world][currentRoom]['heartless'][list(rooms[player.world][currentRoom]['heartless'])[-1]]['status'] = 0
          elif player.story < list(rooms[player.world][currentRoom]['heartless'])[0]:
            pass
          else:
            for story in rooms[player.world][currentRoom]['heartless']:
              if story == player.story:
                rooms[player.world][currentRoom]['heartless'][story]['status'] = 0
                break
              else:
                if story > player.story:
                  rooms[player.world][currentRoom]['heartless'][previusStory]['status'] = 0
                  break
                else:
                  previusStory = story
      ###DEFEAT
      elif result == 'defeat':
          print("---------------------------")
          print('Your HP has dropped to zero!\nGAME OVER')
          result = gameOver()
          if result == '':
            retryBoss = True
          if result == 'run':
            temp = currentRoom
            currentRoom = previusRoom
            previusRoom = temp
            player.calculateHealth()
          if result == 'load':
            player.HP = player.TotalHP
            player.MP = player.TotalMP
            currentRoom = rooms[player.world][0]
            previusRoom = currentRoom
      player.calculateHealth()

    elif 'heartless' in rooms[player.world][currentRoom] and alreadyBattled == 0:           ###### BATTLE
      if player.story > list(rooms[player.world][currentRoom]['heartless'])[-1]:
        alreadyBattled, currentRoom, previusRoom = determineBattle(list(rooms[player.world][currentRoom]['heartless'])[-1], currentRoom, previusRoom)
      elif player.story < list(rooms[player.world][currentRoom]['heartless'])[0]:
        pass
      else:
        for story in rooms[player.world][currentRoom]['heartless']:
          if story == player.story:
            alreadyBattled, currentRoom, previusRoom = determineBattle(story, currentRoom, previusRoom)
            break
          else:
            if story > player.story:
              alreadyBattled, currentRoom, previusRoom = determineBattle(previusStory, currentRoom, previusRoom)
              break
            else:
              previusStory = story


    # player wins if they get to the Third District
    if currentRoom == 'Third District' and  player.story == 1:
      print('You found Donald & Goofy... YOU WIN!')
      break
