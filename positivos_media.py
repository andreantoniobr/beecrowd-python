a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

numbers = [a, b, c, d, e, f]
positive_numbers = []
positive_numbers_amount = 0

for number in numbers:
    if number > 0:
        positive_numbers.append(number)
        positive_numbers_amount += 1

average = sum(positive_numbers) / positive_numbers_amount

print(f"{positive_numbers_amount} valores positivos")
print(f"{average:.1f}")