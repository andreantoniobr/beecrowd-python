def get_middle(a, b, c):
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b   
    return b

def get_middle2(a, b, c):    
    max = a
    middle = a
    min = a

    if b > max:
        max = b
    if c > max:
        max = c
    
    if b < min:
        min = b
    if c < min:
        min = c

    if b != max and b != min:
        middle = b
    if c != max and c != min:
        middle = c
    
    return middle




print(get_middle(3, 5, 9))
print(get_middle(3, 9, 5))
print(get_middle(5, 3, 9))
print(get_middle(5, 9, 3))
print(get_middle(9, 5, 3))
print(get_middle(9, 3, 5))

print()
print(get_middle2(3, 5, 9))
print(get_middle2(3, 9, 5))
print(get_middle2(5, 3, 9))
print(get_middle2(5, 9, 3))
print(get_middle2(9, 5, 3))
print(get_middle2(9, 3, 5))

print(get_middle2(-50, 555, 0))