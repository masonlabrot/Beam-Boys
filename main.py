import pygame
import boy
import enemy
from sys import exit

WIDTH  = 1280
HEIGHT = 720
SCREEN_COLOR = (230, 50, 230)
FPS    = 60

class Game:
    def __init__(self):

        # general setup
        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        pygame.display.set_caption("Beam_Boys")

    def run(self, b1, b2, e1):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            
            # colors screen
            self.screen.fill(SCREEN_COLOR)

            # draws characters
            b1.draw(self.screen)
            b2.draw(self.screen)
            e1.draw(self.screen)
            
            # draws beam
            boy.beam(self.screen, b1, b2)

            # updates boys
            b1.update()
            b2.update()

            # updates enemy
            e1.update_velocity(b1, b2)
            e1.update_position()

            # displays drawn objects
            pygame.display.update()

            # waits 1/FPS seconds
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    b1 = boy.Boy(300, 300, 255, 255, 255, 1)
    b2 = boy.Boy(100, 100, 0, 0, 0, 2)
    e1 = enemy.Enemy(400, 400, 0, 0)
    game.run(b1, b2, e1)
