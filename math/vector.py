class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def negate(self):
        return Vector(-self.x, -self.y)

    def subtract(self, other):
        return self.add(other.negate())

    def dot(self, other):
        return self.x * other.x + self.y * other.y
