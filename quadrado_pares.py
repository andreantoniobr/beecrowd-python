end = int(input())
for number in range(1, end + 1):
    if number % 2 == 0:
        squared = number**2
        print(f"{number}^2 = {squared}")