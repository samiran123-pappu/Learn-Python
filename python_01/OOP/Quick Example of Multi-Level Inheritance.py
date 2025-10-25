class Person:
    def speak(self):
        print("I am a person")

class Student(Person):
    def study(self):
        print("I am studying")

class CollegeStudent(Student):
    def attend(self):
        print("I attend college")

obj = CollegeStudent()
obj.speak()
obj.study()
obj.attend()
