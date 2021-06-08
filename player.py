class player:
    def __init__(self):
        self.HP = 5  ## full: ♥,  empty: ♡
        self.MaxHP = 5
        self.MP = 1  ## full: ●,  empty: ○
        self.MaxMP = 1

        self.magic = []
        self.item = []
        self.keyItems = []

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
        #print the current inventory
        print("HP : " + str(currentHP))
        print("MP : " + str(currentMP))
        print("Items :", self.item)
        #print an item if there is one
        print("---------------------------")