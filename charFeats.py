import json

"""
This script is dedicated to pulling up helpful information on feats, as well as selecting them to be placed on the
character sheet. 
"""

def feats():
    # Open up the json object containing the list of feats.
    featFile = open("feats.txt", "r", encoding="utf-8")
    featInfo = json.load(featFile)
    featFile.close()

    charFile = open("Irixis.txt", "r", encoding="utf-8")
    charInfo = json.load(charFile)
    charFile.close()
    charName = charInfo["name"]
    charLevel = charInfo["level"]
    charHP = charInfo["hitpoints"]
    charHit = charInfo["hit"]
    charTotalFeats = charInfo["total feats"]
    charDamage = charInfo["damage"]
    charAC = charInfo["ac"]
    charXP = charInfo["currentxp"]
    nextLevel = charInfo["nextlevel"]
    remainingFeats = charInfo["remaining feats"]
    charStr = charInfo["strength"]
    charDex = charInfo["dexterity"]
    charCon = charInfo["constitution"]
    charFeatList = charInfo["player feats"]

    # place all keys within a list for comparison later
    featDict = []
    for keys in featInfo[0]:
        featDict.append(keys)

    print("For a list of all the available feats, type 'list'")
    print("For information on a specific feat, type 'help <feat>")
    print("To choose a specific feat, type 'pick <feat>")
    answer = input("Feat> ").lower()
    while answer != 'back':
        if answer == 'list':
            for word in featDict:
                print(word, end=", ")
        elif answer[:4] == 'help':
            answer = answer[5:]
            reqStat = featInfo[0][answer]['stat']
            featStatus = featInfo[0][answer]['status']
            level = featInfo[0][answer]['requirements'][0]
            reqStr = featInfo[0][answer]['requirements'][1]
            reqDex = featInfo[0][answer]['requirements'][2]
            reqCon = featInfo[0][answer]['requirements'][3]
            reqFeats = featInfo[0][answer]['requirements'][4]
            print(answer + " (" + reqStat + ") (" + featStatus + ")")
            print(featInfo[0][answer]['desc'])
            print("Prerequisites: " + "Level: " + str(level) + " Strength: " + str(reqStr) + " Dexterity: " + str(reqDex) + " Constitution: " + str(reqCon) + " Required Feats: " + reqFeats)
        elif answer[:4] == 'pick':
            if remainingFeats == 0:
                print("You have no feat slots left to select a new feat.")
            else:
                answer = answer[5:]
                level = featInfo[0][answer]['requirements'][0]
                reqStr = featInfo[0][answer]['requirements'][1]
                reqDex = featInfo[0][answer]['requirements'][2]
                reqCon = featInfo[0][answer]['requirements'][3]
                reqFeats = featInfo[0][answer]['requirements'][4]

                if answer in featDict and charLevel >= level \
                                      and charStr >= reqStr \
                                      and charDex >= reqDex \
                                      and charCon >= reqCon \
                                      and answer not in charFeatList:
                    print(answer + " has been added to your character sheet.")
                    remainingFeats = remainingFeats - 1
                playerFeats = charFeatList
                playerFeats.append(answer)
                print(playerFeats)

                characterFile = {}

                # basics[0] = Level
                # basics[1] = Hit Points                  abilities[2] = Hit Point Modifier
                # basics[2] = To Hit                      abilities[0] = To Hit Modifier
                # basics[3] = Damage                      abilities[0] = Damage Modifier
                # basics[4] = Total ability points
                # basics[5] = Total feats
                # basics[6] = Armor Class                 abilities[1] = Armor Class Modifier
                # basics[7] = player current xp
                # basics[8] = xp to next level
                # basics[9] = character

                # Fill the dictionary with required information

                characterFile["name"] = charName
                characterFile["level"] = charLevel
                characterFile["hitpoints"] = charHP
                characterFile["total feats"] = charTotalFeats
                characterFile["hit"] = charHit
                characterFile["damage"] = charDamage
                characterFile["ac"] = charAC
                characterFile["currentxp"] = charXP
                characterFile["nextlevel"] = nextLevel
                characterFile["strength"] = charStr
                characterFile["dexterity"] = charDex
                characterFile["constitution"] = charCon
                characterFile["player feats"] = playerFeats
                characterFile["remaining feats"] = remainingFeats


                file = open(charName + ".txt", "w", encoding="utf-8")
                json.dump(characterFile, file, ensure_ascii=False, indent=2)
        print("")
        answer = input("Feat> ").lower()

feats()
