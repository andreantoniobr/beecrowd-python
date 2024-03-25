def get_game_time(start, end):
    if start > end:
        time = (24 - start) + end
    elif start == end:
        time = 24
    elif start < end:
        time = end - start
    return time

def main():
    data = input().split()
    start = int(data[0])
    end = int(data[1])

    time = get_game_time(start, end)
    print(f"O JOGO DUROU {time} HORA(S)")

main()