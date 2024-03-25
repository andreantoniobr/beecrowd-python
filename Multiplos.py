def sort(a, b):    
    if a > b:
        a, b = b, a
    return a, b

def are_multiple(a, b):
    a, b = sort(a, b)
    if b % a == 0:
        return True
    else:
        return False

def main():
    data = input().split()
    a = int(data[0])
    b = int(data[1])

    if are_multiple(a, b):
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")

main()