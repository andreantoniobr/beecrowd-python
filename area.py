numbers = input().split()
a = float(numbers[0])
b = float(numbers[1])
c = float(numbers[2])

PI = 3.14159
triangle_area = (a * c) / 2
circle_area = PI * c ** 2
trapeze_area = ((a + b) * c) / 2
square_area = b ** 2
rectangle_area = a * b

print(f"TRIANGULO: {triangle_area:.3f}")
print(f"CIRCULO: {circle_area:.3f}")
print(f"TRAPEZIO: {trapeze_area:.3f}")
print(f"QUADRADO: {square_area:.3f}")
print(f"RETANGULO: {rectangle_area:.3f}")