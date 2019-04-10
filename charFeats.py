import json

"""
This script is dedicated to pulling up helpful information on feats, as well as selecting them to be placed on the
character sheet. Essentially, all three list functions contain the exact same code, the only difference being the
variables assigned to ensure the function is grabbing from the right category. This makes me feel like this can be
bunched together as one single function. Will look in to this later.
"""

def strfeatList():
    # Open up the json object containing the list of feats.
    featFile = open("feats.txt", "r", encoding="utf-8")
    featInfo = json.load(featFile)
    featFile.close()
    # obtain only the list of feats within the strength dictionary
    strength = featInfo['strength']
    # place all keys within a list for comparison later
    featDict = []
    for keys in strength:
        print(keys)
        featDict.append(keys)
    # keeps the user in the list group until they assign 'quit' to the variable 'select.'
    select = ""
    while select != "quit":
        select = input("For information on a listed feat, type 'help <feat>'\n"
                       "to exit out of the list, type 'quit'").lower()
        featSelected = select[5:]
        # check to see if first 4 characters of 'select' reads 'quit' If so, exit List.
        quitList = select[:4]
        if quitList == "quit":
            print("Exiting List")
        # check to see if the 6th character and beyond match a key in the 'featDict' variable. If not, restart while
        # loop.
        elif featSelected not in featDict:
            print("It appears you typed in a feat that does not exist.")
        # if answer matches a key, grab corresponding information and display it.
        else:
            desc = strength[featSelected]['desc']
            level = strength[featSelected]['requirements'][0]
            reqStr = strength[featSelected]['requirements'][1]
            reqDex = strength[featSelected]['requirements'][2]
            reqCon = strength[featSelected]['requirements'][3]
            reqFeats = strength[featSelected]['requirements'][4]
            print(desc)
            print("Prerequisites: " + "Level: " + str(level) + " Strength: " + str(reqStr) + " Dexterity: " + str(reqDex) + " Constitution: " + str(reqCon) + " Required Feats: " + reqFeats)

def dexfeatList():
    featFile = open("feats.txt", "r", encoding="utf-8")
    featInfo = json.load(featFile)
    featFile.close()
    dexterity = featInfo['dexterity']
    featDict = []
    for keys in dexterity:
        print(keys)
        featDict.append(keys)
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
    featDict = []
    for keys in constitution:
        print(keys)
        featDict.append(keys)
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
            desc = constitution[featSelected]['desc']
            level = constitution[featSelected]['requirements'][0]
            reqStr = constitution[featSelected]['requirements'][1]
            reqDex = constitution[featSelected]['requirements'][2]
            reqCon = constitution[featSelected]['requirements'][3]
            reqFeats = constitution[featSelected]['requirements'][4]
            print(desc)
            print("Prerequisites: " + "Level: " + str(level) + " Strength: " + str(reqStr) + " Dexterity: " + str(
                reqDex) + " Constitution: " + str(reqCon) + " Required Feats: " + reqFeats)