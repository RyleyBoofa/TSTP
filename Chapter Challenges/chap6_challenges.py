# Chapter 6 challenges

""" print every character in a string """
strng = "Python"
print("Printing each character in a string...")
for c in strng:
    print(c)

""" write a program that collects 2 strings from the user
    concatenate these strings into one string and print it """
print("Concatenating strings...")
s1 = input("What did you do yesterday? ")
s2 = input("How was it? ")
s3 = "yesterday you {} and you thought it was {}".format(s1, s2)
print(s3)

""" use a method to make the string gramatically correct """
print("Fixing the string's grammar...")
print(s3.capitalize())

""" split the following string into a list of questions """
splitter = "Who? What? Where? When? Why? How?"
print(f"Spliting: {splitter} into a list of questions...")
q1 = splitter[:4]
q2 = splitter[5:10]
q3 = splitter[11:17]
q4 = splitter[18:23]
q5 = splitter[24:28]
q6 = splitter[29:]
questions = [q1, q2, q3, q4, q5, q6]
for q in questions:
    print(q)

""" turn the list into a sentence """
word_list = ["the", "fox", "jumped", "over", "the", "fence", "."]
print(f"Turning list: {word_list} into a sentence...")
sentence = "{} {} {} {} {} {} {}".format(word_list[0].capitalize(), word_list[1], word_list[2], word_list[3], word_list[4], word_list[5], word_list[6])
print(sentence)

""" replace every 's' with a '$' """
phrase = "A screaming comes across the sky."
print(f"Replacing s's with $'s...")
print(phrase.replace("s", "$"))

""" use a method to find the index of the first 'm' in the following string """
phrs = "Hemingway"
print(f"Finding the index of 'm' in {phrs}...")
print(phrs.index("m"))

""" turn a quote (containing dialogue) into a string """
quote = 'He thought to himself "what the fuck, bro?"'
print(f"String with a quote: {quote}")

""" create the string "three three three" in 2 different ways """
word = "three "
print("Printing with concatenation...")
print(word + word + word)
print("Printing with multiplication...")
print(word*3)

""" slice the string to only include the characters before the comma """
splt = "It was a bright cold day in April, and the clock was striking thirteen."
new = splt.split(",")
print("Printing the start of the string only...")
print(new[0])
