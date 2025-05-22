import matplotlib.pyplot as plt

def dda(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))
    xi = dx / steps
    yi = dy / steps

    x = x1
    y = y1

    x_points = []
    y_points = []

    for _ in range(int(steps) + 1):
        x_points.append(round(x))
        y_points.append(round(y))
        x += xi
        y += yi

    return x_points, y_points

# Get input from user
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

# Generate line points
x_vals, y_vals = dda(x1, y1, x2, y2)

# Plot using matplotlib
plt.figure(figsize=(6, 6))
plt.plot(x_vals, y_vals, marker='o', color='green')
plt.title("DDA Line Drawing")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
#plt.gca().invert_yaxis()
plt.show()
