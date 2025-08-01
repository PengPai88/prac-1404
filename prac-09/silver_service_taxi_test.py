from prac_09.silver_service_taxi import SilverServiceTaxi

fancy_taxi = SilverServiceTaxi("Hummer", 200, 2)
fancy_taxi.drive(18)

print(fancy_taxi)
print(f"Fare: ${fancy_taxi.get_fare():.2f}")

assert round(fancy_taxi.get_fare(), 2) == 48.80
