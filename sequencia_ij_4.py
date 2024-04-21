i = 0
j = 1
x = 1

def convert_value(x):
    if x == int(x):
        x = int(x)
    else:
        x = f"{x:.1f}"
        x = float(x)
    return x

while i <= 2:
    while x <= 3:
        j = x + i
        j = convert_value(j)
        print(f"I={i} J={j}")
        x += 1
    x = 1  
    i += 0.2
    i = convert_value(i)