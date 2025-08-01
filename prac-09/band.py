class Band:
    """Band class - a Band has a list of Musicians."""

    def __init__(self, name=""):
        """Initialise a Band with a name and empty list of musicians."""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add a Musician to the band."""
        self.musicians.append(musician)

    def __str__(self):
        """Return a string representation of the Band and its musicians."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def play(self):
        """Return the result of each musician playing."""
        return "\n".join(musician.play() for musician in self.musicians)
