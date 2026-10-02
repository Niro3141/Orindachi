class Appearance:
    def __init__(self, left_eye=DEFAULT_LEFT_EYE, right_eye=DEFAULT_RIGHT_EYE, hair=DEFAULT_HAIR, body=DEFUALT_BODY, legs=DEFAULT_LEGS):
        self.left_eye = left_eye
        self.right_eye = right_eye
        self.hair = hair
        self.body = body
        self.legs = legs


class Personality:
    def __init__(self, artisticness, cheerfulness, talkativeness, skill):
        self.artisticness = artisticness
        self.cheerfulness = cheerfulness
        self.talkativeness = talkativeness
        self.skill = skill

class Character:
    def __init__(self, name, gender, personality, appearance):
        self.name = name
        self.gender = gender
        self.personality = personality
        self.appearance = appearance



def setup(pygame, width, height, full):
    pygame.init()

    if full:
        return pygame.display.set_mode((width, height), pygame.FULLSCREEN)
    else:
        return pygame.display.set_mode((width, height))

def main_game():
    pygame.display.flip()