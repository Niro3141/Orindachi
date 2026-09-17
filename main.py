def setup(width, height, full):
    import pygame
    pygame.init()

    if full:
        return pygame.display.set_mode((width, height), pygame.FULLSCREEN)
    else:
        return pygame.display.set_mode((width, height))

def main_game():
    pygame.display.flip()