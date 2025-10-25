class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 1️ String representation
    def __str__(self):
        return f"({self.x}, {self.y})"

    # 2️ Add two Point objects
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # 3️ Compare two Point objects
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # 4️ Custom len()
    def __len__(self):
        return int((self.x ** 2 + self.y ** 2) ** 0.5)  # distance from origin


# Create two objects
p1 = Point(3, 4)
p2 = Point(1, 2)

# 1. __str__() is called automatically when printing
print(p1)       # Output: (3, 4)
print(p2)       # Output: (1, 2)

# 2. __add__() is called when using +
p3 = p1 + p2
print(p3)       # Output: (4, 6)

#  3. __eq__() is called when using ==
print(p1 == p2)   # Output: False
p4 = Point(3, 4)
print(p1 == p4)   # Output: True

# 4. __len__() is called when using len()
print(len(p1))    # Output: 5   (distance from origin √(3²+4²) = 5)
print(len(p2))    # Output: 2



