import random
from hangmanboy import *
from wordlist import *

#Randomly choosing word form wordlist defined in wordlist.py
letter = random.choice(word_list)
emptyl = []
for i in range(len(letter)):
    emptyl.append("_")

print(emptyl)
print(asciiart[len(asciiart) - 1])
# finding function for letter in wordlist
def lfind(apl, letter):
    #logic if user guess already guessed number
    for i in range(len(letter)):
        if apl == emptyl[i]:
            return -1
#Checking if guessed letter is gussed right
    k=0
    for i in range(len(letter)):
        if apl == letter[i]:
            emptyl[i] = apl
            k+=1
            
           
    if k>0:
        return k
    return 0

def nischay():
    count = len(asciiart) - 1
    win = 0
    while 1:
        print(emptyl)
        apl = input("\nGuess A alphabet  : ")
        boo = lfind(apl, letter)
        if boo==-1:
            print(asciiart[count])
            print("you already guessed that\n")
            continue
        elif boo==0:
            count-=1
            print(asciiart[count])
            print("\n--Wrong Guess--\n")
            if count<0:
                print(f"\nOriginal word is {letter}\n --YOU LOST--")
                break
        else:
            win+=boo
            print(asciiart[count])
            print("\ncorrect Guess\n")
            if win==len(letter):
                print("\nWOHO YOU WON\n")
                break

# calling the final function
nischay()
