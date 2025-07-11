import pygame
from powerups.powerupshape import PowerUpShape
from powerups.nuke import Nuke


# Nuke power-up that destroys all asteroids in the field
class NukeShape(PowerUpShape):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = "nuke"
        self.icon = "N"  # Icon for the nuke power-up
        self.color = "red"  # Color for the nuke power-up

    def apply(self, player):
        nuke = Nuke(player)

    def update(self, dt):
        return super().update(dt)
