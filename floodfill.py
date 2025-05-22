import matplotlib.pyplot as plt
import numpy as np

# Define the Flood Fill Algorithm
def flood_fill(x, y, target_color, fill_color, canvas):
    # Check if the current pixel is not the target color and not the boundary color
    if (x >= 0 and x < canvas.shape[1] and y >= 0 and y < canvas.shape[0] and 
        (canvas[y, x] == target_color).all() and not (canvas[y, x] == fill_color).all()):
        
        # Fill the pixel with the given fill color
        canvas[y, x] = fill_color
        
        # Recursively fill neighboring pixels (4-directional)
        flood_fill(x + 1, y, target_color, fill_color, canvas)  # Right
        flood_fill(x - 1, y, target_color, fill_color, canvas)  # Left
        flood_fill(x, y + 1, target_color, fill_color, canvas)  # Down
        flood_fill(x, y - 1, target_color, fill_color, canvas)  # Up

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
    
    # Get the target color (the color inside the boundary to be filled)
    target_color = canvas[start_y, start_x]
    
    # Apply the flood fill algorithm
    flood_fill(start_x, start_y, target_color, fill_color, canvas)
    
    # Plot the result
    plot_canvas(canvas)

if __name__ == "__main__":
    main()
