import json
import gameFeats


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

    def charSheet(self):

        featDict = gameFeats.featDict()[0]
        featList = gameFeats.featDict()[1]

        charName = self.name
        charLevel = self.level
        charHP = self.hp
        charFeats = self.tFeats
        charBaseDamage = self.baseDamage
        charHit = self.hit
        charDamage = self.damage
        charAC = self.ac
        charXP = self.xp
        nextLevel = self.nextLevel
        charStr = self.strength
        charDex = self.dexterity
        charCon = self.constitution
        remainingFeats = self.remainingFeats
        hasTaken = self.hasTaken

        for word in hasTaken:
            if word == "dexterous fighter":
                dexMod = int(charDex / 2)
                levelMod = int(1 + (charLevel / 2))
                charHit = dexMod + levelMod

            if word == "crushing blow":
                damageMod = 1
                charDamage = charDamage + damageMod
            elif word == "improved crushing blow":
                damageMod = 3
                charDamage = charDamage + damageMod
            elif word == "greater crushing blow":
                damageMod = 5
                charDamage = charDamage + damageMod
            else:
                pass

            if word == "precision strike":
                hitMod = 1
                charHit = charHit + hitMod
            elif word == "improved precision strike":
                hitMod = 3
                charHit = charHit + hitMod
            elif word == "greater precision strike":
                hitMod = 5
                charHit = charHit + hitMod
            else:
                pass

            if word == "lightning reflexes":
                acMod = 1
                charAC = charAC + acMod
            elif word == "improved lightning reflexes":
                acMod = 3
                charAC = charAC + acMod
            elif word == "greater lightning reflexes":
                acMod = 5
                charAC = charAC + acMod
            else:
                pass

            if word == "endurance":
                hpMod = 5
                charHP = charHP + hpMod
            elif word == "improved endurance":
                hpMod = 15
                charHP = charHP + hpMod
            elif word == "greater endurance":
                hpMod = 30
                charHP == charHP + hpMod
            else:
                pass

        print("Character Name:     " + charName)
        print("Level:              " + str(charLevel) + "       Strength:     " + str(charStr))
        print("Hit Points:         " + str(charHP) + "      Dexterity:    " + str(charDex))
        print("To Hit Modifier:    " + str(charHit) + "       Constitution: " + str(charCon))
        print("Base Damage:        " + charBaseDamage)
        print("Total Feats:        " + str(charFeats))
        print("Damage Modifier:    " + str(charDamage))
        print("Armor Class:        " + str(charAC))
        print("Current XP:         " + str(charXP))
        print("XP needed to level: " + str(nextLevel))

        print("Available feats:    " + str(remainingFeats))

        if not hasTaken:
            print("")
            print("No feats taken yet.")
            print("")
        else:
            print("")
            print(charName + "'s feats:")
            print("")

            for word in hasTaken:
                pos = hasTaken.index(word)
                print(hasTaken[pos] + ": ")
                print(featDict[0][hasTaken[pos]]['desc'])
                print("")


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


