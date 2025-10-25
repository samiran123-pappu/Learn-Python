class Calculator:
    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def square(x):
        return x ** 2

print(Calculator.multiply(3, 4))  # 12
print(Calculator.square(5))       # 25


