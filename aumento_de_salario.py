def get_readjustment(salary):
    readjustment = 0
    if salary > 0 and salary <= 400:
        readjustment = 15
    elif salary > 400 and salary <= 800:
        readjustment = 12
    elif salary > 800 and salary <= 1200:
        readjustment = 10
    elif salary > 1200 and salary <= 2000:
        readjustment = 7
    elif salary > 2000:
        readjustment = 4   
    return readjustment 

def calc_new_salary(salary):
    readjustment = get_readjustment(salary)
    readjustment_in_salary = salary * (readjustment / 100)
    new_salary = salary + readjustment_in_salary
    return new_salary, readjustment_in_salary, readjustment

def print_new_salary(salary):
    new_salary, readjustment_in_salary, readjustment = calc_new_salary(salary)
    print(f"Novo salario: {new_salary:.2f}")
    print(f"Reajuste ganho: {readjustment_in_salary:.2f}")
    print(f"Em percentual: {readjustment} %")

def main():
    salary = float(input())
    print_new_salary(salary)

main()