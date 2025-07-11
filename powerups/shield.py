import pygame
from powerups.powerup import PowerUp


# Shield power-up that provides temporary invincibility to the player
class Shield(PowerUp):
    def __init__(self, player):
        super().__init__()
        self.lifespan = 2.0  # Duration of the shield effect
        self.type = "shield"
        self.player = player

    def update(self, dt):
        self.lifespan -= dt
        if self.lifespan <= 0:
            # Remove the shield effect from the player
            self.player.powerups.remove(self)
            self.kill()
