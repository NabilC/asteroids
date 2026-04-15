import sys
import pygame
from circleshape import CircleShape
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
from constants import *
from logger import *
from shot import Shot

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
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # add player class to updatable and drawable before player object instance is created
    Player.containers = (updatable, drawable)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    # create the player - it gets auto added to both groups
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Shot.containers = (shots, drawable, updatable)

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

        # loop over asteroids group and check if any collide with player
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.kill()


        pygame.display.flip()

if __name__ == "__main__":
    main()
