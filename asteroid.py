import pygame
from circleshape import CircleShape
from constants import ASTEROID_KINDS, ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS, ASTEROID_SPAWN_RATE_SECONDS, LINE_WIDTH

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
       return pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH) 

    def update(self, dt):
        self.position += self.velocity * dt

