class Gender:
    def __init__(self, reference, ownership, ownership_reference, pluralised):
        self.reference = reference #They/she/he etc (String)
        self.ownership = ownership #Them/her/his etc (String)
        self.ownership_reference = ownership_reference #Theirs/Hers/His etc (String)
        self.pluralised = pluralised #Whether it's is or are (Bool)

class OneToTen:
    def __init__(self, n):
        self.n = min(max(n, 1), 10) #Number between 1 and 10 - restricted by max and min (Int)

class Personality:
    def __init__(self, talkativeness, playfulness, sportiness, intelligence, luck, artisticness, kindness, appreciativeness, food_loving):
        self.talkativeness = talkativeness #How often they want attention (OneToTen)
        self.playfulness = playfulness #How likely they are to want to play a game upon interacting, inversely effects reward money for a game (OneToTen)
        self.sportiness = sportiness #How likely they are to win at the foot race minigame, how much foot race pays, how much they appreciate sport-related gifts (OneToTen)
        self.intelligence = intelligence #How likely they are to win memory match minigame, how much memory match pays, how much they appreciate academic-related gifts (OneToTen)
        self.luck = luck #How likely they are to win the dice roll minigame, how much dice roll pays (OneToTen)
        self.artisticness = artisticness #How likely they are to like an art-related gift (OneToTen)
        self.kindness = kindness #How likely they are to give you a gift, not argue with friends, talk kindly (OneToTen)
        self.appreciativeness = appreciativeness #How much satisfaction they gain from being given a gift (OneToTen)
        self.food_loving = food_loving #How much satisfaction they gain from food, how quickly they lose hunger (OneToTen)

class Mood:
    def __init__(self, personality):
        self.personality = personality #Personality of character with this mood (Personality)



class Character:
    def __init__(self, name, gender, personality, mood, appearance, room, x, y, focused):
        self.name = name #Name of character (String)
        self.gender = gender #Gender of character (Gender)
        self.personality = personality #Personality of character (Personality)
        self.mood = mood #Mood of character (Mood)
        self.appearance
        self.room = room
        self.x = x
        self.y = y
        self.focused = focused

class BodyPart:
    def __init__(self, asset, owner, offset):
        self.asset = asset #Image (Pygame sprite with the image)
        self.owner = owner #What character owns this part (Character)
        self.offset = offset #How the image should be offset from the character



def setup(pygame, width, height, full):
    pygame.init()

    if full:
        return pygame.display.set_mode((width, height), pygame.FULLSCREEN)
    else:
        return pygame.display.set_mode((width, height))

def main_game():
    pygame.display.flip()