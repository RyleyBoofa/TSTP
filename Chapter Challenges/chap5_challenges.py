# Chapter 5 challenges

""" create a list of favourite musicians """
musicians = ["Kendrick", "Drake", "J.Cole", "ACDC", "Metallica"]
print(f"List of fav musicians: {musicians}")

""" create a list of tuples containing the coords of somewhere you've lived """
locations = [
    (-37.800492, 145.289081),
    (-37.77333, 145.34284)]
print(f"I used to live at: {locations[1]}, now I live at: {locations[0]}")

""" create a dict that contains attributes about you """
me = {
    "name": "Boofa",
    "height": 180,
    "weight": 80,
    "fav-colour": "blue"
    }
print(f"About me: {me}")


""" write a program that lets the user ask about you,
    and returns the result from the above dict """
print("What do you want to know about me?")
query = input("Type 'name', 'height', 'weight', or 'colour': ")
if query == "name":
    print(me['name'])
elif query == "height":
    print(me['height'])
elif query == "weight":
    print(me['weight'])
elif query == "colour":
    print(me['fav-colour'])
else:
    print("Info not available")

""" create a dict mapping musicians to your fav song by them """
songs = {
    "Drake": "FPS Mode",
    "J Cole": "GOMD",
    "Kendrick": "DNA",
    "ACDC": "Highway to Hell",
    "Metallica": "Master of Puppets"
    }
print(f"Drake sings {songs['Drake']} and ACDC sing {songs['ACDC']}")

""" research sets """
"""
    sets are like a list that is unordered, unchangeable, and unindexed
    sets are defined using curly-brackets {}, but without key-value pairs (dict)
    sets DO NOT ALLOW DUPLICATE VALUES
    once a set is created, you cannot CHANGE values, you can ADD/REMOVE items
    sets can contain a mix of data-types
    use a list when values won't change, and you won't need to index into set
"""
# eg: create a set of fruits
fruits = {"apple", "banana", "orange", "pear"}
print(f"Here is a set of fruits: {fruits}")
