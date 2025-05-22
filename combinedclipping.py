import matplotlib.pyplot as plt

# Define the clip rectangle (you can modify this to be user-defined later)
xmin, ymin, xmax, ymax = 1, 1, 5, 5  # Default Clipping window

# Cohen-Sutherland Outcode for Line Clipping
def compute_outcode(x, y):
    code = 0
    if x < xmin: code |= 1  # Left
    if x > xmax: code |= 2  # Right
    if y < ymin: code |= 4  # Bottom
    if y > ymax: code |= 8  # Top
    return code

# Cohen-Sutherland Line Clipping Algorithm
def cohen_sutherland_clip(x1, y1, x2, y2):
    outcode1 = compute_outcode(x1, y1)
    outcode2 = compute_outcode(x2, y2)
    accept = False

    while True:
        if (outcode1 | outcode2) == 0:
            accept = True
            break
        elif (outcode1 & outcode2) != 0:
            break
        else:
            x, y = 0, 0
            outcode_out = outcode1 if outcode1 > outcode2 else outcode2
            if outcode_out & 8:  # Top
                x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
                y = ymax
            elif outcode_out & 4:  # Bottom
                x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
                y = ymin
            elif outcode_out & 2:  # Right
                y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
                x = xmax
            elif outcode_out & 1:  # Left
                y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
                x = xmin

            if outcode_out == outcode1:
                x1, y1 = x, y
                outcode1 = compute_outcode(x1, y1)
            else:
                x2, y2 = x, y
                outcode2 = compute_outcode(x2, y2)

    if accept:
        return x1, y1, x2, y2
    else:
        return None  # No intersection

# Sutherland-Hodgman Polygon Clipping Algorithm
def clip_polygon(polygon):
    clipped_polygon = polygon
    for edge in [(xmin, ymin, xmax, ymin), (xmax, ymin, xmax, ymax), (xmax, ymax, xmin, ymax), (xmin, ymax, xmin, ymin)]:
        new_polygon = []
        for i in range(len(clipped_polygon)):
            p1 = clipped_polygon[i]
            p2 = clipped_polygon[(i + 1) % len(clipped_polygon)]
            clipped = clip_edge(p1, p2, edge)
            new_polygon.extend(clipped)
        clipped_polygon = new_polygon
    return clipped_polygon

def clip_edge(p1, p2, edge):
    x1, y1 = p1
    x2, y2 = p2
    x_min, y_min, x_max, y_max = edge
    clipped_points = []

    def inside(x, y):
        return x_min <= x <= x_max and y_min <= y <= y_max

    def intersect(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        if x2 - x1 == 0:
            return x1, y_min
        slope = (y2 - y1) / (x2 - x1)
        x = x1 + (y_min - y1) / slope
        return x, y_min

    if inside(x1, y1):
        clipped_points.append((x1, y1))
    if inside(x2, y2):
        clipped_points.append((x2, y2))
    if not inside(x1, y1) and inside(x2, y2):
        clipped_points.append(intersect(p1, p2))
    return clipped_points

# Function to get user input for line clipping
def get_line_input():
    x1 = float(input("Enter x1 coordinate for the line: "))
    y1 = float(input("Enter y1 coordinate for the line: "))
    x2 = float(input("Enter x2 coordinate for the line: "))
    y2 = float(input("Enter y2 coordinate for the line: "))
    return x1, y1, x2, y2

# Function to get user input for polygon clipping
def get_polygon_input():
    n = int(input("Enter the number of vertices of the polygon: "))
    polygon = []
    for i in range(n):
        x = float(input(f"Enter x{i+1} coordinate: "))
        y = float(input(f"Enter y{i+1} coordinate: "))
        polygon.append((x, y))
    return polygon

# Draw function for Line Clipping
def draw_line_clipping(x1, y1, x2, y2):
    clipped_line = cohen_sutherland_clip(x1, y1, x2, y2)
    if clipped_line:
        x1, y1, x2, y2 = clipped_line
        plt.plot([x1, x2], [y1, y2], 'g-', label="Clipped Line")
        plt.xlim(0, 6)
        plt.ylim(0, 6)
        plt.axhline(ymin, color='r')
        plt.axhline(ymax, color='r')
        plt.axvline(xmin, color='r')
        plt.axvline(xmax, color='r')
        plt.legend()
        plt.title("Line Clipping - Cohen-Sutherland Algorithm")
        plt.show()
    else:
        print("The line is outside the clipping window.")

# Draw function for Polygon Clipping
def draw_polygon_clipping(polygon):
    clipped_polygon = clip_polygon(polygon)
    clipped_polygon.append(clipped_polygon[0])  # Close the polygon
    clipped_x, clipped_y = zip(*clipped_polygon)

    plt.plot(clipped_x, clipped_y, 'g-', label="Clipped Polygon")
    plt.fill(clipped_x, clipped_y, 'g', alpha=0.5)
    plt.xlim(0, 6)
    plt.ylim(0, 6)
    plt.axhline(ymin, color='r')
    plt.axhline(ymax, color='r')
    plt.axvline(xmin, color='r')
    plt.axvline(xmax, color='r')
    plt.legend()
    plt.title("Polygon Clipping - Sutherland-Hodgman Algorithm")
    plt.show()

# Main menu to choose between Line or Polygon clipping
def main():
    global xmin, ymin, xmax, ymax
    print("\nClipping Window:")
    xmin = float(input("Enter xmin: "))
    ymin = float(input("Enter ymin: "))
    xmax = float(input("Enter xmax: "))
    ymax = float(input("Enter ymax: "))
    
    while True:
        print("\n--- Main Menu ---")
        print("1. Line Clipping (Cohen-Sutherland)")
        print("2. Polygon Clipping (Sutherland-Hodgman)")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            print("\nLine Clipping:")
            x1, y1, x2, y2 = get_line_input()
            draw_line_clipping(x1, y1, x2, y2)

        elif choice == '2':
            print("\nPolygon Clipping:")
            polygon = get_polygon_input()
            draw_polygon_clipping(polygon)

        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid input, please choose again.")

if __name__ == "__main__":
    main()
