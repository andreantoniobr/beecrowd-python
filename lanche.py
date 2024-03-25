def get_price_by_code(code):
    price = 0
    if code == 1:
        price = 4.00
    elif code == 2:
        price = 4.50
    elif code == 3:
        price = 5.00
    elif code == 4:
        price = 2.00
    elif code == 5:
        price = 1.50
    return price

def main():
    data = input().split()
    code = int(data[0])
    amount = int(data[1])
    total_price = get_price_by_code(code) * amount
    print(f"Total: R$ {total_price:.2f}")

main()