p1 = 2
p2 = 3
p3 = 5
average_amount = int(input())
averages = []

def get_weighted_average(a, b, c):
    return (a * p1 + b * p2 + c * p3) / (p1 + p2 + p3)

for i in range(average_amount):
    averages.append(input().split())

for average in averages:
    a = float(average[0])
    b = float(average[1])
    c = float(average[2])
    weighted_average = get_weighted_average(a, b, c)
    print(f"{weighted_average:.1f}")