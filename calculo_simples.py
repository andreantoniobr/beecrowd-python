parts_value_total = 0

def get_part_price():
    part_data = input().split()
    parts_amount = int(part_data[1])
    part_price = float(part_data[2])
    return parts_amount * part_price

parts_value_total += get_part_price()
parts_value_total += get_part_price()
print(f"VALOR A PAGAR: R$ {parts_value_total:.2f}")