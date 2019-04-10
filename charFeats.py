import json



def featList():
    featFile = open("feats.txt", "r", encoding="utf-8")
    featInfo = json.load(featFile)
    featFile.close()
    for key in featInfo.keys():
        print(key)