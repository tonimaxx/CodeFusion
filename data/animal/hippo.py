# hippo.py

class Hippo:
    """A class to represent a hippo."""

    def __init__(self, name="Hank", weight=1500, water_affinity=8):
        """
        Initialize a Hippo instance.

        Parameters:
            name (str): The name of the hippo.
            weight (int): The weight of the hippo in kilograms.
            water_affinity (int): A measure of how much the hippo loves water, from 1 to 10.
        """
        self.name = name
        self.weight = weight
        self.water_affinity = water_affinity

    def eat(self, food):
        """Simulate the hippo eating."""
        print(f"{self.name} chomps down on {food} and seems very pleased.")

    def swim(self):
        """Simulate the hippo swimming."""
        if self.water_affinity > 5:
            print(f"{self.name} joyfully splashes in the water!")
        else:
            print(f"{self.name} wades in the water but seems indifferent.")

    def make_sound(self):
        """Simulate the hippo making a sound."""
        print(f"{self.name} lets out a deep, rumbling growl!")

# Example usage
if __name__ == "__main__":
    my_hippo = Hippo(name="Lulu", weight=1800, water_affinity=9)
    my_hippo.eat("grass")
    my_hippo.swim()
    my_hippo.make_sound()