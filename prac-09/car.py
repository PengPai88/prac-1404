"""
CP1404/CP5632 Practical
Car class (base class)
"""

class Car:
    def __init__(self, name, fuel):
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def drive(self, distance):
        if distance > self.fuel:
            distance = self.fuel
        self.fuel -= distance
        self.odometer += distance
        return distance

    def __str__(self):
        return f"{self.name}, fuel={self.fuel}, odometer={self.odometer}"
