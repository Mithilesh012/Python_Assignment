import tkinter as tk
import math

def draw_indian_flag(canvas):
    # Define the width and height of the flag
    flag_width = 600
    flag_height = 400

    # Define the height of each stripe
    stripe_height = flag_height // 3

    # Draw the saffron stripe
    canvas.create_rectangle(0, 0, flag_width, stripe_height, fill="#FF9933", outline="")

    # Draw the white stripe
    canvas.create_rectangle(0, stripe_height, flag_width, 2 * stripe_height, fill="white", outline="")

    # Draw the green stripe
    canvas.create_rectangle(0, 2 * stripe_height, flag_width, flag_height, fill="#138808", outline="")

    # Draw the Ashoka Chakra (a blue circle with 24 spokes)
    center_x = flag_width // 2
    center_y = flag_height // 2
    radius = stripe_height // 2

    # Draw the circle
    canvas.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius, outline="#000080", width=2)

    # Add the text "Happy Independence Day from Develearn"
    canvas.create_text(center_x, flag_height + 30, text="happy independence day from DeveLearn 2024", font=("Arial", 15, "bold"), fill="black")

    return center_x, center_y, radius

def animate_chakra(canvas, center_x, center_y, radius, angle=0):
    canvas.delete("spokes")  # Clear previous spokes

    # Draw the 24 spokes
    for i in range(24):
        spoke_angle = i * 15 + angle  # Adjust for rotation
        x_end = center_x + radius * 0.9 * math.cos(math.radians(spoke_angle))
        y_end = center_y + radius * 0.9 * math.sin(math.radians(spoke_angle))
        canvas.create_line(center_x, center_y, x_end, y_end, fill="#000080", width=2, tags="spokes")

    # Schedule the next frame
    canvas.after(100, animate_chakra, canvas, center_x, center_y, radius, angle + 5)

# Set up the main window
root = tk.Tk()
root.title("Indian Flag")

# Create a canvas
canvas = tk.Canvas(root, width=600, height=450)  # Increase height to accommodate text
canvas.pack()

# Draw the flag and get the Ashoka Chakra parameters
center_x, center_y, radius = draw_indian_flag(canvas)

# Start the animation
animate_chakra(canvas, center_x, center_y, radius)

# Start the Tkinter event loop
root.mainloop()