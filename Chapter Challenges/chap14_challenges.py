# Chapter 14 challenges

""" create a square class with a square_list class variable """
class Square():
    squares = [] # class variable containing list of squares

    def __init__(self, s):
        self.size = s
        self.squares.append(self) # append newly created square to list of squares
        print(f"New square created with size {self.size}")

    def __repr__(self):
        # alter the string representation of what a square object is
        return f"Square: {self.size}"

sqr1 = Square(5)
sqr2 = Square(8)
sqr3 = Square(32)
