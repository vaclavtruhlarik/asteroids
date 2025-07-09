import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS


# Shot class representing the bullets fired by the player
class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "white",
            (int(self.position.x), int(self.position.y)),
            self.radius,
            width=2,  # 0 = Filled circle
        )

    def update(self, dt):
        self.position += self.velocity * dt
