# monkey.py

class Monkey:
    """A class to represent a monkey."""

    def __init__(self, name="George", age=5, favorite_food="banana"):
        """
        Initialize a Monkey instance.

        Parameters:
            name (str): The name of the monkey.
            age (int): The age of the monkey in years.
            favorite_food (str): The monkey's favorite food.
        """
        self.name = name
        self.age = age
        self.favorite_food = favorite_food

    def eat(self, food):
        """Simulate the monkey eating."""
        if food == self.favorite_food:
            print(f"{self.name} happily eats the {food}!")
        else:
            print(f"{self.name} reluctantly eats the {food}, but it's not their favorite.")

    def climb(self):
        """Simulate the monkey climbing."""
        print(f"{self.name} climbs up a tree with agility and grace.")

    def make_sound(self):
        """Simulate the monkey making a sound."""
        print(f"{self.name} chatters excitedly!")

# Example usage
if __name__ == "__main__":
    my_monkey = Monkey(name="Bobo", age=3, favorite_food="mango")
    my_monkey.eat("mango")
    my_monkey.climb()
    my_monkey.make_sound()