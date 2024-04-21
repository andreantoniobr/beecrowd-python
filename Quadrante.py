def get_quadrant(x, y):
    quad = ""
    if x > 0 and y > 0:
        quad = "primeiro"
    elif x < 0 and y > 0:
        quad = "segundo"
    elif x < 0 and y < 0:
        quad = "terceiro"
    elif x > 0 and y < 0:
        quad = "quarto"
    return quad

def main():
    x, y = map(int, input().split())
    while x != 0 and y != 0:
        print(get_quadrant(x, y))
        x, y = map(int, input().split())

main()