#3/22/2024
# testing password generator

import string
import random

AJ =list((string.ascii_lowercase[:10].upper()))
print(AJ)

new_word =''

for i in range(0, 4):
     new_word+=AJ[random.randint(0,len(AJ))]

print(new_word)

