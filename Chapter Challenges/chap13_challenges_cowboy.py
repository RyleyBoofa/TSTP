# Chapter 13 challenges

""" create a Horse and a Rider class and use composition to model that the horse has a rider """
class Rider():
    def __init__(self, n):
        self.name = n


class Horse():
    def __init__(self, n, r):
        self.name = n
        self.rider = r

    def add_rider(self, r):
        self.rider = r
        print(f"{self.name} received a new rider.")


rider = Rider("Texas Ranger")
print(f"{rider.name} just rode into town, looking for a new horse.")

horse = Horse("Bucky", None)
print(f"{horse.name} is lonely because his rider is currently {horse.rider}.")

horse.add_rider(rider)
print(f"{horse.name} is happy now because of his new rider, {horse.rider.name}.")
