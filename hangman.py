#Project: Hangman
#Author:r-0n
#Date: 6/11/2024

import random

hangman_intro_UI ="""  _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/     """

hangman= """ """

print(hangman_intro_UI)
words = ["Beekeeper","Bugatti","Redamancy","Abraham Lincoln"]

hangman_word = random.choice(words).lower()

print(f'the solution is {hangman_word}')

display_word = ["_"]* len(hangman_word)
print(display_word)

#game loop
counter =0
game = True

while game:

    user_input = input("Enter a letter").lower()

    for letter in range(0,len(hangman_word)):
        if user_input==hangman_word[letter]:
            display_word[letter]= hangman_word[letter]
    
             
    print(display_word)

    if "_" not in display_word:
        print("You Won!")
        game = False

    elif "_" in display_word and counter ==15:
        print("You Lost!")
        game = False


    counter+=1

