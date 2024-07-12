import pygame, random

#Initialize
pygame.init()

#Set Display
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Ghost Catcher")

#Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

#Define classes
class Game():
    """A class to control game play"""
    def __init__(self):
        """Initialize the game object"""
        pass

    def update(self):
        """Update game object"""
        pass

    def draw(self):
        """Draw HUD and other to display"""
        pass

    def check_collisions(self):
        """check for collisions"""
        pass

    def start_new_round(self):
        """Populate screen with new monsters"""
        pass

    def choose_target(self):
        """Choose target for player"""
        pass

    def pause(self):
        """Pause the game"""
        pass

    def restart_game(self):
        """Restart game is player chooses to continue"""
        pass
    

class Player(pygame.sprite.Sprite):
    """A player class that the user controls"""
    def __init__(self):
        """Initialize the player object"""
        pass

    def update(self):
        """Update the player"""
        pass

    def warp(self):
        """Allows player to warp to safe zone (bottom)"""
        pass

    def reset(self):
        "Resets player position to bottom of the screen"
        pass


class Monster(pygame.sprite.Sprite):
    """A class to create enemy monster objects"""
    def __init__(self):
        """initialize the monster"""
        pass

    def update(self):
        """Update the monster"""
        pass


#Create a player group and object
my_player_group = pygame.sprite.Group()
my_player = Player()
my_player_group.add(my_player)

#Create monster group, adding monsters will occur in game class'
#start new round method
my_monster_group = pygame.sprite.Group()

#Create game object
my_game = Game()

#Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Update display and tick clock
    pygame.display.update
    clock.tick(FPS)


#End game
pygame.quit()