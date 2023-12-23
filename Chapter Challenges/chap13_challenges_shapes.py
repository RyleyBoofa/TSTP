# Chapter 13 challenges

""" create rectangle and square classes with a method called calc_perimeter """
class Shape():
    def __init__(self, w, h):
        self.width = w
        self.height = h
        print(f"Shape {self.width}(w) x {self.height}(h) created.")

    def calc_perimeter(self):
        """ calculate and print the perimeter of the shape """
        self.peri = (2 * self.width) + (2 * self.height)
        if not self.height == self.width:
            print(f"The perimeter of the rectangle is {self.peri}.")
        else:
            print(f"The perimeter of the square is {self.peri}.")

    def what_am_i(self):
        """ determine if square or rectangle and print to the screen """
        if not self.height == self.width:
            print(f"I am a rectangle.")
        else:
            print(f"I am a square.")

    def change_size(self, amount):
        """ change the size of the shape by int: amount """
        self.width += amount
        self.height += amount
        print(f"Changing side lengths by {amount}")
        
class Rectangle(Shape):
    pass


class Square(Shape):
    pass


shp = Shape(10, 5)
shp.what_am_i()
shp.calc_perimeter()
shp.change_size(-2)
shp.calc_perimeter()
print("\n")

rect = Rectangle(5, 10)
rect.what_am_i()
rect.calc_perimeter()
rect.change_size(12)
rect.calc_perimeter()
print("\n")

sqr = Square(10, 10)
sqr.what_am_i()
sqr.calc_perimeter()
sqr.change_size(5)
sqr.calc_perimeter()
print("\n")
