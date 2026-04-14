import pygame
from player import Player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

def main():
    print("Starting Asteroids with pygame version: VERSION")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    # create two empty groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # add player class to updatable and drawable before player object instance is created
    Player.containers = (updatable, drawable)

    # create the player - it gets auto added to both groups
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        log_state()

        screen.fill("black")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000

        # update game loop to use new groups instead of player object directly
        updatable.update(dt)

        # loop over all "drawables" and .draw() them individually
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main()
