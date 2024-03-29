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

def tutorials(tutorialList):
  for tutorial in tutorialList:
    if player.tutorial[tutorial] == 0:
      print(Fore.YELLOW + "tutorial: " + Fore.WHITE + tutorialSpeech[tutorial])
      player.tutorial[tutorial] = 1

def newGame():  ############################################
  choose = ''
  giveUp = ''

  while choose == '':
    print('\nChoose well\n\n1- Power of the warrior (STR+1)\n2- Power of the mystic (MP+1)\n3- Power of the guardian (DEF+1)')
    choose = input('>')
    text='\nAnd what power do you give up in return?\n'


    if '1' in choose:
      text=text+'\n2- Power of the mystic (AP-1)\n3- Power of the guardian (DEF-1)'
      choose='1'
      print('\nThe power of the warrior.\nInvincible courage.\nA sword of terrible destruction.')

    elif '2' in choose:
      text=text+'\n1- Power of the warrior (STR-1)\n3- Power of the guardian (DEF-1)'
      choose='2'
      print('\nThe power of the mystic.\nInner strength.\nA staff of wonder and ruin.')

    elif '3' in choose:
      text=text+'\n1- Power of the warrior (STR-1)\n2- Power of the mystic (AP-1)'
      choose='3'
      print('\nThe power of the guardian.\nKindness to aid friends.\nA shield to repel all.')

    else:
      print('\nChoose one of the powers below')
      choose=''

    if '1' in choose or '2' in choose or '3' in choose:
      answer=input('\nIs this the power you choose?\n>')
      if answer.lower() == 'yes': break
      else: choose = ''

  while giveUp == '':
    print(text)
    giveUp = input('>')

    if '1' in giveUp and '1' not in choose:
      giveUp='1'
      print('\nThe power of the warrior.\nInvincible courage.\nA sword of terrible destruction.')

    elif '2' in giveUp and '2' not in choose:
      giveUp='2'
      print('\nThe power of the mystic.\nInner strength.\nA staff of wonder and ruin.')

    elif '3' in giveUp and '3' not in choose:
      giveUp='3'
      print('\nThe power of the guardian.\nKindness to aid friends.\nA shield to repel all.')

    else:
      print('\nChoose one of the powers below')
      giveUp = ''

    if '1' in giveUp or '2' in giveUp or '3' in giveUp:
      answer=input('\nIs this the power you want to give up?\n>')
      if answer.lower() == 'yes':
        print('\nYour path is set.')
        break
      else: giveUp = ''

  if choose == '1':
    player.path = 'SWORD'
    player.STR+=1
  elif choose == '2':
    player.path = 'ROD'
    player.MaxMP+=1
    player.MP+=1
    player.magicPower+=1
  elif choose == '3':
    player.path = 'SHIELD'
    player.DEF+=1

  if giveUp == '1': player.STR-=1
  elif giveUp == '2':
    player.MaxAP-=1
    player.AP-=1
  elif giveUp == '3': player.DEF-=1


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

def sincBook():
  numberOfPages = player.keyItems.count('Torn Page')
  if numberOfPages > 0 and 'one' not in rooms['100AcreWood']['Old Book']:
    rooms['100AcreWood']['Old Book']['one']='First Page'
    rooms['100AcreWood']['Old Book']['move'].append('one')
  if numberOfPages > 1 and 'two' not in rooms['100AcreWood']['Old Book']:
    rooms['100AcreWood']['Old Book']['two']='Second Page'
    rooms['100AcreWood']['Old Book']['move'].append('two')
  if numberOfPages > 2 and 'three' not in rooms['100AcreWood']['Old Book']:
    rooms['100AcreWood']['Old Book']['three']='Third Page'
    rooms['100AcreWood']['Old Book']['move'].append('three')
  if numberOfPages > 3 and 'four' not in rooms['100AcreWood']['Old Book']:
    rooms['100AcreWood']['Old Book']['four']='Fourth Page'
    rooms['100AcreWood']['Old Book']['move'].append('four')
  if numberOfPages > 4 and 'five' not in rooms['100AcreWood']['Old Book']:
    rooms['100AcreWood']['Old Book']['five']='Fifth Page'
    rooms['100AcreWood']['Old Book']['move'].append('five')

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
      tutorials(['save', 'quit'])
      if "Shop" in currentRoom:
        print('To get out of the shop type: \'leave\'')
  if 'treasure' in rooms[player.world][currentRoom]:
    count=0
    for number in player.treasures[player.world][currentRoom]:
      if number > player.story[player.world]: break
      if player.treasures[player.world][currentRoom][number]['status']=='closed': count+=1
    if count == 0: pass
    elif count == 1:
      print('🔸 You see a treasure chest!')
    elif count > 1:
      print('🔸 You see ' + str(count) + ' treasure chests!')
    tutorials(['treasure chest'])
  if 'book' in rooms[player.world][currentRoom]:
    sincBook()
  print()
  for x in rooms[player.world][currentRoom]['move']:
    if rooms[player.world][currentRoom][x] in player.visitedRooms[player.world]:
      print('➤ ' + x + ': ' + rooms[player.world][currentRoom][x])
    else: print('➤ ' + x + ': ???')
  print(Fore.RED + "---------------------------")
  tutorials(['traverse rooms'])

def openTreasure(number, currentRoom):
  if treasureList[player.world][currentRoom][number]['treasure'] == 'item':

    player.getItem(treasureList[player.world][currentRoom][number]['item'])

  elif treasureList[player.world][currentRoom][number]['treasure'] == 'key item':
    print('Obtained the ' + yellow + treasureList[player.world][currentRoom][number]['key item'] + white + ' key item!')
    player.keyItems.append(treasureList[player.world][currentRoom][number]['key item'])
    player.sortKeyItem()

  elif treasureList[player.world][currentRoom][number]['treasure'] == 'mapUpdate':
    if player.map[player.world][treasureList[player.world][currentRoom][number]['mapUpdate']] == 'no':
      player.map[player.world][treasureList[player.world][currentRoom][number]['mapUpdate']] = 'incomplete'
      print('Obtained ' + player.world + ' ' + treasureList[player.world][currentRoom][number]['mapUpdate'] + ' map!')
    elif player.map[player.world][treasureList[player.world][currentRoom][number]['mapUpdate']] == 'incomplete':
      player.map[player.world][treasureList[player.world][currentRoom][number]] = 'complete'
      print(player.world + ' ' + treasureList[player.world][currentRoom][number]['mapUpdate'] + ' map updated!')
    tutorials(['open map'])

  elif treasureList[player.world][currentRoom][number]['treasure'] == 'keyblade':
    print('Obtained the ' + cyan + treasureList[player.world][currentRoom][number]['keyblade'] + white + ' Keyblade!')
    player.keyblades.append(treasureList[player.world][currentRoom][number]['keyblade'])
    player.sortKeyblades()

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
          enemyLocations[player.world][room][list(enemyLocations[player.world][room])[-1]]['status'] = enemyLocations[player.world][room][list(enemyLocations[player.world][room])[-1]]['waves']
        elif player.story[player.world] < list(enemyLocations[player.world][room])[0]:
          pass
        else:
          for story in enemyLocations[player.world][room]:
            if story > player.story[player.world]:
              enemyLocations[player.world][room][previousStory]['status'] = enemyLocations[player.world][room][previousStory]['waves']
              break
            else:
              previousStory = story

def addToEnemiesList(enemyName):
  if enemyName in player.enemiesList: player.enemiesList[enemyName]+=1
  else: player.enemiesList[enemyName]=1

def levelUP():                                  ###LEVEL UP
  if levelUpStatsBonus[player.level] == 'HP':
    player.MaxHP += levelUpStatsDetails['HP']
    player.HP += levelUpStatsDetails['HP']
    print('Maximum HP increased!')
  elif levelUpStatsBonus[player.level] == 'MP':
    player.MaxMP += levelUpStatsDetails['MP']
    player.MP += levelUpStatsDetails['MP']
    print('Maximum MP increased!')
  elif levelUpStatsBonus[player.level] == 'STR':
    player.STR += levelUpStatsDetails['STR']
    print('Strength increased!')
  elif levelUpStatsBonus[player.level] == 'DEF':
    player.DEF += levelUpStatsDetails['DEF']
    print('Defense increased!')

  if levelUpBonus[player.path][player.level] == '': pass
  elif levelUpBonus[player.path][player.level] == 'item slot':
    player.itemPouch += levelUpStatsDetails['item slot']
  elif levelUpBonus[player.path][player.level] == 'equipment slot':
    player.equipmentNumber += levelUpStatsDetails['equipment slot']
  elif levelUpBonus[player.path][player.level] == 'MP':
    player.MaxMP += levelUpStatsDetails['MP']
    player.MP += levelUpStatsDetails['MP']
    print('Maximum MP increased!')
  else:
    player.abilities.append([levelUpBonus[player.path][player.level], False])
    player.sortAbilities()
    print('\nObtained ' + yellow + levelUpBonus[player.path][player.level] + '!')

def victoryMunny(enemyMunny):
  munny = 3 * random.randint(enemyMunny[0], enemyMunny[1])
  munny=math.ceil(munny+(player.abilities.count(['Jackpot', True])/5))
  print('\nYou defeated the Heartless!\nCONGRATULATIONS!')
  print('\nYou obtained ' + yellow + str(munny) + '🔸 munny!')
  player.munny += munny

def victoryExp(enemyEXP):
  expBoost=0
  if 'exp bracelet' in player.equipment: expBoost+=1
  if 'exp earring' in player.equipment: expBoost+=1
  expBoost+=player.abilities.count(['EXP Boost', True])
  expReceived=math.ceil(enemyEXP+(expBoost)*(enemyEXP)/5)
  print('You gained ' + str(expReceived) + ' exp!')
  player.exp+=expReceived
  while player.exp >= levelUpExp[player.level+1]:
    player.level+=1
    print('\nLevel Up!\nLevel: ' + str(player.level))
    levelUP()

def victoryDrop(enemyDrop):
  y=player.abilities.count(['Lucky Strike', True])
  drops={(x+(20*y)):enemyDrop[x] for x in enemyDrop}
  dropNumber = random.randint(1, 100)
  for drop in drops:
    if dropNumber <= drop:
      if drops[drop] in items:
        player.getItem(drops[drop])
      elif drops[drop] in keybladeStatus:
        player.keyblades.append(drops[drop])
        player.sortKeyblades()
        print('\nObtained the ' + cyan + drops[drop] + white + ' Keyblade!')
      break

def victoryMPRecover():
  recoverMPNumber = random.randint(1, 100)
  recoverMPNumberNeeded = 75-player.abilities.count(['MP Haste', True])
  recoverMP = math.ceil(player.TotalMP/5) + math.ceil((player.TotalMP-player.MP)*(player.abilities.count(['MP Rage', True]))/5)
  if recoverMPNumber > recoverMPNumberNeeded:
    print('\nYou recovered ' + blue + str(recoverMP) + ' ● ' + white + '!')
    player.MP += recoverMP
    if player.MP > player.TotalMP: player.MP = player.TotalMP

def useItem(item):                              ###USE ITEM
  if item in player.item:
    del player.item[player.item.index(item)]
  else:
    del player.stock[player.stock.index(item)]

  if player.autoStockEnabled and item in player.item:
    del player.autoPouch[player.autoPouch.index(item)]

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
  elif 'lixir' in item:
    print(items[item]['speech'][0] + green + items[item]['speech'][1] + white + items[item]['speech'][2] +  blue + items[item]['speech'][3] + white + items[item]['speech'][4])
  elif 'tent' in item:
    print(items[item]['speech'][0] + green + items[item ]['speech'][1] + white + items[item]['speech'][2])

  if items[item]['HP'] == 'full':
    player.HP = player.TotalHP
  else:
    player.HP = player.HP + items[item]['HP']
    if player.HP > player.TotalHP: player.HP = player.TotalHP

  if items[item]['MP'] == 'full':
    player.MP = player.TotalMP
  else:
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
  print('You attacked and unleashed a combo finisher!')
  if any(player.finishers):
    rand_idx = random.randrange(len(player.finishers))
    finish = player.finishers[rand_idx]
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
    elif finish == 'Hurricane Blast':
      print("You used " + yellow + "Hurricane Blast" + white + " and unleashed a powerfull attack!")
      damageDealt = math.ceil(random.randint(17,22)*damage/10)-enemy.defense
    elif finish == 'Discharge':
      if 'Kingdom' in player.keyblade:
        print("You used " + yellow + "Discharge" + white + "! It enhances your " + yellow + "defense" + white + " power!")
        defense += 1
        enemyDamageDealt-=1
        damageDealt = damage-enemy.defense
      elif 'Jungle King' in player.keyblade:
        print("You used " + green + "Discharge" + white + "! You restore " + red + '2 ♥'+ white + " !")
        player.HP+=2
        damageDealt = damage-enemy.defense
      elif 'Lady Luck' in player.keyblade:
        print("You used " + blue + "Discharge" + white + "! It significantly enhances your " + blue + "magical power" + white + "!")
        mPower+=2
        damageDealt = damage-enemy.defense
      elif 'Olympia' in player.keyblade:
        print("You used " + red + "Discharge" + white + "! You can now ignore enemy blocks!")
        damageDealt=damage-enemy.totalDefense
        player.ignoreBlock=True
      elif 'Three Wishes' in player.keyblade:
        print("You used " + red + "Discharge" + white + "! You can now ignore enemy blocks!")
        damageDealt=damage-enemy.totalDefense
        player.ignoreBlock=True
      elif 'Wishing Star' in player.keyblade:
        print("You used " + red + "Discharge" + white + "! It enhances your " + red + "attack power" + white + "!")
        damage+=1
        damageDealt = damage-enemy.defense
      elif 'Spellbinder' in player.keyblade:
        print("You used " + blue + "Discharge" + white + "! It significantly enhances your " + blue + "magical power" + white + "!")
        mPower+=2
        damageDealt = damage-enemy.defense
      elif 'Crabclaw' in player.keyblade:
        print("You used " + blue + "Discharge" + white + "! It enhances your " + blue + "magical power" + white + "!")
        mPower+=1
        damageDealt = damage-enemy.defense
      elif 'Pumpkinhead' in player.keyblade:
        print("You used " + red + "Discharge" + white + "! It enhances your " + red + "attack power" + white + "!")
        damage+=1
        damageDealt = damage-enemy.defense
      elif 'Metal Chocobo' in player.keyblade:
        print("You used " + red + "Discharge" + white + "! It significantly enhances your " + red + "attack power" + white + "!")
        damage+=2
        damageDealt = damage-enemy.defense
      elif 'Fairy Harp' in player.keyblade:
        print("You used " + blue + "Discharge" + white + "! It enhances your " + blue + "magical power" + white + "!")
        mPower+=1
        damageDealt = damage-enemy.defense
      elif 'Divine Rose' in player.keyblade:
        print("You used " + red + "Discharge" + white + "! It enhances your " + red + "attack power" + white + " and you can now ignore enemy blocks!")
        damage+=1
        damageDealt=damage-enemy.totalDefense
        player.ignoreBlock=True
      elif 'Oathkeeper' in player.keyblade:
        print("You used " + green + "Discharge" + white + "! It enhances your " + blue + "magical power" + white + " and also restore " + red + str(math.ceil(player.TotalMP/4)) + ' ♥'+ white + " !")
        player.HP += math.ceil(player.TotalMP/4) #Restore HP based on total MP
        mPower+=1
        damageDealt = damage-enemy.defense
      elif 'Oblivion' in player.keyblade:
        print("You used " + red + "Discharge" + white + "! It significantly enhances your " + red + "attack power" + white + " and enhances your " + blue + "magical power" + white + "!")
        damage+=2
        mPower+=1
        damageDealt = damage-enemy.defense
      elif 'Lionheart' in player.keyblade:
        print("You used " + yellow + "Discharge" + white + "! It enhances both your " + red + "attack power" + white + " and your " + blue + "magical power" + white + "!")
        damage+=1
        mPower+=1
        damageDealt = damage-enemy.defense
      elif 'Diamond Dust' in player.keyblade:
        print("You used " + blue + "Discharge" + white + "! It Greatly enhances your " + blue + "magical power" + white + " and also restore " + blue + str(math.ceil(player.TotalMP/4)) + ' ●'+ white + " !")
        player.MP += math.ceil(player.TotalMP/4)
        mPower+=3
        damageDealt = damage-enemy.defense
      elif 'One-Winged Angel' in player.keyblade:
        print("You used " + blue + "Discharge" + white + "! It dealt " + yellow + "triple" + white + " critical damage!")
        damageDealt = 3*damage-enemy.defense
      elif 'Ultima Weapon' in player.keyblade:
        print("You used " + green + "Discharge" + white + "! It restores " + red + '2 ♥'+ white + " and " + blue + "2 ●" + white +"!")
        player.HP += 2
        player.MP += 2
        damageDealt = damage-enemy.defense
      else:
        print("You used " + green + "Discharge" + white + "! It has no special effect.")
        damageDealt = damage-enemy.defense
    elif finish == 'Ripple Drive':
      print("You used " + blue + "Ripple Drive" + white + " and unleashes a great red orb of energy!")
      if enemy.magicImmunity: damageDealt=0
      else: damageDealt = math.ceil(damage/2)+mPower-enemy.magicResistance
    elif finish == 'Stun Impact':
      print('You used ' + red +'Stun Impact' + white + ' and it caused the enemy to be stunned!')
      enemyDamageDealt = 0
      damageDealt = damage-enemy.defense
    elif finish == 'Zantetsuken':
      print("You used " + yellow + "Zantetsuken" + white + " and dealt " + yellow + "double" + white + " damage!")
      damageDealt = 2*damage-enemy.defense
  else: damageDealt = damage+1-enemy.defense   ###PLAYER HAS NO FINISHER EQUIPPED

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

def comboModifiers(damage, enemy, enemyDamageDealt, enemySpeech):
  slapshotUsed=False
  if any(player.combo):
    rand_idx = random.randrange(len(player.combo))
    comboModifier = player.combo[rand_idx]
    del(player.combo[rand_idx])
    if comboModifier == 'Aerial Sweep':
      if player.ignoreBlock: damageDealt=math.ceil((1.2*damage)-enemy.totalDefense)
      else: damageDealt = math.ceil((1.2*damage)-enemy.defense)
      speech ='Sora hits the enemy 3 times in a quick spiral. You caused ' + red + str(damageDealt) + ' ♥ ' + white + 'of damage!'
    elif comboModifier == 'Slapshot':
      slapshotUsed=True
      name=enemy.name
      if enemy.bossBattle:  damageDealt=damage-bosses[name]['defense']
      else: damageDealt=damage-heartless[name]['defense']
      speech='Sora rapidly striked the enemy. You caused ' + red + str(damageDealt) + ' ♥ ' + white + 'of damage!'
    elif comboModifier == 'Sliding Dash':
      print()
    elif comboModifier == 'Vortex':
      if player.ignoreBlock: damageDealt=damage-enemy.totalDefense
      else: damageDealt = (damage-enemy.defense)
      if 'attacks you' in enemySpeech and random.randint(1, 100)>60:
        enemySpeech=enemySpeech.replace(str(enemyDamageDealt)+' ♥', '0 ♥')
        enemyDamageDealt=0
        speech='Sora striked in a vortex slash parrying the enemy attack. You caused ' + red + str(damageDealt) + ' ♥ ' + white + 'of damage!'
      else:
        speech='Sora striked in a vortex slash. You caused ' + red + str(damageDealt) + ' ♥ ' + white + 'of damage!'
  else:
    if player.ignoreBlock: damageDealt=damage-enemy.totalDefense
    else: damageDealt = (damage-enemy.defense)
    speech='You attacked and caused ' + red + str(damageDealt) + ' ♥ ' + white + 'of damage!'

  if damageDealt < 0:
    speech=speech.replace(str(damageDealt),red+'0')
    damageDealt=0
  print(speech)

  return damageDealt, enemyDamageDealt, enemySpeech, slapshotUsed

def calculateEnemyDamage(bossBattle, enemy, defense):
  if bossBattle == False: enemySpeech, enemyDamageDealt = enemy.selectCommand(defense)
  else: enemySpeech, enemyDamageDealt = enemy.selectCommandBoss(defense)
  return enemySpeech, enemyDamageDealt

def inflictEnemyDamage(enemySpeech, enemyDamageDealt, mPower, enemy, command='', damageDealt=0):

  if command == 'Trinity Limit':
    enemySpeech=enemySpeech.replace('You lost ' + str(damageDealt) + ' ♥','The enemy is lightstruck and causes no damage!')
    enemyDamageDealt=0
  else:
    if enemy.statusEffect != 'none': enemySpeech, enemyDamageDealt = enemy.statusEffectDamageReduction(enemySpeech, enemyDamageDealt, mPower)
    if enemy.aeroEffect != 'none': enemySpeech, enemyDamageDealt = enemy.statusEffectDamageReduction(enemySpeech, enemyDamageDealt, mPower, aero=True)
    if enemy.stopEffect and 'stop' in command[1]: enemySpeech, enemyDamageDealt = enemy.stopped()
  print(enemySpeech)
  player.HP -= enemyDamageDealt
  if ['Second Chance', True] in player.abilities and player.HP<1 and player.HP+enemyDamageDealt>1:
    player.HP=1
    print(green +'Second Chance' + white)

def alliesHelp(enemy):
  for ally in player.allies:
    helpType, helpValue, helpStatus, text = ally.selectCommand(player)
    if helpType == '': pass
    elif helpType == 'heal':
      player.HP = player.HP + helpValue
      print(text)
    else:
      value=helpValue-enemy.defense
      if value<0: value=0
      enemy.HP = enemy.HP - value
      text=text.replace(str(helpValue), str(value))
      print(text)
    if helpStatus != '':
      enemy.statusEffect = helpStatus
      enemy.statusDuration = magics[helpStatus]['status']['duration']

def battle(enemyName, arenaBattle=False):       ###BATTLE
    player.createBKP()
    if enemyName in bosses: bossBattle = True
    elif enemyName in heartless:  bossBattle = False

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
    player.combo=copy.copy(player.comboModifiers)
    command = ''

    while True:
      player.showBattleStatus()
      enemy.damage = enemy.totalDamage
      slapshotUsed=False
      if ['Berserk', True] in player.abilities and player.HPBarColour == 'RED': damage=damageBase+2
      else: damage=damageBase
      if ['Scan', True] in player.abilities:  scan(enemy)
      battleCommands(commandOptions, usingAbility, activeAbilityCount)
      # print(enemy.stopEffect, enemy.stopDuration)
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
  ### Calculate enemy damage
        enemySpeech, enemyDamageDealt = calculateEnemyDamage(bossBattle, enemy, defense)
  ### Allies Help
        if player.allies: alliesHelp(enemy)

        if player.HP > player.TotalHP: player.HP = player.TotalHP
###ATTACK
      elif command == 'attack':       ###ATTACK
          command = ''
  ### Calculate enemy damage
          enemySpeech, enemyDamageDealt = calculateEnemyDamage(bossBattle, enemy, defense)
          if enemy.statusEffect == 'gravity': enemy.defense=enemy.defense-(mPower+1)
  ### Finishers
          if finishCount == 3:
            damage, defense, mPower, enemyDamageDealt, damageDealt = finishAttack(enemy, damage, defense, mPower, enemyDamageDealt)
            finishCount = 0
            if finishingPlusCheck: finishingPlusCheck=False
            else: finishingPlusCheck=True
          elif ['Negative Combo', True] in player.abilities and finishCount == 2:
            damage, defense, mPower, enemyDamageDealt, damageDealt = finishAttack(enemy, damage, defense, mPower, enemyDamageDealt)
            finishCount = 0
            if finishingPlusCheck: finishingPlusCheck=False
            else: finishingPlusCheck=True
          elif ['Finishing Plus', True] in player.abilities and finishingPlusCheck:
            damage, defense, mPower, enemyDamageDealt, damageDealt = finishAttack(enemy, damage, defense, mPower, enemyDamageDealt)
            finishCount = 0
            finishingPlusCheck=False
          else:
            finishCount += 1
            if finishCount == 1:  player.combo=copy.copy(player.comboModifiers)
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

              if player.ignoreBlock: damageDealt=damage-enemy.totalDefense
              else: damageDealt = (damage-enemy.defense)
              if damageDealt < 0: damageDealt=0
              print('You attacked and caused ' + red + str(damageDealt) + ' ♥ ' + white + 'of damage!')

        #Normal attack + Combo Modifier
            else: damageDealt, enemyDamageDealt, enemySpeech, slapshotUsed = comboModifiers(damage, enemy, enemyDamageDealt, enemySpeech)
          enemy.HP = enemy.HP - damageDealt
          player.blocked=False

          if damageDealt==0:
            finishCount = 0
            finishingPlusCheck=False
            if enemySpeech == 'The enemy tries to block all incoming phisical attacks!':
              player.blocked=True

  ### Inflict enemy damage
          inflictEnemyDamage(enemySpeech, enemyDamageDealt, mPower, enemy)
  ### Status effect damage
          if 'fir' in enemy.statusEffect:
            enemy.statusEffectDamage()
  ### Allies Help
          if player.allies: alliesHelp(enemy)
          if player.HP > player.TotalHP: player.HP = player.TotalHP

          usingAbility = ''
###MAGIC
      elif "magic" in command:       ###MAGIC
        command = command.lower().split()
  ###Check magic requirements
        if not player.magic:  print('Magic is still a mystery to you!')
        else:
          if command[1] in player.magic:
            if player.MP >= magics[command[1]]['MP']:

  ### Calculate enemy damage
              enemySpeech, enemyDamageDealt = calculateEnemyDamage(bossBattle, enemy, defense)

            #Combo finisher
              if ['Combo Master', True] not in player.abilities or finishCount == 3:
                finishCount = 0
              finishingPlusCheck=False
              player.blocked=False

  ###COLOR SPEECH
              magicText = magics[command[1]]['speech']
              print('You used ' + blue + str(magics[command[1]]['MP']) +' ● ' + white + '!')
              if 'cur' not in command[1] and 'grav' not in command[1] and 'aer' not in command[1] and 'stop' not in command[1] and not enemy.magicImmunity:
                magicDamage = mPower+magics[command[1]]['damage']-enemy.magicResistance
                if magicDamage<0: magicDamage=0
                print("You cast " + player.colors[magicText[4]] + command[1].capitalize() + white + " and deal " + red + str(magicDamage) + magicText[1] + white + magicText[2] + player.colors[magicText[4]] + magicText[3])
              elif 'grav' in command[1] and not enemy.magicImmunity:
                magicDamage = mPower+math.ceil(enemy.MaxHP/5)-enemy.magicResistance
                if magicDamage<0: magicDamage=0
                print("You cast " + player.colors[magicText[4]] + command[1].capitalize() + white + " and deal " + red + str(magicDamage) + magicText[1] + white + magicText[2] + player.colors[magicText[4]] + magicText[3])
              elif 'aer' in command[1]:
                magicDamage=0
                print("You cast " + blue + command[1].capitalize() + white + " and it reduces the damage taken!")
              elif 'stop' in command[1] and enemy.magicImmunity==False and not enemy.stopImmunity:
                magicDamage=0
                print("You cast " + yellow + command[1].capitalize() + white + " and the enemy suddenly stops moving!")
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
              if 'aer' in command[1]:
                enemy.aeroEffect = command[1]
                enemy.aeroDuration = magics[command[1]]['status']['duration']
              elif 'stop' in command[1] and not enemy.magicImmunity and not enemy.stopImmunity:
                enemy.stopEffect = True
                enemy.stopDuration = magics[command[1]]['status']['duration']
              elif 'cur' not in command[1] and not enemy.magicImmunity:
                enemy.statusEffect = command[1]
                enemy.statusDuration = magics[command[1]]['status']['duration']

  ### Inflict enemy damage
              inflictEnemyDamage(enemySpeech, enemyDamageDealt, mPower, enemy)
  ### Status effect damage
              if 'fir' in enemy.statusEffect:
                enemy.statusEffectDamage()
  ### Allies Help
              if player.allies: alliesHelp(enemy)
              if player.HP > player.TotalHP: player.HP = player.TotalHP
  ###
            else:
              print('Not enough MP!')
          else:
            print('Magic not found!')

        command = ''
        usingAbility = ''
###ITEM
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
              enemySpeech, enemyDamageDealt = calculateEnemyDamage(bossBattle, enemy, defense)
  ### Inflict enemy damage
              inflictEnemyDamage(enemySpeech, enemyDamageDealt, mPower, enemy)
  ### Allies Help
              if player.allies: alliesHelp(enemy)
              if player.HP > player.TotalHP: player.HP = player.TotalHP
  ###
            else:
              print("You don\'t have any ", command[1])
          except IndexError:
              print('try: item [item name]')

        command = ''
        usingAbility = ''

###ACTIVE ABILITY
      elif command in activeAbilitiesSimple or command in activeAbilitiesCommands:       ###ACTIVE ABILITY
        command = command.lower()
        if ' ' in command:  command = command.split()[0]

  ###Check ability requirements
        if not player.activeAbilities:
          print('You don\'t have any active ability equipped!')
        else:
          try: command = [x for x in activeAbilitiesList if command.capitalize() in x][0] #identify ability
          except: command = [x for x in activeAbilitiesList if command in activeAbilities[x]['commands']][0] #identify ability

          if command in player.activeAbilities:
            if player.MP >= activeAbilities[command]['MP'] or command==usingAbility:
              ability = activeAbilities[command]

  ### Calculate enemy damage
              enemySpeech, enemyDamageDealt = calculateEnemyDamage(bossBattle, enemy, defense)
              if enemy.statusEffect == 'gravity': enemy.defense=enemy.defense-(mPower+1)
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
                print(yellow + usingAbility + white + activeAbilities[usingAbility]['speech'][abilityDamageName][0] + red + str(abilityDamage) + ' ♥' + white + ' of damage!' + activeAbilities[usingAbility]['speech'][abilityDamageName][1])
              elif usingAbility != 'Trinity Limit':
                abilityDamage = damage+ability[abilityDamageName]-enemy.defense
                if abilityDamage<0: abilityDamage=0
                print(yellow + usingAbility + white + activeAbilities[usingAbility]['speech'][abilityDamageName][0] + red + str(abilityDamage) + ' ♥' + white + ' of damage!' + activeAbilities[usingAbility]['speech'][abilityDamageName][1])
              else:
                abilityDamage = mPower+ability[abilityDamageName]-enemy.magicResistance
                if abilityDamage<0: abilityDamage=0
                print(yellow + usingAbility + white + activeAbilities[usingAbility]['speech'][abilityDamageName][0] + red + str(abilityDamage) + ' ♥' + white + ' of damage!' + activeAbilities[usingAbility]['speech'][abilityDamageName][1])
              if activeAbilityCount == 0: usingAbility=''
  ###Calculate damage
              enemy.HP = enemy.HP - abilityDamage
  ### Inflict enemy damage
              inflictEnemyDamage(enemySpeech, enemyDamageDealt, mPower, enemy, command, abilityDamage)
  ### Status effect damage
              if 'fir' in enemy.statusEffect:
                enemy.statusEffectDamage()
  ### Allies Help
              if player.allies: alliesHelp(enemy)
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
          player.reAutoStock()
          return 'run'
###ERROR
      else:       ###ERROR
        command = ''
        print('Command not found!')
###DEFEAT
      if player.HP < 1:       ###DEFEAT
        if slapshotUsed and enemy.HP <= 0:  pass
        else: return 'defeat'
###VICTORY
      if enemy.HP <= 0:       ###VICTORY
        addToEnemiesList(enemyName)
        if not arenaBattle:
          victoryMunny(enemy.munny)
          victoryExp(enemy.exp)
          victoryDrop(enemy.drop)
        victoryMPRecover()
        player.reAutoStock()
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

def arenaGameOver(practice=False):                            ###ARENA GAME OVER
  if practice: print('\n\nKINGDOM HEARTS🤍\n\Practice Arena\nretry?\ncontinue?\n\n')
  else: print('\n\nKINGDOM HEARTS🤍\n\nColiseum Arena\nretry?\ncontinue?\n\n')
  command = ''
  while True:
    player.restoreArenaBKP()
    command = input('>').lower()
    if 'retry' in command: return 'retry'
    elif 'continue' in command: return 'continue'
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
          return currentRoom, previousRoom
        if result == 'defeat':
          print("---------------------------")
          print('Your HP has dropped to zero!\nGAME OVER')
          result = gameOver()
        if result == 'run':
          temp = currentRoom
          currentRoom = previousRoom
          previousRoom = temp
          player.calculateHealth()
          return currentRoom, previousRoom
        if result == 'load':
          player.HP = player.TotalHP
          player.MP = player.TotalMP
          return rooms[player.world][0], rooms[player.world][0]
    else: return currentRoom, previousRoom
  
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
          if result == 'continue':
            return

    if retry == False:
      print('\n-----------------------\n\nCongratulations!!')
      trophy = arenaNames[arenaNumber] +' Trophy'
      player.arenaRecords[arenaNumber] = 'Complete'

      ##Already completed the arena before
      if (trophy) in player.keyItems:
        player.getItem(arenaRewards[arenaNumber][2])

      ##First time completing the arena
      else:
        rewards = arenaRewards[arenaNumber][1]
        player.keyItems.append(trophy)
        player.sortKeyItem()
        print('You obtained the ' + trophy + '!\n')

        if 'keyblade' in rewards:
          player.keyblades.append(arenaRewards[arenaNumber]['keyblade'])
          player.sortKeyblades()
          print('You got the ' + cyan + arenaRewards[arenaNumber]['keyblade'] + white + ' Keyblade!')
        if 'magic' in rewards:
          magicName = arenaRewards[arenaNumber]['magic']
          player.magic.append(arenaRewards[arenaNumber]['magic'])
          player.sortMagic()
          print('You learned the ' + player.colors[magics[magicName]['speech'][4]] + magicName + white + ' spell!')
        if 'ability' in rewards:
          abilityName = arenaRewards[arenaNumber]['ability']
          player.abilities.append([abilityName, False])
          player.sortAbilities()
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

def practice(enemyName):
  while True:
    retry = False
    player.createArenaBKP()

    result = battle(enemyName, arenaBattle=True)
    if result == 'victory':
      print(green +'\nEnemy defeated!\n' + white)
      player.restoreArenaBKP()
    elif result == 'defeat':
        
      print("---------------------------")
      print('Your HP has dropped to zero!\nYou were defeated')

      result = arenaGameOver(practice=True)
      if result == 'retry':
        retry = True
        break
      if result == 'continue':
        return

    if retry == False:  break

def selectPractice():
  while True:
    print('\nRoxas: Who do you want to practice against?\n(type the name of the enemy you wish to face. 0 or \'nevermind\' to leave)')
    i=0
    for enemy in player.enemiesList:
      tab=''
      for _ in range(30-len(enemy)):   tab=tab+' '
      print('\n' + str(i+1) + '. ' + Fore.LIGHTRED_EX + enemy.capitalize())
      i+=1

    answer = input('>')
    answer = answer.lower()
    if answer == '0' or answer == 'nevermind':
      print('\nRoxas: Okay, see ya next time.')
      break
    elif answer in player.enemiesList:
      print('\nRoxas: Very well, good luck!')
      practice(answer)
      break
    else: print('\nEnemy not found!')


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

  retryBoss = False
  previousStory = 0
  currentRoom = player.currentRoom
  previousRoom = currentRoom
#
  if currentRoom == 'Snow White\'s Stained Glass': newGame()

  while True:

    if ('boss' in rooms[player.world][currentRoom] and player.story[player.world] == (bosses[rooms[player.world][currentRoom]['boss']]['story']-1)) or retryBoss:           ###### BOSS BATTLE
      retryBoss = False
      bossScene(rooms[player.world][currentRoom]['boss'])
      result = battle(rooms[player.world][currentRoom]['boss'])
      if result == 'victory':
        player.story[player.world] += 1
      ###RESET HEARTLESS STATUS SO PLAYER WON'T FIGHT RIGHT AWAY
        if 'heartless' in rooms[player.world][currentRoom]:
          if player.story[player.world] > list(enemyLocations[player.world][currentRoom])[-1]:
            enemyLocations[player.world][currentRoom][list(enemyLocations[player.world][currentRoom])[-1]]['status'] = 0
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

    elif 'heartless' in rooms[player.world][currentRoom]:           ###### BATTLE
      if player.story[player.world] > list(enemyLocations[player.world][currentRoom])[-1]:
        currentRoom, previousRoom = determineBattle(list(enemyLocations[player.world][currentRoom])[-1], currentRoom, previousRoom)
      elif player.story[player.world] < list(enemyLocations[player.world][currentRoom])[0]:
        pass
      else:
        for story in enemyLocations[player.world][currentRoom]:
          if story == player.story[player.world]:
            currentRoom, previousRoom = determineBattle(story, currentRoom, previousRoom)
            break
          else:
            if story > player.story[player.world]:
              currentRoom, previousRoom = determineBattle(previousStory, currentRoom, previousRoom)
              break
            else:
              previousStory = story


    showStatus()
                             
    move = ''                                     ##### INPUT READER
    while move == '':  
      move = input('>')
    move = move.lower().split()

    if 'journal' in move:                           ###INCOMPLETE
                            #MAKE TUTORIAL
      try:
        option=move[1].lower()
        if 'treasure' in option: player.treasureJournal()
        elif 'map' in option: player.mapJournal()
        elif 'enem' in option: player.enemiesJournal()
        else: print(red + '\nJournal section not found.\n')
      except:
          print('\nWhat section of the Journal you want to open?\n'+', '.join(journalOptions))
          option = input('>').lower()
          if 'treasure' in option: player.treasureJournal()
          elif 'map' in option: player.mapJournal()
          elif 'enem' in option: player.enemiesJournal()
          else: print('\nJournal closed...\n')

    elif 'map' in move and 'world' not in move and 'journal' not in move:         ##### OPEN MAP
      tutorials(['open map'])
      
      print('Opening map...\n')
      from PIL import Image
      mapNumber = rooms[player.world][currentRoom]['map number']
      if player.map[player.world][mapNumber] == 'no':
        print(red +'You have no map of this area!' + white)
      else:
        img = Image.open('images/' + player.world + '/Map' + maps[player.world][mapNumber][player.map[player.world][mapNumber]] + '.jpg')
        img.show()

    elif 'test' in move:                                ##### TEST

      print(player.story['CastleOblivion'])

      print('\ntested!\n')

    elif 'transport' in move:                                ##### TEST

      player.world = 'TraverseTown'
      player.currentRoom= 'Mystical House'
      currentRoom='Mystical House'

      print('\ntransported!\n')
    
    elif 'upgrade' in move:                             ##### TEST 2 (story)

      # player.keyItems.append('Coliseum Shop location')

      print('\nnothing!\n')
    
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

    elif 'abilit' in move:                              ##### EQUIP abilities
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
                player.getItem(move[1])
              else:
                player.equipmentList.append(move[1])
                player.sortEquipmentList()
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
              if move[1] in player.item or move[1] in player.stock:
                useItem(move[1])
                if player.autoStockEnabled: player.reAutoStock()
              else:
                print("You don\'t have any ", move[1])
          except IndexError:
              print('try: use [item]')
          command = ''

    elif 'item' in move:
      player.equipItems()

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
          previousRoom = currentRoom
          currentRoom = rooms[player.world][currentRoom][move[1]]
          addVisitedRoom(currentRoom)
          resetHeartless(currentRoom) ####

        #there is no door (link) to the new room
        elif move[1] == 'back':
            temp = currentRoom
            currentRoom = previousRoom
            previousRoom = temp
            resetHeartless(currentRoom) ####

        else:
          if retryBoss == False:
            print('You can\'t go that way!')

    elif move[0] == 'talk' :                            ##### TALK WITH PERSON
      #if the room contains a person
      
      if "person" in rooms[player.world][currentRoom]:
        peopleToTalk, storyToTalk = verifyPersonStory(rooms[player.world][currentRoom]['person'])

        if move[1].capitalize() in peopleToTalk:
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
                tutorials(['open map'])
              elif reward == 'keyblade':
                player.keyblades.append(people[currentRoom][person][storyToTalk[i]]['keyblade'])
                player.sortKeyblades()
                print('You got the ' + cyan + people[currentRoom][person][storyToTalk[i]]['keyblade'] + white + ' Keyblade!')
              elif reward == 'key item':
                player.keyItems.append(people[currentRoom][person][storyToTalk[i]]['key item'])
                player.sortKeyItem()
                print('You got the "' + people[currentRoom][person][storyToTalk[i]]['key item'] + '" key item!')
              elif reward == 'item':
                player.getItem(people[currentRoom][person][storyToTalk[i]]['item'])
              elif reward == 'arena':
                selectArena()

              elif reward == 'practice':
                selectPractice()

              # elif reward == 'transport':
              #   print(event['transport speech'])

              if reward != 'arena' and reward != 'practice':
                people[currentRoom][person][storyToTalk[i]]['reward'] = 'no'

              if 'Moogle' in rooms[player.world][currentRoom]['person']:
                  shop(currentRoom)

            i+=1

        else: print('Can\'t talk to ' + move[1] + '!')
      else: print('There\'s no one to talk here!')

