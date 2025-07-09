import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE


# Asteroid class representing the asteroids in the game
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "white",
            (int(self.position.x), int(self.position.y)),
            self.radius,
            width=2,
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        # Split the asteroid into two smaller ones
        self.kill()

        # Small asteroid is just destroyed
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Create two smaller asteroids
        random_angle = random.uniform(-20, 50)
        new_velocity1 = self.velocity.rotate(random_angle)
        new_velocity2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = new_velocity1 * 1.2  # Increase speed slightly
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = new_velocity2 * 1.2  # Increase speed slightly
