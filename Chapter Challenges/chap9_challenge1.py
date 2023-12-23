# Chapter 9 challenges

""" write a program that survey's a user and saves their answers in a file """
fp = "chap9_survey_answers.txt"
questions = [
    "What is your name? ",
    "How old are you? ",
    "What is your favourite colour? ",
    "Dogs or cats? "
    ]
with open(fp, "w") as f: # open file for writing and close when finished
    for q in questions:
        f.write(input(q)) # use input method to get answer for each question and write it to the file
        f.write("\n") # new line after each answer
        print("Answer saved.")

print("Retrieving your answers...\n")
with open(fp, "r") as f: # open file for reading and close when finished
    print(f.read()) # use print method and file object's read method to print answers
print("Thank you for taking the quiz. Have a nice day :)")
