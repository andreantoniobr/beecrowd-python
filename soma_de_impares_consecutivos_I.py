start = int(input())
end = int(input())
if start > end:
    start, end = end, start
odd_numbers = [number for number in range(start + 1, end) if number % 2 != 0]
print(sum(odd_numbers))