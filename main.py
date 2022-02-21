# War Game

import random
import time

running = True


class game:
    def __init__(self):
        self.human = human()
        self.computer = computer()


def start():
    print('=' * 60)
    print('rules: https://bicyclecards.com/how-to-play/war/')
    print('The cards are numbered 1 - 13!')
    print('=' * 60,)


# Returns the value of the highest card, 0 if they are equal
def determine_winner(card1, card2):
    if card1 == card2:
        return 0
    elif card1 > card2:
        return card1
    elif card1 < card2:
        return card2
    else:
        return -1


def run_check():
    decision = ''
    while decision == '':
        print('Draw? y/n')
        decision = input()

        if decision == 'y':
            return True
        elif decision == 'n':
            return False
        else:
            decision = ''


class player:
    def __init__(self):
        self.hand = [7, 8, 5, 6, 3, 4, 1, 2, 9, 11, 10, 13, 12]
        self.score = 0
        self.card = -1

    def gen_hand(self):
        self.hand = [7, 8, 5, 6, 3, 4, 1, 2, 9, 11, 10, 13, 12]

    def win(self):
        self.score += 1


class human(player):
    def draw(self):

        if len(self.hand) == 0:
            print('Drawing hand for human...')
            time.sleep(3)
            self.gen_hand()

        print('\nPick a card numbered between 1 and', len(self.hand))

        pick = input()

        acceptable_input = [str(x) for x in range(1, len(self.hand) + 1)]

        # Makes sure you actually pick a card and not like a letter or something
        while pick not in acceptable_input:
            print('Pick one of your cards bozo!')
            print('Pick a card numbered between 1 and', len(self.hand))

            pick = input()

        pick = int(pick)
        self.card = pick

        card = self.hand.pop(pick - 1)

        # sets self.card equal to the card drawn
        self.card = card


class computer(player):
    def draw(self):
        if len(self.hand) == 0:
            print('Drawing hand for computer...')
            time.sleep(3)
            self.gen_hand()

        card = self.hand.pop(random.randint(0, len(self.hand) - 1))
        self.card = card


# Start of program
start()

computer = computer()
human = human()

# Game loop
while running:
    computer.draw()
    human.draw()

    print('You drew', human.card, "the computer drew", computer.card)
    time.sleep(1)

    if determine_winner(computer.card, human.card) == 0:
        print('TIE')
    elif determine_winner(computer.card, human.card) == human.card:
        print('HUMAN VICTORY')
    elif determine_winner(computer.card, human.card) == computer.card:
        print('COMPUTER VICTORY')
    time.sleep(1)

print('Goodbye!')
