"""
A program to help simulate some fighting with the new dice system. This is basic, no feats involved, no stats. Just the
raw dice you obtain from leveling. Checking stress points to see the average win ratio versus levels.
"""
import random

# Put this entire thing in a while loop, so it doesn't constantly needed to be ran.
# As long as your input is 'yes' (lower case, without quotations), it will loop)
answer = "y"
while answer == "y":

    # Input levels for each player
    playerOneLevel = input("Player 1's Level? ")
    playerTwoLevel = input("player 2's Level? ")

    # The dictionary that takes the level input, and spits out hp, and converts dice to show minimum possible damage,
    # and maximum possible damage. Example: Level 5 is 35hp, minimum damage is 1, and maximum damage is 8
    levelDict = {1: [25, 1, 6],
                 2: [30, 1, 6],
                 3: [35, 1, 8],
                 4: [40, 1, 8],
                 5: [45, 1, 10],
                 6: [50, 1, 10],
                 7: [55, 2, 12],
                 8: [60, 2, 12],
                 9: [65, 2, 16],
                10: [70, 2, 16],
                11: [75, 3, 18],
                12: [80, 3, 18],
                13: [85, 2, 20],
                14: [90, 2, 20],
                15: [100, 2, 24],
                16: [110, 4, 24],
                17: [130, 4, 32],
                18: [135, 4, 32],
                19: [140, 3, 36],
                20: [150, 3, 36]}

    # Prints out total hit points for each player
    print("Player 1 has: " + str(levelDict[int(playerOneLevel)][0]) + "HP")
    print("Player 2 has: " + str(levelDict[int(playerTwoLevel)][0]) + "HP")

    # Creates a variable that will store each players current hit points as the script continues
    levelOneCurrentHP = levelDict[int(playerOneLevel)][0]
    levelTwoCurrentHP = levelDict[int(playerTwoLevel)][0]

    # a basic counter to let you know how many rounds has passed by time the script is over
    count = 0

    # will ensure the fight continues until either player 1 or player 2 has reached 0 hit points
    while levelOneCurrentHP > 0 and levelTwoCurrentHP > 0:
        # makes sure to increase the counter every time a round has finished
        count += 1

        # an If statement that first checks to see if player 1 has more than 0 hp
        # If he does, execute damage. The random number generator looks in the dictionary for player 1's minimum
        # damage, as well as maximum damage, then picks a number between that range and prints it out.
        # It is inside this ifstatement that Player 2's total HP is calculated, and printed out
        if levelOneCurrentHP > 0:
            damage = random.randint(levelDict[int(playerOneLevel)][1],levelDict[int(playerOneLevel)][2])
            print("Player 1 did: " + str(damage) + " damage")
            levelTwoCurrentHP = levelTwoCurrentHP - damage
            print("Player 2 is at " + str(levelTwoCurrentHP) + "hp" )


        # Same process as the If Statement above, only this is for Player 2's damage output, and updating Player 1's
        # current HP
        if levelTwoCurrentHP > 0:
            damage = random.randint(levelDict[int(playerTwoLevel)][1],levelDict[int(playerTwoLevel)][2])
            print("Player 2 did: " + str(damage) + " damage")
            levelOneCurrentHP = levelOneCurrentHP - damage
            print("Player 1 is at " + str(levelOneCurrentHP) + "hp")

    # Simple print function that will kick out how many rounds the fight simulation has lasted
    print("This fight lasted: " + str(count) + " rounds")

    # This entire if statement determines if Player 1 is the victor. If he was, print out his remaining HP.
    # From there, the if statement moves in to a nested if statement that determins if Player one's level was either
    # equal to, within 5 levels, or greater than 5 levels. Depending on the output, xp is determined
    if levelOneCurrentHP > 0:
        print("Player 1's remaining hp at end of fight is: " + str(levelOneCurrentHP) + "HP")

        # If levels were equal. xp = Current HP remaining x 25
        if int(playerOneLevel) == int(playerTwoLevel):
            xp = (levelOneCurrentHP * 25)
            print("Player 1's experience gained is: " + str(xp) + "xp")

        # If levels were greater than player 2, but not more than by 6 total levels.
        # Then xp = (CurrentHP x 25) / difference between Player 1 and Player 2's level.
        # This is to make sure higher level players aren't abusing fights with lower level players, and getting a
        # mass amount of xp for it
        elif int(playerOneLevel) > int(playerTwoLevel) and (int(playerOneLevel) - int(playerTwoLevel)) < 6:

            # Adds .5 to players with one level difference, in order to avoid dividing by one
            if int(playerOneLevel) > int(playerTwoLevel) and (int(playerOneLevel) - int(playerTwoLevel)) < 2:
                modifier = 1.5
                xp = int(int((levelOneCurrentHP * 25) / abs(modifier)))
                print("Player 1 has earned: " + str(xp) + "xp")
            else:
                modifier = abs(int(playerOneLevel) - int(playerTwoLevel))
                xp = int((levelOneCurrentHP * 25) / abs(modifier))
                print("Player 1 has earned: " + str(xp) + "xp")

        # if levels were lower than player 2, but not more than by 6 total levels.
        # Then xp = (CurrentHP x 25) + (Level Difference * 50). Since cap is at 5. This amounts to a maximum of a
        # 250xp bonus, should Player 1 beat someone 5 levels higher than him.
        # This is to keep low level players from trying to fight high level players to try and 'get lucky' and earn
        # a mass amount of xp in one fight
        elif int(playerOneLevel) < int(playerTwoLevel) and (abs(int(playerOneLevel) - int(playerTwoLevel))) < 6:
            modifier = abs(int(playerOneLevel) - int(playerTwoLevel))
            xp = (levelOneCurrentHP * 25) + (abs(modifier) * 50)
            print("Player 1 has earned: " + str(xp) + "xp")

        # if Player 1 is more than 5 levels above player 2, yet they still fought. Nothing is gained form it.
        else:
            print("The Level difference of opponents was too high to earn xp for this fight.")

    # The process is repeated for player 2. All if statements are exactly the same, just determining if Player 2 was
    # the victor
    else:
        print("Player 2's remaining hp at end of fight is: " + str(levelTwoCurrentHP) + "HP")
        if int(playerOneLevel) == int(playerTwoLevel):
            xp = (levelTwoCurrentHP * 25)
            print("Player 2's experience gained is: " + str(xp) + "xp")
        elif int(playerTwoLevel) > int(playerOneLevel) and int(playerTwoLevel) - int(playerOneLevel) < 6:
            if int(playerTwoLevel) > int(playerOneLevel) and int(playerTwoLevel) - int(playerOneLevel) < 2:
                modifier = 1.5
                xp = int((levelTwoCurrentHP * 25) / modifier)
                print("Player 2 has earned: " + str(xp) + "xp")
            else:
                modifier = abs(int(playerOneLevel) - int(playerTwoLevel))
                xp = int((levelTwoCurrentHP * 25) / abs(modifier))
                print("Player 2 has earned: " + str(xp) + "xp")
        elif int(playerTwoLevel) < int(playerOneLevel) and (abs(int(playerTwoLevel) - int(playerOneLevel))) < 6:
            modifier = abs(int(playerOneLevel) - int(playerTwoLevel))
            xp = (levelTwoCurrentHP * 25) + (abs(modifier) * 50)
            print("Player 2 has earned: " + str(xp) + "xp")
        else:
            print("The Level difference of opponents was too high to earn xp for this fight.")

    # A loop to determine if you want to run multiple tests.
    answer = input("Again? (y/n) ")


