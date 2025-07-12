import pygame
from powerups.powerup import PowerUp
from powerups.powerupshape import PowerUpShape


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

    def collides(self, other):
        return 0


# Shield power-up that provides temporary invincibility to the player
class ShieldShape(PowerUpShape):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = "shield"
        self.icon = "S"  # Icon for the shield power-up
        self.color = "blue"  # Color for the shield power-up

    def apply(self, player):
        shield = Shield(player)
        player.powerups.append(shield)

    def update(self, dt):
        return super().update(dt)
