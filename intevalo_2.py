def get_numbers_interval(numbers_amount):
    numbers_in_interval_amount = 0
    numbers_out_interval_amount = 0
    i = 0
    while i < numbers_amount:
        number = int(input())
        if number >= 10 and number <= 20:
            numbers_in_interval_amount += 1
        else:
            numbers_out_interval_amount += 1
        i += 1
    return numbers_in_interval_amount, numbers_out_interval_amount

def main():
    numbers_amount = int(input())
    numbers_in_interval_amount, numbers_out_interval_amount = get_numbers_interval(numbers_amount)
    print(f"{numbers_in_interval_amount} in")
    print(f"{numbers_out_interval_amount} out")

main()