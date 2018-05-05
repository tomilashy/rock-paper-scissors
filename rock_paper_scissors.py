'''
Created on May 2, 2018

@author: o_olasub
'''
import random
exits="no";
player1=0;
player2=0;
while exits !="yes":
    user1=input("Enter player 1's choice: ")

    comp=["rock","paper","scissors"]
    user2=random.choice(comp)
    print (f"Computer plays {user2}")
    if user1 and user2:
        if (user1=="rock" or user1=="paper" or user1=="scissors" ) and (user2=="rock" or user2=="paper" or user2=="scissors" ):
            if user1==user2:
                print("Its a draw")
            elif user1=="rock":
                if user2=="paper":
                    print("player 2 wins");player2+=1
                
                else:
                    print("player 1 wins");player1+=1
            elif user1=="paper":
                if user2=="scissors":
                    print("player 2 wins");player2+=1
                else:
                    print("player 1 wins");player1+=1
            elif user1=="scissors":
                if user2=="rock":
                    print("player 2 wins");player2+=1
                else:
                    print("player 1 wins");player1+=1
        else: 
            print("something went wrong")
    else: 
        print("something went wrong")
    
    exits=input("do you want to exit? input \"yes\" or \"no\" ")
print(f"player 1 :{player1} \ncomputer :{player2}")    
    

if player1>player2:
    print("player 1 wins")
elif player1 == player2:
     print("Its a tie")
else:
     print("player 2 wins")
     

