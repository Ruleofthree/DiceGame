import json
import random
class Game:

    def __init__(self):
        self.pOneInfo = {}
        self.pTwoInfo = {}
        self.token = 0
        self.damage = 0 initiative

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

    def getHitPointsPOne(self):
        # print(self.pOneInfo)
        pOneTotalHP = self.pOneInfo['hitpoints']
        pOneCurrentHP = self.pOneInfo['hitpoints']
        pOneCurrentHP = pOneCurrentHP - self.damage
        print("Player one: " + str(pOneCurrentHP) + "/" + str(pOneTotalHP))

    def getHitPointsPTwo(self):
        pTwoTotalHP = self.pOneInfo['hitpoints']
        pTwoCurrentHP = self.pTwoInfo['hitpoints']
        pTwoCurrentHP = pTwoCurrentHP - self.damage
        print("Player two: " + str(pTwoCurrentHP) + "/" + str(pTwoTotalHP))

    def determineHitPOne(self):
        pOneToHit = self.pOneInfo['hit']
        pTwoAC = self.pTwoInfo['ac']
        hit = random.randint(1, 20) + pOneToHit
        if hit > pTwoAC:
            print("Player one rolled a " + str(hit) + " to hit an AC " + str(pTwoAC) + " and was successful.")
            self.determineDamagePOne()
        else:
            print("Player one rolled a " + str(hit) + " to hit an AC " + str(pTwoAC) + " and missed.")
            self.test()

    def determineHitPTwo(self):
        pTwoToHit = self.pTwoInfo['hit']
        pOneAC = self.pOneInfo['ac']
        hit = random.randint(1, 20) + pTwoToHit
        if hit > pOneAC:
            print("Player one rolled a " + str(hit) + " to hit an AC " + str(pOneAC) + " and was successful.")
            self.determineDamagePOne()
        else:
            print("Player one rolled a " + str(hit) + " to hit an AC " + str(pOneAC) + " and missed.")
            self.test()

    def determineDamagePOne(self):
        pOneBaseDamage = self.pOneInfo['base damage']
        pOneModifier = self.pOneInfo['damage modifier']
        pOneMinimum, pOneMaximum = pOneBaseDamage.split('d')
        self.damage = random.randint(int(pOneMinimum), int(pOneMaximum)) + pOneModifier
        print("Player one did " + str(self.damage) + " points of damage.")

    def determineDamagePTwo(self):
        print(self.pTwoInfo)
        pTwoBaseDamage = self.pTwoInfo['base damage']
        pTwoModifier = self.pTwoInfo['damage modifier']
        pTwoMinimum, pTwoMaximum = pTwoBaseDamage.split('d')
        self.damage = random.randint(int(pTwoMinimum), int(pTwoMaximum)) + pTwoModifier
        print("player two did " + str(self.damage) + " points of damage.")

    def test(self):
        print("Am I here?")

game = Game()
game.initative()



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