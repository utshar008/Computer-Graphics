import numpy as np
import matplotlib.pyplot as plt

# 4-connected boundary fill
def boundary_fill_4(x, y, fill_color, boundary_color, canvas):
    if (canvas[y, x] != boundary_color).all() and (canvas[y, x] != fill_color).all():
        canvas[y, x] = fill_color
        if x + 1 < canvas.shape[1]: boundary_fill_4(x + 1, y, fill_color, boundary_color, canvas)  # Right
        if x - 1 >= 0: boundary_fill_4(x - 1, y, fill_color, boundary_color, canvas)  # Left
        if y + 1 < canvas.shape[0]: boundary_fill_4(x, y + 1, fill_color, boundary_color, canvas)  # Down
        if y - 1 >= 0: boundary_fill_4(x, y - 1, fill_color, boundary_color, canvas)  # Up

# 8-connected boundary fill
def boundary_fill_8(x, y, fill_color, boundary_color, canvas):
    if (canvas[y, x] != boundary_color).all() and (canvas[y, x] != fill_color).all():
        canvas[y, x] = fill_color
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1),
                       (-1, -1), (1, -1), (-1, 1), (1, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < canvas.shape[1] and 0 <= ny < canvas.shape[0]:
                boundary_fill_8(nx, ny, fill_color, boundary_color, canvas)

# Create a blank white canvas
def create_canvas(width, height):
    return np.ones((height, width, 3), dtype=np.uint8) * 255

# Draw a rectangle boundary
def draw_rectangle(canvas, x1, y1, x2, y2, color):
    canvas[y1:y2+1, x1] = color
    canvas[y1:y2+1, x2] = color
    canvas[y1, x1:x2+1] = color
    canvas[y2, x1:x2+1] = color

# Plot the canvas
def plot_canvas(canvas, title="Boundary Fill Result"):
    plt.imshow(canvas)
    plt.title(title)
    plt.axis('on')
    plt.show()

# Main function with full user input
def main():
    print("\n--- Boundary Fill Algorithm ---")

    # Canvas size
    width, height = map(int, input("Enter canvas size (width height): ").split())

    # Boundary color
    boundary_color = list(map(int, input("Enter boundary color (R G B): ").split()))

    # Fill color
    fill_color = list(map(int, input("Enter fill color (R G B): ").split()))

    # Rectangle boundary coordinates
    print("Enter top-left and bottom-right coordinates of rectangle boundary:")
    x1, y1 = map(int, input("Top-left (x1 y1): ").split())
    x2, y2 = map(int, input("Bottom-right (x2 y2): ").split())

    # Starting point
    start_x, start_y = map(int, input("Enter seed point inside the shape (x y): ").split())

    # Fill type
    print("Choose fill type:")
    print("1. 4-connected")
    print("2. 8-connected")
    fill_type = input("Enter choice (1 or 2): ")

    # Create and draw canvas
    canvas = create_canvas(width, height)
    draw_rectangle(canvas, x1, y1, x2, y2, boundary_color)

    # Apply boundary fill
    if fill_type == '1':
        boundary_fill_4(start_x, start_y, fill_color, boundary_color, canvas)
        title = "4-Connected Boundary Fill"
    elif fill_type == '2':
        boundary_fill_8(start_x, start_y, fill_color, boundary_color, canvas)
        title = "8-Connected Boundary Fill"
    else:
        print("Invalid fill type.")
        return

    # Plot the result
    plot_canvas(canvas, title)

if __name__ == "__main__":
    main()
