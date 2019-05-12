import json
import random

class Combat:

    def __init__(self):
        self.playerOne = ""
        self.playerTwo = ""
        self.winner = ""
        self.pOneInfo = {}
        self.pTwoInfo = {}
        self.count = 0
        self.token = 0
        self.damage = 0
        self.pOneTotalHP = 0
        self.pTwoTotalHP = 0
        self.pOneCurrentHP = 0
        self.pTwoCurrentHP = 0
        self.pOneLevel = 0
        self.pTwoLevel = 0
        self.xp = 0
        self.currentPlayerXP = 0
        self.nextLevel = 0
        self.levelUp = 0

    # method dedicated to determining who goes first in combat. Simulates a roll of a 20-sided die (1-20), then adds
    # character's dexterity modifier (dexterity score divided by 2). In the event of a tie, determines who goes first
    # by finding the highest dexterity modifier between opponents. Should THAT tie as well, does a coin flip.

    def initiative(self):
        self.playerOne = input("Who is the challenger? ")
        # opens and loads in player one's character sheet. This is done in this method solely because I'm unsure if
        # loading json files in __init__ is actually a good idea. If I understand things correctly, things in a class's
        # __init__ is ran EVERY TIME a method is called within it. If so, then the json files would be opened, loaded,
        # and closed multiple times in a single run. Seems inefficient, and bad coding.
        charFile = open(self.playerOne + ".txt", "r", encoding="utf-8")
        pOneInfo = json.load(charFile)
        charFile.close()
        self.pOneInfo = pOneInfo
        self.playerTwo = input("And their opponent? ")
        # does same for character sheet of player two.
        charFile = open(self.playerTwo + ".txt", "r", encoding="utf-8")
        pTwoInfo = json.load(charFile)
        charFile.close()
        self.pTwoInfo = pTwoInfo
        # I feel this is a terrible place to define the blow assignments, as hit points have nothing to do with initiative
        # but want to get all relevant data in to __init__ for ease of use, without opening, loading, and closing jsons
        # in the __init__ file itself.
        self.pOneTotalHP = pOneInfo['hitpoints']
        self.pTwoTotalHP = pTwoInfo['hitpoints']
        self.pOneCurrentHP = pOneInfo['hitpoints']
        self.pTwoCurrentHP = pTwoInfo['hitpoints']
        self.pOneLevel = pOneInfo['level']
        self.pTwoLevel = pTwoInfo['level']
        playerOneInit = random.randint(1, 20)
        playerOneMod = int(pOneInfo['dexterity'] / 2)
        totalOne = playerOneInit + playerOneMod
        print(self.playerOne +" rolled: " + str(playerOneInit) + " + " + str(playerOneMod) + " and got " + str(totalOne))

        playerTwoInit = random.randint(1, 20)
        playerTwoMod = int(pTwoInfo['dexterity'] / 2)
        totalTwo = playerTwoInit + playerTwoMod
        print(self.playerTwo + " rolled: " + str(playerTwoInit) + " + " + str(playerTwoMod) + " and got " + str(totalTwo))
        if totalOne > totalTwo:
            print(self.playerOne + " Goes first")
            token = 1
            self.token = token
            #self.determineHitPOne()
        elif totalTwo > totalOne:
            print(self.playerTwo + " Goes first")
            token = 2
            self.token = token
            #self.determineHitPTwo()
        elif totalOne == totalTwo:
            print("In result of tie, person with highest dexterity modifier goes first:")
            print(self.playerOne + "'s dexterity: " + str(playerOneMod))
            print(self.playerTwo + "'s dexterity: " + str(playerTwoMod))

            if playerOneMod > playerTwoMod:
                print(self.playerOne + " Goes first")
                token = 1
                self.token = token
                #self.determineHitPOne()
            elif playerOneMod < playerTwoMod:
                print(self.playerTwo + " Goes first")
                token = 2
                self.token = token
                #self.determineHitPTwo()
            else:
                print("As both dexterity values are equal as well. A coin flip. Value of one means " + self.playerOne +  " goes first")
                value = random.randint(1, 2)
                print(value)
                if value == 1:
                    print(self.playerOne + " Goes first")
                    token = 1
                    self.token = token
                    #self.determineHitPOne()
                else:
                    print(self.playerTwo + " Goes first")
                    token = 2
                    self.token = token
                    #self.determineHitPTwo()

    # Next two methods are created to see if a character hit the other character or not. Simulates rolling 1d20 (1-20)
    # then adding any modifiers to the result. If the total either meets or exceeds the other players AC, notify the
    # players that the hit was successful, then move on to the damage methods. If the total does not, notify player
    # that it was a miss, and move on to other player's turn.
    # Note: I want to add in a result that will double damage if the ROLL is a 20, not the total.

    def determineHitPOne(self):
        pOneToHit = self.pOneInfo['hit']
        pTwoAC = self.pTwoInfo['ac']
        hit = random.randint(1, 20) + pOneToHit
        if hit >= pTwoAC:
            print(self.playerOne + " rolled a " + str(hit) + " to hit an AC " + str(pTwoAC) + " and was successful.")
            self.determineDamagePOne()
        else:
            print(self.playerTwo + " rolled a " + str(hit) + " to hit an AC " + str(pTwoAC) + " and missed.")
            self.scoreboard()

    def determineHitPTwo(self):
        pTwoToHit = self.pTwoInfo['hit']
        pOneAC = self.pOneInfo['ac']
        hit = random.randint(1, 20) + pTwoToHit
        if hit >= pOneAC:
            print(self.playerTwo + " rolled a " + str(hit) + " to hit an AC " + str(pOneAC) + " and was successful.")
            self.determineDamagePTwo()
        else:
            print(self.playerTwo + " rolled a " + str(hit) + " to hit an AC " + str(pOneAC) + " and missed.")
            self.scoreboard()

    # Next two methods will determine how much damage is done after a successful hit. It finds the value placed in the
    # 'base damage' key of the character's json, Parses it out to remove the 'd', and uses the first number as the
    # minimum range, and second for the maximum. After determining the random value, then adds any modifiers to the roll
    # and displays that as the damage.
    # Note: Want to add in capabilities to double the ROLL of the damage only, should the player have rolled a 'natural
    # 20' to hit (value of 20 before any modifiers were added)

    def determineDamagePOne(self):
        pOneBaseDamage = self.pOneInfo['base damage']
        pOneModifier = self.pOneInfo['damage modifier']
        pOneMinimum, pOneMaximum = pOneBaseDamage.split('d')
        self.damage = random.randint(int(pOneMinimum), int(pOneMaximum)) + pOneModifier
        print(self.playerOne + " did " + str(self.damage) + " points of damage.")
        self.getHitPointsPTwo()

    def determineDamagePTwo(self):
        pTwoBaseDamage = self.pTwoInfo['base damage']
        pTwoModifier = self.pTwoInfo['damage modifier']
        pTwoMinimum, pTwoMaximum = pTwoBaseDamage.split('d')
        self.damage = random.randint(int(pTwoMinimum), int(pTwoMaximum)) + pTwoModifier
        print(self.playerTwo + " did " + str(self.damage) + " points of damage.")
        self.getHitPointsPOne()

    # Two methods to update hit points as the fight progresses along.

    def getHitPointsPOne(self):
        self.pOneCurrentHP = self.pOneCurrentHP - self.damage
        self.token = 2
        self.scoreboard()

    def getHitPointsPTwo(self):
        self.pTwoCurrentHP = self.pTwoCurrentHP - self.damage
        self.token = 1
        self.scoreboard()

    # Creates the scoreboard to display to players after every turn. The if statement is placed here as a break, to
    # not allow the program to run test runs in one fluid motion. However, I believe this will be the place to obtain
    # player input on if they want to use any special feats they have - such as evasion to halve damage taken, and so on
    # Believe that each feat requiring extra variables will require methods of their own. Unsure of how to go about that yet.

    def scoreboard(self):
        print(self.playerOne + ": " + str(self.pOneCurrentHP) + "/" + str(self.pOneTotalHP) + "  ||  " + self.playerTwo + ": " + str(self.pTwoCurrentHP) + "/" + str(self.pTwoTotalHP))
        answer = input("Am I here? ").lower()
        if answer == "yes":
            self.combatRounds()
        else:
            return

    # the 'meat and potatoes' of combat. This method will keep track of whose turn it is via a token variable I
    # initiated back in the Initiative method. This method will also watch to see if any opponent drops to 0 or below
    # hit points, and when that happens, end combat.

    def combatRounds(self):
        if self.pOneCurrentHP > 0 and self.pTwoCurrentHP > 0:
            if self.token == 1:
                self.count += 1
                self.determineHitPTwo()
            elif self.token == 2:
                self.count += 1
                self.determineHitPOne()
        else:
            self.setXP()

    # Determines xp for the victor. Formula is: 10 * Difference in opponent's HP + (difference in level * 50), where
    # difference in level will never equal 0. Added a small 'if' statement to ensure that level never equals 0, which
    # can only happen if both player character's are of the same level.
    # This is a logic problem in this I'm unsure how to deal with. Right now. High level characters can abuse the xp
    # system by fighting low level characters, and getting a great deal of xp based on how the formula is setup. Want
    # to set up a way in which program detects if winning player was higher level than losing player. If so, change
    # formula to just 10 * Difference in opponent's HP. If winning player was lower, then keep formula as is.

    def setXP(self):
        if self.pOneCurrentHP <= 0:
            print(self.playerTwo + " won in " + str(int(self.count / 2)) + " rounds")
            level = abs(self.pOneLevel - self.pTwoLevel)
            if level == 0:
                level = 1
            levelDiff = level * 50
            differHP = abs(self.pOneCurrentHP - self.pTwoCurrentHP)
            self.xp = 10 * differHP + levelDiff
            print(self.playerTwo + " has earned: " + str(self.xp) + " experience points.")
            self.currentPlayerXP = self.pTwoInfo['currentxp'] + self.xp
            self.nextLevel = self.pTwoInfo['nextlevel']
            self.winner = self.playerTwo
            self.levelUp = self.pTwoInfo['level']
            self.checkLevel()
        elif self.pTwoCurrentHP <= 0:
            print(self.playerOne + " won in " + str(int(self.count / 2)) + " rounds")
            level = abs(self.pOneLevel - self.pTwoLevel)
            if level == 0:
                level = 1
            levelDiff = level * 50
            differHP = abs(self.pOneCurrentHP - self.pTwoCurrentHP)
            self.xp = 10 * differHP + levelDiff
            print(self.playerOne + " has earned: " + str(self.xp) + " experience points.")
            self.currentPlayerXP = self.pOneInfo['currentxp'] + self.xp
            self.nextLevel = self.pOneInfo['nextlevel']
            self.winner = self.playerOne
            self.levelUp = self.pOneInfo['level']
            self.checkLevel()

    # Method to check the value of 'currentxp' on a character's json file. If it exceeds the 'nextlevel' value, notify
    # the winning player that they have leveled up. Then proceed to write all the new values for that level to the
    # json file.
    # this Method opens up levelchart.txt, a json that contains a dictionary containing values for levels 1 through 20.
    def checkLevel(self):

        with open(self.winner + '.txt', 'r+') as file:
            charData = json.load(file)
            charData['currentxp'] = self.currentPlayerXP
            file.seek(0)
            file.write(json.dumps(charData, ensure_ascii=False, indent=2))
            file.truncate()
            file.close()

        if self.currentPlayerXP >= self.nextLevel:
            newLevel = self.levelUp + 1
            newLevel = str(newLevel)
            print(self.winner + " has reached level " + newLevel + "!")
            levelFile = open("levelchart.txt", "r", encoding="utf-8")
            levelDict = json.load(levelFile)
            levelFile.close()

            with open(self.winner + '.txt', 'r+') as file:
                charData = json.load(file)
                charData['level'] = newLevel
                charData['hitpoints'] = levelDict[newLevel][0]
                charData['base damage'] = str(levelDict[newLevel][1]) + "d" + str(levelDict[newLevel][2])
                charData['total feats'] = levelDict[newLevel][4]
                charData['hit'] = levelDict[newLevel][5]
                charData['damage modifier'] = levelDict[newLevel][5]
                charData['ac'] = levelDict[newLevel][6]
                charData['currentxp'] = self.currentPlayerXP
                charData['nextlevel'] = levelDict[newLevel][7]
                file.seek(0)
                file.write(json.dumps(charData, ensure_ascii=False, indent=2))
                file.truncate()
                file.close()
        else:
            pass


# ------------------------------------TEST CODE-----------------------------------------
# Run module as stand alone to test.
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