# Chaper 4 challenges



""" write a function that takes a number as input and returns it squared """
def square_func(x):
    """
    Returns x squared.
    :param x: int.
    :return: int sum of x squared.
    """
    return x * x
print(f"using square_func to find 10 squared: {square_func(10)}")



""" write a function that accepts a string parameter and prints it """
def string_func(string):
    """
    Re-prints a given string.
    :param string: str.
    :return: print the given string to the screen.
    """
    print(string)
answer = input("What do you want to print? ")
string_func(answer)



""" write a function that takes 3 required and 2 optional parameters """
def params_func(x, y, z, a=10, b=20):
    """
    Tries to print the sum of all given numbers.
    :param x: int.
    :param y: int.
    :param z: int.
    :param a: int.
    :param b: int.
    :return: all numbers summed, or error message.
    """
    try:
        print(x + y + z + a + b)
    except ValueError:
        print("x, y, z not defined.")
print("not-providing optional parameters:")
params_func(10, 12, 20)
print("providing optional parameters (should be +25):")
params_func(10, 12, 20, 25, 30)



""" write a program with 2 functions:
    the first takes an int and returns that int divided by 2
    the second takes an int and returns that int multiplied by 4
    call the first, save the result, then pass the result to the second """
print("TWO PART PROGRAM: ")
def division(x):
    """
    Returns x divided by 2.
    :param x: int.
    :return: float sum of x divided by 2.
    """
    return x / 2

def multiply(y):
    """
    Returns y multiplied by 4.
    :param y: int.
    :return: float sum of y multiplied by 4.
    """
    return y * 4

num = int(input("type a number: "))
print("dividing by 2...")
num1 = division(num)
print("multiplying by 4...")
num2 = multiply(num1)
print(f"the final number is {num2}")



""" write a function that converts a string to a float """
def convert(string):
    """
    Converts given string to a float.
    :param string: str.
    :return: float value of given string or error message.
    """
    try:
        return print(float(string))
    except ValueError:
        print(f"{string} cannot be converted to a float.")
        
convert(input("Type something to be converted to a float: "))



""" add a doctring to all above functions """
