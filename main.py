import pygame
import boy
import enemy
from sys import exit

WIDTH  = 1280
HEIGHT = 720
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

            self.screen.fill((230, 50, 230))

            b1.draw(self.screen)
            b2.draw(self.screen)
            boy.beam(self.screen, b1, b2)
            e1.draw(self.screen)
            b1.update()
            b2.update()

            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == "__main__":
    game = Game()
    b1 = boy.Boy(300, 300, 255, 255, 255, 1)
    b2 = boy.Boy(100, 100, 0, 0, 0, 2)
    e1 = enemy.Enemy(400, 400)
    game.run(b1, b2, e1)
