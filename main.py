# War Game

import random
import time


class game:
    def __init__(self):
        self.human = human()
        self.computer = computer()
        self.running = True

        print('=' * 60)
        print('rules: https://bicyclecards.com/how-to-play/war/')
        print('The cards are numbered 1 - 13!')
        print('=' * 60, )

        while self.running:

            self.computer.draw()
            self.human.draw()
            print('Computer Drew:', self.computer.card)
            print('Human Drew:', self.human.card)

            self.determine_winner()

            # temporary
            print(self.human.score, self.computer.score)

    def determine_winner(self):
        if self.computer.card == self.human.card:
            print('Tie')
        elif self.computer.card > self.human.card:
            self.computer.win()
            print('Computer won')
        elif self.computer.card < self.human.card:
            self.human.win()
            print('Human won')
        else:
            print('error')


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
            self.gen_hand()

        print('\nPick a card numbered between 1 and', len(self.hand))

        pick = input()

        acceptable_input = [str(x) for x in range(1, len(self.hand) + 1)]

        # Makes sure you actually pick a card and not like a letter or something
        while pick not in acceptable_input:
            print('Pick one of your cards bozo!\n')
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
            self.gen_hand()

        card = self.hand.pop(random.randint(0, len(self.hand) - 1))
        self.card = card


game = game()
