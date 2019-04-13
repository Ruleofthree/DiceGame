import json

def save(basics, abilities):
    # Create an empty dictionary
    characterFile = {}
    featList = []
    # basics[0] = Level
    # basics[1] = Hit Points                  abilities[2] = Hit Point Modifier
    # basics[2] = To Hit                      abilities[0] = To Hit Modifier
    # basics[3] = Damage                      abilities[0] = Damage Modifier
    # basics[4] = Total ability points
    # basics[5] = Total feats
    # basics[6] = Armor Class                 abilities[1] = Armor Class Modifier
    # basics[7] = player current xp
    # basics[8] = xp to next level
    # basics[9] = character


    # Fill the dictionary with required information

    characterFile["name"] = basics[9]
    name = basics[9]
    characterFile["level"] = basics[0]
    level = basics[0]
    characterFile["hitpoints"] = basics[1] + abilities[2]
    hp = basics[1] + abilities[2]
    characterFile["total feats"] = basics[5]
    tFeats = basics[5]
    characterFile["hit"] = basics[2] + abilities[0]
    hit = basics[2] + abilities[0]
    characterFile["damage"] = basics[2] + abilities[0]
    damage = basics[2] + abilities[0]
    characterFile["ac"] = basics[6] + abilities[1]
    ac = basics[6] + abilities[1]
    characterFile["currentxp"] = basics[7]
    xp = basics[7]
    characterFile["nextlevel"] = basics[8]
    nextLevel = basics[8]
    characterFile["strength"] = int(abilities[3])
    strength = int(abilities[3])
    characterFile["dexterity"] = int(abilities[4])
    dexterity = int(abilities[4])
    characterFile["constitution"] = int(abilities[5])
    constitution = int(abilities[5])
    characterFile["player feats"] = featList
    cFeats = featList
    # apply a hidden counter, that will keep track of number of feats throughout level progression
    characterFile["remaining feats"] = 2
    remainingFeats = 2

    # create the JSON file
    file = open(basics[9] + ".txt", "w", encoding="utf-8")
    json.dump(characterFile, file, ensure_ascii=False, indent=2)

    print("Your character has been created and saved.")
    return name, level, hp, tFeats, hit, damage, ac, xp, nextLevel, strength, dexterity, constitution, cFeats, remainingFeats


# def update(updateChar):
#     characterFile = {}
#
#     # basics[0] = Level
#     # basics[1] = Hit Points                  abilities[2] = Hit Point Modifier
#     # basics[2] = To Hit                      abilities[0] = To Hit Modifier
#     # basics[3] = Damage                      abilities[0] = Damage Modifier
#     # basics[4] = Total ability points
#     # basics[5] = Total feats
#     # basics[6] = Armor Class                 abilities[1] = Armor Class Modifier
#     # basics[7] = player current xp
#     # basics[8] = xp to next level
#     # basics[9] = character
#     #
#     # Fill the dictionary with required information
#
#     characterFile["level"] = charLevel
#     characterFile["strength"] = charStr
#     characterFile["dexterity"] = charDex
#     characterFile["constitution"] = charCon
#     characterFile["player feats"] = playerFeats
#     characterFile["remaining feats"] = remainingFeats
#
#     file = open(charName + ".txt", "w", encoding="utf-8")
#     json.dump(characterFile, file, ensure_ascii=False, indent=2)


