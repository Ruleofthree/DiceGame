import json
import charInfo

class SaveModule:

    def __init__(self, basics, abilities):
        self.name = basics[9]
        self.level = basics[0]
        self.hp = basics[1] + abilities[2]
        self.tFeats = basics[5]
        self.hit = basics[2] + abilities[0]
        self.damage = basics[3] + abilities[0]
        self.ac = basics[6] + abilities[1]
        self.xp = basics[7]
        self.nextLevel = basics[8]
        self.strength = abilities[0]
        self.dexterity = abilities[1]
        self.constitution = abilities[2]


    def outputOriginal(self):

        # Create an empty dictionary
        characterFile = {}

        # Fill the dictionary with required information

        name = self.name
        characterFile["name"] = name
        level = self.level
        characterFile["level"] = level
        hp = self.hp
        characterFile["hitpoints"] = hp
        tFeats = self.tFeats
        characterFile["total feats"] = tFeats
        hit = self.hit
        characterFile["hit"] = hit
        damage = self.damage
        characterFile["damage"] = damage
        ac = self.ac
        characterFile["ac"] = ac
        xp = self.xp
        characterFile["currentxp"] = xp
        nextLevel = self.level
        characterFile["nextlevel"] = nextLevel
        strength = self.strength
        characterFile["strength"] = strength
        dexterity = self.dexterity
        characterFile["dexterity"] = dexterity
        constitution = self.constitution
        characterFile["constitution"] = constitution

        # apply a hidden counters, that will keep track of number of feats throughout level progression
        characterFile["remaining feats"] = 2
        remainingFeats = 2
        hasTaken = 0

        print("Your character has been saved.")
        # create the JSON file
        file = open(name + ".txt", "w", encoding="utf-8")
        json.dump(characterFile, file, ensure_ascii=False, indent=2)
        return [name, level, hp, tFeats, hit, damage, ac, xp, nextLevel, strength, dexterity, constitution, remainingFeats, hasTaken]



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


