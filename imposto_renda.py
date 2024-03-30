def get_tax(salary):
    tax_to_pay = 0 
    
    if salary > 2000:
        tax = 8
        if(salary >= 3000):
            salary_to_calc = 1000
        else:            
            salary_to_calc = salary - 2000
        tax_to_pay += salary_to_calc * (tax / 100)    
    
    if salary > 3000:
        tax = 18       
        if(salary >= 4500):
            salary_to_calc = 1500
        else:            
            salary_to_calc = salary - 3000
        tax_to_pay += salary_to_calc * (tax / 100)
    
    if salary > 4500:
        tax = 28       
        salary_to_calc = salary - 4500
        tax_to_pay += salary_to_calc * (tax / 100)    
    
    return tax_to_pay

def main():
    salary = float(input())
    tax = get_tax(salary)
    if(tax > 0):        
        print(f"R$ {tax:.2f}")
    else:
        print("Isento")

main()