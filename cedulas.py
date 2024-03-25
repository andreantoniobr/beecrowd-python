money_total = int(input())
money = money_total

def get_notes(money, note_value):
    note_amount = money // note_value
    money -= note_amount * note_value
    return note_amount, money

def print_note(note_amount, note_value):
    print(f"{note_amount} nota(s) de R$ {note_value},00")

note_100, money = get_notes(money, 100)
note_50, money = get_notes(money, 50)
note_20, money = get_notes(money, 20)
note_10, money = get_notes(money, 10)
note_5, money = get_notes(money, 5)
note_2, money = get_notes(money, 2)
note_1, money = get_notes(money, 1)

print(money_total)
print_note(note_100, 100)
print_note(note_50, 50)
print_note(note_20, 20)
print_note(note_10, 10)
print_note(note_5, 5)
print_note(note_2, 2)
print_note(note_1, 1)