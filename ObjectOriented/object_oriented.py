# object_oriented.py
"""Python Essentials: Object Oriented Programming.
<Veronica Churchill>
<420>
<5/10/2025>
"""

from math import sqrt


class Backpack:
    """A Backpack object class. Has a name and a list of contents.

    Attributes:
        name (str): the name of the backpack's owner.
        contents (list): the contents of the backpack.
    """

    # Problem 1: Modify __init__() and put(), and write dump().
    def __init__(self, name, color=None, max_size=5):
        """Set the name and initialize an empty list of contents.

        Parameters:
            name (str): the name of the backpack's owner.
        """
        self.name = name
        self.color= color
        self.max_size= max_size
        self.contents = []

    def put(self, item):
        """Add an item to the backpack's list of contents."""
        if len(self.contents) >= self.max_size:
            print("No Room!")
        else:
            self.contents.append(item)

    def take(self, item):
        """Remove an item from the backpack's list of contents."""
        self.contents.remove(item)
    def dump(self):
        self.contents = []

    # Magic Methods -----------------------------------------------------------

    # Problem 3: Write __eq__() and __str__().
    def __add__(self, other):
        """Add the number of contents of each Backpack."""
        return len(self.contents) + len(other.contents)

    def __lt__(self, other):
        """Compare two backpacks. If 'self' has fewer contents
        than 'other', return True. Otherwise, return False.
        """
        return len(self.contents) < len(other.contents)
    
    def __eq__(self, other):
        return (
            self.name == other.name and
            self.color == other.color and
            len(self.contents) == len(other.contents))
    
    def __str__(self):
        return (
            f"Owner:    {self.name}\n"
            f"Color:    {self.color}\n"
            f"Size:     {len(self.contents)}\n"
            f"Max Size: {self.max_size}\n"
            f"Contents: {self.contents}")


# An example of inheritance. You are not required to modify this class.
class Knapsack(Backpack):
    """A Knapsack object class. Inherits from the Backpack class.
    A knapsack is smaller than a backpack and can be tied closed.

    Attributes:
        name (str): the name of the knapsack's owner.
        color (str): the color of the knapsack.
        max_size (int): the maximum number of items that can fit inside.
        contents (list): the contents of the backpack.
        closed (bool): whether or not the knapsack is tied shut.
    """
    def __init__(self, name, color):
        """Use the Backpack constructor to initialize the name, color,
        and max_size attributes. A knapsack only holds 3 item by default.

        Parameters:
            name (str): the name of the knapsack's owner.
            color (str): the color of the knapsack.
            max_size (int): the maximum number of items that can fit inside.
        """
        Backpack.__init__(self, name, color, max_size=3)
        self.closed = True

    def put(self, item):
        """If the knapsack is untied, use the Backpack.put() method."""
        if self.closed:
            print("I'm closed!")
        else:
            Backpack.put(self, item)

    def take(self, item):
        """If the knapsack is untied, use the Backpack.take() method."""
        if self.closed:
            print("I'm closed!")
        else:
            Backpack.take(self, item)

    def weight(self):
        """Calculate the weight of the knapsack by counting the length of the
        string representations of each item in the contents list.
        """
        return sum(len(str(item)) for item in self.contents)


# Problem 2: Write a 'Jetpack' class that inherits from the 'Backpack' class.


# Problem 4: Write a 'ComplexNumber' class.


# Tests for problems
#1 and 3
def test_backpack():
    bp = Backpack("Veronica", "blue", 2)
    print(bp)
    bp.put("book")
    bp.put("pen")
    bp.put("laptop")
    print(bp)
    bp.take("pen")
    print(bp)
    bp.dump()
    print(bp)

    bp2 = Backpack("Veronica", "blue", 2)
    print("Equal?", bp == bp2)  # should be True
if __name__ == "__main__":
    test_backpack()