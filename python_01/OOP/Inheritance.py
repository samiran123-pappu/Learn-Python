class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Student(Person):  # Student inherits from Person
    def __init__(self, name, age, roll):
        super().__init__(name, age)  # call Person's __init__
        self.roll = roll

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Roll: {self.roll}")

s1 = Student("Sam", 21, 101)
s1.display()
s1.show()
