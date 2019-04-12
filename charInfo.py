import json

"""
script that opens the JSON file of the character
"""



def charSheet():
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

    print("Character Name:     " + charName)
    print("Level:              " + str(charLevel) + "       Strength:     " + str(charStr))
    print("Hit Points:         " + str(charHP) + "      Dexterity:    " + str(charDex))
    print("To Hit Modifier:    " + str(charHit) + "       Constitution: " + str(charCon))
    print("Total Feats:        " + str(charFeats))
    print("Damage Modifier:    " + str(charDamage))
    print("Armor Class:        " + str(charAC))
    print("Current XP:         " + str(charXP))
    print("XP needed to level: " + str(nextLevel))

    #print("Available feats:    ") + str(currentFeatTotal)

"""
Reserved for adding in feat information when available.
"""