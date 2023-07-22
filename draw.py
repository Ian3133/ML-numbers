import pygame
import numpy as np
from PIL import Image
from resize import resize


pygame.init()
window_width = 560
window_height = 560
grid_size = 64
cell_size = window_width // grid_size
pen_draw_size = 5  


BLACK =    (0, 0, 0)
WHITE = (255, 255, 255)
grid = np.zeros((grid_size, grid_size), dtype=int)
#creates window
window = pygame.display.set_mode(( window_width, window_height))
pygame.display.set_caption("Draw a Number 0-9")
window.fill(BLACK)
drawing = False

running = True


while running:               # main loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            
        elif event.type == pygame.MOUSEMOTION and drawing:
            mouse_pos = pygame.mouse.get_pos()
            row = mouse_pos[1] // cell_size
            col = mouse_pos[0] // cell_size
            for i in range(-pen_draw_size + 1, 1):
                for j in range(-pen_draw_size + 1, 1):
                    if 0 <= row + i < grid_size and 0 <= col + j < grid_size:
                        grid[row + i][col + j] = 1
            for i in range(-pen_draw_size + 1, 1):
                for j in range(-pen_draw_size + 1, 1):
                    if 0 <= row + i < grid_size and 0 <= col + j < grid_size:
                        pygame.draw.rect(window, WHITE, ((col + j) * cell_size, (row + i) * cell_size,
                                                         cell_size, cell_size))
    pygame.display.flip()




image = Image.fromarray(grid.astype(np.uint8) * 255, mode='L')
image.save('drawn_grid.png')
original_image = Image.open('drawn_grid.png')


new_size = (24,24)                              # i do it twice because it just looked closer to the data set before i changed the input data
resized_image = original_image.resize(new_size) # thats why 64 - 24 - 28
new_size = (28,28)  
resized_image = resized_image.resize(new_size)

resized_image.save('drawn_grid.png')
pygame.quit()

