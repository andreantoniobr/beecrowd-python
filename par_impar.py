input_amount = int(input())
numbers = []
for i in range(input_amount):
    numbers.append(int(input()))

for n in numbers:
    if n != 0 and n % 2 == 0:
        message = "EVEN"
    else:
        message = "ODD"

    if n > 0:
        message += " POSITIVE"
    elif n < 0:
        message += " NEGATIVE"

    if n == 0:
        message = "NULL"

    print(message)