#Project: Hangman
#Author:r-0n
#Date: 6/11/2024

import random

hangman_intro_UI =""" 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/     """

#display stages when user inputs a wrong letter
stages=[''' 
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \ 
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . . Y\\ 
| |       // |   |  \\
| |      //  | . |   \\ 
| |     ')   |   |    ('
| |          ||'||
| |          || ||
| |          || ||
| |          || ||
| |         / | | \ 
| |         `-' `-' 


''', 

'''
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \ 
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . . Y\\ 
| |       // |   |  \\
| |      //  | . |   \\ 
| |     ')   |   |    ('
| |          ||'||
| |          || ||
| |          || ||
| |          || ||
| |          
| |         

''',
''' 
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \ 
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . . Y\\ 
| |       // |   |  \\
| |      //  | . |   \\ 
| |     ')   |   |    ('
| |          ||'||
| |          || ||
| |          
| |         
| |          
| |         


''', 
''' 
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \ 
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . . Y\\ 
| |       // |   |  \\
| |      //  | . |   \\ 
| |

''',
'''
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \ 
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . . Y\\ 
| |       
| |      
| |     
| |                    
| |          
| |          
| |         
| |         
''',

'''
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \ 
| |          ||  `/,|
| |          (\\`_.'
| |          
| |       
| |      
| |     
| |     
| |     
| |     
| |     
| |      
| |     

'''
] 


def game_display(list): ##function to display word progress
    for i in list:
        print(i,end=" ")



print(hangman_intro_UI)
words = ["Beekeeper","Bugatti","Redamancy","Abraham Lincoln"]

hangman_word = random.choice(words).lower()

print(f'the solution is {hangman_word}')

display_word = ["_"]* len(hangman_word)
game_display(display_word)

#game loop
lives = 6
game = True

while game: #game loop

    user_input = input("\nEnter a letter\n").lower()
    

    for letter in range(0,len(hangman_word)):
        if user_input==hangman_word[letter]:
            display_word[letter] = hangman_word[letter]

    if user_input not in hangman_word:
        print(f'You guessed the letter {user_input}, {user_input} is not in the word')
        lives-=1
        print(stages[lives])
    
    
    #print(display_word)
    game_display(display_word)

    if "_" not in display_word:
        print("\nYou Won!")
        game = False

    elif "_" in display_word and lives == 0:
        print("\nYou Lost!")
        game = False


    

