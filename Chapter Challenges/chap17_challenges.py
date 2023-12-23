# Chapter 17 challenges

""" write a regex that matches the word 'Dutch' in 'The Zen of Python' """
import re

with open("zen.txt",
          "r") as f:
    text = f.read()
    dutch = re.findall("Dutch", text, re.IGNORECASE)
    print(dutch)
    

""" write a regex that matches all the digits in the string """
string = "Arizona 479, 501, 870. California 209, 213, 650."
nums = re.findall("\\d", string, re.MULTILINE)
print(nums)


""" write a regex that matches any word that starts with any character and is followed by 2 o's """
story = "The ghost that says boo haunts the loo."
oo = re.findall(".oo", story, re.IGNORECASE)
print(oo)
