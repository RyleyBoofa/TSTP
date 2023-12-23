import re

with open("zen.txt", "r") as f:
    txt = f.read()

    # simple match
    print("\nFinding matches with 'beautiful' ")
    beauty = re.findall("beautiful", txt, re.IGNORECASE)
    print(beauty)

    # match beginning
    print("\nFinding matches with '^If' ")
    sol = re.findall("^If", txt, re.MULTILINE)
    print(sol)

    # match ending
    print("\nFinding matches with 'idea.$' ")
    eol = re.findall("idea.$", txt, re.MULTILINE)
    print(eol)

# match multiple characters
print("\nFinding matches with 't[wo]o' ")
string = "Two too."
ow = re.findall("t[ow]o", string, re.IGNORECASE)
print(ow)

# match digits
print("\nFinding digits with '\\d' ")
line = "123?45 hello?"
digits = re.findall("\\d", line, re.IGNORECASE)
print(digits)

# match repetition
print("\nFinding matches with 'two*' ")
twos = "two twoo twooo not to too or too."
os = re.findall("two*", twos, re.IGNORECASE)
print(os)

# match nested repetition
print("\nFinding matches with '__.*__' ")
hello = "__hello__there"
hi = re.findall("__.*__", hello, re.IGNORECASE)
print(hi)

# greedy asterisk 
print("\nDemonstrating greedy asterisk ")
hello = "__hi__bye__hello__there"
hi = re.findall("__.*__", hello, re.IGNORECASE)
print(hi)

# non-greedy matching
print("\nFinding non-greedy matches with '__.*?__' ")
hello = "__one__ __two__ __three__"
hi = re.findall("__.*?__", hello)
for match in hi:
    print(match)

# escaping characters
print("\nFinding matches with '\\$' ")
dolla = "I love $!"
ds = re.findall("\\$", dolla, re.IGNORECASE)
print(ds)