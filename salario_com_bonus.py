seller_name = input()
fixed_salary = float(input())
sales_value_money = float(input())
commission_percent = 0.15
salary = fixed_salary + sales_value_money * commission_percent
print(f"TOTAL = R$ {salary:.2f}")