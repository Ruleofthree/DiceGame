'''
A script that runs the to hit portion of the game. player rolls 1d20, adds their modifiers, and determines if they
successfully struck the other player, and do damage.
'''
import random

playerOneAC = input("What is Player 1's AC? ")
playerTwoAC = input("What is Player 2's AC? ")
min = 1
max = 20
again = 'y'
while again == 'y':
    turn = 1
    if turn == 1:
        attack = (random.randint(min, max))
        print("Player 1 rolled to attack: " + str(attack))
        if attack >= int(playerOneAC):
            print("Player 1 hits")
            turn += 1
        else:
            print("Player 1 misses")
            turn += 1
    if turn == 2:
        attack = (random.randint(min, max))
        print("Player 2 rolled to attack: " + str(attack))
        if attack >= int(playerTwoAC):
            print("Player 2 hits")
            turn -= 1
        else:
            print("Player 2 misses")
            turn -= 1
    print(input("Again? (y/n)"))