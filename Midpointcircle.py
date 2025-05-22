import matplotlib.pyplot as plt

def plot_circle(xc, yc, x, y):
    points = []
    points.append((xc + x, yc + y))
    points.append((xc - x, yc + y))
    points.append((xc + x, yc - y))
    points.append((xc - x, yc - y))
    points.append((xc + y, yc + x))
    points.append((xc - y, yc + x))
    points.append((xc + y, yc - x))
    points.append((xc - y, yc - x))
    return points

xc = int(input("Enter center x: "))
yc = int(input("Enter center y: "))
r = int(input("Enter radius: "))

x = 0
y = r
d = 1 - r
points = []

points += plot_circle(xc, yc, x, y)

while x < y:
    if d < 0:
        d += 2 * x + 3
    else:
        d += 2 * (x - y) + 5
        y -= 1
    x += 1
    points += plot_circle(xc, yc, x, y)

plt.scatter(*zip(*points))
plt.grid()
plt.axis('equal')
plt.plot(xc,yc,'bo')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()