#Author: Aaron Wajah
#Date:7/06/2023
#Description: This is a simple terminal based game of rock/paper/scissors.

import random

#users choice
def u_choice():
    go = input("Enter your choice (rock, paper, scissors)")
    return go

#computer's choice
def c_choice():
    computer = random.choice(["rock", "paper", "scissors"]) # randomly select r/p/s
    return computer

#this is the winner message
def winner_message(winner):
    if winner ==1:
        return "There's a tie"
    elif winner == 2:
        return "Computer Wins"
    elif winner == 3:
        return "You Win"
    else:
        return "Can't think of a message for you"

#Logic comparison
def game_play(user_choice, comp_choice):
    message = winner_message(0)
    user_choice = user_choice.upper()
    comp_choice = comp_choice.upper()

    if user_choice==comp_choice:
        message = winner_message(1)

    else:
        if user_choice == "ROCK":
            if comp_choice == "PAPER":
                message = winner_message(2)
            else:
                message = winner_message(3)
        
        elif user_choice == "PAPER":
            if comp_choice == "ROCK":
                message = winner_message(3)
            else:
                message = winner_message(2)
        
        else:
            if comp_choice == "PAPER":
                message = winner_message(3)
            else:
                message = winner_message(2)
        
        return message


#real Game
def real_game():
    print("Welcome to Rock Paper Scissors game")
    ready = input("Are you ready to play? Y/N \n")


    while ready.upper() == "Y":
        user = u_choice()
        computer = c_choice()
        print("Computer chose - ", computer)
        final =  game_play(user, computer)
        print(final)
        ready = input("Wanna play again? Y/N \n")


real_game()



