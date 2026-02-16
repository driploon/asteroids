import pygame, sys
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event

def main():
    pygame.init()
    # Creating a group to hold game objects and add Player objects to them
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    # Creating updatable objects
    asteroid_field = AsteroidField()

    # Creating drawable objects
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    # Creating game variables
    fps = pygame.time.Clock()
    dt = 0
    
    while True:
        # Record game state snapshot to game_state.jsonl (for debugging).
        log_state()

        # Process quit and other events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Clear the screen with a black background.
        screen.fill("black")
        # Update player position and rotation from keyboard input.
        updatable.update(dt)
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        # Draw the player ship on the screen.
        for object in drawable:
            object.draw(screen)
        # Display the new frame.
        pygame.display.flip()
        # Limit to 60 FPS and get time since last frame (delta time).
        dt = fps.tick(60) / 1000


if __name__ == "__main__":
    main()
