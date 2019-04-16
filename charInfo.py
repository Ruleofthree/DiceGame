import charWrite
import charCreation
import gameFeats
import json

"""
script that opens the JSON file of the character
"""



def charSheet(info):

    featDict = gameFeats.featDict()[0]
    featList = gameFeats.featDict()[1]

    charName = info[0]
    charLevel = info[1]
    charHP = info[2]
    charFeats = info[3]
    charBaseDamage = info[4]
    charHit = info[5]
    charDamage = info[6]
    charAC = info[7]
    charXP = info[8]
    nextLevel = info[9]
    charStr = info[10]
    charDex = info[11]
    charCon = info[12]
    remainingFeats = info[13]
    hasTaken = info[14]

    print("Character Name:     " + charName)
    print("Level:              " + str(charLevel) + "       Strength:     " + str(charStr))
    print("Hit Points:         " + str(charHP) + "      Dexterity:    " + str(charDex))
    print("To Hit Modifier:    " + str(charHit) + "       Constitution: " + str(charCon))
    print("Base Damage:        " + charBaseDamage)
    print("Total Feats:        " + str(remainingFeats))
    print("Damage Modifier:    " + str(charDamage))
    print("Armor Class:        " + str(charAC))
    print("Current XP:         " + str(charXP))
    print("XP needed to level: " + str(nextLevel))

    print("Available feats:    " + str(remainingFeats))

    if not hasTaken:
        print("")
        print("No feats taken yet.")
        print("")
    else:
        print("")
        print(charName + " feats:")
        print("")

        print(hasTaken[0] + ": ")
        print(featDict[0][hasTaken[0]]['desc'])
        print("")

        print(hasTaken[1] + ": ")
        print(featDict[0][hasTaken[1]]['desc'])
"""
Reserved for adding in feat information when available.
"""