class QuickTree(Tree):
    """Represent a tree that grows more quickly."""

    def grow(self, sunlight, water):
        """Grow by adding exactly sunlight leaves and water trunk height."""
        self._trunk_height += water
        self._number_of_leaves += sunlight
