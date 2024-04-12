# Example 1:
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print("Brand:", self.brand)
        print("Model:", self.model)

my_car = Car("Toyota", "Corolla")
my_car.display_info()

# Example 2:
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

rectangle = Rectangle(5, 3)
print("Area of the rectangle:", rectangle.calculate_area())

# Example 3:
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)

student1 = Student("Alice", 20)
student1.display_info()

# Example 4:
class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return self.pi * self.radius ** 2

circle = Circle(5)
print("Area of the circle:", circle.calculate_area())
