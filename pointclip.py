import matplotlib.pyplot as plt

def is_inside(x, y, xmin, ymin, xmax, ymax):
    return xmin <= x <= xmax and ymin <= y <= ymax

def draw_clipping_window(xmin, ymin, xmax, ymax):
    # Draw clipping rectangle
    rectangle = plt.Rectangle((xmin, ymin), xmax - xmin, ymax - ymin,
                              edgecolor='blue', facecolor='none', linewidth=2, label='Clipping Window')
    plt.gca().add_patch(rectangle)

def main():
    # Clipping window boundaries
    xmin = float(input("Enter xmin (left boundary): "))
    ymin = float(input("Enter ymin (bottom boundary): "))
    xmax = float(input("Enter xmax (right boundary): "))
    ymax = float(input("Enter ymax (top boundary): "))

    # Input point
    x = float(input("Enter x-coordinate of point: "))
    y = float(input("Enter y-coordinate of point: "))

    plt.figure()
    draw_clipping_window(xmin, ymin, xmax, ymax)

    if is_inside(x, y, xmin, ymin, xmax, ymax):
        print("Point is inside the clipping window.")
        plt.plot(x, y, 'go', label='Accepted Point')  # Green = inside
    else:
        print("Point is outside the clipping window.")
        plt.plot(x, y, 'ro', label='Rejected Point')  # Red = outside

    plt.xlim(min(xmin, x) - 10, max(xmax, x) + 10)
    plt.ylim(min(ymin, y) - 10, max(ymax, y) + 10)
    plt.axhline(0, color='gray', lw=0.5)
    plt.axvline(0, color='gray', lw=0.5)
    plt.title("Point Clipping")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.legend()
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

if __name__ == "__main__":
    main()
