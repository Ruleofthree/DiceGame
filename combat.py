import json
import random
class Game:

    def __init__(self):
        self.pOneInfo = {}
        self.pTwoInfo = {}
        self.token = 0

    def combat(self):
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
        elif totalTwo > totalOne:
            print("Player Two Goes first")
            token = 2
            self.token = token
        elif totalOne == totalTwo:
            print("In result of tie, person with highest dexterity modifier goes first:")
            print("Player One's dexterity: " + str(playerOneMod))
            print("Player Two's dexterity: " + str(playerTwoMod))

            if playerOneMod > playerTwoMod:
                print("Player One Goes first")
                token = 1
                self.token = token
            elif playerOneMod < playerTwoMod:
                print("Player Two Goes first")
                token = 2
                self.token = token
            else:
                print("As both dexterity values are equal as well. A coin flip. Value of one means player one goes first")
                value = random.randint(1, 2)
                print(value)
                if value == 1:
                    print("Player One Goes first")
                    token = 1
                    self.token = token
                else:
                    print("Player Two Goes first")
                    token = 2
                    self.token = token


# game = Game()
# game.initative()


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