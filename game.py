import pygame, random

#Initialize pygame
pygame.init()

#Set display window
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Monster Wrangler")

#Set FPS and Clock
FPS = 60
clock = pygame.time.Clock()

#Define classes
class Game():
    """A class to control game play"""
    def __init__(self, player, monster_group):
        """Initialize the game object"""
        #Set game values
        self.score = 0
        self.round_number = 0

        self.round_time = 0
        self.frame_count = 0

        self.player = player
        self.monster_group = monster_group

        #Set sounds and music
        self.level_sound = pygame.mixer.Sound('./sounds/level.wav')
        self.level_sound = pygame.mixer.Sound('./sounds/level.wav')

        #Set fonts
        self.font = pygame.font.Font('./fonts/Abrushow.ttf')

        #set images
        blue_image = pygame.image.load('./images/blue.png')
        green_image = pygame.image.load('./images/green.png')
        yellow_image = pygame.image.load('./images/yellow.png')
        purple_image = pygame.image.load('./images/purple.png')
        #This list corresponds to the monster type attribute
        self.target_monster_images = [blue_image, green_image, purple_image, yellow_image]

        self.target_monster_type = random.randint(0,1)
        self.target_monster_image = self.target_monster_images[self.target_monster_type]

        self.target_monster_rect = self.target_monster_image.get_rect()
        self.target_monster_rect.x = WINDOW_WIDTH//2
        self.target_monster_rect.top = 30


    def update(self):
        """Update game object"""
        self.round_time += 1

        #Check for collision
        self.check_collisions()

    def draw(self):
        """Draw HUD and other to display"""
        #Set colors
        WHITE = (255, 255, 255)
        BLUE = (20, 176, 235)
        GREEN = (87, 201, 47)
        PURPLE = (226, 73, 243)
        YELLOW = (243, 157, 20)

        #Add colors to a list where index matches target monster colors order
        colors = [BLUE, GREEN, PURPLE, YELLOW]

        #Set text
        catch_text = self.font.render("Current Catch", True, WHITE)
        catch_rect = catch_text.get_rect()
        catch_rect.centerx = (WINDOW_WIDTH//2
        catch_rect.top = 5)
    
        score_text = self.font.render("Score" + str(self.score), True, WHITE)
        score_rect = score_text.get_rect()
        score_rect.topleft = (5, 5)
    
        lives_text = self.font.render("Lives" + str(self.player.lives), True, WHITE)
        lives_rect = lives_text.get_rect()
        lives_rect.topleft = (5, 35)
    
        round_text = self.font.render("Current Round" + str(self.round_number), True, WHITE)
        round_rect = round_text.get_rect()
        round_rect.topleft = (5, 65)

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
    """A player class that the user can control"""
    def __init__(self):
        """Initialize the player"""
        super().__init__()
        self.image = pygame.image.load("./images/knight.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = WINDOW_WIDTH//2
        self.rect.bottom = WINDOW_HEIGHT

        self.lives = 5
        self.warps = 2
        self.velocity = 8

        self.catch_sound = pygame.mixer.Sound("./sounds/catch.wav")
        self.die_sound = pygame.mixer.Sound("./sounds/die.wav")
        self.warp_sound = pygame.mixer.Sound("./sounds/warp.wav")


    def update(self):
        """Update the player"""
        keys = pygame.key.get_pressed()

        #Move the player within the bounds of the screen
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT] and self.rect.right < WINDOW_WIDTH:
            self.rect.x += self.velocity
        if keys[pygame.K_UP] and self.rect.top > 100:
            self.rect.y -= self.velocity
        if keys[pygame.K_DOWN] and self.rect.bottom < WINDOW_HEIGHT - 100:
            self.rect.y += self.velocity


    def warp(self):
        """Warp the player to the bottom 'safe zone'"""
        if self.warps > 0:
            self.warps -= 1
            self.warp_sound.play()
            self.rect.bottom = WINDOW_HEIGHT


    def reset(self):
        """Resets the players position"""
        self.rect.centerx = WINDOW_WIDTH//2
        self.rect.bottom = WINDOW_HEIGHT


class Monster(pygame.sprite.Sprite):
    """A class to create enemy monster objects"""
    def __init__(self, x, y, image, monster_type):
        """Initialize the monster"""
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        #Monster type is an int 0 -> blue, 1 -> green, 2 -> purple, 3 -> yellow
        self.type = monster_type

        #Set random motion
        self.dx = random.choice([-1, 1])
        self.dy = random.choice([-1, 1])
        self.velocity = random.randint(1, 5)


    def update(self):
        """Update the monster"""
        self.rect.x += self.dx*self.velocity
        self.rect.y += self.dy*self.velocity

        #Bounce the monster off the edges of the display
        if self.rect.left <= 0 or self.rect.right >= WINDOW_WIDTH:
            self.dx = -1*self.dx
        if self.rect.top <= 100 or self.rect.bottom >= WINDOW_HEIGHT - 100:
            self.dy = -1*self.dy


#Create a player group and Player object
my_player_group = pygame.sprite.Group()
my_player = Player()
my_player_group.add(my_player)

#Create a monster group.
my_monster_group = pygame.sprite.Group()

#Create a game object
my_game = Game(my_player, my_monster_group)

#The main game loop
running = True
while running:
    #Check to see if user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #Player wants to warp
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                my_player.warp()

    #Fill the display
    display_surface.fill((0, 0, 0))

    #Update and draw sprite groups
    my_player_group.update()
    my_player_group.draw(display_surface)

    my_monster_group.update()
    my_monster_group.draw(display_surface)

    #Update and draw the Game
    my_game.update()
    my_game.draw()

    #Update display and tick clock
    pygame.display.update()
    clock.tick(FPS)

#End the game
pygame.quit()

