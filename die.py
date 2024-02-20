from random import randint

class Die:
    """A class represnting a single die."""

    def __init__(self,num_sides=6) -> None:
        """Assume a six-sided die."""
        self.num_sides = num_sides
    
    def roll(self):
        """Return a random value between 2 and number of sides"""
        return randint(1,self.num_sides)
    