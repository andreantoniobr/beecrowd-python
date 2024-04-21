def get_positive_values(input_amount):
    positive_values_amount = 0
    total_value = 0
    i = 0
    while i < input_amount:
        n = float(input())
        if n > 0:
            positive_values_amount += 1
            total_value += n
        i += 1
    return positive_values_amount, total_value

def main():
    input_amount = 6
    positive_values_amount, total_value = get_positive_values(input_amount)
    average = total_value / positive_values_amount
    print(f"{positive_values_amount} valores positivos")
    print(f"{average:.1f}")

main()