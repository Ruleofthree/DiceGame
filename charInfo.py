import json

def charSheet():
    charFile = open("Irixis.txt", "r", encoding="utf-8")
    charInfo = json.load(charFile)
    charFile.close()
    charName = charInfo["name"]
    charLevel = charInfo["level"]
    charHP = charInfo["hitpoints"]
    charHit = charInfo["hit"]
    charDamage = charInfo["damage"]
    charAC = charInfo["ac"]
    charXP = charInfo["currentxp"]
    nextLevel = charInfo["nextlevel"]

    print("Character Name:     " + charName)
    print("Level:              " + str(charLevel))
    print("Hit Points:         " + str(charHP))
    print("To Hit Modifier     " + str(charHit))
    print("Damage Modifier:    " + str(charDamage))
    print("Armor Class:        " + str(charAC))
    print("Current XP:         " + str(charXP))
    print("XP needed to level: " + str(nextLevel))