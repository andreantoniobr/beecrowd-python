for i in range(100):
    number = int(input())
    if i == 0:
        bigger = number
        position = 1
    
    if number > bigger:
        bigger = number
        position = i + 1

print(bigger)
print(position)    