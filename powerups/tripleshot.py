import pygame
from powerups.powerup import PowerUp
from powerups.powerupshape import PowerUpShape
from explosion import Explosion
from shot import Shot
from constants import POWERUP_LIFESPAN, PLAYER_SHOOT_SPEED


# Triple shot power-up that allows the player to shoot three bullets at once
class TripleShot(PowerUp):
    def __init__(self, player):
        super().__init__()
        self.lifespan = POWERUP_LIFESPAN  # Duration of the triple shot effect
        self.type = "triple_shot"
        self.player = player

    def draw(self, screen):
        # Draw the triple shot effect (if needed)
        pass

    def update(self, dt):
        self.lifespan -= dt
        if self.lifespan <= 0:
            self.kill()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.player.shoot_timer <= 0:
            self.shoot()

    def shoot(self):
        forward = pygame.Vector2(0, 1).rotate(self.player.rotation)
        left = forward.rotate(15)  # Rotate left by 15 degrees
        right = forward.rotate(-15)  # Rotate right by 15 degrees
        # Create two shots: one left, and one right, the third shot is produced by the player itself
        left_shot = Shot(
            self.player.position.x, self.player.position.y, left * PLAYER_SHOOT_SPEED
        )
        right_shot = Shot(
            self.player.position.x, self.player.position.y, right * PLAYER_SHOOT_SPEED
        )

    def collides(self, other):
        # Check if the triple shot collides with any other object
        return 0  # No collision logic for triple shot itself


# Triple shot power-up that allows the player to shoot three bullets at once
class TripleShotShape(PowerUpShape):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = "triple_shot"
        self.icon = "T"  # Icon for the triple shot power-up
        self.color = "white"  # Color for the triple shot power-up

    def apply(self, player):
        TripleShot(player)
