def get_interval(x):
    interval = "Fora de intervalo"
    if x >= 0 and x <= 25:
        interval = "Intervalo [0,25]"
    elif x > 25 and x <= 50:
        interval = "Intervalo (25,50]"
    elif x > 50 and x <= 75:
        interval = "Intervalo (50,75]"
    elif x > 75 and x <= 100:
        interval = "Intervalo (75,100]"        
    return interval

def main():
    number = float(input())
    print(get_interval(number))

main()