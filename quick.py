import pygame
import random

# Initialize Pygame
pygame.init()

# Set the window size
WINDOW_SIZE = (800, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set the caption of the window
pygame.display.set_caption("Quicksort Visualization")

# Set the background color
BACKGROUND_COLOR = (255, 255, 255)

# Set the array size and generate random data
ARRAY_SIZE = 100
data = [random.randint(0, WINDOW_SIZE[1]) for i in range(ARRAY_SIZE)]

# Set the delay between each step (in milliseconds)
DELAY = 10

# Define the quicksort algorithm
def quicksort(data, start, end):
    if start >= end:
        return
    pivot = data[end]
    i = start
    for j in range(start, end):
        if data[j] < pivot:
            data[i], data[j] = data[j], data[i]
            i += 1
            draw_array(data, i, j, end, pivot)
            pygame.time.delay(DELAY)
    data[i], data[end] = data[end], data[i]
    draw_array(data, i, end, end, pivot)
    pygame.time.delay(DELAY)
    quicksort(data, start, i - 1)
    quicksort(data, i + 1, end)

# Define the drawing function
def draw_array(data, i, j, k, pivot):
    screen.fill(BACKGROUND_COLOR)
    for index, value in enumerate(data):
        color = (0, 0, 255)
        if index == i:
            color = (0, 255, 0)
        elif index == j:
            color = (255, 0, 0)
        elif index == k:
            color = (255, 255, 0)
        elif value == pivot:
            color = (255, 0, 255)
        pygame.draw.rect(screen, color, (index * 8, WINDOW_SIZE[1] - value, 8, value))
    pygame.display.update()

# Define the restart function
def restart():
    global data
    data = [random.randint(0, WINDOW_SIZE[1]) for i in range(ARRAY_SIZE)]
    draw_array(data, -1, -1, -1, -1)
    quicksort(data, 0, ARRAY_SIZE - 1)

# Initial drawing of the array
draw_array(data, -1, -1, -1, -1)

# Start the quicksort algorithm
quicksort(data, 0, ARRAY_SIZE - 1)

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