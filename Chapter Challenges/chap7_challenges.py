# Chapter 7 challenges

""" print each item in the list """
print("Printing each item in the list... ")
shows = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]
for show in shows:
    print(show)

""" print all numbers from 25 to 50 """
print("Printing all numbers 25-50... ")
for i in range(25, 51):
    print(i)

""" print each item in the list from the first challenge and their indexes """
print("Printing shows list and their indexes... ")
for i, show in enumerate(shows):
    print(f"Show number {i} is {show}")

""" write a program with an infinite loop, with an option to quit """
import random
print("Asking question indefinitely... ")
question = "Guess a number: "
correct = str(random.randint(1, 10))
answer = ""
while answer != correct:
    print("Type q to quit")
    answer = input(question)
    if answer == "q":
        print("Quitting... ")
        break
    elif answer == correct:
        print("Correct!")
    else:
        print("Try again... ")

""" multiply the numbers in one list by the numbers in another list and print results """
print("Multiplying numbers... ")
nums1 = [8, 19, 148, 4]
nums2 = [9, 1, 33, 83]
nums3 = []
for num1 in nums1:
    for num2 in nums2:
        num3 = num1 * num2
        nums3.append(num3)
for num in nums3:
    print(num)
