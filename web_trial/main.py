import pygame, asyncio
import numpy as np
from PIL import Image

# Initialize Pygame
pygame.init()

# Set window dimensions
window_width = 560
window_height = 560

# Set grid dimensions
grid_size = 64
cell_size = window_width // grid_size
pen_draw_size = 5  # Increase this value to increase the pen draw size

# Set colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create a blank grid
grid = np.zeros((grid_size, grid_size), dtype=int)

# Set up the window
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Draw on 28x28 Grid")
window.fill(BLACK)

# Flag to indicate if drawing is active
drawing = False

# Main game loop
async def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
            elif event.type == pygame.MOUSEBUTTONUP:
                drawing = False
            elif event.type == pygame.MOUSEMOTION and drawing:
                # Get the mouse position and calculate the cell coordinates
                mouse_pos = pygame.mouse.get_pos()
                row = mouse_pos[1] // cell_size
                col = mouse_pos[0] // cell_size

                # Set the corresponding cells in the grid to white
                for i in range(-pen_draw_size + 1, 1):
                    for j in range(-pen_draw_size + 1, 1):
                        if 0 <= row + i < grid_size and 0 <= col + j < grid_size:
                            grid[row + i][col + j] = 1

                # Draw white rectangles on the window at the cell positions
                for i in range(-pen_draw_size + 1, 1):
                    for j in range(-pen_draw_size + 1, 1):
                        if 0 <= row + i < grid_size and 0 <= col + j < grid_size:
                            pygame.draw.rect(window, WHITE, ((col + j) * cell_size, (row + i) * cell_size,
                                                            cell_size, cell_size))

        # Update the display
        pygame.display.flip()
    await asyncio.sleep(0)

asynico.run(main())


# Save the drawn grid as an image
image = Image.fromarray(grid.astype(np.uint8) * 255, mode='L')
image.save('drawn_grid.png')

# Print the drawn grid
print("Drawn Grid:")
print(grid)


# Quit Pygame
pygame.quit()

