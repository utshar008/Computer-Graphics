import matplotlib.pyplot as plt

def draw_circle(xc, yc, r):
    x = 0
    y = r
    p = 1 - r
    points = []

    def plot_points(x, y):
        points.extend([
            (xc + x, yc + y),
            (xc - x, yc + y),
            (xc + x, yc - y),
            (xc - x, yc - y),
            (xc + y, yc + x),
            (xc - y, yc + x),
            (xc + y, yc - x),
            (xc - y, yc - x),
        ])

    plot_points(x, y)

    while x < y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1
        plot_points(x, y)

    return points

xc, yc = 0, 0
radius = 50
circle_points = draw_circle(xc, yc, radius)
x_vals, y_vals = zip(*circle_points)

plt.figure(figsize=(6,6))
plt.plot(x_vals, y_vals, color='blue')

# 8 octant lines from center
plt.plot([xc, xc + radius], [yc, yc], 'r')    # 0°
plt.plot([xc, xc + radius//1.41], [yc, yc + radius//1.41], 'g')  # 45°
plt.plot([xc, xc], [yc, yc + radius], 'b')    # 90°
plt.plot([xc, xc - radius//1.41], [yc, yc + radius//1.41], 'orange')  # 135°
plt.plot([xc, xc - radius], [yc, yc], 'purple')  # 180°
plt.plot([xc, xc - radius//1.41], [yc, yc - radius//1.41], 'brown')  # 225°
plt.plot([xc, xc], [yc, yc - radius], 'magenta')  # 270°
plt.plot([xc, xc + radius//1.41], [yc, yc - radius//1.41], 'cyan')  # 315°

plt.title("Midpoint Circle with Octant Lines")
plt.gca().set_aspect('equal')
plt.grid(True)
plt.show()
