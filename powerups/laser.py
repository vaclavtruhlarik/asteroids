import pygame
from powerups.powerup import PowerUp
from powerups.powerupshape import PowerUpShape
from explosion import Explosion
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, POWERUP_LIFESPAN


# Laser power-up that continuously fires lasers instead of regular shots
class Laser(PowerUp):
    def __init__(self, player):
        super().__init__()
        self.lifespan = POWERUP_LIFESPAN
        self.type = "laser"
        self.player = player
        self.width = 5  # Width of the laser beam
        self.end_position = pygame.Vector2(0, 0)  # End position of the laser beam

    def draw(self, screen):
        # Draw the laser beam as a line from the player's position in direction of the player's rotation
        if self.lifespan < 2.0:
            if int(self.lifespan * 10) % 2 == 0:
                pygame.draw.line(
                    screen,
                    "green",
                    (int(self.player.position.x), int(self.player.position.y)),
                    (int(self.end_position.x), int(self.end_position.y)),
                    width=self.width,  # Width of the laser beam
                )
        else:
            pygame.draw.line(
                screen,
                "green",
                (int(self.player.position.x), int(self.player.position.y)),
                (int(self.end_position.x), int(self.end_position.y)),
                width=self.width,  # Width of the laser beam
            )

    def update(self, dt):
        self.lifespan -= dt
        if self.lifespan <= 0:
            self.kill()

        # Calculate the end position of the laser beam based on the player's rotation
        self.end_position = pygame.Vector2(0, 1).rotate(self.player.rotation)
        self.end_position *= max(
            SCREEN_WIDTH, SCREEN_HEIGHT
        )  # Extend the laser beam to the screen width or height
        self.end_position += (
            self.player.position
        )  # Translate the end position to the player's position

    def collides(self, other):
        # Check if the laser collides with any other object
        if self.line_circle_intersection(
            self.player.position, self.end_position, other
        ):
            Explosion(other.position.x, other.position.y)
            other.kill()
            return 1
        return 0

    def line_circle_intersection(self, a, b, circle):
        # Check if the line segment (a, b) intersects with the circle
        ab = b - a
        ac = circle.position - a
        ab_length_squared = ab.length_squared()
        if ab_length_squared == 0:
            # a and b are the same point
            return a.distance_to(circle.position) <= (circle.radius + self.width / 2)
        t = max(0, min(1, ac.dot(ab) / ab_length_squared))
        closest_point = a + ab * t
        return closest_point.distance_to(circle.position) <= (
            circle.radius + self.width / 2
        )


# Laser power-up that provides temporary laser firing capability to the player
class LaserShape(PowerUpShape):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = "laser"
        self.icon = "L"  # Icon for the laser power-up
        self.color = "green"  # Color for the laser power-up

    def apply(self, player):
        Laser(player)
