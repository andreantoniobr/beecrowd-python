start = 1
end = int(input())

for number in range(start, end + 1):
    if number % 2 != 0:
        print(number)