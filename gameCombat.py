import json
import random

class Combat:

    def __init__(self):
        self.pOneInfo = {}
        self.pTwoInfo = {}
        self.count = 0
        self.token = 0
        self.damage = 0
        self.pOneTotalHP = 0
        self.pTwoTotalHP = 0
        self.pOneCurrentHP = 0
        self.pTwoCurrentHP = 0

    def initiative(self):
        playerOne = input("Who is the challenger? ")
        charFile = open(playerOne + ".txt", "r", encoding="utf-8")
        pOneInfo = json.load(charFile)
        charFile.close()
        self.pOneInfo = pOneInfo
        playerTwo = input("And their opponent? ")
        charFile = open(playerTwo + ".txt", "r", encoding="utf-8")
        pTwoInfo = json.load(charFile)
        charFile.close()
        self.pTwoInfo = pTwoInfo
        self.pOneTotalHP = pOneInfo['hitpoints']
        self.pTwoTotalHP = pTwoInfo['hitpoints']
        self.pOneCurrentHP = pOneInfo['hitpoints']
        self.pTwoCurrentHP = pTwoInfo['hitpoints']
        playerOneInit = random.randint(1, 20)
        playerOneMod = int(pOneInfo['dexterity'] / 2)
        totalOne = playerOneInit + playerOneMod
        print("Player One rolled: " + str(playerOneInit) + " + " + str(playerOneMod) + " and got " + str(totalOne))

        playerTwoInit = random.randint(1, 20)
        playerTwoMod = int(pTwoInfo['dexterity'] / 2)
        totalTwo = playerTwoInit + playerTwoMod
        print("Player One rolled: " + str(playerTwoInit) + " + " + str(playerTwoMod) + " and got " + str(totalTwo))
        if totalOne > totalTwo:
            print("Player One Goes first")
            token = 1
            self.token = token
            self.determineHitPOne()
        elif totalTwo > totalOne:
            print("Player Two Goes first")
            token = 2
            self.token = token
            self.determineHitPTwo()
        elif totalOne == totalTwo:
            print("In result of tie, person with highest dexterity modifier goes first:")
            print("Player One's dexterity: " + str(playerOneMod))
            print("Player Two's dexterity: " + str(playerTwoMod))

            if playerOneMod > playerTwoMod:
                print("Player One Goes first")
                token = 1
                self.token = token
                self.determineHitPOne()
            elif playerOneMod < playerTwoMod:
                print("Player Two Goes first")
                token = 2
                self.token = token
                self.determineHitPTwo()
            else:
                print("As both dexterity values are equal as well. A coin flip. Value of one means player one goes first")
                value = random.randint(1, 2)
                print(value)
                if value == 1:
                    print("Player One Goes first")
                    token = 1
                    self.token = token
                    self.determineHitPOne()
                else:
                    print("Player Two Goes first")
                    token = 2
                    self.token = token
                    # self.determineHitPTwo()

    def determineHitPOne(self):
        pOneToHit = self.pOneInfo['hit']
        pTwoAC = self.pTwoInfo['ac']
        hit = random.randint(1, 20) + pOneToHit
        if hit > pTwoAC:
            print("Player One rolled a " + str(hit) + " to hit an AC " + str(pTwoAC) + " and was successful.")
            self.determineDamagePOne()
        else:
            print("Player One rolled a " + str(hit) + " to hit an AC " + str(pTwoAC) + " and missed.")
            self.scoreboard()

    def determineHitPTwo(self):
        pTwoToHit = self.pTwoInfo['hit']
        pOneAC = self.pOneInfo['ac']
        hit = random.randint(1, 20) + pTwoToHit
        if hit > pOneAC:
            print("Player Two rolled a " + str(hit) + " to hit an AC " + str(pOneAC) + " and was successful.")
            self.determineDamagePTwo()
        else:
            print("Player Two rolled a " + str(hit) + " to hit an AC " + str(pOneAC) + " and missed.")
            self.scoreboard()

    def determineDamagePOne(self):
        pOneBaseDamage = self.pOneInfo['base damage']
        pOneModifier = self.pOneInfo['damage modifier']
        pOneMinimum, pOneMaximum = pOneBaseDamage.split('d')
        self.damage = random.randint(int(pOneMinimum), int(pOneMaximum)) + pOneModifier
        print("Player One did " + str(self.damage) + " points of damage.")
        self.getHitPointsPTwo()

    def determineDamagePTwo(self):
        pTwoBaseDamage = self.pTwoInfo['base damage']
        pTwoModifier = self.pTwoInfo['damage modifier']
        pTwoMinimum, pTwoMaximum = pTwoBaseDamage.split('d')
        self.damage = random.randint(int(pTwoMinimum), int(pTwoMaximum)) + pTwoModifier
        print("player Two did " + str(self.damage) + " points of damage.")
        self.getHitPointsPOne()

    def getHitPointsPOne(self):
        self.pOneCurrentHP = self.pOneCurrentHP - self.damage
        self.token = 2
        self.scoreboard()

    def getHitPointsPTwo(self):
        self.pTwoCurrentHP = self.pTwoCurrentHP - self.damage
        self.token = 1
        self.scoreboard()

    def scoreboard(self):
        print("Player One: " + str(self.pOneCurrentHP) + "/" + str(self.pOneTotalHP) + "  ||  " + "Player Two: " + str(self.pTwoCurrentHP) + "/" + str(self.pTwoTotalHP))
        answer = input("Am I here? ").lower()
        if answer == "yes":
            self.combatRounds()
        else:
            return

    def combatRounds(self):
        print(self.pOneCurrentHP)
        print(self.pTwoCurrentHP)
        if self.pOneCurrentHP >= 0 and self.pTwoCurrentHP >= 0:
            if self.token == 1:
                self.count += 1
                self.determineHitPTwo()
            elif self.token == 2:
                self.count += 1
                self.determineHitPOne()
        elif self.pOneCurrentHP <= 0:
            print("Player Two Won in " + str(int(self.count / 2)) + " rounds")
        elif self.pTwoCurrentHP <= 0:
            print("player One Won in " + str(int(self.count / 2)) + " rounds")

# combat = Combat()
# combat.initiative()



    # def powerAttack(self):
    #     answer = input("How many points? ")
    #     print(self.list)
    #     self.list[5] = hit
    #     self.list[6] = damage
    #     print(hit)
    #     print(damage)
    #     hit = hit - answer
    #     damage = damage + answer
    #     print(hit)
    #     print(damage)
    #
    # def players(self):
    #     opponentOne = input("Who is the first opponent?").lower()
    #     charFile = open(opponentOne + ".txt", "r", encoding="utf-8")
    #     charStats = json.load(charFile)
    #     charFile.close()
    #     list = []
    #     for key in charStats:
    #         print(key)
    #         list.append(key)
    #     print(list)
    #     self.list = list