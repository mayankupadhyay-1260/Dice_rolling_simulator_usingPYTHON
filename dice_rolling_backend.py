from timeit import default_timer as timer
# print("\u25CF,\u250C,\u2500,\u2510,\u2502,\u2514,\u2518")
# ●,┌,─,┐,│,└,┘
start = timer()

import random

# "┌─────────┐"
# "│         │"    
# "│         │"    
# "│         │"    
# "└─────────┘"


# Here every key is an integer and every dice is an tuple (immutable) 
''' Every line in the value(tuple/dice shape) is different element for different line
   so seperate every line by a comma '''

dice_art = {
1 :      ("┌─────────┐",
          "│         │",    
          "│    ●    │",    
          "│         │",    
          "└─────────┘") ,
2:       ("┌─────────┐",
          "│ ●       │",   
          "│         │",   
          "│       ● │",   
          "└─────────┘") ,
3:       ("┌─────────┐",
          "│ ●       │",  
          "│    ●    │",  
          "│       ● │",  
          "└─────────┘") ,
4:       ("┌─────────┐",
          "│ ●     ● │", 
          "│         │", 
          "│ ●     ● │", 
          "└─────────┘") ,
5:       ("┌─────────┐",
          "│ ●     ● │",
          "│    ●    │",
          "│ ●     ● │",
          "└─────────┘"),
6:       ("┌─────────┐",
          "│ ●     ● │",
          "│ ●     ● │",
          "│ ●     ● │",
          "└─────────┘")
}

dice = []
total = 0
num_of_dice = int(input("Enter the number of dices you want to roll : "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    

for die in dice:
    total += die
print(f"total {total}")

# Outer for loop for the number of the dice and the inner one is for printing dice art :

# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line,end='\n')

# For this we have to print first line of every dice then second then third until 5
# outer for loop print first line of every dice
def rolledDice():
    for line in range(5):
        for die in dice:
            with open("result.txt","w+") as res:
                res = print(dice_art.get(die)[line],end=" ")

            
        print()

dice = rolledDice()


# import tkinter as tk
# root = tk.Tk()
# root.geometry("720x720")
# # result = tk.Label(root, image=dice)
# result = tk.PhotoImage(file= r"D:\Coding\PYTHON\Advanced Python\result.png")

# result.pack()
# root.mainloop()


stop = timer()

print(stop - start)