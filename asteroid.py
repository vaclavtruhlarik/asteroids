import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE


# Asteroid class representing the asteroids in the game
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.starting_angle = random.uniform(0, 360)  # Random starting angle
        self.points = (
            self.generate_polygon_points()
        )  # Generate points for the polygon shape

    def draw(self, screen):
        # Draw the asteroid as a randomly shaped polygon
        points = []
        for point in self.points:
            # Rotate each point based on the starting angle
            rotated_point = point.rotate(self.starting_angle)
            # Translate the point to the asteroid's position
            translated_point = rotated_point + self.position
            points.append(translated_point)
        pygame.draw.polygon(screen, "white", points, width=2)

        # Draw the asteroid as a circle
        # pygame.draw.circle(
        #     screen,
        #     "white",
        #     (int(self.position.x), int(self.position.y)),
        #     self.radius,
        #     width=2,
        # )

    def update(self, dt):
        self.position += self.velocity * dt
        self.starting_angle = (self.starting_angle + 1) % 360  # Rotate the asteroid

    def generate_polygon_points(self):
        # Generate points for the polygon shape of the asteroid
        num_points = random.randint(5, 10)
        angle_step = 360 / num_points
        points = []
        for i in range(num_points):
            angle = i * angle_step
            point = pygame.Vector2(0, 1).rotate(angle)
            distance = random.uniform(self.radius * 0.8, self.radius * 1.2)
            point = point * distance
            points.append(point)
        return points

    def split(self):
        # Split the asteroid into two smaller ones
        self.kill()

        # Small asteroid is just destroyed
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Create two smaller asteroids
        random_angle = random.uniform(-20, 50)
        new_velocity1 = self.velocity.rotate(random_angle)
        new_velocity2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = new_velocity1 * 1.2  # Increase speed slightly
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = new_velocity2 * 1.2  # Increase speed slightly
