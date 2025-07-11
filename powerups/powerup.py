import pygame


# Base class for all power-ups efects
class PowerUp(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.lifespan = 0.0  # Duration of the power-up effect
        self.type = None  # Type of the power-up

    def draw(self, screen):
        # Specified in the subclasses
        pass

    def update(self, dt):
        # Update the lifespan of the power-up
        self.lifespan -= dt
        if self.lifespan <= 0:
            self.kill()

    def collides(self, other):
        # Check if this power-up collides with another object
        pass
