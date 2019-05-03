import gameFeats
import charWrite
import charCreation
import json

"""
This script is dedicated to pulling up helpful information on feats, as well as selecting them to be placed on the
character sheet. 
"""

class Feats:

    # def __init__(self):
    #     self.stats = []

    # the only method in the program that takes advantage of the save method back in charWrite.py. I don't know how,
    # why, or even if it is working correctly. Clearly it works when using static data, such as a level 1 newly created
    # character, but I have no idea if it will be successful in pulling up updated information, such as when a player
    # hits level 2, and more importantly, 3 - when a new feat can be added to a character sheet.
    def playerFeats(self, info):

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
        hasTaken = info[14]
        remainingFeats = info[13]

        # self.stats = [charName, charLevel, charHP, charFeats, charBaseDamage, charHit, charDamage, charAC
        #              charXP, nextLevel, charStr, charDex, charCon, hasTaken, remainingFeats]
        #place all keys within a list for comparison later


        featDict = gameFeats.featDict()[0]
        featList = gameFeats.featDict()[1]

        print("For a list of all the available feats, type 'list'")
        print("For information on a specific feat, type 'help <feat>")
        print("To choose a specific feat, type 'pick <feat>")
        print("Type 'back' to go back")
        print(hasTaken)
        answer = input("Feat> ").lower()

        # Starting here, everything looks REALLY ugly and just feels inefficient. It works, but the amount of if/else
        # statements used makes me think there HAS to be a way to make it more logical, and concise. Right now, it's just
        # a nested mess.

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
                    if answer not in featList:
                        print("Make sure you have spelled the feat correctly.")
                    else:
                        level = featDict[0][answer]['requirements'][0]
                        reqStr = featDict[0][answer]['requirements'][1]
                        reqDex = featDict[0][answer]['requirements'][2]
                        reqCon = featDict[0][answer]['requirements'][3]
                        reqFeats = featDict[0][answer]['requirements'][4]
                        print(reqCon)
                        print(charCon)
                        if level > charLevel:
                            print("You are not the required level for this feat")
                        elif reqStr > charStr:
                            print("You do not have the required strength for this feat")
                        elif reqDex > charDex:
                            print("You do not have the required dexterity for this feat")
                        elif reqCon > charCon:
                            print("You do not have the required constitution for this feat")
                        elif reqFeats not in hasTaken and reqFeats != "none":
                            print("You do not have the required prerequisites to take this feat")
                        elif answer not in hasTaken:
                            print(answer + " has been added to your character sheet.")
                            remainingFeats = remainingFeats - 1
                            print(remainingFeats)
                            hasTaken.append(answer)
                            if answer == "dexterous fighter":
                                dexMod = int(charDex / 2)
                                strMod = int(charStr / 2)
                                charHit = charHit + dexMod - strMod

                            if answer == "crushing blow":
                                damageMod = 1
                                charDamage = charDamage + damageMod
                            if answer == "improved crushing blow":
                                damageMod = 3
                                charDamage = charDamage + damageMod
                            if answer == "greater crushing blow":
                                damageMod = 5
                                charDamage = charDamage + damageMod

                            if answer == "precision strike":
                                hitMod = 1
                                charHit = charHit + hitMod
                            if answer == "improved precision strike":
                                hitMod = 3
                                charHit = charHit + hitMod
                            if answer == "greater precision strike":
                                hitMod = 5
                                charHit = charHit + hitMod

                            if answer == "lightning reflexes":
                                acMod = 1
                                charAC = charAC + acMod
                            if answer == "improved lightning reflexes":
                                acMod = 3
                                charAC = charAC + acMod
                            if answer == "greater lightning reflexes":
                                acMod = 5
                                charAC = charAC + acMod

                            if answer == "endurance":
                                hpMod = 5
                                charHP = charHP + hpMod
                            if answer == "improved endurance":
                                hpMod = 15
                                charHP = charHP + hpMod
                            if answer == "greater endurance":
                                hpMod = 30
                                charHP = charHP + hpMod

                            with open(charName + '.txt', 'r+') as file:
                                        jsonData = json.load(file)
                                        jsonData['hitpoints'] = charHP
                                        jsonData['ac'] = charAC
                                        jsonData['hit'] = charHit
                                        jsonData['damage modifier'] = charDamage
                                        jsonData['feats taken'] = hasTaken
                                        jsonData['remaining feats'] = remainingFeats
                                        file.seek(0)
                                        file.write(json.dumps(jsonData, ensure_ascii=False, indent=2))
                                        file.truncate()
                                        file.close()
                        else:
                            print("You have already taken this feat.")
            print("For a list of all the available feats, type 'list'")
            print("For information on a specific feat, type 'help <feat>'")
            print("To choose a specific feat, type 'pick <feat>'")
            print("Type 'back' to go back")
            answer = input("Feat> ").lower()


#--------------------------------------------TEST CODE------------------------------------
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

# for word in hasTaken:
#     if word == "dexterous fighter":
#         dexMod = int(charDex / 2)
#         strMod = int(charStr / 2)
#         charHit = charHit + dexMod - strMod
#
#     if word == "crushing blow":
#         damageMod = 1
#         charDamage = charDamage + damageMod
#     elif word == "improved crushing blow":
#         damageMod = 3
#         charDamage = charDamage + damageMod
#     elif word == "greater crushing blow":
#         damageMod = 5
#         charDamage = charDamage + damageMod
#     else:
#         pass
#
#     if word == "precision strike":
#         hitMod = 1
#         charHit = charHit + hitMod
#     elif word == "improved precision strike":
#         hitMod = 3
#         charHit = charHit + hitMod
#     elif word == "greater precision strike":
#         hitMod = 5
#         charHit = charHit + hitMod
#     else:
#         pass
#
#     if word == "lightning reflexes":
#         acMod = 1
#         charAC = charAC + acMod
#     elif word == "improved lightning reflexes":
#         acMod = 3
#         charAC = charAC + acMod
#     elif word == "greater lightning reflexes":
#         acMod = 5
#         charAC = charAC + acMod
#     else:
#         pass
#
#     if word == "endurance":
#         hpMod = 5
#         charHP = charHP + hpMod
#     elif word == "improved endurance":
#         hpMod = 15
#         charHP = charHP + hpMod
#     elif word == "greater endurance":
#         hpMod = 30
#         charHP = charHP + hpMod
#     else:
#         pass
