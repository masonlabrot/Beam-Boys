import pygame 
from sys import exit

pygame.init()

# sets up drawing window
size = width, height = 500, 500
screen = pygame.display.set_mode(size)

# sets title
pygame.display.set_caption("Beam Boys")

clock = pygame.time.Clock()

b1_pos = [0, 0]
b2_pos = [250, 250]

while True:
    # checks if user clicks close button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # sets background color 
    screen.fill((255, 0, 255))

    keys = pygame.key.get_pressed()
    # updates ball 1 position
    if keys[pygame.K_w]:
        b1_pos[1] -= 2
    if keys[pygame.K_s]:
        b1_pos[1] += 2
    if keys[pygame.K_d]:
        b1_pos[0] += 2
    if keys[pygame.K_a]:
        b1_pos[0] -= 2
    # updates ball 2 position
    if keys[pygame.K_UP]:
        b2_pos[1] -= 2
    if keys[pygame.K_DOWN]:
        b2_pos[1] += 2
    if keys[pygame.K_RIGHT]:
        b2_pos[0] += 2
    if keys[pygame.K_LEFT]:
        b2_pos[0] -= 2

    # draws balls
    pygame.draw.circle(screen, (255, 255, 0), (b1_pos[0], b1_pos[1]), 20)
    pygame.draw.circle(screen, (0, 0, 0), (b2_pos[0], b2_pos[1]), 20)
    
    pygame.display.update()
    # sets frame rate upper limit
    clock.tick(60)
