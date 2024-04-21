def main():
    grades_sum = 0
    valid_grades_amount = 0
    while True:
        n = float(input())
        if n >= 0 and n <= 10:
            grades_sum += n
            if valid_grades_amount == 1:                
                average = grades_sum / 2
                print(f"media = {average:.2f}")
                break
            valid_grades_amount += 1
        else:
            print("nota invalida")

main()