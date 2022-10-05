"""Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com
You need guess {NUM_DIGITS}-digit number within {MAX_GUESSES} tries
You get the answer 'Pico' for correct digit in the wrong place
You get the answer 'Fermi' for correct digit in the right place
You get the answer 'Bagels' if there are not corrects digits
"""

import random

NUM_DIGITS = 5  # a constant value max=10 (digits from 0 to 9)
MAX_GUESSES = 10  # a constant value


def get_secret():
    """Return secret number as a string of NUM_DIGITS unique random digits"""
    secret = random.sample(list('0123456789'), NUM_DIGITS)
    return ''.join(secret)


def get_answer(guess, secret):
    """ Return a string with the Pico, Fermi, Bagels as clues for a next guess"""
    answer = []
    for i in range(len(guess)):
        if guess[i] == secret[i]:
            answer.append('Fermi')  # a correct digit in the correct place
        elif guess[i] in secret:
            answer.append('Pico')   # a correct digit in the incorrect place
    if not answer:
        answer.append('Bagels')     # there are incorrect digits at all
    answer.sort()                   # sort the answers to hide an order information
    return ' '.join(answer)         # return an answer in the readable format

def main():
    print(f'''Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com.
I am thinking of {NUM_DIGITS}-digit number with no repeated digits
Try to guess what it is. Here are some clues:
When I say      That means:
  Pico          One digit is correct but in the wrong position.
  Fermi         One digit is correct and in the right position.
  Bagels        No digit is correct.
''')

    play_again = 'yes'

    #main loop
    while play_again == 'yes':
        secret = get_secret()   # get secret number
        print('I have thought up a number.')
        print(f' You have {MAX_GUESSES} guesses to get it.')

        for i in range(1, MAX_GUESSES):

            while True:                           # check input for NUM_DIGITS-digit number
                guess = input(f'Guess #{i}: ')
                if len(guess) != NUM_DIGITS or not guess.isdigit():
                    print(f'Only {NUM_DIGITS}-digit number will be accepted')
                else:
                    break                         # input is OK

            if guess == secret:                   # game over
                print('You got it!')
                break

            answer = get_answer(guess, secret)    # if not -> get answer
            print(answer)                         # output answer in readable format

        print(f'Answer is: {secret}')
        play_again = input('Do you want to play again? (yes or anything for exit) ')
    print('Thanks for playing!')

if __name__ == '__main__':
    main()

