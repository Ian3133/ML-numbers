import tkinter as tk
from PIL import ImageTk, Image
from prediction import predict

root = tk.Tk()
root.geometry("600x600")  # Set the window size to 800x600 pixels

def open_pygame_file():
    # Code to open your Pygame file
    # Replace 'your_pygame_file.py' with the actual filename
    exec(open('draw.py').read())
    refresh_image()  # Refresh the image on the GUI after Pygame window is closed

def refresh_image():
    # Reload and display the image on the GUI
    global original_image, photo_image, image_label

    image_path = 'drawn_grid.png'  # Replace with the actual image filename
    original_image = Image.open(image_path)

    # Resize the image
    resized_image = original_image.resize((300, 400), Image.LANCZOS)

    # Convert the resized image to PhotoImage
    photo_image = ImageTk.PhotoImage(resized_image)

    # Update the image on the label
    image_label.configure(image=photo_image)
    image_label.image = photo_image  # Prevent garbage collection
  
    additional_text = "prediction: " + str(predict()) + "           "
    
    
    additional_label = tk.Label(root, text=additional_text, font=("Helvetica", 16))
    additional_label.grid(row=2, column=2, padx=20, pady=10, sticky="e")  # Place the label to the right of the image


def display_gui():
    # Code to display the GUI elements
    image_path = 'drawn_grid.png'  
    title_text = "ML Number Project"  # Replace with your variable value
    description_text = """ details about the poject and where i got the date set. also porlbem with ---- but sloved using -----, try it out below   """

    # Creating a label to display title text with a larger font size
    title_label = tk.Label(root, text=title_text, font=("Helvetica", 24, "bold"))
    title_label.grid(row=0, column=0, columnspan=3, padx=20, pady=(20, 10))  # Center the title

    # Creating a label to display description text with text wrapping
    description_label = tk.Label(root, text=description_text, wraplength=600)
    description_label.grid(row=1, column=0, columnspan=3, padx=20)  # Center the description

    # Loading and displaying the image
    image = ImageTk.PhotoImage(Image.open(image_path))
    global image_label
    image_label = tk.Label(root, image=image)
    image_label.grid(row=2, column=0, columnspan=2, padx=20, pady=(0, 10))  # Place the image on the left

    original_image = Image.open(image_path)

    # Resize the image
    resized_image = original_image.resize((300, 400), Image.LANCZOS)

    # Convert the resized image to PhotoImage
    photo_image = ImageTk.PhotoImage(resized_image)

    # Update the image on the label
    image_label.configure(image=photo_image)
    image_label.image = photo_image  # Prevent garbage collection

    # Adding some text to the right of the image and above the button
    
    additional_text = "prediction: " + str(predict()) + "           "
    
    
    additional_label = tk.Label(root, text=additional_text, font=("Helvetica", 16))
    additional_label.grid(row=2, column=2, padx=20, pady=10, sticky="e")  # Place the label to the right of the image

    # Creating a button to open the Pygame file
    button = tk.Button(root, text="Draw Number 0-9", command=open_pygame_file)
    # Calculate the coordinates to center the button on the image
    button_x = 20 + (300 - button.winfo_reqwidth()) / 2
    button_y = 10 + (400 - button.winfo_reqheight()) / 2
    button.place(x=button_x, y=button_y)

display_gui()
root.mainloop()
