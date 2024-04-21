def print_numbers_interval_sum(n, m):
    sum = 0
    if n > m:
        n, m = m, n
    while n <= m:
        print(n, end=" ")
        sum += n
        n += 1
    print(f"Sum={sum}")

def main():
    n, m = map(int, input().split())
    while n > 0 and m > 0:
        print_numbers_interval_sum(n, m)
        n, m = map(int, input().split())
    
main()