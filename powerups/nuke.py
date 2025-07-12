import pygame
from powerups.powerup import PowerUp
from powerups.powerupshape import PowerUpShape
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
        # Draw the nuke in the self.explosion class
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
            return 1
        return 0


# Nuke power-up that destroys all asteroids in the field
class NukeShape(PowerUpShape):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = "nuke"
        self.icon = "N"  # Icon for the nuke power-up
        self.color = "red"  # Color for the nuke power-up

    def apply(self, player):
        Nuke(player)
