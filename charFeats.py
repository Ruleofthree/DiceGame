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
    for keys in dexterity:
        print(keys)
    select = input("For information on a listed feat, type 'help <feat>'\n"
          "To choose a listed feet, type 'choose <feat>': ")
    if select[:4] == 'help':
        featSelected = select[5:]
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