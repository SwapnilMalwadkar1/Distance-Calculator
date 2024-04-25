import math

def calculate_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

# Example usage:
x1 = float(input("Enter x-coordinate of point 1: "))
y1 = float(input("Enter y-coordinate of point 1: "))
x2 = float(input("Enter x-coordinate of point 2: "))
y2 = float(input("Enter y-coordinate of point 2: "))

distance = calculate_distance(x1, y1, x2, y2)
print("Distance between the points: {:.2f}".format(distance))
