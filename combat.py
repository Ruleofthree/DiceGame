import json

opponentOne = input("Who is the first opponent?").lower()
charFile = open(opponentOne + ".txt", "r", encoding="utf-8")
charStats = json.load(charFile)
charFile.close()
print(charStats)
opponentTwo = input("Who is the second opponent?").lower()
charFile = open(opponentTwo + ".txt", "r", encoding="utf-8")
charStats = json.load(charFile)
charFile.close()
print(charStats)