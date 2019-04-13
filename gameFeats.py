import json

def featDict():
    # Open up the json object containing the list of feats.
    featFile = open("feats.txt", "r", encoding="utf-8")
    featDict = json.load(featFile)
    featFile.close()

    # place all keys within a list for comparison later
    featList = []
    for keys in featDict[0]:
        featList.append(keys)
    return featDict, featList