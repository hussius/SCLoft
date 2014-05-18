

class Consumption(object):
    def __init__(self):
        self.quantity = 10
        self.energy = 5


class Food(Consumption):

    def __init__(self):
        self = Consumption()
        self.type = "Food"


class Drink(Consumption):

    def __init__(self):
        self = Consumption()
        self.type = "Drinks"
