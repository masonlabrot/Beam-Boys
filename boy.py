import pygame

SPEED = 5
BOY_SIZE = 20
BEAM_COLOR = (255, 255, 0)
BEAM_WIDTH = 5

class Boy:
    def __init__(self, x_pos, y_pos, red, green, blue, label):

        self.pos = [x_pos, y_pos]
        self.color = (red, green, blue)
        # label = 1 for boy 1; label = 2 for boy 2
        self.label = label

    def update(self):
        keys = pygame.key.get_pressed()

        # updates position based on key pressed
        if self.label == 1:
            if keys[pygame.K_w]:
                self.pos[1] -= SPEED
            if keys[pygame.K_s]:
                self.pos[1] += SPEED
            if keys[pygame.K_d]:
                self.pos[0] += SPEED
            if keys[pygame.K_a]:
                self.pos[0] -= SPEED
        if self.label == 2:
            if keys[pygame.K_UP]:
                self.pos[1] -= SPEED
            if keys[pygame.K_DOWN]:
                self.pos[1] += SPEED
            if keys[pygame.K_RIGHT]:
                self.pos[0] += SPEED
            if keys[pygame.K_LEFT]:
                self.pos[0] -= SPEED


    def draw(self, screen):

        pygame.draw.circle(screen, self.color, (self.pos[0], self.pos[1]), BOY_SIZE)

def beam(screen, b1, b2):
    pygame.draw.line(screen, BEAM_COLOR, (b1.pos[0], b1.pos[1]), (b2.pos[0], b2.pos[1]), BEAM_WIDTH)
