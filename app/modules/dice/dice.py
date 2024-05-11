import random


class Dice:
    #empty constructor
    def __init__(self):
        pass

    def roll(self):
        return random.randint(1, 6)
