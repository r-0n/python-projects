import string
import random

AJ =list((string.ascii_lowercase[:10].upper()))

new_word =" "

for i in range(0, 4):
    new_word.append(AJ[random.randint(0,10)])

print(new_word)