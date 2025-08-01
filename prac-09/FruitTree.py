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
