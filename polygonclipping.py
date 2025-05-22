import matplotlib.pyplot as plt

# Sutherland-Hodgman Polygon Clipping Algorithm
def sutherland_hodgman_clip(polygon, xmin, ymin, xmax, ymax):
    def clip_edge(polygon, x1, y1, x2, y2):
        clipped_polygon = []
        for i in range(len(polygon)):
            x0, y0 = polygon[i]
            x1_prev, y1_prev = polygon[i - 1] if i > 0 else polygon[-1]

            # Check if the point is inside or outside the clipping edge
            def is_inside(x, y):
                return (x1 <= x <= x2) and (y1 <= y <= y2)

            # Check the intersection of the polygon with the clipping edge
            def intersection(x1, y1, x2, y2):
                dx1, dy1 = x2 - x1, y2 - y1
                dx2, dy2 = x1_prev - x0, y1_prev - y0
                t = ((x0 - x1) * dy1 - (y0 - y1) * dx1) / (dx2 * dy1 - dx1 * dy2)
                x = x0 + t * dx2
                y = y0 + t * dy2
                return x, y

            # Determine if the edge is inside or outside
            if is_inside(x0, y0) and is_inside(x1_prev, y1_prev):
                clipped_polygon.append((x0, y0))
            elif is_inside(x0, y0):
                clipped_polygon.append(intersection(x0, y0, x1_prev, y1_prev))
            elif is_inside(x1_prev, y1_prev):
                clipped_polygon.append(intersection(x1_prev, y1_prev, x0, y0))
        return clipped_polygon

    # Clip against each of the four edges (left, right, bottom, top)
    polygon = clip_edge(polygon, xmin, ymin, xmin, ymax)  # Left edge
    polygon = clip_edge(polygon, xmax, ymin, xmax, ymax)  # Right edge
    polygon = clip_edge(polygon, xmin, ymin, xmax, ymin)  # Bottom edge
    polygon = clip_edge(polygon, xmin, ymax, xmax, ymax)  # Top edge
    return polygon

# Function to get user input for the clipping window and polygon vertices one by one
def get_user_input():
    # Getting clipping window coordinates one by one
    xmin = float(input("Enter clipping window xmin: "))
    ymin = float(input("Enter clipping window ymin: "))
    xmax = float(input("Enter clipping window xmax: "))
    ymax = float(input("Enter clipping window ymax: "))

    # Getting polygon vertices one by one
    num_vertices = int(input("Enter number of vertices of the polygon: "))
    polygon = []
    print("Enter the vertices (x y) of the polygon:")
    for i in range(num_vertices):
        x = float(input(f"Enter x for vertex {i+1}: "))
        y = float(input(f"Enter y for vertex {i+1}: "))
        polygon.append((x, y))

    return polygon, xmin, ymin, xmax, ymax

# Plotting the result
def plot_polygon(polygon, clipped_polygon, xmin, ymin, xmax, ymax):
    # Plot the original polygon
    x, y = zip(*polygon)
    plt.fill(x, y, 'r', alpha=0.5, label="Original Polygon")

    # Plot the clipped polygon
    if clipped_polygon:
        x, y = zip(*clipped_polygon)
        plt.fill(x, y, 'g', alpha=0.5, label="Clipped Polygon")

    # Plot the clipping window (rectangle)
    plt.plot([xmin, xmax], [ymin, ymin], 'b-', label="Clipping Window (Bottom)")
    plt.plot([xmin, xmax], [ymax, ymax], 'b-', label="Clipping Window (Top)")
    plt.plot([xmin, xmin], [ymin, ymax], 'b-', label="Clipping Window (Left)")
    plt.plot([xmax, xmax], [ymin, ymax], 'b-', label="Clipping Window (Right)")

    plt.xlim(min(xmin, *x), max(xmax, *x))
    plt.ylim(min(ymin, *y), max(ymax, *y))
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid(True)
    plt.show()

# Main execution
def main():
    polygon, xmin, ymin, xmax, ymax = get_user_input()
    clipped_polygon = sutherland_hodgman_clip(polygon, xmin, ymin, xmax, ymax)

    if clipped_polygon:
        print(f"Clipped polygon coordinates: {clipped_polygon}")
    else:
        print("The polygon is completely outside the clipping window.")

    plot_polygon(polygon, clipped_polygon, xmin, ymin, xmax, ymax)

if __name__ == "__main__":
    main()
