import random
import string
from blackjackart import logo
numbers= [11,2,3,4,5,6,7,8,9,10,10,10,10]
user_cards=[]
comp_cards=[]
#user_sum=0
#comp_sum=0
game_over=False
i=1
print(logo)
def compare(x,y):
    """Takes the sum of both user cards and computer's cards and compares them to
    """
    if x>y:
        print(f"your sum is {x}")
        print(f"Dealer's sum is {y}")
        print("SO,THEREFORE YOU WIN")
    elif(y>x):
        print(f"your sum is{x}")
        print(f"Dealer's sum is {y}")
        print("Oops! Looks like you've lost")
    else:
        print(f"your sum is {x}")
        print(f"Dealer's sum is {y}")
        print("It's a draw")
    game_over=True
    return game_over
def sum(user_cards,comp_cards,choice):
    """Takes the lists of user cards and computer cards and
    calculates the sum and then compares."""
    user_sum=0
    comp_sum=0
    for i in range(len(user_cards)):
        user_sum+=user_cards[i]
    for i in range(len(comp_cards)):
        comp_sum += comp_cards[i]
    if choice=="p":
        if user_sum>21:
            print(f"Your cards are {user_cards}")

            print(f"You lose as your sum is {user_sum}")
            game_over=True
        else:
            game_over=False
    else:
        if comp_sum>21:
            print(f"The dealer's cards are: {comp_cards}")

            print(f"You win as the dealer score is {comp_sum}")
            game_over=True
        elif comp_sum<17:
            game_over=False
        else:
            print(f"Your cards are {user_cards}")
            print(f"The dealer's cards are: {comp_cards}")
            game_over=compare(user_sum,comp_sum)





    return game_over


def user_pick():
    """Function to pick user's cards"""
    i=1
    #global user_sum
    if(len(user_cards)==0):

         while i <= 2:
              pick_card = random.choice(numbers)
              user_cards.append(pick_card)
              i += 1
    else:
        pick_card = random.choice(numbers)
        user_cards.append(pick_card)

   # user_sum=sum(user_cards)
    return(user_cards)



def comp_pick():
    """Function to pick computer's cards"""
    i = 1
    #global comp_sum
    if (len(comp_cards) == 0):

        while i <= 2:
            pick_card = random.choice(numbers)
            comp_cards.append(pick_card)
            i += 1
    else:
        pick_card = random.choice(numbers)
        comp_cards.append(pick_card)
    return (comp_cards)

play= "y"

while play!="n":
    game_over=False
    user_cards = []
    comp_cards = []
    user_pick()

    comp_pick()
    play=input("Do you want to play the blackjack game? y or n\n").lower()
    if(play=="y"):

        #Ask the user if he wants to pick a card or pass
        print(user_cards)
        while not game_over:

            choice=input("Would you like to pick a card \"P\" or pass\"n\" \n").lower()
            if choice=="p":
               user_pick()
               print(user_cards)
               game_over=sum(user_cards,comp_cards,choice)
               #user_sum=sum(user_cards)
              # if user_sum>21:
                 #  game_over=True
                   #print(f"You lose as your sum is {user_sum}, which is greater than 21")
            else:
                while not game_over:
                    print(comp_cards)

                    game_over=sum(user_cards,comp_cards,choice)
                    #comp_sum=sum(comp_cards)

                    comp_pick()








        # def compare():
        # def limit_check():


    else:
        print("Thank you for playing")
        exit()