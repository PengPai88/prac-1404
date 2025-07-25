from musician import Musician

class Guitarist(Musician):
    def play(self):
        if not self.instruments:
            return f"{self.name} needs a guitar!"

        return f"{self.name} is shredding: {self.instruments[0]}"

class Drummer(Musician):
    def play(self):
        return f"{self.name} is banging the drums!"

class Singer(Musician):
    def play(self):
        return f"{self.name} is singing!"
