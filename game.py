import pygame
import sys
import os

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Genius Battle")

# Choose the font to set up the text

font_title = pygame.font.Font(None, 60)
font_menu = pygame.font.Font(None, 40)

def render_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))
    
    

# Load player image
assets_dir = os.path.join(os.path.dirname(__file__), 'assets')
player_image = pygame.image.load(os.path.join(assets_dir, 'player.png'))

# Scale up the player image
scale_factor = 10  # You can adjust this scale factor as needed
player_image = pygame.transform.scale(player_image, (player_image.get_width() * scale_factor, player_image.get_height() * scale_factor))

menu_image = pygame.image.load(os.path.join(assets_dir, 'menu.png'))
menu_scale_factor = 10
menu_image = pygame.transform.scale(menu_image, (menu_image.get_width() * menu_scale_factor, menu_image.get_height() * menu_scale_factor * 0.75)) #Short height
# Get the dimensions of the scaled player image to center it
player_width, player_height = player_image.get_size() 

# Positi
# on the player image at the bottom right
player_x = screen_width - player_width
player_y = screen_height - player_height - 150#150 higher than bottom

#Base Stats:
max_health = int(15)
health = int(15)
melee_dmg = int(5)
crit_chance = float(0.1)
crit_amp = float(1.5)
poison_dmg = int(2)
heal_amount = int(1)


# Attack Descriptions and dammage
headshot_dmg = str(melee_dmg+7)
kick_dmg = str(melee_dmg+3)
toxic_dmg = str(poison_dmg+7)
rest_heal = str(heal_amount + 2)


headshot_description = str("Has 20% accuracy and deals " + headshot_dmg + " damage when it hits.")
print(headshot_description)
kick_description = str("Has 95% accuracy and deals "+ kick_dmg +" damage when it hits.")
print(kick_description)
toxic_description = str("Has 70% accuracy and deals no dammage on contact, but does "+ toxic_dmg + " every turn for 3 turns.")
print(toxic_description)
rest_description = str("Has 70% accuracy and deals no dammage, but heals the user by "+ rest_heal + " health when used.")
print(rest_description)

selected_action = 4
# Main game loop
running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((255, 255, 255))  # WhiteBG
    # Menu box
    screen.blit(menu_image, (0, 430))

    #Write text
    render_text("Battle Test", font_title, (0, 0, 0), 300, 50)
    render_text("Headshot", font_menu, (255, 255, 255), 50, 475) #Action 1
    render_text("Kick", font_menu, (255, 255, 255), 50, 545)     #Action 2
    render_text("Toxic", font_menu, (255, 255, 255), 250, 475)   #Action 3
    render_text("Rest", font_menu, (255, 255, 255), 250, 545)    #Action 4

    
    pygame.display.flip()


# Quit Pygame
pygame.quit()
sys.exit()
