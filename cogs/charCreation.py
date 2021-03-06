import json
import os

'''
Character Creation.
'''

'''
This spot is reserved to determine how to ensure one account has one character
'''

'''
key = level
Index   = value type
0       = hit Points
1       = minimum damage
2       = maximum damage
3       = total ability points
4       = total number of feats
5       = base to hit modifier
6       = base Armor Class
7       = experience Points to next level

Strictly speaking, this script only needs the first key in the levelDict. No need to load the level chart json.
'''
class Character:

    def basics(self):
        levelDict = {1: [ 25,  1,   6,   15,   2,  1,  5,    75]}

        # As this is character creation, level will always be equal to 1, and xp always equal to 0
        playerLevel = 1
        playerXP = 0
        # Grabs character's name, and then assigns appropriate values from the dictionary above to display.
        charName = input("What is your characters name? ").lower()
        print("Your character's name is " + charName + ", and will start out at level one with the following stats:")
        print("Hit Points:                 " + str(levelDict[int(playerLevel)][0]))
        statHP = levelDict[int(playerLevel)][0]
        print("Damage:                     " + str(levelDict[int(playerLevel)][1]) + "d" + str(levelDict[int(playerLevel)][2]))
        numberOfDice = str(levelDict[int(playerLevel)][1])
        numberOfSides =  str(levelDict[int(playerLevel)][2])
        print("Ability Points to Allocate: " + str(levelDict[int(playerLevel)][3]))
        statPoints = levelDict[int(playerLevel)][3]
        print("Total Feats:                " + str(levelDict[int(playerLevel)][4]))
        statFeats = levelDict[int(playerLevel)][4]
        print("Total Base To Hit Modifier: " + str(levelDict[int(playerLevel)][5]))
        statHit = levelDict[int(playerLevel)][5]
        print("Total Base damage Modifier: " + str(levelDict[int(playerLevel)][5]))
        statDamage = levelDict[int(playerLevel)][5]
        print("Total Base AC:              " + str(levelDict[int(playerLevel)][6]))
        statAC = levelDict[int(playerLevel)][6]
        toNextLevel = (levelDict[int(playerLevel)][7]) - playerXP
        print("You currently have: " + str(playerXP) + " experience and need: " + str(toNextLevel) + " to reach the next level.")
        return [charName, playerLevel, statHP, statHit, statDamage, numberOfDice, numberOfSides, statPoints, statFeats, statAC, playerXP, toNextLevel,]

        # This method focuses purely on assigning values to the three primary stats: Strength, Dexterity, and
        # Constitution. While loops are set in place to ensure that no value is placed above 10, or any remaining points
        # they player has left to allocate. Once completed, the information is displayed with their appropriate modifiers
        # and the player is asked if they want to keep their setup, or redistribute.

    def abilities(self, basics):
        statPoints = basics[7]
        print("You have " + str(statPoints) + " points to distribute between Strength, Dexterity, and Constitution.")
        print("No single stat can be above 10 points at 1")
        answer = "no"
        while answer == "no":
            # strengthStat = input("How many points do you want to put in Strength? ")
            strengthStat = 0
            while strengthStat not in (range(1, 11)):
                print("You can not allocate more than 10 points in any stat.")
                try:
                    strengthStat = int(input("How many points do you want to put in Strength? "))
                except ValueError:
                    print("Please enter a number between 1 and 10")
            remaining = int(statPoints) - strengthStat
            print("You have put " + str(strengthStat) + " points in Strength, and have " + str(remaining) + " points left.")

            # dexterityStat = input("How many points do you want to put in Dexterity?")
            dexterityStat = None
            while dexterityStat not in (range(1, remaining+1)):
                print("You only have " + str(remaining) + " points left")
                try:
                    dexterityStat = int(input("How many points do you want to put in Dexterity?"))
                except ValueError:
                    print("Please enter a number between 1 and " + str(remaining))
            remaining = remaining - dexterityStat
            print("You have put " + str(dexterityStat) + " points in Dexterity, and have " + str(remaining) + " points left")

            # conStat = input("How many points do you want to put in Constitution?")
            conStat = None
            while conStat not in (range(1, remaining+1)):
                print("You only have " + str(remaining) + " points left")
                try:
                    conStat = int(input("How many points do you want to put in Constitution?"))
                except ValueError:
                    print("Please enter a number between 1 and " + str(remaining))

            strMod = int(strengthStat) / 2
            print("Your Strength: " + str(strengthStat) + " giving you a to Hit and Damage mod of +" + str(int(strMod)))
            dexMod = int(dexterityStat) / 2
            print("Your Dexterity: " + str(dexterityStat) + " giving you a bonus to AC of + " + str(int(dexMod)))
            conMod = conStat * 5
            print("Your Constitution: " + str(conStat) + " giving you bonus HP of + " + str(int(conMod)))
            answer = input("Do you wish to keep these stats? (yes/no)").lower()
        return [strMod, dexMod, conMod, strengthStat, dexterityStat, conStat]


    def save(self, basics, abilities):

        """
        basics[0]  = Character Name
        basics[1]  = Level
        basics[2]  = Hit Points       +          abilities[2] = Constitution Modifier
        basics[3]  = To Hit Modifier  +          abilities[0] = Strength Modifier
        basics[3]  = Damage Modifier  +          abilities[0] = Strength Modifier
        basics[5]  = Number of Dice
        basics[6]  = Number of Sides
        basics[7]  = Stat Points
        basics[8]  = Number of Feats
        basics[9]  = Armor Class      +          abilities[1] = Dexterity Modifier
        basics[10] = Player XP
        basics[11] = XP needed to level

        abilities[3] = Strength
        abilities[4] = Dexterity
        abilities[5] = Constitution
        """
        # Create an empty dictionary
        characterFile = {}

        # Fill the dictionary with required information
        name = basics[0]
        characterFile["name"] = name
        level = basics[1]
        characterFile["level"] = level
        hp = int(basics[2] + abilities[2])
        characterFile["hitpoints"] = hp
        tFeats = basics[8]
        characterFile["total feats"] = tFeats
        numberOfDice = basics[5]
        numberOfSides = basics[6]
        characterFile["base damage"] = numberOfDice + "d" + numberOfSides
        hit = int(basics[3] + abilities[0])
        characterFile["hit"] = hit
        damage = int(basics[3] + abilities[0])
        characterFile["damage modifier"] = damage
        ac = int(basics[9] + abilities[1])
        characterFile["ac"] = ac
        xp = basics[10]
        characterFile["currentxp"] = xp
        nextLevel = basics[11]
        characterFile["nextlevel"] = nextLevel
        strength = abilities[3]
        characterFile["strength"] = strength
        dexterity = abilities[4]
        characterFile["dexterity"] = dexterity
        constitution = abilities[5]
        characterFile["constitution"] = constitution
        ap = basics[7]
        characterFile["total ap"] = ap
        hasTaken = []
        characterFile["feats taken"] = hasTaken

        # apply a hidden counters, that will keep track of number of feats throughout level progression
        remainingFeats = 2
        characterFile["remaining feats"] = remainingFeats
        # characterFile["crippling"] = 1
        # characterFile["staggering"] = 1
        # characterFile["evasion"] = 1
        # characterFile["quick"] = 1
        # characterFile["riposte"] = 1
        # characterFile["deflect"] = 1
        # characterFile["reckless"] = 1
        # characterFile["titan's blow"] = 1
        # characterFile["true strike"] = 1


        print("Your character has been saved.")
        # create the JSON file
        path = os.getcwd()
        charFolder = os.path.join(path + "/characters/")
        print(charFolder)
        file = open(charFolder + name + ".txt", "w", encoding="utf-8")
        json.dump(characterFile, file, ensure_ascii=False, indent=2)


# for testing purposes
# basics = basics()
# abilities = abilities(basics)
