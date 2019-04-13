import gameFeats
import charWrite
import json

"""
This script is dedicated to pulling up helpful information on feats, as well as selecting them to be placed on the
character sheet. 
"""

def feats():
    
    # Open up character information
    # charFile = open("Irixis.txt", "r", encoding="utf-8")
    # charInfo = json.load(charFile)
    # charFile.close()
    # charLevel = charInfo["level"]
    # remainingFeats = charInfo["remaining feats"]
    # charStr = charInfo["strength"]
    # charDex = charInfo["dexterity"]
    # charCon = charInfo["constitution"]
    # charfeatList = charInfo["player feats"]

    # place all keys within a list for comparison later
    
    featDict = gameFeats.featDict()[0]
    featList = gameFeats.featDict()[1]
 
    print("For a list of all the available feats, type 'list'")
    print("For information on a specific feat, type 'help <feat>")
    print("To choose a specific feat, type 'pick <feat>")
    answer = input("Feat> ").lower()
    while answer != 'back':
        if answer == 'list':
            for word in featList:
                print(word, end=", ")
        elif answer[:4] == 'help':
            answer = answer[5:]
            reqStat = featDict[0][answer]['stat']
            featStatus = featDict[0][answer]['status']
            level = featDict[0][answer]['requirements'][0]
            reqStr = featDict[0][answer]['requirements'][1]
            reqDex = featDict[0][answer]['requirements'][2]
            reqCon = featDict[0][answer]['requirements'][3]
            reqFeats = featDict[0][answer]['requirements'][4]
            print(answer + " (" + reqStat + ") (" + featStatus + ")")
            print(featDict[0][answer]['desc'])
            print("Prerequisites: " + "Level: " + str(level) + " Strength: " + str(reqStr) + " Dexterity: " + str(reqDex) + " Constitution: " + str(reqCon) + " Required Feats: " + reqFeats)
        elif answer[:4] == 'pick':
            if remainingFeats == 0:
                print("You have no feat slots left to select a new feat.")
            else:
                answer = answer[5:]
                level = featDict[0][answer]['requirements'][0]
                reqStr = featDict[0][answer]['requirements'][1]
                reqDex = featDict[0][answer]['requirements'][2]
                reqCon = featDict[0][answer]['requirements'][3]
                reqFeats = featDict[0][answer]['requirements'][4]

                if answer in featDict and charLevel >= level \
                                      and charStr >= reqStr \
                                      and charDex >= reqDex \
                                      and charCon >= reqCon \
                                      and answer not in charfeatList:
                    print(answer + " has been added to your character sheet.")
                    remainingFeats = remainingFeats - 1
                playerFeats = charfeatList
                playerFeats.append(answer)
                print(playerFeats)
        print("")
        answer = input("Feat> ").lower()
    return charLevel, remainingFeats, charStr, charDex, charCon, charfeatList

#
#                 # characterFile = {}
#                 #
#                 # # basics[0] = Level
#                 # # basics[1] = Hit Points                  abilities[2] = Hit Point Modifier
#                 # # basics[2] = To Hit                      abilities[0] = To Hit Modifier
#                 # # basics[3] = Damage                      abilities[0] = Damage Modifier
#                 # # basics[4] = Total ability points
#                 # # basics[5] = Total feats
#                 # # basics[6] = Armor Class                 abilities[1] = Armor Class Modifier
#                 # # basics[7] = player current xp
#                 # # basics[8] = xp to next level
#                 # # basics[9] = character
#                 #
#                 # # Fill the dictionary with required information
#                 #
#                 # characterFile["name"] = charName
#                 # characterFile["level"] = charLevel
#                 # characterFile["hitpoints"] = charHP
#                 # characterFile["total feats"] = charTotalFeats
#                 # characterFile["hit"] = charHit
#                 # characterFile["damage"] = charDamage
#                 # characterFile["ac"] = charAC
#                 # characterFile["currentxp"] = charXP
#                 # characterFile["nextlevel"] = nextLevel
#                 # characterFile["strength"] = charStr
#                 # characterFile["dexterity"] = charDex
#                 # characterFile["constitution"] = charCon
#                 # characterFile["player feats"] = playerFeats
#                 # characterFile["remaining feats"] = remainingFeats
#                 #
#                 #
#                 # file = open(charName + ".txt", "w", encoding="utf-8")
#                 # json.dump(characterFile, file, ensure_ascii=False, indent=2)

