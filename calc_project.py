# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 11:17:17 2023

@author: Lenovo
"""

## Calculuator-project
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)

# Operations of Calculator


def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2

dict_calc = { 
             "+": add,
             "/": div,
             "*": mul,
             "-": sub,
             }

def calculator():
    print(logo)
    num1 = float(input("Enter first number: "))

    for symbol in dict_calc:
        print(symbol)
        
    cont = True
    
    while cont:
        symbol = input("Enter opertation: ")    
        num2 = float(input("Enter second number number: "))
        answer = dict_calc[symbol]
        result = answer(num1,num2)
        
        print(f"result = {num1} {symbol} {num2} = {result}")
        
        user_choice = input(f"If want to continue with {result} calculations: Yes or No "
                            )
        if user_choice == "yes":
            num1 = result       
        else:
            cont = False
            calculator()

calculator()        
        


