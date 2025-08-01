"""
CP1404/CP5632 Practical
Tree class with inherited (specialised tree) classes
by Trevor Andersen
"""
import random

TREE_LEAVES_PER_ROW = 3


class Tree:
    """Represent a tree, with trunk height and a number of leaves."""

    def __init__(self):
        """Initialise a Tree with trunk_height of 1 and full row of leaves."""
        self._trunk_height = 1
        self._number_of_leaves = TREE_LEAVES_PER_ROW

    def __str__(self):
        """Return a string representation of the full Tree, e.g.
         ###
         ###
          |
          |    """
        return self.get_ascii_leaves() + self.get_ascii_trunk()

    def get_ascii_leaves(self):
        """Return a string representation of the tree's leaves."""
        result = ""
        if self._number_of_leaves % TREE_LEAVES_PER_ROW > 0:
            result += "#" * (self._number_of_leaves % TREE_LEAVES_PER_ROW)
            result += "\n"
        for i in range(self._number_of_leaves // TREE_LEAVES_PER_ROW):
            result += "#" * TREE_LEAVES_PER_ROW
            result += "\n"
        return result

    def get_ascii_trunk(self):
        """Return a string representation of the tree's trunk."""
        result = ""
        # the _ (underscore) variable is a convention for an unused variable
        for _ in range(self._trunk_height):
            result += " | \n"
        return result

    def grow(self, sunlight, water):
        """Grow a tree based on the sunlight and water parameters.
        Randomly grow the trunk height by a number between 0 and water.
        Randomly increase the leaves by a number between 0 and sunlight."""
        self._trunk_height += random.randint(0, water)
        self._number_of_leaves += random.randint(0, sunlight)


class QuickTree(Tree):
    """Represent a tree that grows more quickly."""

    def grow(self, sunlight, water):
        """Grow by adding exactly sunlight leaves and water trunk height."""
        self._trunk_height += water
        self._number_of_leaves += sunlight


class FruitTree(Tree):
    """Represent a tree that has fruit as well as leaves."""

    def __init__(self):
        super().__init__()
        self._fruit = 1

    def grow(self, sunlight, water):
        """Grow tree and randomly add/remove fruit."""
        super().grow(sunlight, water)
        # 1/2 chance to add a fruit
        if random.randint(1, 2) == 1:
            self._fruit += 1
        # 1/5 chance to lose a fruit
        if self._fruit > 0 and random.randint(1, 5) == 1:
            self._fruit -= 1

    def get_ascii_leaves(self):
        """Show fruit (.) above leaves, wrapping within max width (3)."""
        max_width = 3
        result = ""
        # Add fruit dots in rows of max_width
        full_rows, remainder = divmod(self._fruit, max_width)
        for _ in range(full_rows):
            result += "." * max_width + "\n"
        if remainder > 0:
            result += "." * remainder + "\n"
        # Then add leaves using base class logic
        result += super().get_ascii_leaves()
        return result
