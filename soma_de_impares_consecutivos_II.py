def print_interval_sum(x, y):
    sum = 0
    if x > y:
        x, y = y, x
    while x < y:
        x += 1
        if x == y:
            break
        if x % 2 != 0:
            sum += x        
    print(sum)

def main():
    n = int(input())
    i = 0    
    while i < n:
        x, y = map(int, input().split())
        print_interval_sum(x, y)
        i += 1

main()