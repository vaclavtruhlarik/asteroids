import pygame
from circleshape import CircleShape
from constants import EXPLOSION_RADIUS, EXPLOSION_DURATION


class Explosion(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, EXPLOSION_RADIUS)
        self.current_radius = 0
        self.lifespan = EXPLOSION_DURATION
        self.saturation = 1.0

    def update(self, dt):
        self.lifespan -= dt
        if self.lifespan <= 0:
            self.kill()
        else:
            self.current_radius = self.radius * (
                1 - (self.lifespan / EXPLOSION_DURATION)
            )
            self.saturation = max(0, self.saturation - dt / EXPLOSION_DURATION)

    def draw(self, screen):
        alpha = int(self.saturation * 255)
        pygame.draw.circle(
            screen,
            (255, 255, 255, alpha),
            (self.position.x, self.position.y),
            int(self.current_radius),
        )

    def collides(self, other):
        # Check if the explosion collides with another circle
        return self.position.distance_to(other.position) < (
            self.current_radius + other.radius
        )
