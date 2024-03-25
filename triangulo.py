def can_form_triangle(a, b, c):
    a, b, c = sort_reversed(a, b, c)
    return a < b + c

def sort_reversed(a, b, c):
    if a < c:
        a, c = c, a
    if a < b:
        a, b = b, a
    if b < c:
        b, c = c, b    
    return a, b, c

def print_perimeter(a, b, c):
    perimeter = a + b + c
    print(f"Perimetro = {perimeter:.1f}")

def print_area(a, b, c):
    area = ((a + b) * c) / 2
    print(f"Area = {area:.1f}")

def main():
    data = input().split()
    a = float(data[0])
    b = float(data[1])
    c = float(data[2])
    
    if can_form_triangle(a, b, c):
        print_perimeter(a, b, c)
    else:
        print_area(a, b, c)

main()