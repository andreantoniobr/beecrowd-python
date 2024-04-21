def print_numbers_rest_two(number):
    i = 1
    while i <= 10000:
        if i % number == 2:
            print(i)
        i += 1

def main():
    number = int(input())
    print_numbers_rest_two(number)

main()