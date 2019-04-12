import json

"""
This script is dedicated to pulling up helpful information on feats, as well as selecting them to be placed on the
character sheet. Essentially, all three list functions contain the exact same code, the only difference being the
variables assigned to ensure the function is grabbing from the right category. This makes me feel like this can be
bunched together as one single function. Will look in to this later.
"""

def feats():
    # Open up the json object containing the list of feats.
    featFile = open("feats.txt", "r", encoding="utf-8")
    featInfo = json.load(featFile)
    featFile.close()
    # place all keys within a list for comparison later
    featDict = []
    for keys in featInfo[0]:
        featDict.append(keys)
    print(featDict)
    print(featInfo[0][featDict[0]]['stat'])
    print(featDict[0])
feats()
