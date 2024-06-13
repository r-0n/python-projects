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



print(stages[0])

print(hangman_intro_UI)
words = ["Beekeeper","Bugatti","Redamancy","Abraham Lincoln"]

hangman_word = random.choice(words).lower()

print(f'the solution is {hangman_word}')

display_word = ["_"]* len(hangman_word)
print(display_word)

#game loop
lives = 6
game = True

while game:

    user_input = input("Enter a letter").lower()

    for letter in range(0,len(hangman_word)):
        if user_input==hangman_word[letter]:
            display_word[letter] = hangman_word[letter]

    if user_input not in hangman_word:
        print(f'You guessed the letter{user_input}, {user_input} is not in the word')
        
        print(stages[lives-1])
    
    print(stages[lives-1])
    print(display_word)

    if "_" not in display_word:
        print("You Won!")
        game = False

    elif "_" in display_word and lives == 0:
        print("You Lost!")
        game = False


    lives-=1

