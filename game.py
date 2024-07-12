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
        super().__init__()
        self.image = pygame.image.load('./images/knight.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = WINDOW_WIDTH//2
        self.rect.bottom = WINDOW_HEIGHT

        self.lives = 5
        self.velocity = 8
        self.warps = 2

        self.catch_sound = pygame.mixer.Sound('./sounds/catch.wav')
        self.die_sound = pygame.mixer.Sound('./sounds/die.wav')
        self.warp_sound = pygame.mixer.Sound('./sounds/warp.wav')

    def update(self):
        """Update the player"""
        keys = pygame.key.get_pressed()

        #Move player within game bounds
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT] and self.rect.right < WINDOW_WIDTH:
            self.rect.x += self.velocity
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.velocity
        if keys[pygame.K_LEFT] and self.rect.bottom < WINDOW_HEIGHT:
            self.rect.y += self.velocity

    def warp(self):
        """Allows player to warp to safe zone (bottom)"""
        if self.warps > 0:
            self.warps -= 1
            self.warp_sound.play()
            self.rect.bottom = WINDOW_HEIGHT

    def reset(self):
        "Resets player position to bottom of the screen"
        self.rect.centerx = WINDOW_WIDTH//2
        self.rect.bottom = WINDOW_HEIGHT


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

    #Fill display
    display.fill(0,0,0)

    #Update and draw sprite groups
    my_player_group.update()
    my_player_group.draw(display)

    my_monster_group.update()
    my_monster_group.draw(display)

    #Update and draw the game
    my_game.update()
    my_game.draw()

    #Update display and tick clock
    pygame.display.update
    clock.tick(FPS)


#End game
pygame.quit()