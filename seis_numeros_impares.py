def print_odd_values(n, max_numbers_amount):
    numbers_amount = 0
    i = n
    while numbers_amount < max_numbers_amount:
        if i % 2 != 0:
            numbers_amount += 1
            print(i)
        i += 1

def main():
    n = int(input())
    max_numbers_amount = 6
    print_odd_values(n, max_numbers_amount)
    
main()