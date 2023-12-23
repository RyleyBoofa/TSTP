# Chapter 14 challenges

""" write a function that takes 2 objects and returns whether or not they're the same type """
def check_objects(obj1, obj2):
    print(type(obj1) == type(obj2))

class Object1():
    pass

class Object2():
    pass

o1 = Object1()
o2 = Object2()

check_objects(o1, o2)

o1 = o2

check_objects(o1, o2)
