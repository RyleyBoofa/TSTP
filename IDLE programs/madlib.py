# MADLIB

print("We're going to write a Mad Lib together!")
n1 = input("Enter a noun: ")
v = input("Enter a verb: ")
adj = input("Enter an adjective: ")
n2 = input("Enter a noun: ")

madlib = "The {} {} the {} {}".format(n1, v, adj, n2)

print(madlib)
