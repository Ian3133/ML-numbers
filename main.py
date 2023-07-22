import tkinter as tk
import pygame
from PIL import ImageTk, Image
from prediction import predict
import tensorflow as tf
from resize import resize


root = tk.Tk()
root.geometry("600x600")  

def open_pygame_file():
    exec(open('draw.py').read())
    refresh_image() 

def refresh_image():
    global original_image, photo_image, image_label
    
    image_path = 'drawn_grid.png' 
    original_image = Image.open(image_path)
    resized_image = original_image.resize((300, 400), Image.LANCZOS)
    photo_image = ImageTk.PhotoImage(resized_image)
    image_label.configure(image=photo_image)
    image_label.image = photo_image  
  
    additional_text = "prediction: " + str(predict()) + "           "
    additional_label = tk.Label(root, text=additional_text, font=("Helvetica", 16))
    additional_label.grid(row=2, column=2, padx=20, pady=10, sticky="e") 


def display_gui():
    image_path = 'drawn_grid.png'  
    title_text = "ML Number Project"  
    description_text = """This is my introductory project into Machine Learning. The dataset i used is in Python's dataset library under 'mnist.' All the data was centered and scaled, and that led to my, less then perfect, inputs being unreliable. This was fixed by by rotating, shrinking and moving the numbers up or down (x & y-axis), I also added noise to every input image. This made the program perform much better.
    Give it a try tap the button below."""


    title_label = tk.Label(root, text=title_text, font=("Helvetica", 24, "bold"))
    title_label.grid(row=0, column=0, columnspan=3, padx=20, pady=(20, 10))  
    description_label = tk.Label(root, text=description_text, wraplength=550)
    description_label.grid(row=1, column=0, columnspan=3, padx=20)
    
    image = ImageTk.PhotoImage(Image.open(image_path))
    global image_label
    image_label = tk.Label(root, image=image)
    image_label.grid(row=2, column=0, columnspan=2, padx=20, pady=(0, 10))  
    original_image = Image.open(image_path)
    resized_image = original_image.resize((300, 400), Image.LANCZOS)

    photo_image = ImageTk.PhotoImage(resized_image)
    image_label.configure(image=photo_image)
    image_label.image = photo_image 
    
    additional_text = "prediction: " + str(predict()) + "           "
    additional_label = tk.Label(root, text=additional_text, font=("Helvetica", 16))
    additional_label.grid(row=2, column=2, padx=20, pady=10, sticky="e")  
    
    button = tk.Button(root, text="Draw Number 0-9", command=open_pygame_file)
    button_x = 20 + (300 - button.winfo_reqwidth()) / 2
    button_y = 10 + (400 - button.winfo_reqheight()) / 2
    button.place(x=button_x, y=button_y)

display_gui()
root.mainloop()
