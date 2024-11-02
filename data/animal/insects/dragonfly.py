# dragonfly.py

class Dragonfly:
    """A class to represent a dragonfly."""

    def __init__(self, name="Dart", wing_span=5.0, flight_speed=10.0):
        """
        Initialize a Dragonfly instance.

        Parameters:
            name (str): The name of the dragonfly.
            wing_span (float): The wing span of the dragonfly in centimeters.
            flight_speed (float): The flight speed of the dragonfly in km/h.
        """
        self.name = name
        self.wing_span = wing_span
        self.flight_speed = flight_speed

    def fly(self):
        """Simulate the dragonfly flying."""
        print(f"{self.name} is darting around at {self.flight_speed} km/h with a wingspan of {self.wing_span} cm!")

    def rest(self):
        """Simulate the dragonfly resting."""
        print(f"{self.name} gently lands on a leaf, resting its delicate wings.")

    def make_sound(self):
        """Simulate the dragonfly making a faint buzzing sound."""
        print(f"{self.name} makes a faint buzzing sound as its wings vibrate.")

# Example usage
if __name__ == "__main__":
    my_dragonfly = Dragonfly(name="Skimmer", wing_span=7.5, flight_speed=15.0)
    my_dragonfly.fly()
    my_dragonfly.rest()
    my_dragonfly.make_sound()