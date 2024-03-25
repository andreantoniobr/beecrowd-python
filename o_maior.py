def get_bigger_two(a, b):
    return int((a + b + abs(a - b)) / 2)

def get_bigger(a, b, c):
    return get_bigger_two(get_bigger_two(a, b), c)

numbers = input().split()
a = int(numbers[0])
b = int(numbers[1])
c = int(numbers[2])
bigger = get_bigger(a, b, c)
print(f"{bigger} eh o maior")