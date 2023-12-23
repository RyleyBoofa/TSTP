# Chapter 8 challenges

""" call a different function from the stats module """
import statistics
nums = [1, 3, 5, 7, 9, 11]
print(f"The variance from {nums} is... ")
print(statistics.variance(nums))

""" create a 'cube' module """
import chap8_challenges_module
num = int(input("Number: "))
print(chap8_challenges_module.cube_number(num))
