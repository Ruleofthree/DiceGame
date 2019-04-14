import json

class SaveModule:

    def __init__(self, basics, abilities):
        self.name = basics[9]
        # self.level = level
        self.hp = basics[1] + abilities[2]
        # self.tFeats = tFeats
        # self.hit = shit
        # self.damage = damage
        # self.ac = ac
        # self.xp = xp
        # self.nextLevel = nextLevel
        # self.strength = strength
        # self.dexterity = dexterity
        # self.constitution = constitution
        # create the JSON file
        # file = open(basics[9] + ".txt", "w", encoding="utf-8")
        # json.dump(characterFile, file, ensure_ascii=False, indent=2)
        #
        # print("Your character has been created and saved.")

    def outputOriginal(self):
        SaveModule.__init__(self, basics, abilities)


        # Create an empty dictionary
        # characterFile = {}
        # featList = []
        # # basics[0] = Level
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

        # characterFile["name"] = self.name
        # name = self.name
        # characterFile["level"] = name
        # level = name
        # characterFile["hitpoints"] = basics[1] + abilities[2]
        # hp = basics[1] + abilities[2]
        # characterFile["total feats"] = basics[5]
        # tFeats = basics[5]
        # characterFile["hit"] = basics[2] + abilities[0]
        # hit = basics[2] + abilities[0]
        # characterFile["damage"] = basics[2] + abilities[0]
        # damage = basics[2] + abilities[0]
        # characterFile["ac"] = basics[6] + abilities[1]
        # ac = basics[6] + abilities[1]
        # characterFile["currentxp"] = basics[7]
        # xp = basics[7]
        # characterFile["nextlevel"] = basics[8]
        # nextLevel = basics[8]
        # characterFile["strength"] = int(abilities[3])
        # strength = int(abilities[3])
        # characterFile["dexterity"] = int(abilities[4])
        # dexterity = int(abilities[4])
        # characterFile["constitution"] = int(abilities[5])
        # constitution = int(abilities[5])
        # characterFile["player feats"] = featList
        # cFeats = featList
        # # apply a hidden counter, that will keep track of number of feats throughout level progression
        # characterFile["remaining feats"] = 2
        # remainingFeats = 2
        #
        # # create the JSON file
        # file = open(basics[9] + ".txt", "w", encoding="utf-8")
        # json.dump(characterFile, file, ensure_ascii=False, indent=2)
        # self.name = name
        # self.level = level
        # self.hp = hp
        # self.tFeats = tFeats
        # self.hit = shit
        # self.damage = damage
        # self.ac = ac
        # self.xp = xp
        # self.nextLevel = nextLevel
        # self.strength = strength
        # self.dexterity = dexterity
        # self.constitution = constitution


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


