# ladybug.py

class Ladybug:
    """A class to represent a ladybug."""

    def __init__(self, name="Dot", color="red", spots=7):
        """
        Initialize a Ladybug instance.

        Parameters:
            name (str): The name of the ladybug.
            color (str): The color of the ladybug.
            spots (int): The number of spots on the ladybug's wings.
        """
        self.name = name
        self.color = color
        self.spots = spots

    def crawl(self):
        """Simulate the ladybug crawling."""
        print(f"{self.name} is crawling slowly on a leaf.")

    def fly(self):
        """Simulate the ladybug flying."""
        print(f"{self.name} spreads its {self.color} wings with {self.spots} spots and takes flight.")

    def make_sound(self):
        """Simulate the ladybug making a faint, soft rustling sound."""
        print(f"{self.name} makes a faint rustling sound as it moves.")

# Example usage
if __name__ == "__main__":
    my_ladybug = Ladybug(name="Luna", color="yellow", spots=5)
    my_ladybug.crawl()
    my_ladybug.fly()
    my_ladybug.make_sound()