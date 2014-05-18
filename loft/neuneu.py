import numpy as np


class Neuneu(object):
    def __init__(self, energy=10):
        self.energy = energy
        self.position = np.random.randint(0, 100, 2)

    def move(self):
        direction = np.random.randint(-5, 5, 2)
        self.position += direction
