import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Update everything
        updatable.update(dt)

        # Check for collisions
        for asteroid in asteroids:
            # Check if asteroid collides with any shot
            asteroid_killed = False
            for shot in shots:
                if asteroid.collides(shot):
                    asteroid.split()
                    shot.kill()
                    asteroid_killed = True
                    break  # No need to check other shots for this asteroid
            if asteroid_killed:
                continue

            # Check if asteroid collides with player
            if asteroid.collides(player):
                print("Game over!")
                pygame.quit()
                return

        # Draw everything
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000  # seconds passed since last frame


if __name__ == "__main__":
    main()
