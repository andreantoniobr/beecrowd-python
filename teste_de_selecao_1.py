numbers = input().split()
a = int(numbers[0])
b = int(numbers[1])
c = int(numbers[2])
d = int(numbers[3])

def are_valid_values(a, b, c, d):
    cond_1 = b > c and d > a
    cond_2 = (c + d) > (a + b)
    cond_3 = c > 0 and d > 0
    cond_4 = a % 2 == 0
    return cond_1 and cond_2 and cond_3 and cond_4

if are_valid_values(a, b, c, d):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")