##Quick code to generate password randomly. this is still being developed

import string
import random

pass_len = int(input('How many characters in your password? '))

new_password = pass_len

all_chars = string.ascii_letters + string.digits + string.punctuation
password = ''
for char in range(size):
        rand_char = random.choice(all_chars)
        password = password + rand_char
        
print('Your new password is: ', password)

