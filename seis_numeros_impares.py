number = int(input())
max_odd_numbers_amount = 6
current_odd_numbers_amount = 0

while current_odd_numbers_amount < max_odd_numbers_amount:
    if number % 2 != 0:
        print(number)
        current_odd_numbers_amount += 1
    number += 1
