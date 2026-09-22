class Appearance:
    def __init__(self, ):


class Personality:
    def __init__(self, artisticness, cheerfulness, talkativeness, skill):
        self.artisticness = artisticness
        self.cheerfulness = cheerfulness
        self.talkativeness = talkativeness
        self.skill = skill

class Character:
    def __init__(self, name, personality, gender, appearance):
        self.name = name
        self.personality = personality
        self.gender = gender
        self.appearance = appearance



def setup(pygame, width, height, full):
    pygame.init()

    if full:
        return pygame.display.set_mode((width, height), pygame.FULLSCREEN)
    else:
        return pygame.display.set_mode((width, height))

def main_game():
    pygame.display.flip()