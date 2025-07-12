import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from explosion import Explosion
from powerups.powerupshape import PowerUpShape
from powerups.powerupspawner import PowerUpSpawner
from powerups.powerup import PowerUp


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    score = 0

    # groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    powerup_shapes = pygame.sprite.Group()
    powerups = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, drawable, shots)
    Explosion.containers = (updatable, drawable)
    PowerUpShape.containers = (updatable, drawable, powerup_shapes)
    PowerUpSpawner.containers = updatable
    PowerUp.containers = (updatable, drawable, powerups)

    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    asteroid_field = AsteroidField()
    powerup_spawner = PowerUpSpawner()

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
                    score += 1  # Increase score for destroying an asteroid
                    break  # No need to check other shots for this asteroid
            if asteroid_killed:
                continue

            # If player is invincible, skip collision check
            if player.is_invincible():
                continue
            if player.collides(asteroid):
                player.lives -= 1
                player.frames_after_hit = FRAMES_AFTER_HIT
                asteroid.kill()  # Destroy the asteroid
                Explosion(asteroid.position.x, asteroid.position.y)
                if player.lives <= 0:
                    print("Game over!")
                    pygame.quit()
                    return  # Exit the game if player is out of lives

        # Check if player collides with powerup
        for powerup in powerup_shapes:
            if player.collides(powerup):
                powerup.apply(player)
                powerup.kill()  # Remove the powerup after applying it

        for powerup in powerups:
            for asteroid in asteroids:
                score += powerup.collides(asteroid)

        # Draw everything
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
        # Draw the score
        font = pygame.font.Font(None, 36)
        text = font.render(f"Score: {score}", True, "white")
        screen.blit(text, (10, 10))
        pygame.display.flip()

        dt = clock.tick(60) / 1000  # seconds passed since last frame


if __name__ == "__main__":
    main()
