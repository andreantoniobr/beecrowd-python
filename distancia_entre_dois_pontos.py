def get_two_points_distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def get_point_data():
    point_data = input().split()
    x = float(point_data[0])
    y = float(point_data[1])
    return x, y

x1, y1 = get_point_data()
x2, y2 = get_point_data()
distance = get_two_points_distance(x1, y1, x2, y2)
print(f"{distance:.4f}")