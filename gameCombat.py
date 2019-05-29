import json
import random
import gameFeats

class Combat:

    def __init__(self):
        #STRINGS
        self.playerOne = ""
        self.playerTwo = ""
        self.winner = ""
        # PLAYER INFO
        self.pOneInfo = {}
        self.pTwoInfo = {}
        # HP AND TURN COUNTERS
        self.count = 0
        self.token = 0
        self.critical = 0
        self.totalDamage = 0
        self.pOneTotalHP = 0
        self.pTwoTotalHP = 0
        self.pOneCurrentHP = 0
        self.pTwoCurrentHP = 0
        # PLAYER ONE FEAT COUNTERS
        self.pOnepMod = 0
        self.pOnecMod = 0
        self.pOnedMod = 0
        self.pOnemMod = 0
        self.pOneEvade = 1
        self.pOneQuickDamage = 0
        self.pOneFeatInfo = None
        self.pOneSpentFeat =[]
        # self.pOneCripple = 0
        # PLAYER TWO FEAT COUNTERS
        self.pTwopMod = 0
        self.pTwocMod = 0
        self.pTwodMod = 0
        self.pTwomMod = 0
        self.pTwoEvade = 1
        self.pTwoQuickDamage = 0
        self.pTwoFeatInfo = None
        self.pTwoSpentFeat = []
        # self.pTwoCripple = 0
        # XP AND LEVEL COUNTERS
        self.pOneLevel = 0
        self.pTwoLevel = 0
        self.xp = 0
        self.currentPlayerXP = 0
        self.nextLevel = 0
        self.levelUp = 0


    def setupData(self):
        # opens and loads in player one's character sheet. This is done in this method solely because I'm unsure if
        # loading json files in __init__ is actually a good idea. If I understand things correctly, things in a class's
        # __init__ is ran EVERY TIME a method is called within it. If so, then the json files would be opened, loaded,
        # and closed multiple times in a single run. Seems inefficient, and bad coding.
        self.playerOne = input("Who is the challenger? ")
        charFile = open(self.playerOne + ".txt", "r", encoding="utf-8")
        pOneInfo = json.load(charFile)
        charFile.close()
        self.pOneInfo = pOneInfo

        self.playerTwo = input("And their opponent? ")
        charFile = open(self.playerTwo + ".txt", "r", encoding="utf-8")
        pTwoInfo = json.load(charFile)
        charFile.close()
        self.pTwoInfo = pTwoInfo

        self.pOneTotalHP = pOneInfo['hitpoints']
        self.pTwoTotalHP = pTwoInfo['hitpoints']
        self.pOneCurrentHP = pOneInfo['hitpoints']
        self.pTwoCurrentHP = pTwoInfo['hitpoints']
        self.pOneLevel = pOneInfo['level']
        self.pTwoLevel = pTwoInfo['level']

        self.initiative()

    # method dedicated to determining who goes first in combat. Simulates a roll of a 20-sided die (1-20), then adds
    # character's dexterity modifier (dexterity score divided by 2). In the event of a tie, determines who goes first
    # by finding the highest dexterity modifier between opponents. Should THAT tie as well, does a coin flip.

    def initiative(self):
        playerOneInit = random.randint(1, 20)
        playerOneMod = int(self.pOneInfo['dexterity'] / 2)
        totalOne = playerOneInit + playerOneMod
        print(self.playerOne.capitalize() +" rolled: " + str(playerOneInit) + " + " + str(playerOneMod) + " and got " + str(totalOne))

        playerTwoInit = random.randint(1, 20)
        playerTwoMod = int(self.pTwoInfo['dexterity'] / 2)
        totalTwo = playerTwoInit + playerTwoMod
        print(self.playerTwo.capitalize() + " rolled: " + str(playerTwoInit) + " + " + str(playerTwoMod) + " and got " + str(totalTwo))

        if totalOne > totalTwo:
            print(self.playerOne.capitalize() + " Goes first")
            token = 1
            self.token = token
            self.pOneFeatUsed()
            self.determineHitPOne()
        elif totalTwo > totalOne:
            print(self.playerTwo.capitalize() + " Goes first")
            token = 2
            self.token = token
            self.pTwoFeatUsed()
            self.determineHitPTwo()
        elif totalOne == totalTwo:
            print("In result of tie, person with highest dexterity modifier goes first:")
            print(self.playerOne.capitalize() + "'s dexterity: " + str(playerOneMod))
            print(self.playerTwo.capitalize() + "'s dexterity: " + str(playerTwoMod))

            if playerOneMod > playerTwoMod:
                print(self.playerOne.capitalize() + " Goes first")
                token = 1
                self.token = token
                self.pOneFeatUsed()
                self.determineHitPOne()
            elif playerOneMod < playerTwoMod:
                print(self.playerTwo.capitalize() + " Goes first")
                token = 2
                self.token = token
                self.pTwoFeatUsed()
                self.determineHitPTwo()
            else:
                print("As both dexterity values are equal as well. A coin flip. Value of one means " + self.playerOne +  " goes first")
                value = random.randint(1, 2)
                print(value)

                if value == 1:
                    print(self.playerOne + " Goes first")
                    token = 1
                    self.token = token
                    self.pOneFeatUsed()
                    self.determineHitPOne()
                else:
                    print(self.playerTwo + " Goes first")
                    token = 2
                    self.token = token
                    self.pTwoFeatUsed()
                    self.determineHitPTwo()

    def pOneFeatUsed(self):
        featDict = gameFeats.featDict()[0]
        pOneLastFeat = None
        while pOneLastFeat is None:
            pOneLastFeat = input(self.playerOne.capitalize() + " Do you wish to use a feat? (type full name of feat here, or 'none'): ")
            if pOneLastFeat == 'none':
                pOneLastFeat = None
                self.pOneFeatInfo = pOneLastFeat
                return pOneLastFeat
            elif pOneLastFeat in ('power attack', 'combat expertise', 'defensive fighting', 'masochist', 'hurt me', 'improved hurt me', 'greater hurt me', 'hurt me more', 'evasion', 'improved evasion', 'greater evasion'):
                print(pOneLastFeat + " will be determined after this phase.")
                pOneLastFeat = None
            elif pOneLastFeat in self.pOneSpentFeat:
                print("You have already used this feat. Please select another or type 'none.': ")
                pOneLastFeat = None
            elif pOneLastFeat in self.pOneInfo['feats taken']:
                print()
                self.pOneSpentFeat.append(pOneLastFeat)
                self.pOneFeatInfo = [pOneLastFeat, featDict[0][pOneLastFeat]['action']]
                return self.pOneFeatInfo
            elif pOneLastFeat not in self.pOneInfo['feats taken']:
                print("Either you do not have that feat, or you did not type it correctly")
                pOneLastFeat = None

    def pTwoFeatUsed(self):
        featDict = gameFeats.featDict()[0]
        pTwoLastFeat = None
        while pTwoLastFeat is None:
            pTwoLastFeat = input(self.playerTwo.capitalize() + " Do you wish to use a feat? (type full name of feat here, or 'none'): ")
            if pTwoLastFeat == 'none':
                pTwoLastFeat = None
                self.pTwoFeatInfo = pTwoLastFeat
                return pTwoLastFeat
            elif pTwoLastFeat in (
            'power attack', 'combat expertise', 'defensive fighting', 'masochist', 'hurt me', 'improved hurt me',
            'greater hurt me', 'hurt me more', 'evasion', 'improved evasion', 'greater evasion'):
                print(pTwoLastFeat + " will be determined after this phase.")
                pTwoLastFeat = None
            elif pTwoLastFeat in self.pTwoSpentFeat:
                print("You have already used this feat. Please select another or type 'none.': ")
                pTwoLastFeat = None
            elif pTwoLastFeat in self.pTwoInfo['feats taken']:
                print()
                self.pTwoSpentFeat.append(pTwoLastFeat)
                self.pTwoFeatInfo = [pTwoLastFeat, featDict[0][pTwoLastFeat]['action']]
                return self.pTwoFeatInfo
            elif pTwoLastFeat not in self.pTwoInfo['feats taken']:
                print("Either you do not have that feat, or you did not type it correctly")
                pTwoLastFeat = None

    # Next two methods are created to see if a character hit the other character or not. Simulates rolling 1d20 (1-20)
    # then adding any modifiers to the result. If the total either meets or exceeds the other players AC, notify the
    # players that the hit was successful, then move on to the damage methods. If the total does not, notify player
    # that it was a miss, and move on to other player's turn.
    # Note: I want to add in a result that will double damage if the ROLL is a 20, not the total.

    def determineHitPOne(self):

        # assign both player's feat selections to variables
        pOneFeatUsed = self.pOneFeatInfo
        pTwoFeatUsed = self.pTwoFeatInfo

        # If a feat wasn't used by a player, assign it default values.
        if pOneFeatUsed is None:
            pOneFeatUsed = ["none", 0]
        if pTwoFeatUsed is None:
            pTwoFeatUsed = ["none", 0]
        print(pOneFeatUsed)

        # If the feat used was 'true strike' forgo rolling to see if player hit opponent, and go straight to damage.
        if pOneFeatUsed[0] == "true strike":
            print(self.playerOne.capitalize() + " used the feat 'True Strike.' And forgoes the need to determine if hit was success.")
            self.determineDamagePOne()

        # Otherwise, continue on with the bulk of this method
        else:
            pOneToHit = self.pOneInfo['hit']
            pTwoAC = self.pTwoInfo['ac']

            # If Player One has power attack, combat expertise, defensive fighting, or masochist, go to those methods first
            # before continuing.
            for word in self.pOneInfo["feats taken"]:
                if word == "power attack":
                    self.pOnepMod = self.pOnePowerAttack()
                if word == "combat expertise":
                    self.pOnecMod = self.pOneCombatExpertise()
                if word == "defensive fighting":
                    self.pOnedMod = self.pOneDefensiveFighting()
                if word == "masochist":
                    self.pOnemMod = self.pOneMasochist()
            pMod = self.pOnepMod
            cMod = self.pOnecMod
            dMod = self.pOnedMod
            mMod = self.pOnemMod
            pTwodMod = self.pTwodMod
            pTwomMod = self.pTwomMod

            # determine the roll of the 1d20.
            hit = random.randint(1, 20)

            # if the raw result is equal to 20, count the critical counter up to 1.
            if hit == 20:
                self.critical = 1
                print(self.playerOne.capitalize() + " has critically hit.")

            # calculate the total after modifiers
            total = int(hit + pOneToHit - pMod + cMod - dMod + mMod)

            # if any version of crippling blow was used, tack on the penalty to the above total
            if pTwoFeatUsed[0] == "crippling blow" or pTwoFeatUsed[0] == "improved crippling blow" or pTwoFeatUsed[0] == "greater crippling blow":
                print(self.playerTwo + " Used " + pTwoFeatUsed[0] + ", Giving " + self.playerOne + " a " + str(pTwoFeatUsed[1]) + " To their attack.")
                total = total + pTwoFeatUsed[1]

            # testing data to see that modifiers are carrying over correctly. Delete this when project is finished.
            print("Roll: " + str(hit) + " Base: " + str(pOneToHit) + " PA: " + str(pMod) + " CE: " + str(cMod) + " DF: " + str(dMod) + " MC: " + str(mMod))

            # find Player One's total AC
            totalAC = pTwoAC + pTwodMod - pTwomMod

            # testing data to see that modifiers are carrying over correctly. Delete this when project is finished.
            print("P2 AC: " + str(pTwoAC) + " DF: " + str(pTwodMod) + " MC: " + str(pTwomMod))

            # determine if the total roll, after all modifiers have been included, is a successful hit or not. then
            # head to the appropriate method
            if total >= totalAC:
                print(self.playerOne + " rolled a " + str(total) + " to hit an AC " + str(totalAC) + " and was successful.")
                self.pTwodMod = 0
                self.pTwomMod = 0
                self.determineDamagePOne()
            else:
                print(self.playerTwo + " rolled a " + str(total) + " to hit an AC " + str(totalAC) + " and missed.")
                self.pTwodMod = 0
                self.pTwomMod = 0
                self.scoreboard()

    def determineHitPTwo(self):
        # assign both player's feat selections to variables
        pOneFeatUsed = self.pOneFeatInfo
        pTwoFeatUsed = self.pTwoFeatInfo

        # If a feat wasn't used by a player, assign it default values.
        if pOneFeatUsed is None:
            pOneFeatUsed = ["none", 0]
        if pTwoFeatUsed is None:
            pTwoFeatUsed = ["none", 0]

        # If the feat used was 'true strike' forgo rolling to see if player hit opponent, and go straight to damage.
        if pTwoFeatUsed[0] == "true strike":
            print(self.playerTwo.capitalize() + " used the feat 'True Strike.' And forgoes the need to determine if hit was success.")
            self.determineDamagePTwo()

        # Otherwise, continue on with the bulk of this method
        else:
            pTwoToHit = self.pTwoInfo['hit']
            pOneAC = self.pOneInfo['ac']

            # If Player Two has power attack, combat expertise, defensive fighting, or masochist, go to those methods first
            # before continuing.
            for word in self.pTwoInfo["feats taken"]:
                if word == "power attack":
                    self.pTwopMod = self.pTwoPowerAttack()
                if word == "combat expertise":
                    self.pTwocMod = self.pTwoCombatExpertise()
                if word == "defensive fighting":
                    self.pTwodMod = self.pTwoDefensiveFighting()
                if word == "masochist":
                    self.pTwomMod = self.pTwoMasochist()
            pMod = self.pTwopMod
            cMod = self.pTwocMod
            dMod = self.pTwodMod
            mMod = self.pTwomMod
            pOnedMod = self.pOnedMod
            pOnemMod = self.pOnemMod

            # determine the roll of the 1d20.
            hit = random.randint(1, 20)

            # if the raw result is equal to 20, count the critical counter up to 1.
            if hit == 20:
                self.critical = 1
                print(self.playerTwo.capitalize() + " has critically hit.")

            # calculate the total after modifiers
            total = int(hit + pTwoToHit - pMod + cMod - dMod + mMod)

            # if any version of crippling blow was used, tack on the penalty to the above total
            if pOneFeatUsed[0] == "crippling blow" or pOneFeatUsed[0] == "improved crippling blow" or pOneFeatUsed[0] == "greater crippling blow":
                print(self.playerOne.capitalize() + " Used " + pOneFeatUsed[0] + ", Giving " + self.playerTwo.capitalize() + " a " + str(pOneFeatUsed[1]) + " To their attack.")
                total = total + pOneFeatUsed[1]

            # testing data to see that modifiers are carrying over correctly. Delete this when project is finished.
            print("Roll: " + str(hit) + " Base: " + str(pTwoToHit) + " PA: " + str(pMod) + " CE: " + str(cMod) + " DF: " + str(dMod) + " MC: " + str(mMod))

            # find Player One's total AC
            totalAC = int(pOneAC + pOnedMod - pOnemMod)

            # testing data to see that modifiers are carrying over correctly. Delete this when project is finished.
            print(" P1 AC: " + str(pOneAC) + " DF: " + str(pOnedMod) + " MC: " + str(pOnemMod))

            # determine if the total roll, after all modifiers have been included, is a successful hit or not. then
            # head to the appropriate method
            if total >= pOneAC:
                print(self.playerTwo.capitalize() + " rolled a " + str(total) + " to hit an AC " + str(totalAC) + " and was successful.")
                self.pOnedMod = 0
                self.pOnemMod = 0
                self.determineDamagePTwo()
            else:
                print(self.playerTwo.capitalize() + " rolled a " + str(total) + " to hit an AC " + str(totalAC) + " and missed.")
                self.pOnedMod = 0
                self.pOnemMod = 0
                self.scoreboard()


    # Next two methods will determine how much damage is done after a successful hit. It finds the value placed in the
    # 'base damage' key of the character's json, Parses it out to remove the 'd', and uses the first number as the
    # minimum range, and second for the maximum. After determining the random value, then adds any modifiers to the roll
    # and displays that as the damage.
    # Note: Want to add in capabilities to double the ROLL of the damage only, should the player have rolled a 'natural
    # 20' to hit (value of 20 before any modifiers were added)

    def determineDamagePOne(self):

        # assign both player's feat selections to variables.
        pOneFeatUsed = self.pOneFeatInfo
        pTwoFeatUsed = self.pTwoFeatInfo

        # If a feat wasn't used by a player, assign it default values.
        if pOneFeatUsed is None:
            pOneFeatUsed = ["none", 0]
        if pTwoFeatUsed is None:
            pTwoFeatUsed = ["none", 0]

        # Obtain Player One's base damage and base modifier, and roll damage. Assign 'power attack' and 'combat defense'
        # modifiers to variables, and roll damage.
        pOneBaseDamage = self.pOneInfo['base damage']
        pOneModifier = self.pOneInfo['damage modifier']
        pOneMinimum, pOneMaximum = pOneBaseDamage.split('d')
        pMod = self.pOnepMod
        cMod = self.pOnecMod
        damage = random.randint(int(pOneMinimum), int(pOneMaximum))

        # if critical counter is a value of 1, double the damage done, then reset counter to 0.
        if self.critical == 1:
            damage = damage * 2
            self.critical = 0

        # if Player One used feat 'titan blow', apply 50% bonus damage.
        if pOneFeatUsed[0] == "titan blow":
            print(self.playerOne.capitalize() + " used the feat 'titan blow'.")
            damage = damage * float(pOneFeatUsed[1])

        # if Player Two use 'staggering blow' half damage done.
        if pTwoFeatUsed[0] == "staggering blow":
            print(self.playerTwo.capitalize() + " used the feat 'staggering blow', halving " + self.playerOne.capitalize() + "'s damage roll")
            damage = damage * float(pTwoFeatUsed[1])

        # ensure that no matter what, raw damage can not fall below 1, then assign total damage to variable, and in turn
        # assign it to variable to be accessed for scoreboard.
        if damage < 1:
            damage = 1
        total = int(damage + pOneModifier + pMod - cMod)

        # if Player Two used 'quick strike', 'improved quick strike', or 'greater quick strike', apply the return
        # damage here
        pTwoBaseDamage = self.pTwoInfo['base damage']
        pTwoModifier = self.pTwoInfo['damage modifier']
        pTwoMinimum, pTwoMaximum = pTwoBaseDamage.split('d')
        pMod = self.pTwopMod
        cMod = self.pTwocMod

        # apply the damage from 'quick strike', 'improved quick strike', or 'greater quick strike' if such feats were
        # used
        if pTwoFeatUsed[0] == "quick strike":

            # Roll damage for Player One, and multiply it by desired amount.
            damage = random.randint(int(pTwoMinimum), int(pOTwoMaximum))
            total = (damage + pTwoModifier + pMod - cMod)
            quickDamage = int(total * float(pTwoFeatUsed[1]))

            # Ensure damage is always at least 1hp and print out result
            if quickDamage < 1:
                quickDamage = 1
            self.pTwoQuickDamage = quickDamage
            self.pOneCurrentHP = self.pOneCurrentHP - self.pTwoQuickDamage
            print(self.playerTwo.capitalize() + " used 'quick strike,' managing to do an additional " + str(
                self.pTwoQuickDamage) + "hp of damage.")

        if pTwoFeatUsed[0] == "improved quick strike":

            # Roll damage for Player one, and multiply it by desired amount.
            damage = random.randint(int(pTwoMinimum), int(pTwoMaximum))
            total = (damage + pTwoModifier + pMod - cMod)
            quickDamage = int(total * float(pTwoFeatUsed[1]))

            # Ensure damage is always at least 1hp and print out result
            if quickDamage < 1:
                quickDamage = 1
            self.pTwoQuickDamage = quickDamage
            self.pOneCurrentHP = self.pOneCurrentHP - self.pTwoQuickDamage
            print(self.playerTwo.capitalize() + " used 'quick strike,' managing to do an additional " + str(
                self.pTwoQuickDamage) + "hp of damage.")

        if pTwoFeatUsed[0] == "greater quick strike":
            # roll damage for player One, and multiply it by desired amount
            damage = random.randint(int(pTwoMinimum), int(pTwoMaximum))
            total = (damage + pTwoModifier + pMod - cMod)
            quickDamage = int(total * float(pTwoFeatUsed[1]))

            # Ensure damage is always at least 1hp and print out result
            self.pTwoQuickDamage = quickDamage
            self.pOneCurrentHP = self.pOneCurrentHP - self.pTwoQuickDamage
            print(self.playerTwo.capitalize() + " used 'quick strike,' managing to do an additional " + str(
                self.pTwoQuickDamage) + "hp of damage.")

        #If Player Two has Evasion, Improved Evasion, or Greater Evasion, give them the option to use it.
        for word in self.pTwoInfo['feats taken']:
            if self.pTwoEvade == 1 and word == "evasion":
                answer = input(self.playerTwo.capitalize() + ", do you wish to evade?").lower()
                if answer == "yes":
                    total = int(total * 0.75)
                    self.totalDamage = total
                    self.pTwoEvade = 0
            elif self.pTwoEvade == 1 and word == "improved evasion":
                answer = input(self.playerTwo.capitalize() + ", do you wish to evade?").lower()
                if answer == "yes":
                    total = int(total * 0.5)
                    self.totalDamage = total
                    self.pTwoEvade = 0
            elif self.pTwoEvade == 1 and word == "improved evasion":
                answer = input(self.playerTwo.capitalize() + ", do you wish to evade?").lower()
                if answer == "yes":
                    total = 0
                    self.totalDamage = total
                    self.pTwoEvade = 0

        self.totalDamage = total

        # testing data to see that modifiers are carrying over correctly. Delete this when project is finished.
        print("Roll: " + str(damage) + " Modifier: " + str(pOneModifier) + " PA: " + str(pMod) + " CD: " + str(cMod))

        # display total damage done, and reset passive feat counters (power attack and combat defense)
        print(self.playerOne.capitalize() + " did " + str(total) + " points of damage.")
        self.pOnepMod = 0
        self.pOnecMod = 0
        self.getHitPointsPTwo()

    def determineDamagePTwo(self):

        # assign both player's feat selections to variables.
        pOneFeatUsed = self.pOneFeatInfo
        pTwoFeatUsed = self.pTwoFeatInfo

        # If a feat wasn't used by a player, assign it default values.
        if pOneFeatUsed is None:
            pOneFeatUsed = ["none", 0]
        if pTwoFeatUsed is None:
            pTwoFeatUsed = ["none", 0]

        # Obtain Player Two's base damage and base modifier, and roll damage. Assign 'power attack' and 'combat defense'
        # modifiers to variables, and roll damage.
        pTwoBaseDamage = self.pTwoInfo['base damage']
        pTwoModifier = self.pTwoInfo['damage modifier']
        pTwoMinimum, pTwoMaximum = pTwoBaseDamage.split('d')
        pMod = self.pTwopMod
        cMod = self.pTwocMod
        damage = random.randint(int(pTwoMinimum), int(pTwoMaximum))

        # if critical counter is a value of 1, double the damage done, then reset counter to 0.
        if self.critical == 1:
            damage = damage * 2
            self.critical = 0

        # if Player Two used feat 'titan blow', apply 50% bonus damage.
        if pTwoFeatUsed[0] == "titan blow":
            print(self.playerTwo.capitalize() + " used the feat 'titan blow'.")
            damage = damage * float(pTwoFeatUsed[1])

        # if Player One use 'staggering blow' half damage done.
        if pOneFeatUsed[0] == "staggering blow":
            print(self.playerOne.capitalize() + " used the feat 'staggering blow', halving " + self.playerTwo.capitalize() + "'s damage roll")
            damage = damage * float(pOneFeatUsed[1])

        # ensure that no matter what, raw damage can not fall below 1, then assign total damage to variable, and in turn
        # assign it to variable to be accessed for scoreboard.
        if damage < 1:
            damage = 1
        total = int(damage + pTwoModifier + pMod - cMod)

        # if Player One used 'quick strike', 'improved quick strike', or 'greater quick strike', apply the return
        # damage here
        pOneBaseDamage = self.pOneInfo['base damage']
        pOneModifier = self.pOneInfo['damage modifier']
        pOneMinimum, pOneMaximum = pOneBaseDamage.split('d')
        pMod = self.pOnepMod
        cMod = self.pOnecMod

        # apply the damage from 'quick strike', 'improved quick strike', or 'greater quick strike' if such feats were
        # used
        if pOneFeatUsed[0] == "quick strike":

            # Roll damage for Player One, and multiply it by desired amount.
            damage = random.randint(int(pOneMinimum), int(pOneMaximum))
            total = (damage + pOneModifier + pMod - cMod)
            quickDamage = int(total * float(pOneFeatUsed[1]))

            # Ensure damage is always at least 1hp and print out result
            if quickDamage < 1:
                quickDamage = 1
            self.pOneQuickDamage = quickDamage
            self.pTwoCurrentHP = self.pTwoCurrentHP - self.pOneQuickDamage
            print(self.playerOne.capitalize() + " used 'quick strike,' managing to do an additional " + str(
                self.pOneQuickDamage) + "hp of damage.")

        if pOneFeatUsed[0] == "improved quick strike":

            # Roll damage for Player one, and multiply it by desired amount.
            damage = random.randint(int(pOneMinimum), int(pOneMaximum))
            total = (damage + pOneModifier + pMod - cMod)
            quickDamage = int(total * float(pOneFeatUsed[1]))

            # Ensure damage is always at least 1hp and print out result
            if quickDamage < 1:
                quickDamage = 1
            self.pOneQuickDamage = quickDamage
            self.pTwoCurrentHP = self.pTwoCurrentHP - self.pOneQuickDamage
            print(self.playerOne.capitalize() + " used 'quick strike,' managing to do an additional " + str(
                self.pOneQuickDamage) + "hp of damage.")

        if pOneFeatUsed[0] == "greater quick strike":

            #roll damage for player One, and multiply it by desired amount
            damage = random.randint(int(pOneMinimum), int(pOneMaximum))
            total = (damage + pOneModifier + pMod - cMod)
            quickDamage = int(total * float(pOneFeatUsed[1]))

            # Ensure damage is always at least 1hp and print out result
            self.pOneQuickDamage = quickDamage
            self.pTwoCurrentHP = self.pTwoCurrentHP - self.pOneQuickDamage
            print(self.playerOne.capitalize() + " used 'quick strike,' managing to do an additional " + str(self.pOneQuickDamage) + "hp of damage.")

        #If Player One has Evasion, Improved Evasion, or Greater Evasion, give them the option to use it.
        for word in self.pOneInfo['feats taken']:
            if self.pOneEvade == 1 and word == "evasion":
                answer = input(self.playerOne.capitalize() + ", do you wish to evade?").lower()
                if answer == "yes":
                    total = int(total * 0.75)
                    self.totalDamage = total
                    self.pOneEvade = 0
            elif self.pOneEvade == 1 and word == "improved evasion":
                answer = input(self.playerOne.capitalize() + ", do you wish to evade?").lower()
                if answer == "yes":
                    total = int(total * 0.5)
                    self.totalDamage = total
                    self.pOneEvade = 0
            elif self.pOneEvade == 1 and word == "improved evasion":
                answer = input(self.playerOneo.capitalize() + ", do you wish to evade?").lower()
                if answer == "yes":
                    total = 0
                    self.totalDamage = total
                    self.pOneEvade = 0

        self.totalDamage = total
        # testing data to see that modifiers are carrying over correctly. Delete this when project is finished.
        print("Roll: " + str(damage) + " Modifier: " + str(pTwoModifier) + " PA: " + str(pMod) + " CD: " + str(cMod))

        # display total damage done, and reset passive feat counters (power attack and combat defense).
        print(self.playerTwo.capitalize() + " did " + str(total) + " points of damage.")
        self.pTwopMod = 0
        self.pTwocMod = 0
        self.getHitPointsPOne()

    # Two methods to update hit points as the fight progresses along.

    def getHitPointsPOne(self):
        if self.pTwoQuickDamage != 0:
            self.pOneCurrentHP = self.pOneCurrentHP - self.totalDamage - self.pTwoQuickDamage
            self.pTwoQuickDamage = 0
        else:
            self.pOneCurrentHP = self.pOneCurrentHP - self.totalDamage
        self.token = 2
        self.scoreboard()

    def getHitPointsPTwo(self):
        if self.pOneQuickDamage != 0:
            self.pTwoCurrentHP = self.pTwoCurrentHP - self.totalDamage - self.pOneQuickDamage
            self.pOneQuickDamage = 0
        else:
            self.pTwoCurrentHP = self.pTwoCurrentHP - self.totalDamage
        self.token = 1
        self.scoreboard()

    # Creates the scoreboard to display to players after every turn. The if statement is placed here as a break, to
    # not allow the program to run test runs in one fluid motion. However, I believe this will be the place to obtain
    # player input on if they want to use any special feats they have - such as evasion to halve damage taken, and so on
    # Believe that each feat requiring extra variables will require methods of their own. Unsure of how to go about that yet.

    def scoreboard(self):
        print(self.playerOne.capitalize() + ": " + str(self.pOneCurrentHP) + "/" + str(self.pOneTotalHP) + "  ||  " + self.playerTwo.capitalize() + ": " + str(self.pTwoCurrentHP) + "/" + str(self.pTwoTotalHP))
        self.combatRounds()

    # the 'meat and potatoes' of combat. This method will keep track of whose turn it is via a token variable I
    # initiated back in the Initiative method. This method will also watch to see if any opponent drops to 0 or below
    # hit points, and when that happens, end combat.

    def combatRounds(self):
        if self.pOneCurrentHP > 0 and self.pTwoCurrentHP > 0:
            if self.token == 1:
                self.count += 1
                self.pTwoFeatUsed()
                self.determineHitPTwo()
            elif self.token == 2:
                self.count += 1
                self.pOneFeatUsed()
                self.determineHitPOne()
        else:
            self.setXP()

    # Determines xp for the victor. Formula is: 10 * Difference in opponent's HP + (difference in level * 50), where
    # difference in level will never equal 0. Added a small 'if' statement to ensure that level never equals 0, which
    # can only happen if both player character's are of the same level.
    # This is a logic problem in this I'm unsure how to deal with. Right now. High level characters can abuse the xp
    # system by fighting low level characters, and getting a great deal of xp based on how the formula is setup. Want
    # to set up a way in which program detects if winning player was higher level than losing player. If so, change
    # formula to just 10 * Difference in opponent's HP. If winning player was lower, then keep formula as is.

    def setXP(self):
        if self.pOneCurrentHP <= 0:
            print(self.playerTwo.capitalize() + " won in " + str(int(self.count / 2)) + " rounds")
            level = abs(self.pOneLevel - self.pTwoLevel)
            if level == 0:
                level = 1
            levelDiff = level * 50
            differHP = abs(self.pOneCurrentHP - self.pTwoCurrentHP)
            self.xp = 10 * differHP + levelDiff
            print(self.playerTwo.capitalize() + " has earned: " + str(self.xp) + " experience points.")
            self.currentPlayerXP = self.pTwoInfo['currentxp'] + self.xp
            self.nextLevel = self.pTwoInfo['nextlevel']
            self.winner = self.playerTwo
            self.levelUp = self.pTwoInfo['level']
            self.checkLevel()
        elif self.pTwoCurrentHP <= 0:
            print(self.playerOne.capitalize() + " won in " + str(int(self.count / 2)) + " rounds")
            level = abs(self.pOneLevel - self.pTwoLevel)
            if level == 0:
                level = 1
            levelDiff = level * 50
            differHP = abs(self.pOneCurrentHP - self.pTwoCurrentHP)
            self.xp = 10 * differHP + levelDiff
            print(self.playerOne.capitalize() + " has earned: " + str(self.xp) + " experience points.")
            self.currentPlayerXP = self.pOneInfo['currentxp'] + self.xp
            self.nextLevel = self.pOneInfo['nextlevel']
            self.winner = self.playerOne
            self.levelUp = self.pOneInfo['level']
            self.checkLevel()

    # Method to check the value of 'currentxp' on a character's json file. If it exceeds the 'nextlevel' value, notify
    # the winning player that they have leveled up. Then proceed to write all the new values for that level to the
    # json file.
    # this Method opens up levelchart.txt, a json that contains a dictionary containing values for levels 1 through 20.
    def checkLevel(self):

        with open(self.winner + '.txt', 'r+') as file:
            charData = json.load(file)
            charData['currentxp'] = self.currentPlayerXP
            file.seek(0)
            file.write(json.dumps(charData, ensure_ascii=False, indent=2))
            file.truncate()
            file.close()

        if self.currentPlayerXP >= self.nextLevel:
            newLevel = self.levelUp + 1
            newLevel = str(newLevel)
            print(self.winner.capitalize() + " has reached level " + newLevel + "!")
            levelFile = open("levelchart.txt", "r", encoding="utf-8")
            levelDict = json.load(levelFile)
            levelFile.close()

            with open(self.winner + '.txt', 'r+') as file:
                charData = json.load(file)
                charData['level'] = int(newLevel)
                charData['hitpoints'] = int(levelDict[newLevel][0])
                charData['base damage'] = str(levelDict[newLevel][1]) + "d" + str(levelDict[newLevel][2])
                charData['total feats'] = levelDict[newLevel][4]
                charData['hit'] = int(levelDict[newLevel][5])
                charData['damage modifier'] = int(levelDict[newLevel][5])
                charData['ac'] = int(levelDict[newLevel][6])
                charData['currentxp'] = int(self.currentPlayerXP)
                charData['nextlevel'] = int(levelDict[newLevel][7])
                file.seek(0)
                file.write(json.dumps(charData, ensure_ascii=False, indent=2))
                file.truncate()
                file.close()
        else:
            pass
    #----------------------------------------------- FEAT METHODS ------------------------------------------------------
    def pOnePowerAttack(self):
        mod = 0
        if self.pOneLevel <= 4:
            mod = "1"
        elif  4 < self.pOneLevel <= 8:
            mod = "2"
        elif  8 < self.pOneLevel <= 12:
            mod = "3"
        elif 12 < self.pOneLevel <= 16:
            mod = "4"
        elif 16 < self.pOneLevel <= 20:
            mod = "5"
        pMod = 6
        while pMod > int(mod):
            try:
                pMod = int(input("Select point allocation for Power Attack (0-" + mod + "): "))
            except ValueError:
                print("Please select a number between 0 and " + mod + ": ")
        return int(pMod)

    def pTwoPowerAttack(self):
        mod = 0
        print(type(self.pTwoLevel))
        if self.pTwoLevel <= 4:
            mod = "1"
        elif  4 < self.pTwoLevel <= 8:
            mod = "2"
        elif  8 < self.pTwoLevel <= 12:
            mod = "3"
        elif 12 < self.pTwoLevel <= 16:
            mod = "4"
        elif 16 < self.pTwoLevel <= 20:
            mod = "5"
        pMod = 6
        while pMod > int(mod):
            try:
                pMod = int(input("Select point allocation for Power Attack (0-" + mod + "): "))
            except ValueError:
                print("Please select a number between 0 and " + mod + ": ")
        return int(pMod)


    def pOneCombatExpertise(self):
        mod = 0
        if self.pTwoLevel <= 4:
            mod = "1"
        elif  4 < self.pOneLevel <= 8:
            mod = "2"
        elif  8 < self.pOneLevel <= 12:
            mod = "3"
        elif 12 < self.pOneLevel <= 16:
            mod = "4"
        elif 16 < self.pOneLevel <= 20:
            mod = "5"
        cMod = 6
        while cMod > int(mod):
            try:
                cMod = int(input("Select point allocation for Combat Expertise (0-" + mod + "): "))
            except ValueError:
                print("Please select a number between 0 and " + mod + ": ")
        return int(cMod)

    def pTwoCombatExpertise(self):
        mod = 0
        if self.pTwoLevel <= 4:
            mod = "1"
        elif  4 < self.pTwoLevel <= 8:
            mod = "2"
        elif  8 < self.pTwoLevel <= 12:
            mod = "3"
        elif 12 < self.pTwoLevel <= 16:
            mod = "4"
        elif 16 < self.pTwoLevel <= 20:
            mod = "5"
        cMod = 6
        while cMod > int(mod):
            try:
                cMod = int(input("Select point allocation for Combat Expertise (0- " + mod + "): "))
            except ValueError:
                print("Please select a number between 0 and " + mod + ": ")
        return int(cMod)

    def pOneDefensiveFighting(self):
        mod = 0
        if self.pTwoLevel <= 4:
            mod = "1"
        elif  4 < self.pOneLevel <= 8:
            mod = "2"
        elif  8 < self.pOneLevel <= 12:
            mod = "3"
        elif 12 < self.pOneLevel <= 16:
            mod = "4"
        elif 16 < self.pOneLevel <= 20:
            mod = "5"
        dMod = 6
        while dMod > int(mod):
            try:
                dMod = int(input("Select point allocation for Defensive Fighting (0-" + mod + "): "))
            except ValueError:
                print("Please select a number between 0 and " + mod + ": ")
        return int(dMod)

    def pTwoDefensiveFighting(self):
        mod = 0
        if self.pTwoLevel <= 4:
            mod = "1"
        elif  4 < self.pTwoLevel <= 8:
            mod = "2"
        elif  8 < self.pTwoLevel <= 12:
            mod = "3"
        elif 12 < self.pTwoLevel <= 16:
            mod = "4"
        elif 16 < self.pTwoLevel <= 20:
            mod = "5"
        dMod = 6
        while dMod > int(mod):
            try:
                dMod = int(input("Select point allocation for Defensive Fighting (0-" + mod + "): "))
            except ValueError:
                print("Please select a number between 0 and " + mod + ": ")
        return int(dMod)

    def pOneMasochist(self):
        mod = 0
        if self.pTwoLevel <= 4:
            mod = "1"
        elif  4 < self.pOneLevel <= 8:
            mod = "2"
        elif  8 < self.pOneLevel <= 12:
            mod = "3"
        elif 12 < self.pOneLevel <= 16:
            mod = "4"
        elif 16 < self.pOneLevel <= 20:
            mod = "5"
        mMod = 6
        while mMod > int(mod):
            try:
                mMod = int(input("Select point allocation for Masochist (0-" + mod + "): "))
            except ValueError:
                print("Please select a number between 0 and " + mod + ": ")
        return int(mMod)

    def pTwoMasochist(self):
        mod = 0
        if self.pTwoLevel <= 4:
            mod = "1"
        elif  4 < self.pTwoLevel <= 8:
            mod = "2"
        elif  8 < self.pTwoLevel <= 12:
            mod = "3"
        elif 12 < self.pTwoLevel <= 16:
            mod = "4"
        elif 16 < self.pTwoLevel <= 20:
            mod = "5"
        mMod = 6
        while mMod > int(mod):
            try:
                mMod = int(input("Select point allocation for Masochist (0-" + mod + "): "))
            except ValueError:
                print("Please select a number between 0 and " + mod + ": ")
        return int(mMod)

    # def pOneUseFeat(self):
    #     crippling = self.pOneInfo['crippling']
    #     staggering = self.pOneInfo["staggering"]
    #     evasion = self.pOneInfo["evasion"]
    #     quick = self.pOneInfo["quick"]
    #     ripose = self.pOneInfo["ripose"]
    #     deflect = self.pOneInfo["deflect"]
    #     reckless = self.pOneInfo["reckless"]
    #     titan = self.pOneInfo["titan's blow"]
    #     strike = self.pOneInfo["true strike"]



    # def pOneCripple(self):
    #     crippling = self.pOneInfo['crippling']
    #     if crippling == 0:
    #         print("You have already used this feat.")
    #     else:
    #         crippling -= 1
    #     if active == "crippling blow":
    #         crippleMod = -1
    #         return crippleMod
    #     elif active == "improved crippling blow":
    #         crippleMod = -2
    #         return crippleMod
    #     elif active == "greater crippling blow":
    #         crippleMod = -3
    #         return crippleMod


# ------------------------------------TEST CODE-----------------------------------------
# Run module as stand alone to test.
# combat = Combat()
# combat.initiative()



    # def powerAttack(self):
    #     answer = input("How many points? ")
    #     print(self.list)
    #     self.list[5] = hit
    #     self.list[6] = damage
    #     print(hit)
    #     print(damage)
    #     hit = hit - answer
    #     damage = damage + answer
    #     print(hit)
    #     print(damage)
    #
    # def players(self):
    #     opponentOne = input("Who is the first opponent?").lower()
    #     charFile = open(opponentOne + ".txt", "r", encoding="utf-8")
    #     charStats = json.load(charFile)
    #     charFile.close()
    #     list = []
    #     for key in charStats:
    #         print(key)
    #         list.append(key)
    #     print(list)
    #     self.list = list