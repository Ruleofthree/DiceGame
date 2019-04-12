import json

# nestedDict = {1: {'name': 'Derek', 'age': 34, 'sex': 'male'},
#               2: {'name': 'Heather', 'age': 36, 'sex': 'female'}}
#
# print(nestedDict[2]['name'])

#
#  for keys in strength:
#         print(keys)
#         featDict.append(keys)
#     # keeps the user in the list group until they assign 'quit' to the variable 'select.'
#     select = ""
#     while select != "quit":
#         select = input("For information on a listed feat, type 'help <feat>'\n"
#                        "to exit out of the list, type 'quit'").lower()
#         featSelected = select[5:]
#         # check to see if first 4 characters of 'select' reads 'quit' If so, exit List.
#         quitList = select[:4]
#         if quitList == "quit":
#             print("Exiting List")
#         # check to see if the 6th character and beyond match a key in the 'featDict' variable. If not, restart while
#         # loop.
#         elif featSelected not in featDict:
#             print("It appears you typed in a feat that does not exist.")
#         # if answer matches a key, grab corresponding information and display it.
#         else:
#             desc = strength[featSelected]['desc']
#             level = strength[featSelected]['requirements'][0]
#             reqStr = strength[featSelected]['requirements'][1]
#             reqDex = strength[featSelected]['requirements'][2]
#             reqCon = strength[featSelected]['requirements'][3]
#             reqFeats = strength[featSelected]['requirements'][4]
#             print(desc)
#             print("Prerequisites: " + "Level: " + str(level) + " Strength: " + str(reqStr) + " Dexterity: " + str(reqDex) + " Constitution: " + str(reqCon) + " Required Feats: " + reqFeats)
#
# def dexfeatList():
#     featFile = open("feats.txt", "r", encoding="utf-8")
#     featInfo = json.load(featFile)
#     featFile.close()
#     dexterity = featInfo['dexterity']
#     featDict = []
#     for keys in dexterity:
#         print(keys)
#         featDict.append(keys)
#     select = ""
#     while select != "quit":
#         select = input("For information on a listed feat, type 'help <feat>'\n"
#                        "to exit out of the list, type 'quit'").lower()
#         featSelected = select[5:]
#         quitList = select[:4]
#         if quitList == "quit":
#             print("Exiting List")
#         elif featSelected not in featDict:
#             print("It appears you typed in a feat that does not exist.")
#         else:
#             desc = dexterity[featSelected]['desc']
#             level = dexterity[featSelected]['requirements'][0]
#             reqStr = dexterity[featSelected]['requirements'][1]
#             reqDex = dexterity[featSelected]['requirements'][2]
#             reqCon = dexterity[featSelected]['requirements'][3]
#             reqFeats = dexterity[featSelected]['requirements'][4]
#             print(desc)
#             print("Prerequisites: " + "Level: " + str(level) + " Strength: " + str(reqStr) + " Dexterity: " + str(reqDex) + " Constitution: " + str(reqCon) + " Required Feats: " + reqFeats)
#
# def confeatList():
#     featFile = open("feats.txt", "r", encoding="utf-8")
#     featInfo = json.load(featFile)
#     featFile.close()
#     constitution = featInfo['constitution']
#     featDict = []
#     for keys in constitution:
#         print(keys)
#         featDict.append(keys)
#     select = ""
#     while select != "quit":
#         select = input("For information on a listed feat, type 'help <feat>'\n"
#                        "to exit out of the list, type 'quit'").lower()
#         featSelected = select[5:]
#         quitList = select[:4]
#         if quitList == "quit":
#             print("Exiting List")
#         elif featSelected not in featDict:
#             print("It appears you typed in a feat that does not exist.")
#         else:
#             desc = constitution[featSelected]['desc']
#             level = constitution[featSelected]['requirements'][0]
#             reqStr = constitution[featSelected]['requirements'][1]
#             reqDex = constitution[featSelected]['requirements'][2]
#             reqCon = constitution[featSelected]['requirements'][3]
#             reqFeats = constitution[featSelected]['requirements'][4]
#             print(desc)
#             print("Prerequisites: " + "Level: " + str(level) + " Strength: " + str(reqStr) + " Dexterity: " + str(
#                 reqDex) + " Constitution: " + str(reqCon) + " Required Feats: " + reqFeats)
#
# def getFeat():
#     # Make the feat list accessible inside this function
#     featFile = open("feats.txt", "r", encoding="utf-8")
#     featInfo = json.load(featFile)
#     featFile.close()
#
#     # make a single dictionary for all feats
#     strength = featInfo['strength']
#     dexterity = featInfo['dexterity']
#     constitution = featInfo['constitution']
#     featList = []
#     for keys in strength:
#         featList.append(keys)
#     for keys in dexterity:
#         featList.append(keys)
#     for keys in constitution:
#         featList.append(keys)
#
#     # pull in data from the character json
#     charFile = open("Irixis.txt", "r", encoding="utf-8")
#     charInfo = json.load(charFile)
#     charFile.close()
#     charName = charInfo["name"]
#     charLevel = charInfo["level"]
#     charHP = charInfo["hitpoints"]
#     charHit = charInfo["hit"]
#     charTotalFeats = charInfo["total feats"]
#     charDamage = charInfo["damage"]
#     charAC = charInfo["ac"]
#     charXP = charInfo["currentxp"]
#     nextLevel = charInfo["nextlevel"]
#     remainingFeats = charInfo["remaining feats"]
#     charStr = charInfo["strength"]
#     charDex = charInfo["dexterity"]
#     charCon = charInfo["constitution"]
#     charFeatList = charInfo["player feats"]
#
#     # Find out how many feats the character has available to learn
#     choice = ""
#     while choice != "back":
#         if remainingFeats == 0:
#             print("You have no feat slots left to select a new feat.")
#         if remainingFeats > 0:
#             print("You have " + str(remainingFeats) + " slots left to fill with feats")
#             print("Please type <feat> here to select and save ")
#             print("Or type 'back' to exit")
#             choice = input("Feat Chosen > " ).lower()
#             if choice not in featList:
#                 print("It appears you typed in a feat that does not exist.")
#             else:
#                 isSure = input("Are you sure you want " + choice + "? Once chosen, it can not be replaced easily. (yes/no)").lower()
#                 while isSure != "yes":
#                     choice = input("Feat Chosen > ").lower()
#                     isSure = input("Are you sure you want " + choice + "? Once chosen, it can not be replaced easily.").lower()
#
#                 if choice in featList and charLevel >= charLevel \
#                                       and charStr >= strength[choice]['requirements'][1] \
#                                       and charDex >= strength[choice]['requirements'][2] \
#                                       and charCon >= strength[choice]['requirements'][3] \
#                                       and choice not in charFeatList:
#                     print(choice + " has been added to your character sheet.")
#                     remainingFeats = remainingFeats - 1
#
#                     characterFile = {}
#                     featList = []
#                     # basics[0] = Level
#                     # basics[1] = Hit Points                  abilities[2] = Hit Point Modifier
#                     # basics[2] = To Hit                      abilities[0] = To Hit Modifier
#                     # basics[3] = Damage                      abilities[0] = Damage Modifier
#                     # basics[4] = Total ability points
#                     # basics[5] = Total feats
#                     # basics[6] = Armor Class                 abilities[1] = Armor Class Modifier
#                     # basics[7] = player current xp
#                     # basics[8] = xp to next level
#                     # basics[9] = character
#
#                     # Fill the dictionary with required information
#
#                     characterFile["name"] = charName
#                     characterFile["level"] = charLevel
#                     characterFile["hitpoints"] = charHP
#                     characterFile["total feats"] = charTotalFeats
#                     characterFile["hit"] = charHit
#                     characterFile["damage"] = charDamage
#                     characterFile["ac"] = charAC
#                     characterFile["currentxp"] = charXP
#                     characterFile["nextlevel"] = nextLevel
#                     characterFile["strength"] = charStr
#                     characterFile["dexterity"] = charDex
#                     characterFile["constitution"] = charCon
#                     characterFile["player feats"] = choice
#                     characterFile["remaining feats"] = remainingFeats
#
#
#                     file = open(charName + ".txt", "w", encoding="utf-8")
#                     json.dump(characterFile, file, ensure_ascii=False, indent=2)

#
# stats = openCharacter()
# feats ={
#            "power attack":{
#                "desc": "Subtract -1 from your bonus to hit, and add it to your bonus to damage. You and only take out a number of points from your bonus to hit equal to your level divided by 4(-1 at level 1, -2 at level 5, -3 at level 9, -4 at level 13, and -5 at level 17, and only if you have that many points in your to hit bonus to take away. Example: If you are 7th level, and have +5 to hit. You can only take out 3 points, to have +2 to hit, and add +3 to your damage modifier.",
#                "requirements": [1, 3, None, None, None],
#                "status": "active"
#               },
#
#            "crushing blow":{
#                "desc": "adds +1 to your damage modifier",
#                "requirements": [3, 5, None, None, None],
#                "status": "passive"
#               },
#            "improved crushing blow":{
#                "desc": "improves the bonus of crushing blow to +3 to damage.",
#                "requirements": [5, 7, None, None, "crushing blow"],
#                "status": "passive"
#               },
#
#            "greater crushing blow":{
#                "desc": "improves the bonus of crushing blow to +5 to damage",
#                "requirements": [7, 9, None, None, "improved crushing blow"],
#                "status": "passive"
#               },
#
#            "titan's blow":{
#                "desc": "Your next attack deals 50% more damage, can only be used once per fight.",
#                "requirements": [15, 10, None, None, "greater crushing blow"],
#                "status": "active"
#            },
#
#            "combat expertise":{
#                "desc": "Subtract -1 from your bonus to damage, and add it to your bonus to hit. You and only take out a number of points from your bonus to damage equal to your level divided by 4(-1 at level 1, -2 at level 5, -3 at level 9, -4 at level 13, and -5 at level 17, and only if you have that many points in your to hit bonus to take away. Example: If you are 7th level, and have +5 to damage. You can only take out 3 points, to have +2 to damage, and add +3 to your to hit modifier.",
#                "requirements": [1, None, 3, None, None],
#                "status": "active"
#            },
#
#            "precision strike":{
#                "desc": "adds +1 to your hit modifier",
#                "requirements": [3, None, 5, None, None],
#                "status": "passive"
#            },
#
#            "improved precision strike":{
#                "desc": "improves the bonus of precision strike to +3 to hit.",
#                "requirements": [5, None, 7, None, "precision strike"],
#                "status": "passive"
#            },
#
#            "greater precision strike":{
#                "desc": "improves the bonus of precision strike to +5 to hit",
#                "requirements": [7, None, 9, None, "improved precision strike"],
#                "status": "passive"
#            },
#
#            "true strike":{
#                "desc": "Allows you to attack with absolute precision, forgoing any attack roll, but doing 50% less damage",
#                "requirements": [15, None, 10, None, "greater precision strike"],
#                "status": "active"
#            },
#
#            "crippling blow":{
#                "desc": "You strike your opponent with such a force that it hinders their own attempts to strike back, given them a -1 to their next attack.",
#                "requirements": [3, 5, 3, None, None],
#                "status": "active"
#            },
#
#            "improved crippling blow":{
#                "desc": "improves crippling blow to -3 to their next attack.",
#                "requirements": [5, 6, 4, None, "crippling blow"],
#                "status": "active"
#            },
#
#            "greater crippling blow":{
#                "desc": "improves crippling blow to -5 to their next attack.",
#                "requirements": [7, 7, 5, None, "improved crippling blow"],
#                "status": "active"
#            },
#
#            "staggering blow":{
#                "desc": "Apply no modifier to damage, but a successful hit will make the opponents next attack deal 50% less damage",
#                "requirements": [15, 9, 6, None, "greater crippling blow"],
#                "status": "active"
#            },
#
#
#
#           "defensive fighting":{
#                "desc": "Subtract -1 from your bonus to hit, and add it to your Armor Class. You and only take out a number of points from your bonus to hit equal to your level divided by 4(-1 at level 1, -2 at level 5, -3 at level 9, -4 at level 13, and -5 at level 17, and only if you have that many points in your to hit bonus to take away. Example: If you are 7th level, and have +5 to hit. You can only take out 3 points, to have +2 to hit, and add +3 to your Armor Class.",
#                "requirements": [1, None, 3, None, None],
#                "status": "active"
#            },
#
#            "evasion":{
#                "desc": "automatically reduce damage from the next attack by 25%",
#                "requirements": [3, None, 5, None, None],
#                "status": "active"
#            },
#
#            "improved evasion":{
#                "desc": "improves damage reduction to 50%",
#                "requirements": [5, None, 7, None, "evasion"],
#                "status": "active"
#            },
#
#            "greater evasion":{
#                "desc": "improves damage taken by 100%",
#                "requirements": [7, None, 9, None, "greater evasion"],
#                "status": "active"
#            },
#
#            "dexterous fighter":{
#                "desc": "Use your Dexterity instead of your strength as a modifier to determine to hit bonuses",
#                "requirements": [1, None, 3, None, None],
#                "status": "passive"
#            },
#
#            "quick strike":{
#                "desc": "roll damage immediately after getting hit. 15% of total damage is applied to opponent. This effect fails if opponent misses",
#                "requirements": [5, None, 5, None, None],
#                "status": "active"
#            },
#
#            "improved quick strike":{
#                "desc": "improves strike to 30% of total damage.",
#                "requirements": [7, None, 7, None, "quick strike"],
#                "status": "active"
#            },
#
#            "greater quick strike":{
#                "desc": "improves quick strike to 50% total damage.",
#                "requirements": [9, None, 8, None, "improved quick strike"],
#                "status": "active"
#            },
#
#            "riposte":{
#                "desc": "If opponent misses attack, you gain a +5 bonus to hit on your next attack.",
#                "requirements": [13, None, 10, None, "greater quick strike"],
#                "status": "active"
#            },
#
#            "deflect":{
#                "desc": "Roll damage immediately after opponent. If your damage is higher, you only take 90% of total damage",
#                "requirements": [1, None, 3, None, None],
#                "status": "active"
#            },
#
#            "improved deflect":{
#                "desc": "Roll damage immediately after opponent. If your damage is higher, you only take 80% of total damage",
#                "requirements": [5, None, 5, None, None],
#                "status": "active"
#            },
#
#            "greater deflect":{
#                "desc": "Roll damage immediately after opponent. If your damage is higher, you only take 70% of total damage",
#                "requirements": [7, None, 7, None, None],
#                "status": "active"
#            },
#
#            "lightning reflexes":{
#                "desc": "gives +1 to Armor Class",
#                "requirements": [1, None, 3, None, None],
#                "status": "passive"
#            },
#
#            "improved lightning reflexes":{
#                "desc": "increases lightning reflexes bonus to +2",
#                "requirements": [3, None, 5, None, "lightning reflexes"],
#                "status": "passive"
#            },
#
#            "greater lightning reflexes":{
#                "desc": "increases lightning reflexes bonus to +3",
#                "requirements": [5, None, 7, None, "improved lightning reflexes"],
#                "status": "passive"
#            },
#
#
#
#            "hurt me":{
#                "desc": "gives +1 to damage for every 25% of hit points lost",
#                "requirements": [2, None, None, 4, None],
#                "status": "passive"
#            },
#
#            "improved hurt me":{
#                "desc": "increases hurt me bonus to +2",
#                "requirements": [5, None, None, 6, "hurt me"],
#                "status": "passive"
#            },
#
#            "greater hurt me":{
#                "desc": "increases hurt me bonus to +3",
#                "requirements": [10, None, 8, None, "improved hurt me"],
#                "status": "passive"
#            },
#
#            "hurt me more":{
#                "name": "hurt me more",
#                "desc": "applies the +3 bonus for every 20% lost",
#                "requirements": [15, None, 10, None, "greater hurt me"],
#                "status": "passive"
#            }
#       },
#
# featsJSON =json.dumps(feats, ensure_ascii=False,indent=2)
#
# print(featsJSON)
# featFile = open("feats.txt", "r", encoding="utf-8")
# featInfo = json.load(featFile)
# featFile.close()
# again = "yes"




