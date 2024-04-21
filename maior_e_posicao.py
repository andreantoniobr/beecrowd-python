def get_bigger(numbers_amount):
    i = 1
    bigger = 0
    bigger_position = 0
    while i <= numbers_amount:
        n = int(input())
        if n > bigger:
            bigger = n
            bigger_position = i
        i += 1
    return bigger, bigger_position

def main():
    numbers_amount = 100
    bigger, bigger_position = get_bigger(numbers_amount)
    print(bigger)
    print(bigger_position)

main()