start = 1
end = 10_000
n = int(input())

for i in range(start, end + 1):
    if i % n == 2:
        print(i)