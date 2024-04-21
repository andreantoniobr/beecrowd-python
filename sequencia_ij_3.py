i = 1
y = 3
j = 7
x = j
while i <= 9:
    while y > 0:
        print(f"I={i} J={j}")
        y -= 1
        j -= 1
    x += 2
    y = 3
    j = x  
    i += 2