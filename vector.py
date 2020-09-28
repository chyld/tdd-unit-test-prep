class Vector:
    def __init__(self, *nums):
        self.nums = nums

    def __add__(self, other):
        return Vector(*[a + b for a, b in zip(self.nums, other.nums)])

    def dot(self, other):
        return sum([a * b for a, b in zip(self.nums, other.nums)])

    def __mul__(self, scalar):
        # scale
        return Vector(*[n * scalar for n in self.nums])

    def norm(self):
        return self.dot(self) ** 0.5

