import pygame

SPEED = 5

class Boy:
    def __init__(self, x, y, r, g, b, label):

        self.x = x
        self.y = y
        self.r = r
        self.g = g
        self.b = b
        self.label = label

    def update(self):
        keys = pygame.key.get_pressed()

        if self.label == 1:
            if keys[pygame.K_w]:
                self.y -= SPEED
            if keys[pygame.K_s]:
                self.y += SPEED
            if keys[pygame.K_d]:
                self.x += SPEED
            if keys[pygame.K_a]:
                self.x -= SPEED
        if self.label == 2:
            if keys[pygame.K_UP]:
                self.y -= SPEED
            if keys[pygame.K_DOWN]:
                self.y += SPEED
            if keys[pygame.K_RIGHT]:
                self.x += SPEED
            if keys[pygame.K_LEFT]:
                self.x -= SPEED


    def draw(self, screen):

        pygame.draw.circle(screen, (self.r, self.g, self.b), (self.x, self.y), 20)

def beam(screen, b1, b2):
    pygame.draw.line(screen, (255, 255, 0), (b1.x, b1.y), (b2.x, b2.y), 5)
