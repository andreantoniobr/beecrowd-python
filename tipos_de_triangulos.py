def sort_reversed(a, b, c):
    if a < c:
        a, c = c, a
    if a < b:
        a, b = b, a
    if b < c:
        b, c = c, b
    return a, b, c

def can_form_triangle(a, b, c):    
    return a < c + b

def print_triangle_types(a, b, c):
    a, b, c = sort_reversed(a, b, c)
    if can_form_triangle(a, b, c):
        if a ** 2 == b ** 2 + c ** 2:
            print("TRIANGULO RETANGULO")
        elif a ** 2 > b ** 2 + c ** 2:
            print("TRIANGULO OBTUSANGULO")
        elif a ** 2 < b ** 2 + c ** 2:
            print("TRIANGULO ACUTANGULO")
        
        if a == b and b == c:
            print("TRIANGULO EQUILATERO")
        elif (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
            print("TRIANGULO ISOSCELES")
    else:
        print("NAO FORMA TRIANGULO")

def main():
    data = input().split()
    a = float(data[0])
    b = float(data[1])
    c = float(data[2])

    print_triangle_types(a, b, c)

main()