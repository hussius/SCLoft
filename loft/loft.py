import numpy as np

from loft import case


class Loft(object):
    def __init__(self, width=100, height=100):
        self.width = width
        self.height = height
        loft = []
        for i in range(width):
            row = []
            for j in range(height):
                row.append(case.Case())
            loft.append(row)

        loft = np.array(loft)
