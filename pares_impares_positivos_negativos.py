a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

numbers = [a, b, c, d, e]

pair_numbers_amount = 0
odd_numbers_amount = 0
positive_numbers_amount = 0
negative_numbers_amount = 0

for number in numbers:
    if number % 2 == 0:
        pair_numbers_amount += 1
    else:
        odd_numbers_amount += 1

    if number > 0:
        positive_numbers_amount += 1
    elif number < 0:
        negative_numbers_amount += 1  

print(f"{pair_numbers_amount} valor(es) par(es)")
print(f"{odd_numbers_amount} valor(es) impar(es)")
print(f"{positive_numbers_amount} valor(es) positivo(s)")
print(f"{negative_numbers_amount} valor(es) negativo(s)")