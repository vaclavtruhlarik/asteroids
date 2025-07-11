import pygame
from powerups.powerupshape import PowerUpShape
from powerups.shield import Shield


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
