import matplotlib.pyplot as plt
import numpy as np

# Define the Boundary Fill Algorithm
def boundary_fill(x, y, fill_color, boundary_color, canvas):
    # If current pixel is not boundary or already filled with the fill color
    if (canvas[y, x] != boundary_color).all() and (canvas[y, x] != fill_color).all():
        # Fill the pixel with the given fill color
        canvas[y, x] = fill_color
        
        # Recursively fill neighboring pixels (4-directional)
        if x+1 < canvas.shape[1]:  # Right
            boundary_fill(x+1, y, fill_color, boundary_color, canvas)
        if x-1 >= 0:  # Left
            boundary_fill(x-1, y, fill_color, boundary_color, canvas)
        if y+1 < canvas.shape[0]:  # Down
            boundary_fill(x, y+1, fill_color, boundary_color, canvas)
        if y-1 >= 0:  # Up
            boundary_fill(x, y-1, fill_color, boundary_color, canvas)

# Function to create a blank canvas (white background)
def create_canvas(width, height):
    # 2D canvas initialized with white (255, 255, 255) RGB color
    canvas = np.ones((height, width, 3), dtype=int) * 255
    return canvas

# Function to plot the result
def plot_canvas(canvas):
    plt.imshow(canvas)
    plt.axis('off')
    plt.show()

# Function to get user input
def get_user_input():
    # Get canvas size
    width, height = map(int, input("Enter canvas size (width height): ").split())
    
    # Get boundary color
    boundary_color = list(map(int, input("Enter boundary color (R G B): ").split()))
    
    # Get fill color
    fill_color = list(map(int, input("Enter fill color (R G B): ").split()))
    
    # Get the starting point for filling
    start_x, start_y = map(int, input("Enter starting point (x y): ").split())
    
    return width, height, boundary_color, fill_color, start_x, start_y

# Main function
def main():
    # Get user input
    width, height, boundary_color, fill_color, start_x, start_y = get_user_input()
    
    # Create a blank white canvas
    canvas = create_canvas(width, height)
    
    # Draw a boundary (black box) on the canvas, for example:
    canvas[20:80, 20:80] = boundary_color  # Boundary as a rectangle
    
    # Apply the boundary fill algorithm
    boundary_fill(start_x, start_y, fill_color, boundary_color, canvas)
    
    # Plot the result
    plot_canvas(canvas)

if __name__ == "__main__":
    main()
