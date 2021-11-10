import random 
import time

startTime = time.time()
endTime = startTime+15
now = 0
score = [0]
userInput = ""

def flashcard():
    randomint1 = random.randint(0,9)
    randomint2 = random.randint(0,9)
    randomIntProduct = randomint1*randomint2
    print(randomint1)
    print("X")
    print(randomint2)
    userInput = input()
    userInput = int(userInput)
    if userInput==randomIntProduct:
        score[0]=score[0] + 1
        print("CORRECT")
        print()
    else:
        print("WRONG")

while userInput != "Y":
    userInput = input('Would you like to play a game: ')
    if userInput == 'Y':
            print("great!")
            print('Let the game begin')
            break
    elif userInput == "N":
        print("sorry to hear that!")
        exit()


while(now <= endTime):
    flashcard()
    now = time.time()
totalScore = score[0]
totalScore = str(totalScore)
print("You got " + totalScore + " correct")
