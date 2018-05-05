'''
Created on May 2, 2018

@author: o_olasub
'''
import random


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
                print("player 2 wins")
            else:
                print("player 1 wins")
        elif user1=="paper":
            if user2=="scissors":
                print("player 2 wins")
            else:
                print("player 1 wins")
        elif user1=="scissors":
            if user2=="rock":
                print("player 2 wins")
            else:
                print("player 1 wins")
    else: 
        print("something went wrong")
else: 
    print("something went wrong")