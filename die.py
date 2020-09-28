class Die:
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return r.randint(1, self.sides)

