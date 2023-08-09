# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 15:39:47 2023

@author: Lenovo
"""
import random as rand
import sys
def clr():
    print ("\n"*80)
clr()   
computer_choice  = rand.randint(1,100)
#print(computer_choice)
mode = input("Enter the mode ypu want to play: ")
n = 0
count = 0
if mode == "hard":
    n = 5
elif mode  == "medium":
    n = 7
elif mode == "easy":
    n = 10
def guess():
    global n
    user_Input = int(input("Enter Your choice between 1 and 100: "))
    if user_Input < computer_choice:
        print("Too Low")
        print(f"you have {n-count-1} chances left. ")
    elif user_Input > computer_choice:
        print("Too high")
        #n = n - 1
        print(f"you have {n-count-1} chances left. ")
    else:
        print("You guessed it right. ")
        sys.exit()

while count <= n:
    guess()
    count+=1
    if (n-count) == 0:
        print("You loose")
        break
    
    

  

