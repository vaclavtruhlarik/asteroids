import pygame
from powerups.powerup import PowerUp
from powerups.powerupshape import PowerUpShape
from explosion import Explosion
from constants import POWERUP_LIFESPAN


# Shield power-up that provides temporary invincibility to the player
class Shield(PowerUp):
    def __init__(self, player):
        super().__init__()
        self.lifespan = POWERUP_LIFESPAN
        self.type = "shield"
        self.player = player
        self.radius = 50  # Radius of the shield effect

    def draw(self, screen):
        # Draw the shield effect around the player
        # Blink the shield when only a few seconds left
        if self.lifespan < 2.0:
            if int(self.lifespan * 10) % 2 == 0:
                pygame.draw.circle(
                    screen,
                    "blue",
                    (int(self.player.position.x), int(self.player.position.y)),
                    self.radius,  # Radius of the shield effect
                    width=2,
                )
        else:
            pygame.draw.circle(
                screen,
                "blue",
                (int(self.player.position.x), int(self.player.position.y)),
                self.radius,  # Radius of the shield effect
                width=2,
            )

    def update(self, dt):
        self.lifespan -= dt
        if self.lifespan <= 0:
            self.kill()

    def collides(self, other):
        # Check if the shield collides with any other object
        if self.player.position.distance_to(other.position) < (
            self.radius + other.radius
        ):
            other.kill()
            Explosion(other.position.x, other.position.y)
            return 1
        return 0


# Shield power-up that provides temporary invincibility to the player
class ShieldShape(PowerUpShape):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = "shield"
        self.icon = "S"  # Icon for the shield power-up
        self.color = "blue"  # Color for the shield power-up

    def apply(self, player):
        Shield(player)
