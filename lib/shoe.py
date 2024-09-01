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


stan_smith= Shoe("Adidas stan-smith", 9)


print(f"Brand: {stan_smith.brand}")
print(f"Size: {stan_smith.size}")
print(f"Condition: {stan_smith.condition}")


stan_smith.cobble()


print(f"Condition after repair: {stan_smith.condition}")
