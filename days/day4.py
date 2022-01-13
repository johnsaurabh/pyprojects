import random
scissors=  """

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)


"""
rock= """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper= """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

"""



yourchoice= int(input("Choose a number, 0 for rock, 1 paper and 2 for scissors "))
names=["rock", "paper", "scissors"]
rpslist=[rock,paper,scissors]
compchoice=random.randint(0,2)

if yourchoice==compchoice:
   win=2
elif yourchoice==0 and compchoice==1:
    win=0
elif yourchoice==0 and compchoice==2:
    win=1
elif yourchoice==1 and compchoice==0:
    win=1
elif yourchoice==1 and compchoice==2:
    win=0
elif yourchoice==2 and compchoice==0:
    win=0
elif yourchoice==2 and compchoice==1:
    win=1
else:
    print("Invalid INPUT")
    exit()

print("You chose " +names[yourchoice])

print(rpslist[yourchoice])

print("computer choice "+ names[compchoice])

print(rpslist[compchoice])

if win==1:
    print("You win")
elif win==0:
    print("You lose")
else:
    print("It's a draw")








