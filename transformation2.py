import math
import matplotlib.pyplot as plt

def translate_shape(points, tx, ty):
    return [(x + tx, y + ty) for x, y in points]

def rotate_shape(points, angle_deg):
    angle_rad = math.radians(angle_deg)
    return [
        (x * math.cos(angle_rad) - y * math.sin(angle_rad),
         x * math.sin(angle_rad) + y * math.cos(angle_rad))
        for x, y in points
    ]

def scale_shape(points, sx, sy):
    return [(x * sx, y * sy) for x, y in points]

def reflect_shape(points, axis):
    if axis == 'x':
        return [(x, -y) for x, y in points]
    elif axis == 'y':
        return [(-x, y) for x, y in points]
    elif axis == 'origin':
        return [(-x, -y) for x, y in points]
    else:
        raise ValueError("Invalid axis. Use 'x', 'y', or 'origin'.")

def shear_shape(points, shx, shy):
    return [(x + shx * y, y + shy * x) for x, y in points]

def draw_shape(points_old, points_new, title):
    plt.figure()
    x_old, y_old = zip(*points_old)
    x_new, y_new = zip(*points_new)

    if points_old[0] != points_old[-1]:
        x_old += (x_old[0],)
        y_old += (y_old[0],)
    if points_new[0] != points_new[-1]:
        x_new += (x_new[0],)
        y_new += (y_new[0],)

    plt.plot(x_old, y_old, 'ro-', label='Original Shape')
    plt.plot(x_new, y_new, 'go-', label='Transformed Shape')
    plt.title(title)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.legend()
    plt.axis('equal')
    plt.show()

def get_shape():
    print("\nChoose a shape:")
    print("1. Point")
    print("2. Line")
    print("3. Triangle")
    print("4. Rectangle (Four points)")

    shape_choice = input("Enter your choice (1-4): ")
    points = []

    if shape_choice == '1':
        x = float(input("Enter x coordinate: "))
        y = float(input("Enter y coordinate: "))
        points = [(x, y)]

    elif shape_choice == '2':
        print("Enter coordinates for two points:")
        for i in range(2):
            x = float(input(f"Enter x{i+1}: "))
            y = float(input(f"Enter y{i+1}: "))
            points.append((x, y))

    elif shape_choice == '3':
        print("Enter coordinates for three points:")
        for i in range(3):
            x = float(input(f"Enter x{i+1}: "))
            y = float(input(f"Enter y{i+1}: "))
            points.append((x, y))

    elif shape_choice == '4':
        print("Enter four points for the rectangle:")
        for i in range(4):
            x = float(input(f"Enter x{i+1}: "))
            y = float(input(f"Enter y{i+1}: "))
            points.append((x, y))

    else:
        print("Invalid choice.")
    
    return points

def main():
    print("\n--- Shape Selection ---")
    points = get_shape()
    if not points:
        print("No shape selected. Exiting.")
        return

    current_points = points

    while True:
        print("\n--- Transformation Menu ---")
        print("1. Translation")
        print("2. Rotation")
        print("3. Scaling")
        print("4. Reflection")
        print("5. Shearing")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            tx = float(input("Enter translation in x (tx): "))
            ty = float(input("Enter translation in y (ty): "))
            new_points = translate_shape(current_points, tx, ty)
            draw_shape(current_points, new_points, "Translation")
            current_points = new_points

        elif choice == '2':
            angle = float(input("Enter rotation angle (in degrees): "))
            direction = input("Enter direction (clockwise/anticlockwise): ").lower()
            if direction == "clockwise":
                angle = -angle
            new_points = rotate_shape(current_points, angle)
            draw_shape(current_points, new_points, "Rotation")
            current_points = new_points

        elif choice == '3':
            sx = float(input("Enter scaling factor in x (sx): "))
            sy = float(input("Enter scaling factor in y (sy): "))
            new_points = scale_shape(current_points, sx, sy)
            draw_shape(current_points, new_points, "Scaling")
            current_points = new_points

        elif choice == '4':
            axis = input("Reflect across which axis? (x/y/origin): ").lower()
            if axis in ['x', 'y', 'origin']:
                new_points = reflect_shape(current_points, axis)
                draw_shape(current_points, new_points, f"Reflection across {axis}-axis")
                current_points = new_points
            else:
                print("Invalid axis. Please choose 'x', 'y', or 'origin'.")

        elif choice == '5':
            shx = float(input("Enter shearing factor in x (shx): "))
            shy = float(input("Enter shearing factor in y (shy): "))
            new_points = shear_shape(current_points, shx, shy)
            draw_shape(current_points, new_points, f"Shearing (shx={shx}, shy={shy})")
            current_points = new_points

        elif choice == '6':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
