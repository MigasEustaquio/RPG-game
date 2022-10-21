#!/bin/python3
# from os import X_OK
import random

import time
from utilities.allyClasses import *
from utilities.enemyClasses import *
from utilities.screen import *
from dictionaries.people import *
from dictionaries.location import *
from dictionaries.enemies import *
from dictionaries.scenes import *
from dictionaries.enemyLocations import *

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

def verifyPersonStory(peolpeInRoom):            ###Check person's speech and reward based on story
  peopleToTalk = []
  storyToTalk = []
  for person in peolpeInRoom:
      if player.story[player.world] > list(people[currentRoom][person])[-1]:
        if people[currentRoom][person][list(people[currentRoom][person])[-1]]['present'] == 'yes':
          peopleToTalk.append(person)
          storyToTalk.append(list(people[currentRoom][person])[-1])
      elif player.story[player.world] < list(people[currentRoom][person])[0]:
        pass
      else:
        for story in people[currentRoom][person]:
          if story == player.story[player.world]:
            if people[currentRoom][person][story]['present'] == 'yes':
              peopleToTalk.append(person)
              storyToTalk.append(story)
            break
          else:
            if story > player.story[player.world]:
              if people[currentRoom][person][previousStory]['present'] == 'yes':
                peopleToTalk.append(person)
                storyToTalk.append(previousStory)
              break
            else:
              previousStory = story
  return peopleToTalk, storyToTalk

def bossScene(enemyName):                       ###Print Scenes
  skip = input('Skip scene?(yes/no)\n>')
  print()
  if skip.lower() == 'yes':
    pass
  else:
    for phrase in bossScenes[enemyName]:
     print(phrase)
     time.sleep(3)
    print()

def showStatus():                               ###SHOW STATUS
  #print the player's current status
  print(Fore.RED + '\n---------------------------')
  print(Fore.WHITE + 'You are in the ' + currentRoom)
  if "person" in rooms[player.world][currentRoom]:
    peopleToTalk, storyToTalk = verifyPersonStory(rooms[player.world][currentRoom]['person'])
    for person in peopleToTalk:
      print('❕ You see ' + person)
  if "shop" in rooms[player.world][currentRoom]:
    if (currentRoom+' Shop location') in player.keyItems or rooms[player.world][rooms[player.world][currentRoom]['shop']]['key'] in player.keyItems:
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
  if 'treasure' in rooms[player.world][currentRoom]:
    count=0
    for number in player.treasures[player.world][currentRoom]:
      if number > player.story[player.world]: break
      if player.treasures[player.world][currentRoom][number]['status']=='closed': count+=1
    if count == 0: return
    elif count == 1:
      print('🔸 You see a treasure chest!')
    elif count > 1:
      print('🔸 You see ' + str(count) + ' treasure chests!')
    if player.tutorial['treasure chest'] == 0:
      print(Fore.YELLOW + "tutorial: " + Fore.WHITE + tutorialSpeech['treasure chest'])
      player.tutorial['treasure chest'] = 1
  print()
  for x in rooms[player.world][currentRoom]['move']:
    if rooms[player.world][currentRoom][x] in player.visitedRooms[player.world]:
      print('➤ ' + x + ': ' + rooms[player.world][currentRoom][x])
  print(Fore.RED + "---------------------------")

def openTreasure(number, currentRoom):

  if treasureList[player.world][currentRoom][number]['treasure'] == 'item':
    print('Obtained a "' + treasureList[player.world][currentRoom][number]['item'] + '"!')
    if len(player.item) < player.itemPouch:
      player.item.append(treasureList[player.world][currentRoom][number]['item'])
    else:
      player.stock.append(treasureList[player.world][currentRoom][number]['item'])
      print('Your item pouch is full, item send to stock!!')

  elif treasureList[player.world][currentRoom][number]['treasure'] == 'key item':
    print('Obtained the "' + treasureList[player.world][currentRoom][number]['key item'] + '" key item!')
    player.keyItems.append(treasureList[player.world][currentRoom][number]['key item'])

  elif treasureList[player.world][currentRoom][number]['treasure'] == 'mapUpdate':
    if player.map[player.world][treasureList[player.world][currentRoom][number]['mapUpdate']] == 'no':
      player.map[player.world][treasureList[player.world][currentRoom][number]['mapUpdate']] = 'incomplete'
      print('Obtained ' + player.world + ' ' + treasureList[player.world][currentRoom][number]['mapUpdate'] + ' map!')
    elif player.map[player.world][treasureList[player.world][currentRoom][number]['mapUpdate']] == 'incomplete':
      player.map[player.world][treasureList[player.world][currentRoom][number]] = 'complete'
      print(player.world + ' ' + treasureList[player.world][currentRoom][number]['mapUpdate'] + ' map updated!')
    if player.tutorial['open map'] == 0:
      print(Fore.YELLOW + "tutorial: " + Fore.WHITE + tutorialSpeech['open map'])
      player.tutorial['open map'] = 1

  elif treasureList[player.world][currentRoom][number]['treasure'] == 'keyblade':
    print('Obtained the ' + cyan + treasureList[player.world][currentRoom][number]['keyblade'] + white + ' Keyblade!')
    player.keyblades.append(treasureList[player.world][currentRoom][number]['keyblade'])

  player.treasures[player.world][currentRoom][number]['status']='opened'

def shop(currentRoom):                          ###SHOP
    for item in shops[currentRoom]:
        print(item, '   \tcost:', shops[currentRoom][item], 'munny!')

def resetHeartless(currentRoom, previousStory=0):
  for room in rooms[player.world][currentRoom]['resetHeartless']:
    if 'heartless' in rooms[player.world][room]:
      if player.story[player.world] in enemyLocations[player.world][room]:
        if enemyLocations[player.world][room][player.story[player.world]]['status'] == 0:
          enemyLocations[player.world][room][player.story[player.world]]['status'] = enemyLocations[player.world][room][player.story[player.world]]['waves']
      else:
        if player.story[player.world] > list(enemyLocations[player.world][room])[-1]:
          enemyLocations[player.world][room][-1]['status'] = enemyLocations[player.world][room][-1]['waves']
        elif player.story[player.world] < list(enemyLocations[player.world][room])[0]:
          pass
        else:
          for story in enemyLocations[player.world][room]:
            if story > player.story[player.world]:
              enemyLocations[player.world][room][previousStory]['status'] = enemyLocations[player.world][room][previousStory]['waves']
              break
            else:
              previousStory = story

def levelUP():                                  ###LEVEL UP
  if levelUp[player.level]['ability'] != 'none':
    player.abilities.append([levelUp[player.level]['ability'], False])
    print('\nObtained ' + yellow + levelUp[player.level]['ability'] + '!')
    # if levelUp[player.level]['ability'][0] in finishersList:
    #   player.finishers.append(levelUp[player.level]['ability'])
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

def useItem(item):                              ###USE ITEM
  del player.item[player.item.index(item)]
  player.itemBKP.append(item)
  player.ArenaitemBKP.append(item)

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

def scan(enemy):                                ###SCAN
  heartlessHealthDisplay = ''
  i=0
  while i< enemy.MaxHP:
    if i<enemy.HP:
      heartlessHealthDisplay += '♥'
    else:
      heartlessHealthDisplay += '♡'
    i+=1

    if enemy.HP<= math.ceil(0.25*enemy.MaxHP):
      colour=red
    elif enemy.HP<= math.ceil(0.5*enemy.MaxHP):
      colour=yellow
    else: colour=green

  print(Fore.MAGENTA + '---------------------------')
  print("Scan : " + enemy.name)
  print("HP : " + colour + heartlessHealthDisplay)
  print(Fore.MAGENTA + "---------------------------")

def finishAttack(enemy, damage, defense, mPower, enemyDamageDealt):                ###FINISHERS
  if len(player.finishers) == 1: finish = player.finishers[0]
  else: finish = player.finishers[random.randint(0, (len(player.finishers)-1))]
  print('You attacked and unleashed a combo finisher!')
  if finish == 'Blitz':
    print("You used " + yellow + "Blitz" + white + " and dealt " + yellow + "critical" + white + " damage!")
    damageDealt = math.ceil(1.5*damage)-enemy.defense
  elif finish == 'Gravity Break':
    print("You used " + blue + "Gravity Break" + white + " and cast the gravity spell!")
    if enemy.magicImmunity:
      print("You cast " + blue + "Gravity" + white + " but it doesn\'t have any effect!")
      damageDealt=0
    else:
      damageDealt = math.ceil(damage/2)+mPower+math.ceil(enemy.MaxHP/5)-enemy.magicResistance
      if damageDealt<0: damageDealt=0
      print("You cast " + blue + "Gravity" + white + " and deal " + red + str(damageDealt) + " ♥" + white + " of damage!\nThe enemy is now too heavy too attack!")
      enemy.statusEffect = "gravity"
      enemy.statusDuration = magics["gravity"]['status']['duration']
    return damage, defense, mPower, enemyDamageDealt, damageDealt

  elif finish == 'Hurricane Blast':   ##NOT IMPLEMENTED
    # print("You used Zantetsuken and dealt " + yellow + "triple" + white + " damage!" + ' You caused ' + red + str(3*damage) + ' ♥ ' + white + 'of damage!')
    print('Hurricane Blast (not implemented)')
  elif finish == 'Ripple Drive':
    if 'Kingdom' in player.keyblade:
      print("You used " + yellow + "Ripple Drive" + white + "! It enhances your " + yellow + "defense" + white + " power!")
      defense += 1
      enemyDamageDealt-=1
      damageDealt = damage-enemy.defense
    elif 'Jungle King' in player.keyblade:
      print("You used " + green + "Ripple Drive" + white + "! You restore " + red + '2 ♥'+ white + " !")
      player.HP+=2
      damageDealt = damage-enemy.defense
    elif 'Lady Luck' in player.keyblade:
      print("You used " + blue + "Ripple Drive" + white + "! It significantly enhances your " + blue + "magical power" + white + "!")
      mPower+=2
      damageDealt = damage-enemy.defense
    elif 'Olympia' in player.keyblade:
      print("You used " + red + "Ripple Drive" + white + "! You can now ignore enemy blocks!")
      damageDealt=damage-enemy.totalDefense
      player.ignoreBlock=True
    elif 'Three Wishes' in player.keyblade:
      print("You used " + red + "Ripple Drive" + white + "! You can now ignore enemy blocks!")
      damageDealt=damage-enemy.totalDefense
      player.ignoreBlock=True
    elif 'Wishing Star' in player.keyblade:
      print("You used " + red + "Ripple Drive" + white + "! It enhances your " + red + "attack power" + white + "!")
      damage+=1
      damageDealt = damage-enemy.defense
    elif 'Spellbinder' in player.keyblade:
      print("You used " + blue + "Ripple Drive" + white + "! It significantly enhances your " + blue + "magical power" + white + "!")
      mPower+=2
      damageDealt = damage-enemy.defense
    elif 'Crabclaw' in player.keyblade:
      print("You used " + blue + "Ripple Drive" + white + "! It enhances your " + blue + "magical power" + white + "!")
      mPower+=1
      damageDealt = damage-enemy.defense
    elif 'Pumpkinhead' in player.keyblade:
      print("You used " + red + "Ripple Drive" + white + "! It enhances your " + red + "attack power" + white + "!")
      damage+=1
      damageDealt = damage-enemy.defense
    elif 'Metal Chocobo' in player.keyblade:
      print("You used " + red + "Ripple Drive" + white + "! It significantly enhances your " + red + "attack power" + white + "!")
      damage+=2
      damageDealt = damage-enemy.defense
    elif 'Fairy Harp' in player.keyblade:
      print("You used " + blue + "Ripple Drive" + white + "! It enhances your " + blue + "magical power" + white + "!")
      mPower+=1
      damageDealt = damage-enemy.defense
    elif 'Divine Rose' in player.keyblade:
      print("You used " + red + "Ripple Drive" + white + "! It enhances your " + red + "attack power" + white + " and you can now ignore enemy blocks!")
      damage+=1
      damageDealt=damage-enemy.totalDefense
      player.ignoreBlock=True
    elif 'Oathkeeper' in player.keyblade:
      print("You used " + green + "Ripple Drive" + white + "! It enhances your " + blue + "magical power" + white + " and also restore " + red + str(math.ceil(player.TotalMP/4)) + ' ♥'+ white + " !")
      player.HP += math.ceil(player.TotalMP/4) #Restore HP based on total MP
      mPower+=1
      damageDealt = damage-enemy.defense
    elif 'Oblivion' in player.keyblade:
      print("You used " + red + "Ripple Drive" + white + "! It significantly enhances your " + red + "attack power" + white + " and enhances your " + blue + "magical power" + white + "!")
      damage+=2
      mPower+=1
      damageDealt = damage-enemy.defense
    elif 'Lionheart' in player.keyblade:
      print("You used " + yellow + "Ripple Drive" + white + "! It enhances both your " + red + "attack power" + white + " and your " + blue + "magical power" + white + "!")
      damage+=1
      mPower+=1
      damageDealt = damage-enemy.defense
    elif 'Diamond Dust' in player.keyblade:
      print("You used " + blue + "Ripple Drive" + white + "! It Greatly enhances your " + blue + "magical power" + white + " and also restore " + blue + str(math.ceil(player.TotalMP/4)) + ' ●'+ white + " !")
      player.MP += math.ceil(player.TotalMP/4)
      mPower+=3
      damageDealt = damage-enemy.defense
    elif 'One-Winged Angel' in player.keyblade:
      print("You used " + blue + "Ripple Drive" + white + "! It dealt " + yellow + "triple" + white + " critical damage!")
      damageDealt = 3*damage-enemy.defense
    elif 'Ultima Weapon' in player.keyblade:
      print("You used " + green + "Ripple Drive" + white + "! It restores " + red + '2 ♥'+ white + " and " + blue + "2 ●" + white +"!")
      player.HP += 2
      player.MP += 2
      damageDealt = damage-enemy.defense
    else:
      print('You shouldn\'t have this keyblade... Anyway it has no bonus effect')
      damageDealt = damage-enemy.defense
  elif finish == 'Stun Impact':
    print('You used ' + red +'Stun Impact' + white + ' and it caused the enemy to be stunned!')
    enemyDamageDealt = 0
    damageDealt = damage-enemy.defense
  elif finish == 'Zantetsuken':
    print("You used " + yellow + "Zantetsuken" + white + " and dealt " + yellow + "double" + white + " damage!")
    damageDealt = 2*damage-enemy.defense
 
  if damageDealt<0: damageDealt=0
  print('You caused ' + red + str(damageDealt) + ' ♥ ' + white + 'of damage!')
  return damage, defense, mPower, enemyDamageDealt, damageDealt

def battleCommands(commandOptions, usingAbility, activeAbilityCount):
    print("---------------------------")
    if usingAbility!='':
      ability=activeAbilities[usingAbility]
      if activeAbilityCount==ability['duration']: print(commandOptions.replace('[item name]','[item name]'+yellow+'\n'+ability['commands'][1]+'/'+ability['commands'][0]+white))
      else: print(commandOptions.replace('[item name]','[item name]'+yellow+'\n'+ability['commands'][0]+white))
    else: print(commandOptions)

def battle(enemyName, arenaBattle=False):       ###BATTLE
  ###
    player.createBKP()
    if enemyName in bosses:
      bossBattle = True
    elif enemyName in heartless:
      bossBattle = False

    damageBase = keybladeStatus[player.keyblade]['damage'] + player.STR
    defense = player.DEF
    mPower = player.magicPower

    for accessory in player.equipment:
      damageBase += equipments[accessory]['STR']
      defense += equipments[accessory]['DEF']

    print("---------------------------")
    commandOptions = 'commands: \n\nattack \nmagic [magic name] \nitem [item name]'
    if bossBattle: print('Boss Battle! ' + enemyName  + '!\n')
    else:
      print('You see a ' + red + 'Heartless' + white +'! It\'s a '+ red + enemyName + white + '!')
      commandOptions = commandOptions + ' \nrun'
    
    enemy = Heartless(enemyName, bossBattle)

    finishingPlusCheck=False
    finishCount = 0
    player.ignoreBlock=False
    player.blocked=False
    activeAbilityCount=0
    usingAbility = ''
    command = ''

    while True:
        player.showBattleStatus()
        enemy.damage = enemy.totalDamage

        if ['Berserk', True] in player.abilities and player.HPBarColour == 'RED':
          damage=damageBase+2
        else: damage=damageBase

        if ['Scan', True] in player.abilities:
          scan(enemy)

        battleCommands(commandOptions, usingAbility, activeAbilityCount)

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
          if bossBattle == False: enemySpeech, enemyDamageDealt = enemy.selectCommand(defense)
          else: enemySpeech, enemyDamageDealt = enemy.selectCommandBoss(defense)
    ### Allies Help
          if player.allies:
            for ally in player.allies:
              helpType, helpValue, helpStatus = ally.selectCommand(player)
              if helpType == 'heal': player.HP = player.HP + helpValue
              else:
                helpValue=helpValue-enemy.defense
                if helpValue<0: helpValue=0
                enemy.HP = enemy.HP - helpValue
              if helpStatus != '':
                enemy.statusEffect = helpStatus
                enemy.statusDuration = magics[helpStatus]['status']['duration']
          if player.HP > player.TotalHP: player.HP = player.TotalHP
  ###ATTACK
    ###
        elif command == 'attack':       ###ATTACK
            command = ''
    ### Calculate enemy damage
            if bossBattle == False: enemySpeech, enemyDamageDealt = enemy.selectCommand(defense)
            else: enemySpeech, enemyDamageDealt = enemy.selectCommandBoss(defense)
    ### Finishers
            if any(item in player.finishers for item in finishersList) and finishCount == 3:
              damage, defense, mPower, enemyDamageDealt, damageDealt = finishAttack(enemy, damage, defense, mPower, enemyDamageDealt)
              finishCount = 0
              if finishingPlusCheck: finishingPlusCheck=False
              else: finishingPlusCheck=True
            elif any(item in player.finishers for item in finishersList) and ['Negative Combo', True] in player.abilities and finishCount == 2:
              damage, defense, mPower, enemyDamageDealt, damageDealt = finishAttack(enemy, damage, defense, mPower, enemyDamageDealt)
              finishCount = 0
              if finishingPlusCheck: finishingPlusCheck=False
              else: finishingPlusCheck=True
            elif any(item in player.finishers for item in finishersList) and ['Finishing Plus', True] in player.abilities and finishingPlusCheck:
              damage, defense, mPower, enemyDamageDealt, damageDealt = finishAttack(enemy, damage, defense, mPower, enemyDamageDealt)
              finishCount = 0
              finishingPlusCheck=False
            else:
          #Conterattack
              if ['Counterattack', True] in player.abilities and player.blocked:
                damage=math.ceil(1.5*damage)
                if ['Counter Replenisher', True] in player.abilities:
                  print(blue + 'Counterattack' + white + '!')
                  replenishMP = math.ceil((player.TotalMP-player.MP)/8)
                  print('You gained ' + blue + str(replenishMP) + ' ● ' + white + '!\n')
                  player.MP += replenishMP
                  if player.MP > player.TotalMP: player.MP = player.TotalMP
                else: print('Counterattack!')
          #Normal attack
              finishCount += 1
              if player.ignoreBlock: damageDealt=damage-enemy.totalDefense
              else: damageDealt = (damage-enemy.defense)
              if damageDealt < 0: damageDealt=0
              print('You attacked and caused ' + red + str(damageDealt) + ' ♥ ' + white + 'of damage!')

            enemy.HP = enemy.HP - damageDealt
            player.blocked=False

            if damageDealt==0:
              finishCount = 0
              finishingPlusCheck=False
              if enemySpeech == 'The enemy tries to block all incoming phisical attacks!':
                player.blocked=True

    ### Inflict enemy damage
            if enemy.statusEffect != 'none': enemySpeech, enemyDamageDealt = enemy.statusEffectDamageReduction(enemySpeech, enemyDamageDealt, mPower)
            print(enemySpeech)
            player.HP -= enemyDamageDealt
            if  ['Second Chance', True] in player.abilities and player.HP<1 and player.HP+enemyDamageDealt>1:
              player.HP=1
              print(green +'Second Chance' + white)
    ### Status effect damage
            if 'fir' in enemy.statusEffect:
              enemy.statusEffectDamage()
    ### Allies Help
            if player.allies:
              for ally in player.allies:
                helpType, helpValue, helpStatus = ally.selectCommand(player)
                if helpType == 'heal': player.HP = player.HP + helpValue
                else:
                  helpValue=helpValue-enemy.defense
                  if helpValue<0: helpValue=0
                  enemy.HP = enemy.HP - helpValue
                if helpStatus != '':
                  enemy.statusEffect = helpStatus
                  enemy.statusDuration = magics[helpStatus]['status']['duration']
            if player.HP > player.TotalHP: player.HP = player.TotalHP

            usingAbility = ''
  ###MAGIC
    ###
        elif "magic" in command:       ###MAGIC
          command = command.lower().split()
    ###Check magic requirements
          if not player.magic:  print('Magic is still a mystery to you!')
          else:
            if command[1] in player.magic:
              if player.MP >= magics[command[1]]['MP']:

    ### Calculate enemy damage
                if bossBattle == False: enemySpeech, enemyDamageDealt = enemy.selectCommand(defense)
                else: enemySpeech, enemyDamageDealt = enemy.selectCommandBoss(defense)

              #Combo finisher
                if ['Combo Master', True] not in player.abilities or finishCount == 3:
                  finishCount = 0
                finishingPlusCheck=False
                player.blocked=False

    ###COLOR SPEECH
                magicText = magics[command[1]]['speech']
                print('You used ' + blue + str(magics[command[1]]['MP']) +' ● ' + white + '!')
                if 'cur' not in command[1] and 'grav' not in command[1] and enemy.magicImmunity==False:
                  magicDamage = mPower+magics[command[1]]['damage']-enemy.magicResistance
                  if magicDamage<0: magicDamage=0
                  print("You cast " + player.colors[magicText[4]] + command[1].capitalize() + white + " and deal " + red + str(magicDamage) + magicText[1] + white + magicText[2] + player.colors[magicText[4]] + magicText[3])
                elif 'grav' in command[1] and enemy.magicImmunity==False:
                  magicDamage = mPower+math.ceil(enemy.MaxHP/5)-enemy.magicResistance
                  if magicDamage<0: magicDamage=0
                  print("You cast " + player.colors[magicText[4]] + command[1].capitalize() + white + " and deal " + red + str(magicDamage) + magicText[1] + white + magicText[2] + player.colors[magicText[4]] + magicText[3])
                elif 'cur' not in command[1]:
                  magicDamage=0
                  print("You cast " + player.colors[magicText[4]] + command[1].capitalize() + white + " but it doesn\'t have any effect!")
                else:
                  print("You cast " + green + command[1].capitalize() + white + " and restore " + red + str(mPower+magics[command[1]]['heal']) + magicText[1] + white + magicText[2])
                player.MP = player.MP - magics[command[1]]['MP']
    ###Calculate damage
                if ['Leaf Bracer', True] in player.abilities and 'cur' in command[1]:
                  print(green + 'Leaf Bracer' + white +' protects you from damage while casting a Healing spell!')
                  enemySpeech=enemySpeech.replace(str(enemyDamageDealt) + ' ♥',Fore.RED + '0 ♥' + Fore.WHITE)
                  enemyDamageDealt = 0
                else:
                  enemy.HP = enemy.HP - magicDamage
                if 'cur' in command[1]: player.HP = player.HP + (magics[command[1]]['heal']+mPower)
    ### Start status effect
                if 'cur' not in command[1] and enemy.magicImmunity==False:
                  enemy.statusEffect = command[1]
                  enemy.statusDuration = magics[command[1]]['status']['duration']
    ### Inflict enemy damage
                if enemy.statusEffect != 'none': enemySpeech, enemyDamageDealt = enemy.statusEffectDamageReduction(enemySpeech, enemyDamageDealt, mPower)
                print(enemySpeech)
                player.HP -= enemyDamageDealt
                if ['Second Chance', True] in player.abilities and player.HP<1 and player.HP+enemyDamageDealt>1:
                  player.HP=1
                  print(green +'Second Chance' + white)
    ### Status effect damage
                if 'fir' in enemy.statusEffect:
                  enemy.statusEffectDamage()
    ### Allies Help
                if player.allies:
                  for ally in player.allies:
                    helpType, helpValue, helpStatus = ally.selectCommand(player)
                    if helpType == 'heal': player.HP = player.HP + helpValue
                    else:
                      helpValue=helpValue-enemy.defense
                      if helpValue<0: helpValue=0
                      enemy.HP = enemy.HP - helpValue
                    if helpStatus != '':
                      enemy.statusEffect = helpStatus
                      enemy.statusDuration = magics[helpStatus]['status']['duration']
                if player.HP > player.TotalHP: player.HP = player.TotalHP
    ###
              else:
                print('Not enough MP!')
            else:
              print('Magic not found!')

          command = ''
          usingAbility = ''
  ###ITEM
    ###
        elif "item" in command:       ###ITEM
          command = command.lower().split()
          if not player.item:
            print('You have no items!')
          else:
            try:
              if command[1] in player.item:

              #Combo finisher
                finishCount = 0
                finishingPlusCheck=False
                player.blocked=False

                useItem(command[1])
    ### Status effect damage
                if 'fir' in enemy.statusEffect:
                  enemy.statusEffectDamage()
    ### Calculate enemy damage
                if bossBattle == False: enemySpeech, enemyDamageDealt = enemy.selectCommand(defense)
                else: enemySpeech, enemyDamageDealt = enemy.selectCommandBoss(defense)
    ### Inflict enemy damage
                if enemy.statusEffect != 'none': enemySpeech, enemyDamageDealt = enemy.statusEffectDamageReduction(enemySpeech, enemyDamageDealt, mPower)
                print(enemySpeech)
                player.HP -= enemyDamageDealt
                if ['Second Chance', True] in player.abilities and player.HP<1 and player.HP+enemyDamageDealt>1:
                  player.HP=1
                  print(green +'Second Chance' + white)
    ### Allies Help
                if player.allies:
                  for ally in player.allies:
                    helpType, helpValue, helpStatus = ally.selectCommand(player)
                    if helpType == 'heal': player.HP = player.HP + helpValue
                    else:
                      helpValue=helpValue-enemy.defense
                      if helpValue<0: helpValue=0
                      enemy.HP = enemy.HP - helpValue
                    if helpStatus != '':
                      enemy.statusEffect = helpStatus
                      enemy.statusDuration = magics[helpStatus]['status']['duration']
                if player.HP > player.TotalHP: player.HP = player.TotalHP
    ###
              else:
                print("You don\'t have any ", command[1])
            except IndexError:
                print('try: item [item name]')

          command = ''
          usingAbility = ''

  ###ACTIVE ABILITY
    ###
        elif command in activeAbilitiesSimple or command in activeAbilitiesCommands:       ###ACTIVE ABILITY
          command = command.lower()
          if ' ' in command:  command = command.split()[0]

    ###Check ability requirements
          if not player.activeAbilities:
            print('You don\'t have any active ability equipped!')
          else:
            try:
              command = [x for x in activeAbilitiesList if command.capitalize() in x][0] #identify ability
            except:
              command = [x for x in activeAbilitiesList if command in activeAbilities[x]['commands']][0] #identify ability

            if command in player.activeAbilities:
              if player.MP >= activeAbilities[command]['MP'] or command==usingAbility:
                ability = activeAbilities[command]

    ### Calculate enemy damage
                if bossBattle == False: enemySpeech, enemyDamageDealt = enemy.selectCommand(defense)
                else: enemySpeech, enemyDamageDealt = enemy.selectCommandBoss(defense)

              #Combo finisher
                finishCount = 0
                finishingPlusCheck=False
                player.blocked=False

    ###ABILITY COUNT AND MP
                if command!=usingAbility:
                  print('You used ' + blue + str(ability['MP']) +' ● ' + white + '!')
                  player.MP = player.MP - ability['MP']
                usingAbility=command
                if activeAbilityCount<ability['duration']:
                  abilityDamageName='damage'
                  activeAbilityCount+=1
                else:
                  abilityDamageName='final damage'
                  activeAbilityCount=0

    ###COLOR SPEECH
                if usingAbility == 'Ragnarok' and abilityDamageName=='final damage':
                  abilityDamage = mPower+ability[abilityDamageName]-enemy.magicResistance
                  if abilityDamage<0: abilityDamage=0
                  print('dano: ', abilityDamage)
                  # print("You cast " + green + command[1].capitalize() + white + " and restore " + red + str(mPower+magics[command[1]]['heal']) + magicText[1] + white + magicText[2])
                elif usingAbility != 'Trinity Limit':
                  abilityDamage = damage+ability[abilityDamageName]-enemy.defense
                  if abilityDamage<0: abilityDamage=0
                  print('dano: ', abilityDamage)
                  # print("You cast " + player.colors[magicText[4]] + command[1].capitalize() + white + " and deal " + red + str(magicDamage) + magicText[1] + white + magicText[2] + player.colors[magicText[4]] + magicText[3])
                else:
                  abilityDamage = mPower+ability[abilityDamageName]-enemy.magicResistance
                  if abilityDamage<0: abilityDamage=0
                  print('dano: ', abilityDamage)
                  # print("You cast " + green + command[1].capitalize() + white + " and restore " + red + str(mPower+magics[command[1]]['heal']) + magicText[1] + white + magicText[2])
                if activeAbilityCount == 0: usingAbility=''
    ###Calculate damage
                enemy.HP = enemy.HP - abilityDamage
    ### Inflict enemy damage
                if usingAbility == 'Trinity Limit':
                  enemySpeech=enemySpeech.replace('You lost ' + str(damageDealt) + ' ♥','The enemy is lightstruck and causes no damage!')
                  enemyDamageDealt=0
                elif enemy.statusEffect != 'none': enemySpeech, enemyDamageDealt = enemy.statusEffectDamageReduction(enemySpeech, enemyDamageDealt, mPower)
                print(enemySpeech)
                player.HP -= enemyDamageDealt
                if ['Second Chance', True] in player.abilities and player.HP<1 and player.HP+enemyDamageDealt>1:
                  player.HP=1
                  print(green +'Second Chance' + white)
    ### Status effect damage
                if 'fir' in enemy.statusEffect:
                  enemy.statusEffectDamage()
    ### Allies Help
                if player.allies:
                  for ally in player.allies:
                    helpType, helpValue, helpStatus = ally.selectCommand(player)
                    if helpType == 'heal': player.HP = player.HP + helpValue
                    else:
                      helpValue=helpValue-enemy.defense
                      if helpValue<0: helpValue=0
                      enemy.HP = enemy.HP - helpValue
                    if helpStatus != '':
                      enemy.statusEffect = helpStatus
                      enemy.statusDuration = magics[helpStatus]['status']['duration']
                if player.HP > player.TotalHP: player.HP = player.TotalHP
    ###
              else:
                print('Not enough MP!')
            else:
              print('Ability not found!')

          command = ''


  ###RUN
        elif "run" in command:       ###RUN
          if bossBattle == True:
            print('You can\'t run from a boss battle!')
            command = ''
          elif arenaBattle == True:
            print('You can\'t run from the arena!')
            command = ''
          else:
            command = ''
            print('You got away successfully!')
            return 'run'
  ###ERROR
        else:       ###ERROR
          command = ''
          print('Command not found!')
  ###DEFEAT
        if player.HP < 1:       ###DEFEAT
            return 'defeat'
  ###VICTORY
        if enemy.HP <= 0:       ###VICTORY
          if not arenaBattle:
    ###MUNNY
            munny = 3 * random.randint(enemy.munny[0], enemy.munny[1])
            if ['Jackpot', True] in player.abilities: munny=math.ceil(munny*6/5)
            print('\nYou defeated the Heartless!\nCONGRATULATIONS!')
            print('\nYou obtained ' + yellow + str(munny) + '🔸 munny!')
            player.munny += munny
    ###EXP
            if 'exp bracelet' in player.equipment or 'exp earring' in player.equipment: enemy.exp = math.ceil(enemy.exp*6/5)
            print('You gained ' + str(enemy.exp) + ' exp!')
            player.exp += enemy.exp
            while player.exp >= levelUp[player.level]['next']:
              player.level+=1
              print('\nLevel Up!\nLevel: ' + str(player.level))
              levelUP()
    ###DROP
            if ['Lucky Strike', True] in player.abilities: enemy.drop = enemy.luckyDrop
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
          if ['Mp Haste', True] in player.abilities: recoverMPNumberNeeded = 55
          else: recoverMPNumberNeeded = 75
          if ['Mp Rage', True] in player.abilities: recoverMP = math.ceil(player.TotalMP/4) + math.ceil((player.TotalMP-player.MP)/4)
          else: recoverMP = math.ceil(player.TotalMP/4)

          if recoverMPNumber > recoverMPNumberNeeded:
            print('\nYou recovered ' + blue + str(recoverMP) + ' ● ' + white + '!')
            player.MP += recoverMP
            if player.MP > player.TotalMP: player.MP = player.TotalMP

          return 'victory'
        enemy.statusEffectEnd()

def gameOver():                                 ###GAME OVER
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

def arenaGameOver():                            ###ARENA GAME OVER
  print('\n\nKINGDOM HEARTS🤍\n\nColiseum Arena\nretry?\nquit?\n\n')
  command = ''
  while True:
    player.restoreArenaBKP()
    command = input('>').lower()
    if 'retry' in command: return 'retry'
    elif 'quit' in command: return 'quit'
    else:
      print('Command not found!\n')
      command = ''

def determineBattle(story, currentRoom, previousRoom):   ###DETERMINE ENEMY TO BATTLE
    status = enemyLocations[player.world][currentRoom][story]['status']
    if status > 0:
      while True:
        result = battle(enemyLocations[player.world][currentRoom][story]['wave'][status])
        if result == 'victory':
          enemyLocations[player.world][currentRoom][story]['status'] = (status - 1)
          player.calculateHealth()
          return 1, currentRoom, previousRoom
        if result == 'defeat':
          print("---------------------------")
          print('Your HP has dropped to zero!\nGAME OVER')
          result = gameOver()
        if result == 'run':
          temp = currentRoom
          currentRoom = previousRoom
          previousRoom = temp
          player.calculateHealth()
          return 0, currentRoom, previousRoom
        if result == 'load':
          player.HP = player.TotalHP
          player.MP = player.TotalMP
          return 0, rooms[player.world][0], rooms[player.world][0]
    else: return 0, currentRoom, previousRoom
  
def unrestrict(room):                           ###UNRESTRICT AREAS

  if len(rooms[player.world][room]['unlock'][x])>2:
    del rooms[player.world][rooms[player.world][room]['unlock'][x][2]]['restricted'][rooms[player.world][room]['unlock'][x][3]]
    if rooms[player.world][room]['unlock'][x][2] in player.restrictionLifted[player.world]:
      player.restrictionLifted[player.world][rooms[player.world][room]['unlock'][x][2]].append(rooms[player.world][room]['unlock'][x][3])
    else:
      player.restrictionLifted[player.world][rooms[player.world][room]['unlock'][x][2]]=[rooms[player.world][room]['unlock'][x][3]]
  del rooms[player.world][room]['restricted'][rooms[player.world][room]['unlock'][x][0]]

  if room in player.restrictionLifted[player.world]:
    player.restrictionLifted[player.world][room].append(rooms[player.world][room]['unlock'][x][0])
  else:
    player.restrictionLifted[player.world][room]=[rooms[player.world][room]['unlock'][x][0]]

def addVisitedRoom(room):                       ###SAVE VISITED AREAS
  if room not in player.visitedRooms[player.world]: player.visitedRooms[player.world].append(room)

def worldMap():                                 ###WORLD MAP
  while True:
    # showStatus()        #### MAKE A WORLD MAP SHOW STATUS
    print(cyan + '\nWorld Map\n\n' + white + 'Available worlds:')
    for world in player.unlockedWorlds:
      print(worldDisplayName[world])
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
      print('\nDo you want to land in ' + worldDisplayName[world] + '?')
      answer = input('>')
      if 'yes' in answer.lower():
        resetHeartless('Rooms List')
        player.world=world
        addVisitedRoom(rooms[world][0])
        return rooms[world][0]  ###############################

    if 'save' in move:
      player.currentRoom = currentRoom
      with open('utilities/saveFile.txt', 'r') as f:
        saves = ast.literal_eval(f.read())
      saveScreen(player, saves)

def arena(arenaNumber):                         ###ARENA FIGHT

  while True:
    retry = False
    print(Fore.YELLOW + '\n\nWelcome to the ' + arenaNames[arenaNumber] + Fore.WHITE)
    player.createArenaBKP()
    for wave in arenaFights[arenaNumber]:
      print('\nWave ' + str(wave) + '\n')
      result = battle(arenaFights[arenaNumber][wave], arenaBattle=True)
      if result == 'victory': print(green +'\nEnemies defeated!\n' + white)
      elif result == 'defeat':
          if arenaNumber in player.arenaRecords:
            if player.arenaRecords[arenaNumber] != 'Complete' and int(player.arenaRecords[arenaNumber]) < wave:
              player.arenaRecords[arenaNumber] = str(int(wave)-1)
          else: player.arenaRecords[arenaNumber] = str(int(wave)-1)
          
          print("---------------------------")
          print('Your HP has dropped to zero!\nArena Failed')
          result = arenaGameOver()
          if result == 'retry':
            retry = True
            break
          if result == 'quit':
            return

    if retry == False:
      print('\n-----------------------\n\nCongratulations!!')
      trophy = arenaNames[arenaNumber] +' Trophy'
      player.arenaRecords[arenaNumber] = 'Complete'

      ##Already completed the arena before
      if (trophy) in player.keyItems:
        print('You got a ' + green + arenaRewards[arenaNumber][2] + white + '!')
        if len(player.item) < player.itemPouch:
          player.item.append(arenaRewards[arenaNumber][2])
        else:
          player.stock.append(arenaRewards[arenaNumber][2])
          print('Your item pouch is full, item send to stock!!')

      ##First time completing the arena
      else:
        rewards = arenaRewards[arenaNumber][1]
        player.keyItems.append(trophy)
        print('You obtained the ' + trophy + '!\n')

        if 'keyblade' in rewards:
          player.keyblades.append(arenaRewards[arenaNumber]['keyblade'])
          print('You got the ' + cyan + arenaRewards[arenaNumber]['keyblade'] + white + ' Keyblade!')
        if 'magic' in rewards:
          magicName = arenaRewards[arenaNumber]['magic']
          player.magic.append(arenaRewards[arenaNumber]['magic'])
          print('You learned the ' + player.colors[magics[magicName]['speech'][4]] + magicName + white + ' spell!')
        if 'ability' in rewards:
          abilityName = arenaRewards[arenaNumber]['ability']
          player.abilities.append([abilityName, False])
          print('\nObtained ' + yellow + abilityName + '!')

      break

def selectArena():                              ###SELECT ARENA
  while True:
    print('\nPhil: What arena do you wish to enter?\n(type the number of the arena you wish to enter. 0 or \'nevermind\' to leave)')
    for number in player.unlockedArenas:
      if number in player.arenaRecords:
        if player.arenaRecords[number] ==  'Complete':
          print(number + '  ' + arenaNames[number] + green + '\t  Complete!' + white)
        else:
          print(number + '  ' + arenaNames[number] + yellow + '\t  Record: ' + player.arenaRecords[number] + white)
      else:
          print(number + '  ' + arenaNames[number])
    
    answer = input('>')
    answer = str(answer).lower()

    if answer == '0' or answer == 'nevermind':
      print('\nPhil: Okay kid, talk to me if you wish to become a hero!')
      break
    elif answer in player.unlockedArenas:
      print('\nPhil: Very well kid, good luck!')
      arena(answer)
      break
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
  previousStory = 0
  currentRoom = player.currentRoom
  previousRoom = currentRoom
#
  showInstructions()
  while True:
    showStatus()

    if retryBoss == False:                              ##### INPUT READER
      move = ''
      while move == '':  
        move = input('>')
      move = move.lower().split()

    if 'journal' in move:                           ###INCOMPLETE
                            #MAKE TUTORIAL
      try:
        option=move[1].lower()
        if 'treasure' in option: player.treasureJournal()
        elif 'map' in option: player.mapJournal()
        else: print(red + '\nJournal section not found.\n')
      except:
          print('\nWhat section of the Journal you want to open?\n'+', '.join(journalOptions))
          option = input('>').lower()
          if 'treasure' in option: player.treasureJournal()
          elif 'map' in option: player.mapJournal()
          else: print('\nJournal closed...\n')

    elif 'map' in move and 'world' not in move:         ##### OPEN MAP
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

      # player.allies.append(Ally('Donald&Goofy', player))

      player.treasureInfo()

      # if bool(player.arenaRecords):
      #   for record in player.arenaRecords:
      #     print(arenaNames[record] + ' record: ' + player.arenaRecords[record])
      # else:
      #   print('There are no arena records!')

      print('\ntested!\n')
    
    elif 'upgrade' in move:                             ##### TEST 2 (story)

      # print(player.allies)

      player.story[player.world] += 1
      print('Story: ' + str(player.story[player.world]))

      print('\ntested!\n')
    
    elif 'treasure' in move:                            ##### TREASURE
      if 'treasure' in rooms[player.world][currentRoom]:
        count=0
        for number in player.treasures[player.world][currentRoom]:
          if number > player.story[player.world]: break
          if player.treasures[player.world][currentRoom][number]['status']=='closed':
            count+=1
            openTreasure(number, currentRoom)
        if count==0: print('There\'s no treasure chest in this room!')
      else:
        print('There\'s no treasure chest in this room!')

    elif 'menu' in move:                                ##### SHOW MENU
        player.menu()

    elif 'ability' in move or 'abilities' in move:      ##### EQUIP abilities
        player.equipAbilities()

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

    elif 'world' in move:                               ##### SAVE
      if 'Shop' in currentRoom or 'Save' in rooms[player.world][currentRoom]:
        print('Do you want to jump into the gummi ship and get to the world map?')
        answer = input('>')
        if 'yes' in answer.lower(): previousRoom = currentRoom = worldMap()
        else: print('Aborting...')
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
                if player.MP >= magics[move[1]]['MP']:
                  unlockCast = 'yes'
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
          previousRoom = currentRoom
          currentRoom = rooms[player.world][currentRoom][move[1]]
          addVisitedRoom(currentRoom)

          resetHeartless(currentRoom) ####

        #there is no door (link) to the new room
        elif move[1] == 'back':
            alreadyBattled = 0
            temp = currentRoom
            currentRoom = previousRoom
            previousRoom = temp

            resetHeartless(currentRoom) ####

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
              if player.story[player.world] == (people[currentRoom][person][storyToTalk[i]]['story']-1):
                player.story[player.world] += 1
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


    if 'boss' in rooms[player.world][currentRoom] and player.story[player.world] == (bosses[rooms[player.world][currentRoom]['boss']]['story']-1):           ###### BOSS BATTLE
      retryBoss = False
      bossScene(rooms[player.world][currentRoom]['boss'])
      result = battle(rooms[player.world][currentRoom]['boss'])
      if result == 'victory':
        player.story[player.world] += 1
      ###RESET HEARTLESS STATUS SO PLAYER WON'T FIGHT RIGHT AWAY
        if 'heartless' in rooms[player.world][currentRoom]:
          if player.story[player.world] > list(enemyLocations[player.world][currentRoom])[-1]:
            enemyLocations[player.world][currentRoom][-1]['status'] = 0
          elif player.story[player.world] < list(enemyLocations[player.world][currentRoom])[0]:
            pass
          else:
            for story in enemyLocations[player.world][currentRoom]:
              if story == player.story[player.world]:
                enemyLocations[player.world][currentRoom][story]['status'] = 0
                break
              else:
                if story > player.story[player.world]:
                  enemyLocations[player.world][currentRoom][previousStory]['status'] = 0
                  break
                else:
                  previousStory = story
      ###DEFEAT
      elif result == 'defeat':
          print("---------------------------")
          print('Your HP has dropped to zero!\nGAME OVER')
          result = gameOver()
          if result == '':
            retryBoss = True
          if result == 'run':
            temp = currentRoom
            currentRoom = previousRoom
            previousRoom = temp
            player.calculateHealth()
          if result == 'load':
            player.HP = player.TotalHP
            player.MP = player.TotalMP
            currentRoom = rooms[player.world][0]
            previousRoom = currentRoom
      player.calculateHealth()

    elif 'heartless' in rooms[player.world][currentRoom] and alreadyBattled == 0:           ###### BATTLE
      if player.story[player.world] > list(enemyLocations[player.world][currentRoom])[-1]:
        alreadyBattled, currentRoom, previousRoom = determineBattle(list(enemyLocations[player.world][currentRoom])[-1], currentRoom, previousRoom)
      elif player.story[player.world] < list(enemyLocations[player.world][currentRoom])[0]:
        pass
      else:
        for story in enemyLocations[player.world][currentRoom]:
          if story == player.story[player.world]:
            alreadyBattled, currentRoom, previousRoom = determineBattle(story, currentRoom, previousRoom)
            break
          else:
            if story > player.story[player.world]:
              alreadyBattled, currentRoom, previousRoom = determineBattle(previousStory, currentRoom, previousRoom)
              break
            else:
              previousStory = story


    # player wins if they get to the Third District
    if currentRoom == 'Third District' and  player.story[player.world] == 1:
      print('You found Donald & Goofy... YOU WIN!')
      break
