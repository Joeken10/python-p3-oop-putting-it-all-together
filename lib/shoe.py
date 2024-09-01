#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = "New"

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        else:
            self._size = value

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"

# Create an instance of the Shoe class
stan_smith= Shoe("Adidas", 9)

# Access and print the attributes and methods
print(f"Brand: {stan_smith.brand}")
print(f"Size: {stan_smith.size}")
print(f"Condition: {stan_smith.condition}")

# Call the cobble method
stan_smith.cobble()

# Print the updated condition
print(f"Condition after repair: {stan_smith.condition}")
