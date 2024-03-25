def get_delta(a, b, c):
    return b ** 2 - 4 * a * c

def bhaskara(a, b, c):
    delta = get_delta(a, b, c)
    can_calculate = False
    x1 = 0
    x2 = 0
    if a != 0 and delta >= 0:
        x1 = (-b + delta ** 0.5) / (2 * a)
        x2 = (-b - delta ** 0.5) / (2 * a)
        can_calculate = True
    return can_calculate, x1, x2

def main():
    numbers = input().split()
    a = float(numbers[0])
    b = float(numbers[1])
    c = float(numbers[2])

    can_calculate, x1, x2 = bhaskara(a, b, c)
    if can_calculate:
        print(f"R1 = {x1:.5f}")
        print(f"R2 = {x2:.5f}")
    else:
        print("Impossivel calcular")

main()