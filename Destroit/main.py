import pygame
import math
import time

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption('Destroit Game')
clock = pygame.time.Clock()

menu_image = pygame.image.load('mainMenu.png')
background_image = pygame.image.load('background.jpg')
ground_image = pygame.image.load('ground.png')

menu_bip_sound = pygame.mixer.Sound("bip.mp3")
menu_bip_sound.set_volume(1.0)
pygame.mixer.music.load("mainMenu.mp3")
pygame.mixer.music.set_volume(0.3)
game_music = pygame.mixer.Sound("theGame.mp3")
game_music.set_volume(0.3)
shot_voice = pygame.mixer.Sound("shot.mp3")
shot_voice.set_volume(1.0)
shotOK_voice = pygame.mixer.Sound("shot ok.mp3")
shotOK_voice.set_volume(1.0)
youWin_voice = pygame.mixer.Sound("you win.mp3")

text = "Choose Language"
myFont = pygame.font.SysFont("arialblack", 40)
myText = myFont.render(text, True, (222, 222, 222))

left_archery_image = pygame.image.load('leftArchery.png')
right_archery_image = pygame.image.load('rightArchery.png')
wizard_image = pygame.image.load('wizard.png')
ninja_image = pygame.image.load('ninja.png')
arrows_image = pygame.image.load('arrows.png')
magic_image = pygame.image.load('magic.png')
star_image = pygame.image.load('star.png')
turkish_image = pygame.image.load("turkish.png")
turkish_position = turkish_image.get_rect(center=(300, 450))
english_image = pygame.image.load("english.png")
english_position = english_image.get_rect(center=(900, 450))
archer2_image = pygame.image.load("archer2.png")
archer2_position = archer2_image.get_rect(center=(250, 450))
wizard2_image = pygame.image.load("wizard2.png")
wizard2_position = wizard2_image.get_rect(center=(600, 450))
ninja2_image = pygame.image.load("ninja2.png")
ninja2_position = ninja2_image.get_rect(center=(950, 450))
archer3_image = pygame.image.load("archer3.png")
wizard3_image = pygame.image.load("wizard3.png")
ninja3_image = pygame.image.load("ninja3.png")
heart_image = pygame.image.load("heart.png")

left_player_position = (150, 580)
right_player_position = (1040, 520)

twidth = 400
theight = 125
cho = -1
choLang = -1
p1_image = None
p2_image = None
s1_image = None
s2_image = None
lp_image = None
rp_image = None
pl_image = None
pr_image = None
nump1 = 5
nump2 = 5


def update_hearts():
    global heart1, heart2
    heart1 = [heart_image] * nump1
    heart2 = [heart_image] * nump2


update_hearts()

show_menu = True
pygame.mixer.music.play(-1)
while show_menu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if cho == -1:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if turkish_position.collidepoint(mouse_pos):
                    menu_bip_sound.play()
                    choLang = 0
                    cho += 1
                elif english_position.collidepoint(mouse_pos):
                    menu_bip_sound.play()
                    choLang = 1
                    cho += 1
        elif cho == 0:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if archer2_position.collidepoint(mouse_pos):
                    menu_bip_sound.play()
                    p1_image = left_archery_image
                    s1_image = arrows_image
                    lp_image = archer3_image
                    pl_image = archer2_image
                    cho += 1
                elif wizard2_position.collidepoint(mouse_pos):
                    menu_bip_sound.play()
                    p1_image = wizard_image
                    s1_image = magic_image
                    lp_image = wizard3_image
                    pl_image = wizard2_image
                    cho += 1
                elif ninja2_position.collidepoint(mouse_pos):
                    menu_bip_sound.play()
                    p1_image = ninja_image
                    s1_image = star_image
                    lp_image = ninja3_image
                    pl_image = ninja2_image
                    cho += 1
        elif cho == 1:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if archer2_position.collidepoint(mouse_pos):
                    menu_bip_sound.play()
                    p2_image = right_archery_image
                    s2_image = arrows_image
                    rp_image = archer3_image
                    pr_image = archer2_image
                    show_menu = False
                elif wizard2_position.collidepoint(mouse_pos):
                    menu_bip_sound.play()
                    p2_image = wizard_image
                    s2_image = magic_image
                    rp_image = wizard3_image
                    pr_image = wizard2_image
                    show_menu = False
                elif ninja2_position.collidepoint(mouse_pos):
                    menu_bip_sound.play()
                    p2_image = ninja_image
                    s2_image = star_image
                    rp_image = ninja3_image
                    pr_image = ninja2_image
                    show_menu = False

    screen.blit(menu_image, (0, 0))
    if cho == -1:
        screen.blit(turkish_image, turkish_position)
        screen.blit(english_image, english_position)
    if cho == 0:
        if choLang == 0:
            twidth = 360
            text = "Birinci Oyuncu seçin"
            myText = myFont.render(text, True, (222, 222, 222))
        elif choLang == 1:
            twidth = 360
            text = "Choose First Player"
            myText = myFont.render(text, True, (222, 222, 222))
        screen.blit(archer2_image, archer2_position)
        screen.blit(wizard2_image, wizard2_position)
        screen.blit(ninja2_image, ninja2_position)
    if cho == 1:
        if choLang == 0:
            twidth = 360
            text = "İkinci Oyuncu seçin"
            myText = myFont.render(text, True, (222, 222, 222))
        elif choLang == 1:
            twidth = 360
            text = "Choose Second Player"
            myText = myFont.render(text, True, (222, 222, 222))
        screen.blit(archer2_image, archer2_position)
        screen.blit(wizard2_image, wizard2_position)
        screen.blit(ninja2_image, ninja2_position)
    screen.blit(myText, (twidth, theight))
    pygame.display.update()

pygame.mixer.music.stop()
game_music.play(-1)

shooting1 = False
shooting2 = False
shooting1_position = None
shooting2_position = None
current_turn = 1  # Player 1 starts first


def shot1(start_pos):
    global shooting1, shooting1_position, shooting1_velocity, current_turn
    if current_turn == 1 and not shooting1:
        shot_voice.play()
        shooting1_position = pygame.Rect(left_player_position[0], left_player_position[1], s1_image.get_width(),
                                         s1_image.get_height())
        shooting1 = True
        direction_x = start_pos[0] - left_player_position[0]
        direction_y = start_pos[1] - left_player_position[1]
        length = math.hypot(direction_x, direction_y)
        direction_x /= length
        direction_y /= length
        shooting1_speed = 22
        shooting1_velocity = (direction_x * shooting1_speed, direction_y * shooting1_speed)
        current_turn =  2


def shot2(start_pos):
    global shooting2, shooting2_position, shooting2_velocity, current_turn
    if current_turn == 2 and not shooting2:
        shot_voice.play()
        shooting2_position = pygame.Rect(right_player_position[0], right_player_position[1], s2_image.get_width(),
                                         s2_image.get_height())
        shooting2 = True
        direction_x = start_pos[0] - right_player_position[0]
        direction_y = start_pos[1] - right_player_position[1]
        length = math.hypot(direction_x, direction_y)
        direction_x /= length
        direction_y /= length
        shooting2_speed = 30
        shooting2_velocity = (direction_x * shooting2_speed, direction_y * shooting2_speed)
        current_turn = 1


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if current_turn == 1:
                shot1(event.pos)
            elif current_turn == 2:
                shot2(event.pos)

    if shooting1:
        shooting1_position.x += shooting1_velocity[0]
        shooting1_position.y += shooting1_velocity[1]
        acceleration = 0.5
        shooting1_velocity = (shooting1_velocity[0], shooting1_velocity[1] + acceleration)
        if (shooting1_position.bottom < 0 or shooting1_position.right < 0 or
                shooting1_position.left > screen.get_width() or shooting1_position.top > screen.get_height()):
            shooting1 = False
            shooting1_position = None

    if shooting2:
        shooting2_position.x += shooting2_velocity[0]
        shooting2_position.y += shooting2_velocity[1]
        acceleration = 0.85
        shooting2_velocity = (shooting2_velocity[0], shooting2_velocity[1] + acceleration)
        if (shooting2_position.bottom < 0 or shooting2_position.right < 0 or
                shooting2_position.left > screen.get_width() or shooting2_position.top > screen.get_height()):
            shooting2 = False
            shooting2_position = None

    if shooting1 and shooting1_position:
        if shooting1_position.colliderect(pygame.Rect(right_player_position, (64, 64))):
            if nump2 != 1:
                shotOK_voice.play()
            nump2 -= 1
            update_hearts()
            shooting1 = False
            if nump2 == 0:
                running = False

    if shooting2 and shooting2_position:
        if shooting2_position.colliderect(pygame.Rect(left_player_position, (64, 64))):
            if nump1 != 1:
                shotOK_voice.play()
            nump1 -= 1
            update_hearts()
            shooting2 = False
            if nump1 == 0:
                running = False

    screen.blit(background_image, (0, 0))
    screen.blit(p1_image, left_player_position)
    screen.blit(p2_image, right_player_position)
    screen.blit(ground_image, (0, 105))

    if shooting1:
        screen.blit(s1_image, shooting1_position.topleft)
    if shooting2:
        screen.blit(s2_image, shooting2_position.topleft)

    if choLang == 0:
        text = "Birinci Oyuncu"
    else:
        text = "First Player"
    myFont = pygame.font.SysFont("arialblack", 32)
    myText = myFont.render(text, True, (222, 0, 0))
    screen.blit(myText, (210, 50))

    for i, heart in enumerate(heart1):
        screen.blit(heart, (210 + i * 60, 110))

    pygame.draw.polygon(screen, (255, 255, 255), [(50, 50), (178, 50), (178, 178), (50, 178)])
    screen.blit(lp_image, (50, 50))
    pygame.draw.line(screen, (0, 220, 40), (50, 50), (50, 178), 10)
    pygame.draw.line(screen, (0, 220, 40), (50, 50), (178, 50), 10)
    pygame.draw.line(screen, (0, 220, 40), (178, 50), (178, 178), 10)
    pygame.draw.line(screen, (0, 220, 40), (50, 178), (178, 178), 10)
    pygame.draw.polygon(screen, (255, 255, 255), [(1150, 50), (1022, 50), (1022, 178), (1150, 178)])

    if choLang == 0:
        text = "İkinci Oyuncu"
    else:
        text = "Second Player"
    myFont = pygame.font.SysFont("arialblack", 32)
    myText = myFont.render(text, True, (222, 0, 0))
    screen.blit(myText, (750, 50))

    for i, heart in enumerate(heart2):
        screen.blit(heart, (940 - i * 60, 110))

    screen.blit(rp_image, (1022, 50))
    pygame.draw.line(screen, (0, 220, 40), (1150, 50), (1150, 178), 10)
    pygame.draw.line(screen, (0, 220, 40), (1150, 50), (1022, 50), 10)
    pygame.draw.line(screen, (0, 220, 40), (1022, 50), (1022, 178), 10)
    pygame.draw.line(screen, (0, 220, 40), (1150, 178), (1022, 178), 10)

    pygame.display.flip()
    clock.tick(60)
game_music.stop()

pygame.mixer.music.play(-1)
show_menu = True
while show_menu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()



    screen.blit(menu_image, (0, 0))
    if choLang == 0:
        text = "KAZANAN"
        myFont = pygame.font.SysFont("arialblack", 64)
        myText = myFont.render(text, True, (222, 222, 222))
        screen.blit(myText, (twidth + 60, theight - 15))
        if nump2 == 0:
            text = "Birinci Oyuncu"
            myFont = pygame.font.SysFont("arialblack", 40)
            myText = myFont.render(text, True, (222, 0, 0))
            screen.blit(myText, (twidth + 60, theight + 120))
            screen.blit(pl_image, (twidth + 80, theight + 200))
        else:
            text = "İkinci Oyuncu"
            myFont = pygame.font.SysFont("arialblack", 40)
            myText = myFont.render(text, True, (222, 0, 0))
            screen.blit(myText, (twidth + 60, theight + 120))
            screen.blit(pr_image, (twidth + 80, theight + 200))




    else:
        text = "WINNER"
        myFont = pygame.font.SysFont("arialblack", 64)
        myText = myFont.render(text, True, (222, 222, 222))
        screen.blit(myText, (twidth + 60, theight - 15))
        if nump2 == 0:
            text = "First Player"
            myFont = pygame.font.SysFont("arialblack", 40)
            myText = myFont.render(text, True, (222, 0, 0))
            screen.blit(myText, (twidth + 60, theight + 120))
            screen.blit(pl_image, (twidth + 80, theight + 200))
        else:
            text = "Second Player"
            myFont = pygame.font.SysFont("arialblack", 40)
            myText = myFont.render(text, True, (222, 0, 0))
            screen.blit(myText, (twidth + 60, theight + 120))
            screen.blit(pr_image, (twidth + 80, theight + 200))



    pygame.display.update()

pygame.quit()
