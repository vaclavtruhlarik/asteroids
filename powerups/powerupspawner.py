import pygame
import random
from powerups.powerupshape import PowerUpShape
from powerups.nuke import NukeShape
from powerups.shield import ShieldShape
from powerups.laser import LaserShape
from powerups.tripleshot import TripleShotShape
from powerups.boost import BoostShape
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, POWERUP_SPAWN_RATE, POWERUP_TYPES


class PowerUpSpawner(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = POWERUP_SPAWN_RATE

    def randomly_select_type(self):
        num = random.random()
        chance_sum = 0
        for type, chance in POWERUP_TYPES.items():
            chance_sum += chance
            if num < chance_sum:
                return type

    def spawn(self, position):
        type = self.randomly_select_type()
        if type == "nuke":
            powerup = NukeShape(position.x, position.y)
        elif type == "shield":
            powerup = ShieldShape(position.x, position.y)
        elif type == "laser":
            powerup = LaserShape(position.x, position.y)
        elif type == "triple_shot":
            powerup = TripleShotShape(position.x, position.y)
        elif type == "boost":
            powerup = BoostShape(position.x, position.y)

    def update(self, dt):
        self.spawn_timer -= dt
        if self.spawn_timer <= 0:
            self.spawn_timer = POWERUP_SPAWN_RATE

            # spawn a new power-up at a random position
            position = pygame.Vector2(
                random.randint(0 + 50, SCREEN_WIDTH - 50),
                random.randint(0 + 50, SCREEN_HEIGHT - 50),
            )
            self.spawn(position)
