"""
    The Self Taught Programmer
    Chapter 8: Modules
"""

# this line will run when imported as it's not constrained to this files "main"
print("This code WILL run when module is imported")

if __name__ == "__main__":
    # this line won't run when imported as it's constrained to this files "main"
    print("This code will NOT run when the module is imported")