# Chapter 12 challenges

""" define an Apple class with 4 instance variables """
class Apple():
    def __init__(self, s, c, w, d):
        """ strain, colour, weight (oz), diameter (cm) """
        self.strain = s
        self.colour = c
        self.weight = w
        self.diameter = d
        print("Apple created.")



""" create a circle class with a method called area """
import math

class Circle():
    def __init__(self, r):
        """ radius in mm """
        self.radius = r
        print("Circle created.")

    def area(self):
        self.area = math.pi * (self.radius**2)
        print("The area of the circle is... {}".format(self.area))



""" create a triangle class with a method called area """
class Triangle():
    def __init__(self, h, w):
        """ height (mm), width (mm) """
        self.height = h
        self.width = w
        print("Triangle created.")

    def area(self):
        self.area = 0.5 * (self.width * self.height)
        print("The area of the triangle is... {}".format(self.area))



""" create a hexagon class with a method called calculate_perimeter """
class Hexagon():
    def __init__(self, sl):
        """ side-length (mm) """
        self.side_length = sl
        print("Hexagon created.")

    def calculate_perimeter(self):
        self.perimeter = 6 * self.side_length
        print("The perimeter of the hexagon is... {}".format(self.perimeter))



# testing
print("APPLE: ")
apple = Apple("pink-lady", "red", 10, 6)
print(apple.strain)
print(apple.colour)
print(apple.weight)
print(apple.diameter)
print("\n")

print("CIRCLE: ")
circle = Circle(10)
circle.area()
print("\n")

print("TRIANGLE: ")
tri = Triangle(10, 6)
tri.area()
print("\n")

print("HEXAGON: ")
h = Hexagon(8)
h.calculate_perimeter()
print("\n")
