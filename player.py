from dictionaries.dictionaries import *
class player:
    def __init__(self):
        self.HP = 5  ## full: ♥,  empty: ♡
        self.MaxHP = 5
        self.MP = 1  ## full: ●,  empty: ○
        self.MaxMP = 1

        self.magic = []
        self.item = []
        self.keyItems = []
        self.munny = 0

        #STORY RELATED
        self.world = 'TraverseTown'
        self.map = str(wordMaps[self.world])
        self.story = 0

    def showBattleStatus(self):
        #print the player's current battle status
        currentHP = ''
        currentMP = ''
        i=0
        while i<self.MaxHP:
            if i<self.HP:
                currentHP += '♥'
            else:
                currentHP += '♡'
            i+=1
        i=0
        while i<self.MaxMP:
            if i<self.MP:
                currentMP += '●'
            else:
                currentMP += '○'
            i+=1
        
        print('\n---------------------------')
        print("HP : " + str(currentHP))
        print("MP : " + str(currentMP))
        print("Items :", self.item)
        print("---------------------------")

    def menu(self):
        self.showBattleStatus()
        print('Munny: ' + str(self.munny))
        print("Key items :", self.keyItems)
        # print('\nTo cast a magic spell just type \'cast [magic]\'')
        print('To use an item just type \'use [item]\'')
        print('To open the map of the current World just type \'map\'')
        print("---------------------------")