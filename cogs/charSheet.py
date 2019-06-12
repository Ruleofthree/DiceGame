import json
from cogs import gameFeats
import os

"""
This entire module is suppose to be your one stop shop for json files. It would detect which character profile you want
to load up (The program would prompt you to type in your character's name, which would also be the name of the text file
for that character's profile. I.E: A character named 'Irixis' would have a json named 'irixis.txt'), open the json file,
assign all values to a variable, then be allowed to carry those values to other modules. So far, it works for ONE other
module. charFeats.py pulls the returned values from the 'save' method correctly, but I'm unsure if I even did THAT
right, or even if that data is just 'static' data, and will not pull from updated information, such as when a character
has leveled.

In short, this method was SUPPOSE to be your place to write to, save, and load jsons. Right now though, I feel like it's
a failed attempt.

The only thing I have in this module that I am certain is working as intended is the charSheet method. When running the
dice game from diceGame.py. Typing 'char' then, 'viewchar', then entering a valid name of a character that has a json,
it will display that character's 'character sheet.'
"""

class SaveModule:
    #---------------------------------------VALUE LEGEND --------------------------------------------------------------
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


    # initialize needed variables. Did not put the three lines of code to open, load, and close a json file in __init__
    # because I am unsure if that is a smart thing to do. From what I understand, __init__ is ran every time a method
    # within it's class is ran. I don't need or want to have a json file open, load, and close every single time this
    # module is used. It seems inefficient and incorrect.
    def __init__(self):

        self.name = ""
        self.level = 0
        self.hp = 0
        self.tFeats = 0
        self.baseDamage = 0
        self.hit = 0
        self.damage = 0
        self.ac = 0
        self.xp = 0
        self.nextLevel = 0
        self.strength = 0
        self.dexterity = 0
        self.constitution = 0
        self.remainingFeats = 0
        self.hasTaken = 0
        self.ap = 0

    # A method INTENDED to be the hub of obtaining json data, and distributing it across modules when needed. Unsure if
    # it works as intended. Suspect it is not.
    # def save(self):
    #     name = self.name
    #     level = self.level
    #     hp = self.hp
    #     tFeats = self.tFeats
    #     baseDamage = self.baseDamage
    #     hit = self.hit
    #     damage = self.damage
    #     ac = self.ac
    #     xp = self.xp
    #     nextLevel = self.nextLevel
    #     strength = self.strength
    #     dexterity = self.dexterity
    #     constitution = self.constitution
    #     remainingFeats = self.remainingFeats
    #     hasTaken = self.hasTaken
    #     totalAP = self.ap
    #
    #     info = []
    #
    #     info.append(name)
    #     info.append(level)
    #     info.append(hp)
    #     info.append(tFeats)
    #     info.append(baseDamage)
    #     info.append(hit)
    #     info.append(damage)
    #     info.append(ac)
    #     info.append(xp)
    #     info.append(nextLevel)
    #     info.append(strength)
    #     info.append(dexterity)
    #     info.append(constitution)
    #     info.append(remainingFeats)
    #     info.append(hasTaken)
    #     info.append(totalAP)
    #
    #     return info

    # The one part of this module that does work. Loads in json of the desired character, and assigns variables to all
    # the data. Then displays the data in an easy to read format for the user.
    def charSheet(self):

        featDict = gameFeats.featDict()[0]
        featList = gameFeats.featDict()[1]

        character = input("Character name: ").lower()
        path = os.getcwd()
        charFolder = os.path.join(path + "/characters/")
        charFile = open(charFolder + character + ".txt", "r", encoding="utf-8")
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
        self.ap = charStats['total ap']

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
        charAP = self.ap

        # Looks in character json and sees if it has taken any of the following feats: dexterous fighter and any
        # variation of: crushing blow, precision strike, lightning reflexes, and endurance. If so, assign new values
        # accordingly.
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
                charHP = charHP + hpMod
            else:
                pass

        print("Character Name:     " + charName)
        print("Level:              " + str(charLevel) + "       Strength:     " + str(charStr))
        print("Hit Points:         " + str(charHP) + "      Dexterity:    " + str(charDex))
        print("To Hit Modifier:    " + str(int(charHit)) + "       Constitution: " + str(charCon))
        print("Base Damage:        " + charBaseDamage + "     Total Ability Points: " + str(charAP))
        print("Total Feats:        " + str(charFeats))
        print("Damage Modifier:    " + str(int(charDamage)))
        print("Armor Class:        " + str(int(charAC)))
        print("Current XP:         " + str(charXP))
        print("XP needed to level: " + str(nextLevel))
        print("Available feats:    " + str(remainingFeats))

        # Find if character sheet has any feats the list held in the 'feats taken' key of character's json. If the list
        # is empty, tell the player 'no feats taken yet.' If there are values, list them.
        if not hasTaken:
            print("")
            print("No feats taken yet.")
            print("")
        else:
            print("")
            print(charName + "'s feats:")
            print("")

            # take value index by index, and look in the feats json to display relevant information on character sheet,
            # along with feat name.
            for word in hasTaken:
                pos = hasTaken.index(word)
                print(hasTaken[pos] + ": ")
                print(featDict[0][hasTaken[pos]]['desc'])
                print("")


#-------------------------------------TEST CODE------------------------------------
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


