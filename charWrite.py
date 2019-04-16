import json
import charInfo


class SaveModule:

    #                 # # basics[0] = Level
    #                 # # basics[1] = Hit Points                  abilities[2] = Hit Point Modifier
    #                 # # basics[2] = To Hit                      abilities[0] = To Hit Modifier
    #                 # # basics[3] = Damage                      abilities[0] = Damage Modifier
    #                 # # basics[4] = Total ability points
    #                 # # basics[5] = Total feats
    #                 # # basics[6] = Armor Class                 abilities[1] = Armor Class Modifier
    #                 # # basics[7] = player current xp
    #                 # # basics[8] = xp to next level
    #                 # # basics[9] = character

    def __init__(self):

        charFile = open("Irixis.txt", "r", encoding="utf-8")
        charStats = json.load(charFile)
        charFile.close()
        self.name = charStats['name']
        self.level = charStats['level']
        self.hp = charStats['hitpoints']
        self.tFeats = charStats['total feats']
        self.baseDamage = charStats['base damage']
        self.hit = charStats['hit']
        self.damage = charStats['damage modifier']
        self.ac = charStats['ac']
        self.xp = charStats['currentxp']
        self.nextLevel = charStats['nextlevel']
        self.strength = charStats['strength']
        self.dexterity = charStats['dexterity']
        self.constitution = charStats['constitution']
        self.remainingFeats = charStats['remaining feats']
        self.hasTaken = charStats['feats taken']


    def save(self):
        name = self.name
        level = self.level
        hp = self.hp
        tFeats = self.tFeats
        baseDamage = self.baseDamage
        hit = self.hit
        damage = self.damage
        ac = self.ac
        xp = self.xp
        nextLevel = self.nextLevel
        strength = self.strength
        dexterity = self.dexterity
        constitution = self.constitution
        remainingFeats = self.remainingFeats
        hasTaken = self.hasTaken

        info = []

        info.append(name)
        info.append(level)
        info.append(hp)
        info.append(tFeats)
        info.append(baseDamage)
        info.append(hit)
        info.append(damage)
        info.append(ac)
        info.append(xp)
        info.append(nextLevel)
        info.append(strength)
        info.append(dexterity)
        info.append(constitution)
        info.append(remainingFeats)
        info.append(hasTaken)

        return info


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


