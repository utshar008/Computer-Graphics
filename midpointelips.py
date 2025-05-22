import matplotlib.pyplot as plt

def plot_ellipse(xc, yc, x, y):
    points = []
    points.append((xc + x, yc + y))
    points.append((xc - x, yc + y))
    points.append((xc + x, yc - y))
    points.append((xc - x, yc - y))
    return points

xc = int(input("Enter center x: "))
yc = int(input("Enter center y: "))
rx = int(input("Enter Horizontal Radius: "))
ry = int(input("Enter Vertical Radius: "))

x = 0
y = ry
points = []

# Region 1
d1 = (ry**2) - (rx**2 * ry) + (0.25 * rx**2)
dx = 2 * ry**2 * x
dy = 2 * rx**2 * y

while dx < dy:
    points += plot_ellipse(xc, yc, x, y)
    if d1 < 0:
        x += 1
        dx += 2 * ry**2
        d1 += dx + ry**2
    else:
        x += 1
        y -= 1
        dx += 2 * ry**2
        dy -= 2 * rx**2
        d1 += dx - dy + ry**2

# Region 2
d2 = (ry**2 * (x + 0.5)**2) + (rx**2 * (y - 1)**2) - (rx**2 * ry**2)

while y >= 0:
    points += plot_ellipse(xc, yc, x, y)
    if d2 > 0:
        y -= 1
        dy -= 2 * rx**2
        d2 += rx**2 - dy
    else:
        y -= 1
        x += 1
        dx += 2 * ry**2
        dy -= 2 * rx**2
        d2 += dx - dy + rx**2

plt.scatter(*zip(*points))
plt.grid(linestyle='--')
plt.axis('equal')
plt.plot(xc,yc,'bo')
plt.title('Midpoint Ellipse Drawing')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()