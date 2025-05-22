import math
import matplotlib.pyplot as plt

# Cohen-Sutherland Outcode for Line Clipping
def compute_outcode(x, y, xmin, ymin, xmax, ymax):
    code = 0
    if x < xmin: code |= 1  # Left
    if x > xmax: code |= 2  # Right
    if y < ymin: code |= 4  # Bottom
    if y > ymax: code |= 8  # Top
    return code

# Cohen-Sutherland Line Clipping Algorithm
def cohen_sutherland_clip(x1, y1, x2, y2, xmin, ymin, xmax, ymax):
    outcode1 = compute_outcode(x1, y1, xmin, ymin, xmax, ymax)
    outcode2 = compute_outcode(x2, y2, xmin, ymin, xmax, ymax)
    accept = False

    while True:
        if (outcode1 | outcode2) == 0:  # Both points are inside the rectangle
            accept = True
            break
        elif (outcode1 & outcode2) != 0:  # Both points are outside the rectangle
            break
        else:
            # Choose one of the points and clip it
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

            # Update the point with the new coordinates
            if outcode_out == outcode1:
                x1, y1 = x, y
                outcode1 = compute_outcode(x1, y1, xmin, ymin, xmax, ymax)
            else:
                x2, y2 = x, y
                outcode2 = compute_outcode(x2, y2, xmin, ymin, xmax, ymax)

    if accept:
        return x1, y1, x2, y2
    else:
        return None  # No intersection


# Function to get user input for the clipping window and line
def get_user_input():
    print("Enter the clipping window boundaries:")
    xmin = float(input("Enter xmin: "))
    ymin = float(input("Enter ymin: "))
    xmax = float(input("Enter xmax: "))
    ymax = float(input("Enter ymax: "))

    print("\nEnter the line endpoints to be clipped:")
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))

    return x1, y1, x2, y2, xmin, ymin, xmax, ymax


# Function to plot the line and the clipped line
def plot_lines(x1, y1, x2, y2, clipped_x1, clipped_y1, clipped_x2, clipped_y2, xmin, ymin, xmax, ymax):
    # Plot the original line
    plt.plot([x1, x2], [y1, y2], 'r-', label="Original Line")

    # Plot the clipped line
    if clipped_x1 is not None and clipped_y1 is not None and clipped_x2 is not None and clipped_y2 is not None:
        plt.plot([clipped_x1, clipped_x2], [clipped_y1, clipped_y2], 'g-', label="Clipped Line")

    # Plot the clipping window (rectangle)
    plt.plot([xmin, xmax], [ymin, ymin], 'b-')
    plt.plot([xmin, xmax], [ymax, ymax], 'b-')
    plt.plot([xmin, xmin], [ymin, ymax], 'b-')
    plt.plot([xmax, xmax], [ymin, ymax], 'b-')

    plt.xlim(min(xmin, x1, x2), max(xmax, x1, x2))
    plt.ylim(min(ymin, y1, y2), max(ymax, y1, y2))
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Line Clipping using Cohen-Sutherland Algorithm")
    plt.legend()
    plt.grid(True)
    plt.show()


# Main function
def main():
    # Get user input
    x1, y1, x2, y2, xmin, ymin, xmax, ymax = get_user_input()

    # Perform the clipping
    clipped_line = cohen_sutherland_clip(x1, y1, x2, y2, xmin, ymin, xmax, ymax)

    if clipped_line:
        clipped_x1, clipped_y1, clipped_x2, clipped_y2 = clipped_line
        print(f"Clipped line coordinates: ({clipped_x1}, {clipped_y1}) to ({clipped_x2}, {clipped_y2})")
    else:
        print("The line is completely outside the clipping window and does not intersect.")

    # Plot the original and clipped lines
    plot_lines(x1, y1, x2, y2, clipped_x1, clipped_y1, clipped_x2, clipped_y2, xmin, ymin, xmax, ymax)


if __name__ == "__main__":
    main()
