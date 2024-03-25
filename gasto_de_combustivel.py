time = int(input())
velocity = int(input())
distance = velocity * time
CAR_FUEL_AUTONOMY = 12
total_fuel = distance / CAR_FUEL_AUTONOMY
print(f"{total_fuel:.3f}")