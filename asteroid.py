import pygame
import random
from logger import log_event
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        # If the radius of the asteroid is less than or equal to ASTEROID_MIN_RADIUS,
        # just return; this was a small asteroid and we're done.
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")

        random_angle = random.uniform(20, 50)

        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = a * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.veloctiy = b * 1.2


# Alt. method for implementing splitting asteroid
        # random_angle = random.uniform(20,50) # nosec
        # new_asteroid1 = Asteroid(self.position[0], self.position[1], self.radius / 2)
        # new_asteroid2 = Asteroid(self.position[0], self.position[1], self.radius / 2)
        # new_asteroid1.velocity = pygame.math.Vector2.rotate(self.velocity, random_angle)*1.2
        # new_asteroid2.velocity = pygame.math.Vector2.rotate(self.velocity, -random_angle)*1.2
