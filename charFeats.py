import json

def strfeatList():
    featFile = open("feats.txt", "r", encoding="utf-8")
    featInfo = json.load(featFile)
    featFile.close()
    strength = featInfo['strength']
    for keys in strength:
        print(keys)

def dexfeatList():
    featFile = open("feats.txt", "r", encoding="utf-8")
    featInfo = json.load(featFile)
    featFile.close()
    dexterity = featInfo['dexterity']
    featDict = []
    for keys in dexterity:
        print(keys)
        featDict.append(keys)
    print(featDict)
    select = ""
    while select != "quit":
        select = input("For information on a listed feat, type 'help <feat>'\n"
                       "to exit out of the list, type 'quit'").lower()
        featSelected = select[5:]
        quitList = select[:4]
        if quitList == "quit":
            print("Exiting List")
        elif featSelected not in featDict:
            print("It appears you typed in a feat that does not exist.")
        else:
            desc = dexterity[featSelected]['desc']
            level = dexterity[featSelected]['requirements'][0]
            reqStr = dexterity[featSelected]['requirements'][1]
            reqDex = dexterity[featSelected]['requirements'][2]
            reqCon = dexterity[featSelected]['requirements'][3]
            reqFeats = dexterity[featSelected]['requirements'][4]
            print(desc)
            print("Prerequisites: " + "Level: " + str(level) + " Strength: " + str(reqStr) + " Dexterity: " + str(reqDex) + " Constitution: " + str(reqCon) + " Required Feats: " + reqFeats)

def confeatList():
    featFile = open("feats.txt", "r", encoding="utf-8")
    featInfo = json.load(featFile)
    featFile.close()
    constitution = featInfo['constitution']
    for keys in constitution:
        print(keys)