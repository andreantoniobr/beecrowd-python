salary = float(input())

def get_salary_to_apply_tax_min(salary:float, min:float) -> float:  
    salary_to_apply_tax = 0
    if salary > min:
        salary_to_apply_tax = salary - min
    return salary_to_apply_tax

def get_salary_to_apply_tax_max(salary:float, max:float) -> float:  
    salary_to_apply_tax = 0
    if salary > max:
        salary_to_apply_tax = max
    return salary_to_apply_tax

def get_salary_to_apply_tax_in_range(salary:float, min:float, max:float) -> float:
    salary_to_apply_tax = 0
    salary_to_apply_tax += get_salary_to_apply_tax_max(salary, max)
    salary_to_apply_tax += get_salary_to_apply_tax_min(salary, min)    
    return salary_to_apply_tax

def get_tax_min(tax_per_cent:int, salary:float, min:float) -> float:
    return (tax_per_cent / 100) * get_salary_to_apply_tax_min(salary, min)

def get_tax_in_range(tax_per_cent:int, salary:float, min:float, max:float) -> float:
    return (tax_per_cent / 100) * get_salary_to_apply_tax_in_range(salary, min, max)

def try_get_tax(salary:float):
    can_get_tax = False
    tax = 0
    tax += get_tax_in_range(8, salary, 2000, 3000)    
    tax += get_tax_in_range(18, salary, 3000, 4500)    
    tax += get_tax_min(28, salary, 4500)    
    if tax > 0:
        can_get_tax = True
    return can_get_tax, tax

can_get_tax, tax = try_get_tax(salary)
if(can_get_tax):
    print(tax)
else:
    print("Isento")