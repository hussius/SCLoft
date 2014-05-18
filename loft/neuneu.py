import numpy as np


class Neuneu(object):
    def __init__(self, energy=10, random_state=None):
        if random_state is None:
            random_state = np.random.RandomState()
        if type(random_state) == int:
            random_state = np.random.RandomState(seed=random_state)
        self.random_state = random_state
        self.energy = energy
        self.position = random_state.randint(0, 100, 2)

    def go(self, direction):
        self.position += direction


class Eratic(Neuneu):
    def move(self):
        direction = self.random_state.randint(-5, 5, 2)
        self.go(direction)
