import charWrite
import charCreation
import gameFeats
import json

"""
script that opens the JSON file of the character
"""



def charSheet():

    featDict = gameFeats.featDict()[0]
    featList = gameFeats.featDict()[1]


    charFile = open("Irixis.txt", "r", encoding="utf-8")
    charInfo = json.load(charFile)
    charFile.close()
    charName = charInfo["name"]
    charLevel = charInfo["level"]
    charHP = charInfo["hitpoints"]
    charFeats = charInfo["total feats"]
    charHit = charInfo["hit"]
    charDamage = charInfo["damage"]
    charAC = charInfo["ac"]
    charXP = charInfo["currentxp"]
    nextLevel = charInfo["nextlevel"]
    charStr = charInfo["strength"]
    charDex = charInfo["dexterity"]
    charCon = charInfo["constitution"]
    hasTaken = charInfo["player feats"]
    remainingFeats = charInfo["remaining feats"]

    featInfo = open("feats.txt", "r", encoding="utf-8")
    featDict = json.load(featInfo)

    print("Character Name:     " + charName)
    print("Level:              " + str(charLevel) + "       Strength:     " + str(charStr))
    print("Hit Points:         " + str(charHP) + "      Dexterity:    " + str(charDex))
    print("To Hit Modifier:    " + str(charHit) + "       Constitution: " + str(charCon))
    print("Total Feats:        " + str(charFeats))
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