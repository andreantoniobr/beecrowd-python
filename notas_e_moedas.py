money = float(input())
money *= 100

def get_money_type_amount(money, money_value):
    money_type_amount = int(money // money_value)
    money -= money_type_amount * money_value
    return money_type_amount, money

def print_note(note_amount, note_value):
    print(f"{note_amount} nota(s) de R$ {note_value:.2f}")

def print_coin(coin_amount, coin_value):
    print(f"{coin_amount} moeda(s) de R$ {coin_value:.2f}")

note_100, money = get_money_type_amount(money, 10000)
note_50, money = get_money_type_amount(money, 5000)
note_20, money = get_money_type_amount(money, 2000)
note_10, money = get_money_type_amount(money, 1000)
note_5, money = get_money_type_amount(money, 500)
note_2, money = get_money_type_amount(money, 200)

coin_1, money = get_money_type_amount(money, 100)
coin_2, money = get_money_type_amount(money, 50)
coin_3, money = get_money_type_amount(money, 25)
coin_4, money = get_money_type_amount(money, 10)
coin_5, money = get_money_type_amount(money, 5)
coin_6, money = get_money_type_amount(money, 1)

print("NOTAS:")
print_note(note_100, 100)
print_note(note_50, 50)
print_note(note_20, 20)
print_note(note_10, 10)
print_note(note_5, 5)
print_note(note_2, 2)

print("MOEDAS:")
print_coin(coin_1, 1.00)
print_coin(coin_2, 0.50)
print_coin(coin_3, 0.25)
print_coin(coin_4, 0.10)
print_coin(coin_5, 0.05)
print_coin(coin_6, 0.01)