a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

numbers = [a, b, c, d, e]
pair_numbers_amount = 0

for number in numbers:
    if number % 2 == 0:
        pair_numbers_amount += 1

print(f"{pair_numbers_amount} valores pares")