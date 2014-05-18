import numpy as np


class Neuneu(object):
    def __init__(self, energy=10):
        """
        Creates a Neuneu

        Parameters
        ==========

        energy : int, optional, default: 10

        """
        self.energy = energy
        self.position = np.random.randint(0, 100, 2)

    def move(self):
        """
        Moves in a random direction
        """
        direction = np.random.randint(-5, 5, 2)
        self.position += direction
