import pygame
from powerups.powerup import PowerUp
from explosion import Explosion
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


# Nuke power-up that destroys all asteroids in the field
class Nuke(PowerUp):
    def __init__(self, player):
        super().__init__()
        self.lifespan = 0.0  # Duration of the nuke effect
        self.type = "nuke"
        self.explosion = Explosion(player.position.x, player.position.y)
        self.explosion.radius = max(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.lifespan = self.explosion.lifespan

    def draw(self, screen):
        # Draw the nuke effect on the screen
        pass

    def update(self, dt):
        self.lifespan -= dt
        if self.lifespan <= 0:
            self.kill()

    def collides(self, other):
        # Check if the nuke effect collides with any asteroids
        if self.explosion.collides(other):
            # Destroy the asteroid and create an explosion effect
            other.kill()
            Explosion(other.position.x, other.position.y)
            return
