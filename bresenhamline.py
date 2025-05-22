#Bresenham
import matplotlib.pyplot as plt



x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

dx = abs(x2 - x1)
dy = abs(y2 - y1)
slope = dy > dx

if slope:
    x1, y1 = y1, x1
    x2, y2 = y2, x2

if x1 > x2:
    x1, x2 = x2, x1
    y1, y2 = y2, y1

dx = x2 - x1
dy = abs(y2 - y1)
error = dx // 2
y = y1
ystep = 1 if y1 < y2 else -1
points = []

for x in range(x1, x2 + 1):
    points.append((y, x) if slope else (x, y))
    error -= dy
    if error < 0:
        y += ystep
        error += dx

plt.plot(*zip(*points), marker='o')
plt.grid()
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()