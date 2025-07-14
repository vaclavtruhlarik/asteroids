import pygame
from powerups.powerup import PowerUp
from powerups.powerupshape import PowerUpShape
from constants import POWERUP_LIFESPAN


# Boost power-up that temporarily increases the player's speed
class Boost(PowerUp):
    def __init__(self, player):
        super().__init__()
        self.lifespan = POWERUP_LIFESPAN  # Duration of the boost effect
        self.type = "boost"
        self.player = player
        self.boost_amount = 2  # Factor by which the player's speed is increased
        self.player.speed *= self.boost_amount  # Increase player's speed

    def draw(self, screen):
        backward = -pygame.Vector2(0, 1).rotate(self.player.rotation)
        start = (
            self.player.position + backward * self.player.radius
        )  # Start point of the boost effect line
        end = backward * 20  # Length of the boost effect line
        end += start

        # Draw the boost effect as a line from the player's position in the direction of the backward vector
        if self.lifespan < 2.0:
            if int(self.lifespan * 10) % 2 == 0:
                pygame.draw.line(
                    screen,
                    "yellow",
                    (int(start.x), int(start.y)),
                    (int(end.x), int(end.y)),
                    width=5,  # Width of the boost effect line
                )
        else:
            pygame.draw.line(
                screen,
                "yellow",
                (int(start.x), int(start.y)),
                (int(end.x), int(end.y)),
                width=5,  # Width of the boost effect line
            )

    def update(self, dt):
        self.lifespan -= dt
        if self.lifespan <= 0:
            self.player.speed /= self.boost_amount  # Reset player's speed
            self.kill()  # Remove the power-up when its lifespan ends

    def collides(self, other):
        return 0


# Boost power-up shape
class BoostShape(PowerUpShape):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = "boost"
        self.icon = "B"  # Icon for the boost power-up
        self.color = "yellow"  # Color for the boost power-up

    def apply(self, player):
        Boost(player)  # Apply the boost effect to the player
