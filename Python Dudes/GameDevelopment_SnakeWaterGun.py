import random

swg = ['S', 'W', 'G']

f = 0
w = 0
c = 0

while c < 10:
    comp_choice = random.choice(swg)
    user_choice = input('Enter \'S\' for Snake, \'W\' for Water and \'G\' for Gun: ')
    # while user_choice != 's' or user_choice != 'w' or user_choice != 'g' or user_choice != 'S' or user_choice != 'W' or user_choice != 'G':
    #     user_choice = input('Re-Enter \'S\' for Snake, \'W\' for Water and \'G\' for Gun: ')
    if comp_choice == 'S':
        if user_choice == 'W' or user_choice == 'w':
            f = f + 1
        if user_choice == 'G' or user_choice == 'g':
            w = w + 1
    elif comp_choice == 'W':
        if user_choice == 'S' or user_choice == 's':
            w = w + 1
        if user_choice == 'G' or user_choice == 'g':
            f = f + 1
    else:
        if user_choice == 'S' or user_choice == 's':
            f = f + 1
        if user_choice == 'W' or user_choice == 'w':
            w = w + 1
    c = c + 1

if f > w:
    print('You loose the match! In the match... ')
    print(f'You won {w} times.')
    print(f'You loose {f} times.')
elif f < w:
    print('You Won the match! In the match... ')
    print(f'You won {w} times.')
    print(f'You loose {f} times.')
else:
    print('The match is draw! In the match... ')
    print(f'You won {w} times.')
    print(f'You loose {f} times.')
