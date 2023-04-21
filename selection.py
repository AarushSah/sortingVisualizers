import pygame
import random

# Initialize Pygame
pygame.init()

# Set the window size
WINDOW_SIZE = (800, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set the caption of the window
pygame.display.set_caption("Selection Sort Visualization")

# Set the background color
BACKGROUND_COLOR = (255, 255, 255)

# Set the array size and generate random data
ARRAY_SIZE = 100
data = [random.randint(0, WINDOW_SIZE[1]) for i in range(ARRAY_SIZE)]

# Set the delay between each step (in milliseconds)
DELAY = 10

# Define the selection sort algorithm
def selection_sort(data):
    for i in range(len(data)):
        min_index = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min_index]:
                min_index = j
            draw_array(data, i, j, min_index)
            pygame.time.delay(DELAY)
        data[i], data[min_index] = data[min_index], data[i]
        draw_array(data, i, j, min_index)
        pygame.time.delay(DELAY)

# Define the drawing function
def draw_array(data, i, j, min_index):
    screen.fill(BACKGROUND_COLOR)
    for index, value in enumerate(data):
        color = (0, 0, 255)
        if index == i:
            color = (0, 255, 0)
        elif index == j:
            color = (255, 0, 0)
        elif index == min_index:
            color = (255, 255, 0)
        pygame.draw.rect(screen, color, (index * 8, WINDOW_SIZE[1] - value, 8, value))
    pygame.display.update()

# Define the restart function
def restart():
    global data
    data = [random.randint(0, WINDOW_SIZE[1]) for i in range(ARRAY_SIZE)]
    draw_array(data, -1, -1, -1)
    selection_sort(data)

# Initial drawing of the array
draw_array(data, -1, -1, -1)

# Start the selection sort algorithm
selection_sort(data)

# Set up the restart button
font = pygame.font.SysFont(None, 30)
text = font.render("Restart", True, (0, 0, 0))
text_rect = text.get_rect()
text_rect.center = (WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] - 30)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if text_rect.collidepoint(event.pos):
                restart()
    screen.blit(text, text_rect)
    pygame.display.update()

# Quit Pygame
pygame.quit()