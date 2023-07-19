import tkinter as tk
import pygame
from PIL import ImageTk, Image

def open_pygame_file():
    # Code to open your Pygame file
    # Replace 'your_pygame_file.py' with the actual filename
    exec(open('draw.py').read())
    refresh_image()  # Refresh the image on the GUI after Pygame window is closed

def refresh_image():
    # Reload and display the image on the GUI
    image_path = 'drawn_grid.png'  # Replace with the actual image filename

    image = ImageTk.PhotoImage(Image.open(image_path))
    image_label.configure(image=image)
    image_label.image = image

root = tk.Tk()
root.geometry("500x300")  # Set the window size to 400x300 pixels

def display_gui():
    # Code to display the GUI elements
    image_path = 'drawn_grid.png'  # Replace with the actual image filename
    variable_text = "Example Text mach 2"  # Replace with your variable value

    # Creating a label to display text
    text_label = tk.Label(root, text=variable_text)
    text_label.pack()

    # Loading and displaying the image
    image = ImageTk.PhotoImage(Image.open(image_path))
    global image_label
    image_label = tk.Label(root, image=image)
    image_label.pack()

    # Creating a button to open the Pygame file
    button = tk.Button(root, text="Open Pygame File", command=open_pygame_file)
    button.pack()

display_gui()
root.mainloop()
