from food import Drinks, Food


class Case(object):
    def __init__(self, x, y):
        self.position = (x, y)
        self.who = []
        # XXX Implement random attribution of food
        self.food = []

