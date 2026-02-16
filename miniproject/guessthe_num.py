import random

target=random.randint(1,100)

while True:
    userchoice=input("enter your choice: or Ouit(Q):")
    if(userchoice=="Q"):
        break
    userchoice=int(userchoice)
    if(userchoice==target):
        print("successfully guessed")
        break
    elif(userchoice>target):
        print("Too big take small guess")
    else:
        print("Too small take bigger guess")

print("------GAME OVER------")