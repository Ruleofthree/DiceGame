import json

# a simple function designed to open up the feats json, and parse out all the keys into a separate list. Intended for
# ease of use in other modules. Works as intended in charFeats.py
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