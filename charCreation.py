'''
Character Creation.
'''

'''
This spot is reserved to determine how to ensure one account has one character
'''

'''
key = level
Element = value
0       = hit Points
1       = minimum damage
2       = maximum damage
3       = total ability points
4       = total number of feats
5       = base to hit modifier
6       = base Armor Class
7       = experience Points to next level

Strictly speaking, this script only needs the first key in the levelDict. However, the entire dictionary is placed here
if needed later.
'''
class Character():

    def basics(self):
        levelDict = {1: [ 25,  1,   6,   15,   2,  1,  5,   30],
                     2: [ 30,  1,   6,   15,   2,  2,  6,   90],
                     3: [ 35,  1,   8,   15,   3,  2,  7,  180],
                     4: [ 40,  1,   8,   15,   3,  3,  8,  300],
                     5: [ 45,  1,  10,   16,   4,  3,  9,  450],
                     6: [ 50,  1,  10,   16,   4,  4, 10,  630],
                     7: [ 55,  2,  12,   16,   5,  4, 11,  840],
                     8: [ 60,  2,  12,   16,   5,  5, 12, 1080],
                     9: [ 65,  2,  16,   16,   6,  5, 13, 1350],
                    10: [ 70,  2,  16,   17,   6,  6, 15, 1650],
                    11: [ 75,  3,  18,   17,   7,  6, 16, 1980],
                    12: [ 80,  3,  18,   17,   7,  7, 17, 2340],
                    13: [ 85,  2,  20,   17,   8,  7, 18, 2730],
                    14: [ 90,  2,  20,   17,   8,  8, 19, 3150],
                    15: [100,  2,  24,   18,   9,  8, 20, 3600],
                    16: [110,  4,  24,   18,   9,  9, 21, 4080],
                    17: [130,  4,  32,   18,  10,  9, 22, 4590],
                    18: [135,  4,  32,   18,  10, 10, 23, 5130],
                    19: [140,  3,  36,   18,  11, 10, 24, 5700],
                    20: [150,  3,  36,   19,  11, 11, 25, 6300]}

        # As this is character creation, level will always be equal to 1, and xp always equal to 0
        playerLevel = 1
        playerXP = 0
        # Grabs character's name, and then assigns appropriate values from the dictionary above to display.
        charName = input("What is your characters name? ")
        print("Your character's name is " + charName + ", and will start out at level one with the following stats:")
        print("Hit Points:                 " + str(levelDict[int(playerLevel)][0]))
        statHP = levelDict[int(playerLevel)][0]
        print("Damage:                     " + str(levelDict[int(playerLevel)][1]) + "d" + str(levelDict[int(playerLevel)][2]))
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
        return [playerLevel, statHP, statHit, statDamage, statPoints, statFeats, statAC, playerXP, toNextLevel, charName]

    '''
    basics[0] = Level
    basics[1] = Hit Points
    basics[2] = To Hit Modifier
    basics[3] = Damage Modifier
    basics[4] = Total ability points
    basics[5] = Total feats
    basics[6] = Armor Class
    basics[7] = player current xp
    basics[8] = xp to next level
    basics[9] = character name
    '''
        # This function focuses purely on assigning values to the three primary stats: Strength, Dexterity, and
        # Constitution. While loops are set in place to ensure that no value is placed above 10, or any remaining points
        # they player has left to allocate. Once completed, the information is displayed with their appropriate modifiers
        # and the player is asked if they want to keep their setup, or redistribute.

    def abilities(self, basics):
        statPoints = basics[4]
        print("You have " + str(statPoints) + " points to distribute between Strength, Dexterity, and Constitution.")
        print("No single stat can be above 10 points")
        answer = "no"
        while answer == "no":
            strengthStat = input("How many points do you want to put in Strength? ")
            while int(strengthStat) > 10:
                print("You can not allocate more than 10 points in any stat.")
                strengthStat = input("How many points do you want to put in Strength? ")
            remaining = int(statPoints) - int(strengthStat)
            print("You have put " + str(strengthStat) + " points in Strength, and have " + str(remaining) + " points left.")

            dexterityStat = input("How many points do you want to put in Dexterity?")
            while int(dexterityStat) > remaining:
                print("You only have " + str(remaining) + " points left")
                dexterityStat = input("How many points do you want to put in Dexterity?")
            remaining = remaining - int(dexterityStat)
            print("You have put " + str(dexterityStat) + " points in Dexterity, and have " + str(remaining) + " points left")

            conStat = input("How many points do you want to put in Constitution?")
            while int(conStat) > remaining:
                print("You only have " + str(remaining) + " points left")
                conStat = input("How many points do you want to put in Constitution?")

            strMod = int(int(strengthStat) / 2)
            print("Your Strength: " + str(strengthStat) + " giving you a to Hit and Damage mod of +" + str(int(strMod)))
            dexMod = int(int(dexterityStat) / 2)
            print("Your Dexterity: " + str(dexterityStat) + " giving you a bonus to AC of + " + str(int(dexMod)))
            conMod = int(conStat) * 5
            print("Your Constitution: " + str(conStat) + " giving you bonus HP of + " + str(int(conMod)))
            answer = input("Do you wish to keep these stats? (yes/no)").lower()
        return [strMod, dexMod, conMod, strengthStat, dexterityStat, conStat]

    # Grabs all the necessary information from the above functions, and commits them to a JSON file labeled with their
    # character name.


# for testing purposes
# basics = basics()
# abilities = abilities(basics)
