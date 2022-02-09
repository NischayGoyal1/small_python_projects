import random

def asum(lis):
    sum=0
    for i in range(len(lis)):
        sum+=int(lis[i])
    return sum


list=[11,1,2,3,4,5,6,7,8,9,10,10,10,10]
human_choice=[]
computer_choice=[]
ctimes=random.randint(1,5)
human_choice.append(random.choice(list))
human_choice.append(random.choice(list))
computer_choice.append(random.choice(list))
def result(c,h):
    if asum(h)>21:
        print(f"Your cards {h} \n computers cards{c}")
        print("you lost as u exceed our 21")
    elif asum(c)>21:
        print(f"Your cards {h} \n computers cards{c}")
        print("you won as computer exceed our 21")
    elif asum(c)>asum(h):
        print(f"Your cards {h} \n computers cards{c}")
        print("you lost")
    elif asum(c)<asum(h):
        print(f"Your cards {h} \n computers cards{c}")
        print("you won")
    else:
        print(f"Your cards {h} \n computers cards{c}")
        print("Draw")
def compue(ctimes):
    for i in range(ctimes):
        computer_choice.append(random.choice(list))

    

def human():
   
    while 1:
        print(f"Your intials cards are {human_choice} \n computers cards are {computer_choice}")
        take=input("Do you want to choose a card 'y or no' ")
        if take=="n":
         compue(ctimes)
         result(computer_choice,human_choice)
         break
        else:
         human_choice.append(random.choice(list))
         

human()

