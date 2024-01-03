import pygame 
from math import sqrt

ENEMY_COLOR = (0, 0, 255)
ENEMY_WIDTH = 20
ENEMY_HEIGHT = 20
ENEMY_SPEED = 1

class Enemy:
    def __init__(self, x_pos, y_pos, x_vel, y_vel):
        self.pos = [x_pos, y_pos]
        self.vel = [x_vel, y_vel]

    def update_velocity(self, b1, b2):
        # vector from enemy to first boy
        vec_1 = [b1.pos[0] - self.pos[0], b1.pos[1] - self.pos[1]]
        length_1 = sqrt((vec_1[0] ** 2) + (vec_1[1] ** 2))

        # vector from enemy to second boy
        vec_2 = [b2.pos[0] - self.pos[0], b2.pos[1] - self.pos[1]]
        length_2 = sqrt((vec_2[0] ** 2) + (vec_2[1] ** 2))

        # normalizes shorter vector to get direction to nearest boy
        if length_1 < length_2:
            direction = [vec_1[0] / length_1, vec_1[1] / length_1]
        else:
            direction = [vec_2[0] / length_2, vec_2[1] / length_2]

        # multiplies direction by speed to get velocity
        self.vel = [direction[0] * ENEMY_SPEED, direction[1] * ENEMY_SPEED]

    def update_position(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

    def draw(self, screen):
        pygame.draw.rect(screen, ENEMY_COLOR, (self.pos[0], self.pos[1], ENEMY_WIDTH, ENEMY_HEIGHT))
