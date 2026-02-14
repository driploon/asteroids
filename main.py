import pygame
from player import Player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

def main():
    pygame.init()
    # Creating a group to hold game objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

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
        # Draw the player ship on the screen.
        for object in drawable:
            object.draw(screen)
        # Display the new frame.
        pygame.display.flip()
        # Limit to 60 FPS and get time since last frame (delta time).
        dt = fps.tick(60) / 1000


if __name__ == "__main__":
    main()
