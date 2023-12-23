import re

text = """Giraffes have aroused the curiosity of __PLURAL_NOUN__ since earliest 
        times. The giraffe is the tallest of all living __PLURAL_NOUN__, but 
        scientists are unable to explain how it got it's long 
        __PART_OF_THE_BODY__. The giraffe's tremendous height, which might reach 
        __NUMBER__ __PLURAL_NOUN__, comes from it's legs and __BODYPART__."""

def mad_libs(mls):
    """
    :param mls: String 
    with parts the user must fill out surrounded by double underscores. 
    """

    # get a list of hints by matching all words surrounded by doube underscores
    hints = re.findall("__.*?__", mls)
    if hints is not None:
        for word in hints:
            # use the hint to prompt the user for a word and store their answer
            q = f"Enter a {word} "
            new = input(q)
            # replace each hint with the user's words
            mls = mls.replace(word, new, 1)
        print('\n')
        # format text to print nicely
        mls = mls.replace("\n", "")
        print(mls)
    else:
        print("Invalid mls.")

mad_libs(text)