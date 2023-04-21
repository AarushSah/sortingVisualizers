import pygame
import random

# Initialize Pygame
pygame.init()

# Set the window size
WINDOW_SIZE = (800, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set the caption of the window
pygame.display.set_caption("Heapsort Visualization")

# Set the background color
BACKGROUND_COLOR = (255, 255, 255)

# Set the array size and generate random data
ARRAY_SIZE = 100
data = [random.randint(0, WINDOW_SIZE[1]) for i in range(ARRAY_SIZE)]

# Set the delay between each step (in milliseconds)
DELAY = 10

# Define the heapsort algorithm
def heapsort(data):
    n = len(data)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i)

    # Sort the heap
    for i in range(n - 1, 0, -1):
        data[0], data[i] = data[i], data[0]
        draw_array(data, 0, -1, -1, -1)
        pygame.time.delay(DELAY)
        heapify(data, i, 0)

# Define the heapify function
def heapify(data, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and data[left] > data[largest]:
        largest = left

    if right < n and data[right] > data[largest]:
        largest = right

    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        draw_array(data, i, largest, -1, -1)
        pygame.time.delay(DELAY)
        heapify(data, n, largest)

# Define the drawing function
def draw_array(data, i, j, k, pivot):
    screen.fill(BACKGROUND_COLOR)
    for index, value in enumerate(data):
        color = (0, 0, 255)
        if index == i or index == j or index == k:
            color = (255, 0, 0)
        pygame.draw.rect(screen, color, (index * 8, WINDOW_SIZE[1] - value, 8, value))
    pygame.display.update()

# Define the restart function
def restart():
    global data
    data = [random.randint(0, WINDOW_SIZE[1]) for i in range(ARRAY_SIZE)]
    draw_array(data, -1, -1, -1, -1)
    heapsort(data)

# Initial drawing of the array
draw_array(data, -1, -1, -1, -1)

# Start the heapsort algorithm
heapsort(data)

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
