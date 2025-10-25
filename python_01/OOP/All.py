class Point:
    #  Class variable (shared by all)
    type_name = "Point"

    #  Constructor (Instance Method)
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #  Instance Method
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        print(f"Moved to ({self.x}, {self.y})")

    #  Class Method
    @classmethod
    def show_type(cls):
        print(f"This is a {cls.type_name} class.")

    #  Static Method
    @staticmethod
    def origin():
        return Point(0, 0)

    #  Dunder Method — string form
    def __str__(self):
        return f"({self.x}, {self.y})"

    #  Dunder Method — addition
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    #  Dunder Method — equality
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    #  Dunder Method — custom len()
    def __len__(self):
        return int((self.x ** 2 + self.y ** 2) ** 0.5)  # distance from origin


#  Inheritance Example
class ColoredPoint(Point):
    def __init__(self, x, y, color):
        # super() calls the parent (Point) constructor
        super().__init__(x, y)
        self.color = color

    def show_color(self):
        print(f"Color of the point is {self.color}")


#  ----------- USING ALL METHODS ------------

# 1️ Create Point objects
p1 = Point(3, 4)
p2 = Point(1, 2)

# 2️ Call Instance Method
p1.move(2, 3)   # moves to (5, 7)

# 3️ Call Class Method
Point.show_type()

# 4️⃣ Call Static Method
origin = Point.origin()
print("Origin:", origin)

# 5️ Dunder Methods in action
print("p1:", p1)            # __str__
print("p2:", p2)
print("p1 + p2:", p1 + p2)  # __add__
print("p1 == p2:", p1 == p2)  # __eq__
print("len(p1):", len(p1))    # __len__

# 6️ Inherited class usage
cp = ColoredPoint(2, 3, "red")
print("Colored Point:", cp)
cp.show_color()

# 7️ Add two different objects (still works due to inheritance)
sum_point = p1 + cp
print("Sum Point:", sum_point)



