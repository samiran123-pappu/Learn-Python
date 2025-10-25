class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hi, I am {self.name} age is {self.age}")

p1 = Person("Sam", 21)
p1.greet()
