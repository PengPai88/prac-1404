from prac_09.unreliable_car import UnreliableCar

unreliable_car = UnreliableCar("Unreliable", 100, 30)

total_distance = 0
for _ in range(100):
    total_distance += unreliable_car.drive(1)

print(f"Total distance driven in 100 tries with 30% reliability: {total_distance} km")
