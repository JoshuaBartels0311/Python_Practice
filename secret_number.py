# This is a simple text based game
print('Welcome to the Secret Numbers Game!!')

import random
secret = random.randint(1, 100)

number = 0


while number != secret:

    number = int(input('Guess a number 1 - 100 '))

    if number > secret:
        print('{} is larger than secret number. '.format(number))

    elif number < secret:
        print('{} is less than secret number. '.format(number))

    elif number == secret:
        print('{} is the secret number. '.format(secret))
        print('You Win! ')
        exit()
