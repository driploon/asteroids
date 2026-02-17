import pygame
from circleshape import *
from shot import Shot
from constants import PLAYER_RADIUS, PLAYER_SHOOT_SPEED, PLAYER_TURN_SPEED, PLAYER_SPEED, SHOT_RADIUS

class Player(CircleShape):
    def __init__(self, x, y):
        # Initialize base CircleShape at (x, y) with player radius.
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def draw(self, screen):
        # Draw the ship as a white triangle (nose, left corner, right corner).
        return pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt):
        # Change rotation angle by turn speed * dt (positive = clockwise).
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def shoot(self):
        new_shot = Shot(self.position.x, self.position.y)
        direction = pygame.Vector2(0, 1).rotate(self.rotation) 
        new_shot.velocity = direction * PLAYER_SHOOT_SPEED

        return new_shot


    def update(self, dt):
        # Get currently held keys to drive rotation and movement.
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            # Rotate left.
            self.rotate(-dt)
        if keys[pygame.K_d]:
            # Rotate right.
            self.rotate(dt)
        if keys[pygame.K_w]:
            # Move forward in current facing direction.
            self.move(dt)
        if keys[pygame.K_s]:
            # Move backward.
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            # Shoot 
            self.shoot()


    def move(self, dt):
        # Point (0, 1) rotated by ship heading, then scaled by speed and dt.
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        # Apply movement to position.
        self.position += rotated_with_speed_vector

    def triangle(self):
        # Build three vertices: nose (forward) and two rear corners (left/right).
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right

        return [a, b, c]
    

