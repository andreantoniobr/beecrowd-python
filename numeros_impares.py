def print_odd_numbers(start, end):
    i = start
    while i <= end:
        if i % 2 != 0:
            print(i)
        i += 1

def main():
    start = 1
    end = int(input())
    print_odd_numbers(start, end)

main()