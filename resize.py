from PIL import Image

# Open the original image
original_image = Image.open('drawn_grid.png')

# Set the desired new size
new_size = (24,24)  # Specify the width and height in pixels

# Resize the image
resized_image = original_image.resize(new_size)

new_size = (28,28)  # Specify the width and height in pixels

# Resize the image
resized_image = resized_image.resize(new_size)

resized_image.save('test_image.png')