def sort(a, b, c):
    if a > c:
        a, c = c, a
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    return a, b, c

def print_values(a, b, c):
    print(a)
    print(b)
    print(c)

def main():
    data = input().split()
    a = int(data[0])
    b = int(data[1])
    c = int(data[2])

    x, y, z = sort(a, b, c)

    print_values(x, y, z)
    print()
    print_values(a, b, c)

main()