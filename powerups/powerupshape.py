import pygame
from circleshape import CircleShape
from constants import POWERUP_RADIUS, POWERUP_DURATION


# Base class for power-ups
class PowerUpShape(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, POWERUP_RADIUS)
        self.lifespan = POWERUP_DURATION
        self.type = None
        self.color = "white"
        self.icon = "TODO"

    def draw(self, screen):
        # Draw the power-up as a white circle with the text icon inside with self.color and black outline
        pygame.draw.circle(
            screen,
            "white",
            (int(self.position.x), int(self.position.y)),
            self.radius,
            width=2,
        )
        # Draw the icon text
        font = pygame.font.Font(None, 36)
        text = font.render(self.icon, True, self.color, "black")
        text_rect = text.get_rect(center=(int(self.position.x), int(self.position.y)))
        screen.blit(text, text_rect)

    def update(self, dt):
        self.lifespan -= dt
        if self.lifespan <= 0:
            self.kill()

    def apply(self, player):
        # Apply the power-up effect to the player
        # This method should be overridden by subclasses
        pass
