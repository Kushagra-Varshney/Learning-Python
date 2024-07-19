class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        elif isinstance(other, int) or isinstance(other, float):
            return Point(self.x + other, self.y + other)
        else:
            raise TypeError("Unsupported operand type for +")

    def __sub__(self, other):
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)
        elif isinstance(other, int) or isinstance(other, float):
            return Point(self.x - other, self.y - other)
        else:
            raise TypeError("Unsupported operand type for -")

    # decide how the object should be represented when it’s printed
    def __str__(self):
        return f"({self.x}, {self.y})"

# Usage
p1 = Point(2, 3)
p2 = Point(4, 5)

p3 = p1 + p2
print(p3)  # Output: (6, 8)

p4 = p2 - p1
print(p4)  # Output: (2, 2)

p5 = p1 + 2
print(p5)  # Output: (4, 5)

p6 = p2 - 1
print(p6)  # Output: (3, 4)