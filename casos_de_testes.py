money = 0.3
money_value = 0.1

money_fixed = money * 100
money_value_fixed = money_value * 100
money_type_amount = int(money_fixed // money_value_fixed)

print(money_type_amount)