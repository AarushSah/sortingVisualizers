import pygame
import random

# Initialize Pygame
pygame.init()

# Set the window size
WINDOW_SIZE = (800, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set the caption of the window
pygame.display.set_caption("Mergesort Visualization")

# Set the background color
BACKGROUND_COLOR = (255, 255, 255)

# Set the array size and generate random data
ARRAY_SIZE = 100
data = [random.randint(0, WINDOW_SIZE[1]) for i in range(ARRAY_SIZE)]

# Set the delay between each step (in milliseconds)
DELAY = 10

# Define the merge sort algorithm
def mergesort(data, left, right):
    if left < right:
        middle = (left + right) // 2
        mergesort(data, left, middle)
        mergesort(data, middle + 1, right)
        merge(data, left, middle, right)

def merge(data, left, middle, right):
    left_data = data[left:middle + 1]
    right_data = data[middle + 1:right + 1]
    i = j = 0
    k = left
    while i < len(left_data) and j < len(right_data):
        if left_data[i] < right_data[j]:
            data[k] = left_data[i]
            i += 1
        else:
            data[k] = right_data[j]
            j += 1
        k += 1
        draw_array(data, i + left, j + middle + 1, k - 1, None)
        pygame.time.delay(DELAY)
    while i < len(left_data):
        data[k] = left_data[i]
        i += 1
        k += 1
        draw_array(data, i + left, j + middle + 1, k - 1, None)
        pygame.time.delay(DELAY)
    while j < len(right_data):
        data[k] = right_data[j]
        j += 1
        k += 1
        draw_array(data, i + left, j + middle + 1, k - 1, None)
        pygame.time.delay(DELAY)

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
        pygame.draw.rect(screen, color, (index * 8, WINDOW_SIZE[1] - value, 8, value))
    pygame.display.update()

# Define the restart function
def restart():
    global data
    data = [random.randint(0, WINDOW_SIZE[1]) for i in range(ARRAY_SIZE)]
    draw_array(data, -1, -1, -1, -1)
    mergesort(data, 0, ARRAY_SIZE - 1)

# Initial drawing of the array
draw_array(data, -1, -1, -1, -1)

# Start the merge sort algorithm
mergesort(data, 0, ARRAY_SIZE - 1)

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