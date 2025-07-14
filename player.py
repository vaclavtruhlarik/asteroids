import pygame
from time import sleep
from circleshape import CircleShape
from shot import Shot
from constants import (
    PLAYER_RADIUS,
    PLAYER_TURN_SPEED,
    PLAYER_SPEED,
    PLAYER_SHOOT_SPEED,
    PLAYER_SHOOT_COOLDOWN,
    PLAYER_LIVES,
)


# Player class representing the spaceship
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0  # Initial rotation angle
        self.shoot_timer = 0.0  # Cooldown time in seconds
        self.lives = PLAYER_LIVES  # Number of lives the player has
        self.frames_after_hit = 0  # Frames after the player was hit
        self.speed = PLAYER_SPEED  # Speed of the player

    def draw(self, screen):
        if self.frames_after_hit > 0:
            # Flash the player for a few frames after being hit
            if self.frames_after_hit % 10 == 0:
                pygame.draw.polygon(
                    screen,
                    "white",
                    self.triangle(self.position, self.rotation),
                    width=2,
                )
            self.frames_after_hit -= 1
        else:
            # Draw the player normally
            pygame.draw.polygon(
                screen, "white", self.triangle(self.position, self.rotation), width=2
            )
        self.draw_lives(screen)  # Draw player lives as triangles

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE] and self.shoot_timer <= 0:
            self.shoot()
            self.shoot_timer = PLAYER_SHOOT_COOLDOWN

        # Update the shoot timer
        self.shoot_timer -= dt

    def draw_lives(self, screen):
        # Draw player lives as triangles at the top right corner of the screen
        for i in range(self.lives):
            triangle_pos = pygame.Vector2(
                screen.get_width() - 2 * self.radius * (i + 1), 2 * self.radius
            )
            triangle = self.triangle(triangle_pos, 0)
            pygame.draw.polygon(screen, "white", triangle, width=2)

    def triangle(self, position, rotation):
        forward = pygame.Vector2(0, 1).rotate(rotation)
        right = pygame.Vector2(0, 1).rotate(rotation + 90) * self.radius / 1.5
        a = position + forward * self.radius
        b = position - forward * self.radius - right
        c = position - forward * self.radius + right
        return [a, b, c]

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        self.rotation %= 360  # Keep the rotation within 0-360 degrees

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * self.speed * dt

    def shoot(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        velocity = forward * PLAYER_SHOOT_SPEED
        shot = Shot(self.position.x, self.position.y, velocity)

    def collides(self, other):
        # Check if the player triangle collides with another circle
        if not isinstance(other, CircleShape):
            return False

        # Triangle vertices
        triangle_vertices = self.triangle(self.position, self.rotation)
        for i in range(3):
            a = triangle_vertices[i]
            b = triangle_vertices[i - 1]
            # Check if the line segment (a, b) intersects with the circle
            if self.line_circle_intersection(a, b, other):
                return True

        return False  # No collision detected

    def line_circle_intersection(self, a, b, circle):
        # Check if the line segment (a, b) intersects with the circle
        ab = b - a
        ac = circle.position - a
        ab_length_squared = ab.length_squared()
        if ab_length_squared == 0:
            # a and b are the same point
            return a.distance_to(circle.position) <= circle.radius
        t = max(0, min(1, ac.dot(ab) / ab_length_squared))
        closest_point = a + ab * t
        return closest_point.distance_to(circle.position) <= circle.radius

    def is_invincible(self):
        # Check if the player is invincible (e.g., after being hit)
        return self.frames_after_hit > 0
