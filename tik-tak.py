#Author: Aaron Wajah


#1importing libraries for usage
import string 
import os 
import random 
import time 

print("This Game is a Game of WAR👽👾🤖💀")
#time.sleep(3)

rows_and_column = 10
game =[]
ship_size = 4
AJ =list((string.ascii_lowercase[:10].upper()))# column header from A to J


#creating the 10x10 board for simulation
for row in range(rows_and_column):
    rowlist = []
    for col in range(rows_and_column):
        rowlist.append(" ")
    game.append(rowlist)

for col_num in range(rows_and_column):
    print("   "+ AJ[col_num],end =" ")
    
print("\n +"+"----+"* rows_and_column)

for row in range(rows_and_column):
    print(str(row)+"| ", end =" ")
    for col in range(rows_and_column):
        print(game[row][col] + " | ", end=" ")
    print("\n +"+"----+"*rows_and_column)

print("Prepare to Play battleship👾👾")
time.sleep(1)
#Placing the random ship on the grid
ship_row= random.randint(0,rows_and_column-1)
ship_column= random.randint(0,rows_and_column-1)
print(ship_row,ship_column)


while ship_row > rows_and_column-4 and ship_column> rows_and_column-4:
    ship_row= random.randint(0,rows_and_column-1)
    ship_column= random.randint(0,rows_and_column-1)

if ship_row > rows_and_column-4:
    for a in range(ship_size):
        game[ship_row][ship_column]="X"
        ship_column+=1

elif ship_column > rows_and_column-4:
    for a in range(ship_size):
        game[ship_row][ship_column]="X"
        ship_row+=1
else: 
    portrait= random.randint(0,1)
    if portrait ==0:
        for a in range(ship_size):
            game[ship_row][ship_column]="X"
            ship_column+=1
    else:
        for a in range(ship_size):
            game[ship_row][ship_column]="X"
            ship_row+=1
print("---------------------------------------------------------------------------------")
print("|"+"Guess a possible coordinate of ship by column (alphabet)\
followed by row(number)"+"|")
print("---------------------------------------------------------------------------------")
guess_count=0
guess_column = input("Guess Column Letter")
guess_row = int(input("Guess Row Number"))

wrong_input = False
while wrong_input:
    if guess_column not in AJ:
        print("please input a Capital letter for COLUMN and number for row")
    elif guess_row > (rows_and_column-1):
        print("Please enter a valid row number")
    elif guess_row<0:
        print("Please enter a valid row number (0-9)")
    else:
        if guess_column == AJ[ship_column] and guess_row== ship_row:
            game[guess_column][guess_row].append("x")
            guess_count+=1
            if guess_count == 4:
                print("Congrats, You sunk the ship man!!")
        else:
            game[guess_column][guess_row].append("#")
            guess_count+=1
    

for row in range(rows_and_column):
    rowlist = []
    for col in range(rows_and_column):
        rowlist.append(" ")
    game.append(rowlist)

for col_num in range(rows_and_column):
    print("   "+ AJ[col_num],end =" ")   
print("\n +"+"----+"* rows_and_column)

for row in range(rows_and_column):
    print(str(row)+"| ", end =" ")
    for col in range(rows_and_column):
        if "X" in game[row][col]:
            print(game[row][col] + " | ", end=" ")
        else:
            game[row][col]=" "
            print(game[row][col] + " | ", end=" ")
    print("\n +"+"----+"*rows_and_column)