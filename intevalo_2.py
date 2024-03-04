numbers = []
numbers_in = 0
numbers_out = 0
range_start = 10
range_end = 20
input_amount = int(input())

for number in range(input_amount):
    numbers.append(int(input()))

for number in numbers:
    if number >= range_start and number <= range_end:
        numbers_in += 1

numbers_out = len(numbers) - numbers_in

print(f"{numbers_in} in")
print(f"{numbers_out} out")