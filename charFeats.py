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

def confeatList():
    featFile = open("feats.txt", "r", encoding="utf-8")
    featInfo = json.load(featFile)
    featFile.close()
    constitution = featInfo['constitution']
    for keys in constitution:
        print(keys)