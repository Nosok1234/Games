import pygame

pygame.init()

W = 1000
H = 1000
move = 0

jump = False

sc = pygame.display.set_mode((W, H))
sc_rect = sc.get_rect()
pygame.display.set_caption("0_0")

hero = pygame.image.load('hero_right.png')
hero = pygame.transform.scale(hero, (hero.get_rect().width * 4, hero.get_rect().height * 4))
hero_rect = hero.get_rect()
hero_rect.x = 450
hero_rect.y = 768

wall = pygame.image.load('wall.png')

wall1 = pygame.transform.scale(wall, (wall.get_rect().width * 2, wall.get_rect().height // 4))
wall1_rect = wall1.get_rect()
wall1_rect.x = 800
wall1_rect.y = 750

wall2 = pygame.transform.scale(wall, (wall.get_rect().width * 3, wall.get_rect().height // 4))
wall2_rect = wall2.get_rect()
wall2_rect.x = 1300
wall2_rect.y = 750

wall3 = pygame.transform.scale(wall, (wall.get_rect().width * 2.5, wall.get_rect().height // 4))
wall3_rect = wall2.get_rect()
wall3_rect.x = 1550
wall3_rect.y = 350

wall4 = pygame.transform.scale(wall, (wall.get_rect().width * 2, wall.get_rect().height // 4))
wall4_rect = wall2.get_rect()
wall4_rect.x = 2200
wall4_rect.y = 350

wall5 = pygame.transform.scale(wall, (wall.get_rect().width * 2, wall.get_rect().height // 4))
wall5_rect = wall2.get_rect()
wall5_rect.x = 2700
wall5_rect.y = 250

wall6 = pygame.transform.scale(wall, (wall.get_rect().width * 2, wall.get_rect().height // 4))
wall6_rect = wall2.get_rect()
wall6_rect.x = 3100
wall6_rect.y = 200

ground = pygame.image.load('ground.png')
ground = pygame.transform.scale(ground, (ground.get_rect().width * 40, ground.get_rect().height // 2))
ground_rect = ground.get_rect()

town = pygame.image.load('town.png')
town = pygame.transform.scale(town, (town.get_rect().width * 10, town.get_rect().height * 10))
town_rect = town.get_rect()

platform1 = pygame.image.load('platform.png')
platform1 = pygame.transform.scale(platform1, (platform1.get_rect().width * 0.5, platform1.get_rect().height * 1))
platform1_rect = platform1.get_rect()
platform1_rect.x = 1400
platform1_rect.y = 550

ladder1 = pygame.image.load('ladder.png')
ladder1 = pygame.transform.scale(ladder1, (ladder1.get_rect().width * 1, ladder1.get_rect().height * 1.5))
ladder1_rect = ladder1.get_rect()
ladder1_rect.x = 2400
ladder1_rect.y = 350

platform = pygame.image.load('platform.png')
platform = pygame.transform.scale(platform, (platform.get_rect().width * 1.75, platform.get_rect().height * 1))
platform_rect = platform.get_rect()
platform_rect.x = 1800
platform_rect.y = 350


ground_rect.bottom = sc_rect.bottom

hero_rect.bottom = ground_rect.top

FPS = 60
clock = pygame.time.Clock()

def fly():
    hero_rect.y -= 10
    if 0 < hero_rect.right < W:
        if move == 1:
            wall1_rect.x += 5
            wall2_rect.x += 5
            wall3_rect.x += 5
            wall4_rect.x += 5
            wall5_rect.x += 5
            wall6_rect.x += 5
            ground_rect.x += 5
            ladder1_rect.x += 5
            platform_rect.x += 5
            platform1_rect.x += 5
        if move == 2:
            wall1_rect.x -= 5
            wall2_rect.x -= 5
            wall3_rect.x -= 5
            wall4_rect.x -= 5
            wall5_rect.x -= 5
            wall6_rect.x -= 5
            ground_rect.x -= 5
            ladder1_rect.x -= 5
            platform_rect.x -= 5
            platform1_rect.x -= 5
    sc.blit(town, town_rect)
    sc.blit(ground, ground_rect)
    sc.blit(hero, hero_rect)
    sc.blit(wall1, wall1_rect)
    sc.blit(wall2, wall2_rect)
    sc.blit(wall3, wall3_rect)
    sc.blit(wall4, wall4_rect)
    sc.blit(wall5, wall5_rect)
    sc.blit(wall6, wall6_rect)
    sc.blit(ladder1, ladder1_rect)
    sc.blit(platform, platform_rect)
    sc.blit(platform1, platform1_rect)
    clock.tick(FPS)
    pygame.display.update()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed()

        # gravitazija
    if hero_rect.bottom < ground_rect.top:
        if hero_rect.bottom == wall1_rect.top and wall1_rect.x + 200 > hero_rect.x > wall1_rect.x - 93:
            hero_rect.bottom = wall1_rect.top
        elif hero_rect.bottom == wall2_rect.top and wall2_rect.x + 300 > hero_rect.x > wall2_rect.x - 93:
            hero_rect.bottom = wall2_rect.top
        elif hero_rect.bottom == wall3_rect.top and wall3_rect.x + 250 > hero_rect.x > wall3_rect.x - 93:
            hero_rect.bottom = wall3_rect.top
        elif hero_rect.bottom == wall4_rect.top and wall4_rect.x + 200 > hero_rect.x > wall4_rect.x - 93:
            hero_rect.bottom = wall4_rect.top
        elif hero_rect.bottom == wall5_rect.top and wall5_rect.x + 200 > hero_rect.x > wall5_rect.x - 93:
            hero_rect.bottom = wall5_rect.top
        elif hero_rect.bottom == wall6_rect.top and wall6_rect.x + 200 > hero_rect.x > wall6_rect.x - 93:
            hero_rect.bottom = wall6_rect.top
        elif hero_rect.bottom == platform_rect.top and platform_rect.x + 500 > hero_rect.x > platform_rect.x - 93:
            hero_rect.bottom = platform_rect.top
        elif hero_rect.bottom == platform1_rect.top and platform1_rect.x + 100 > hero_rect.x > platform1_rect.x - 93:
            hero_rect.bottom = platform1_rect.top
        else:
            hero_rect.bottom += 5

    if keys[97]:
        hero = pygame.image.load('hero_left.png')
        hero = pygame.transform.scale(hero, (hero.get_rect().width * 4, hero.get_rect().height * 4))
        if ground_rect.x == 300:
            wall1_rect.x = 900
            wall2_rect.x = 1400
            wall3_rect.x = 1800
            wall4_rect.x = 2500
            wall5_rect.x = 2700
            wall6_rect.x = 3400
            platform_rect.x = 2900
        else:
            if hero_rect.left > 0 and hero_rect.colliderect(ladder1_rect) is False:
                wall1_rect.x += 5
                wall2_rect.x += 5
                wall3_rect.x += 5
                wall4_rect.x += 5
                wall5_rect.x += 5
                wall6_rect.x += 5
                ground_rect.x += 5
                ladder1_rect.x += 5
                platform_rect.x += 5
                platform1_rect.x += 5
                move = 1

    elif keys[100]:
        hero = pygame.image.load('hero_right.png')
        hero = pygame.transform.scale(hero, (hero.get_rect().width * 4, hero.get_rect().height * 4))
        if ground_rect.x == -4000:
            wall1_rect.x = -3400
            wall2_rect.x = -2900
            wall3_rect.x = -2500
            wall4_rect.x = -1800
            wall5_rect.x = -1600
            wall6_rect.x = -900
            platform_rect.x = -1400
        else:
            if hero_rect.right < W:
                wall1_rect.x -= 5
                wall2_rect.x -= 5
                wall3_rect.x -= 5
                wall4_rect.x -= 5
                wall5_rect.x -= 5
                wall6_rect.x -= 5
                ground_rect.x -= 5
                ladder1_rect.x -= 5
                platform_rect.x -= 5
                platform1_rect.x -= 5
                move = 2
        
    if keys[32]:
        if hero_rect.top > 0 and hero_rect.bottom == ground_rect.top:
            jump = True
        elif wall1_rect.x + 200 > hero_rect.x > wall1_rect.x - 93 and hero_rect.bottom == wall1_rect.top:
            jump = True
        elif wall2_rect.x + 200 > hero_rect.x > wall2_rect.x - 93 and hero_rect.bottom == wall2_rect.top:
            jump = True
        elif wall3_rect.x + 200 > hero_rect.x > wall3_rect.x - 93 and hero_rect.bottom == wall3_rect.top:
            jump = True
        elif wall4_rect.x + 200 > hero_rect.x > wall4_rect.x - 93 and hero_rect.bottom == wall4_rect.top:
            jump = True
        elif wall5_rect.x + 200 > hero_rect.x > wall5_rect.x - 93 and hero_rect.bottom == wall5_rect.top:
            jump = True
        elif wall6_rect.x + 200 > hero_rect.x > wall6_rect.x - 93 and hero_rect.bottom == wall6_rect.top:
            jump = True
        elif hero_rect.bottom == platform_rect.top and platform_rect.x + 500 > hero_rect.x > platform_rect.x - 93:
            jump = True
        elif hero_rect.bottom == platform1_rect.top and platform1_rect.x + 100 > hero_rect.x > platform1_rect.x - 93:
            jump = True
        if jump:
            jump = False
            for _ in range(30):
                fly()
                if hero_rect.top == wall1_rect.bottom and wall1_rect.x + 200 > hero_rect.x > wall1_rect.x - 100:
                    break
                elif hero_rect.top == wall2_rect.bottom and wall2_rect.x + 200 > hero_rect.x > wall2_rect.x - 100:    
                    break
                elif hero_rect.top == wall3_rect.bottom and wall3_rect.x + 200 > hero_rect.x > wall3_rect.x - 100:
                    break
                elif hero_rect.top == wall4_rect.bottom and wall4_rect.x + 200 > hero_rect.x > wall4_rect.x - 100:
                    break
                elif hero_rect.top == wall5_rect.bottom and wall5_rect.x + 200 > hero_rect.x > wall5_rect.x - 100:
                    break
                elif hero_rect.top == wall6_rect.bottom and wall6_rect.x + 200 > hero_rect.x > wall6_rect.x - 100:
                    break

                if hero_rect.right > wall1_rect.left and hero_rect.colliderect(wall1_rect) is True and hero_rect.x < wall1_rect.x:
                    break
                elif hero_rect.right > wall2_rect.left and hero_rect.colliderect(wall2_rect) is True and hero_rect.x < wall2_rect.x:
                    break
                elif hero_rect.right > wall3_rect.left and hero_rect.colliderect(wall3_rect) is True and hero_rect.x < wall3_rect.x:
                    break
                elif hero_rect.right > wall4_rect.left and hero_rect.colliderect(wall4_rect) is True and hero_rect.x < wall4_rect.x: 
                    break
                elif hero_rect.right > wall5_rect.left and hero_rect.colliderect(wall5_rect) is True and hero_rect.x < wall5_rect.x:
                    break
                elif hero_rect.right > wall6_rect.left and hero_rect.colliderect(wall6_rect) is True and hero_rect.x < wall6_rect.x:
                    break

                if hero_rect.left < wall1_rect.right and hero_rect.colliderect(wall1_rect) is True and hero_rect.x > wall1_rect.x:
                    break
                elif hero_rect.left < wall2_rect.right and hero_rect.colliderect(wall2_rect) is True and hero_rect.x > wall2_rect.x:
                    break
                elif hero_rect.left < wall3_rect.right and hero_rect.colliderect(wall3_rect) is True and hero_rect.x > wall3_rect.x:
                    break
                elif hero_rect.left < wall4_rect.right and hero_rect.colliderect(wall4_rect) is True and hero_rect.x > wall4_rect.x: 
                    break
                elif hero_rect.left < wall5_rect.right and hero_rect.colliderect(wall5_rect) is True and hero_rect.x > wall5_rect.x:
                    break
                elif hero_rect.left < wall6_rect.right and hero_rect.colliderect(wall6_rect) is True and hero_rect.x > wall6_rect.x:
                    break
                if hero_rect.y <= 0:
                    break

    if keys[115] and hero_rect.bottom == platform_rect.top and platform_rect.x + 400 > hero_rect.x > platform_rect.x:
        hero_rect.y += 5
        move = 0
    else:
        move = 0

    if hero_rect.top == wall1_rect.bottom and wall1_rect.x + 200 > hero_rect.x > wall1_rect.x - 100:
        punch = True
    else:
        punch = False

    if hero_rect.right > wall1_rect.left and hero_rect.colliderect(wall1_rect) is True and hero_rect.x < wall1_rect.x and hero_rect.top < wall1_rect.top:
        hero_rect.right = wall1_rect.left
    elif hero_rect.right > wall2_rect.left and hero_rect.colliderect(wall2_rect) is True and hero_rect.x < wall2_rect.x and hero_rect.top < wall2_rect.top:
        hero_rect.right = wall2_rect.left
    elif hero_rect.right > wall3_rect.left and hero_rect.colliderect(wall3_rect) is True and hero_rect.x < wall3_rect.x and hero_rect.top < wall3_rect.top:
        hero_rect.right = wall3_rect.left
    elif hero_rect.right > wall4_rect.left and hero_rect.colliderect(wall4_rect) is True and hero_rect.x < wall4_rect.x and hero_rect.top < wall4_rect.top:
        hero_rect.right = wall4_rect.left
    elif hero_rect.right > wall5_rect.left and hero_rect.colliderect(wall5_rect) is True and hero_rect.x < wall5_rect.x and hero_rect.top < wall5_rect.top:
        hero_rect.right = wall5_rect.left
    elif hero_rect.right > wall6_rect.left and hero_rect.colliderect(wall6_rect) is True and hero_rect.x < wall6_rect.x and hero_rect.top < wall6_rect.top:
        hero_rect.right = wall6_rect.left

    elif hero_rect.left < wall1_rect.right and hero_rect.colliderect(wall1_rect) is True and hero_rect.x > wall1_rect.x and hero_rect.top < wall1_rect.top:
        hero_rect.left = wall1_rect.right
    elif hero_rect.left < wall2_rect.right and hero_rect.colliderect(wall2_rect) is True and hero_rect.x > wall2_rect.x and hero_rect.top < wall2_rect.top:
        hero_rect.left = wall2_rect.right
    elif hero_rect.left < wall3_rect.right and hero_rect.colliderect(wall3_rect) is True and hero_rect.x > wall3_rect.x and hero_rect.top < wall3_rect.top:
        hero_rect.left = wall3_rect.right
    elif hero_rect.left < wall4_rect.right and hero_rect.colliderect(wall4_rect) is True and hero_rect.x > wall4_rect.x and hero_rect.top < wall4_rect.top:
        hero_rect.left = wall4_rect.right
    elif hero_rect.left < wall5_rect.right and hero_rect.colliderect(wall5_rect) is True and hero_rect.x > wall5_rect.x and hero_rect.top < wall5_rect.top:
        hero_rect.left = wall5_rect.right
    elif hero_rect.left < wall6_rect.right and hero_rect.colliderect(wall6_rect) is True and hero_rect.x > wall6_rect.x and hero_rect.top < wall6_rect.top:
        hero_rect.left = wall6_rect.right

    if move == 0 and hero_rect.x < 450:
        hero_rect.x += 10
        wall1_rect.x += 10
        wall2_rect.x += 10
        wall3_rect.x += 10
        wall4_rect.x += 10
        wall5_rect.x += 10
        wall6_rect.x += 10
        ground_rect.x += 10
        ladder1_rect.x += 10
        platform_rect.x += 10
        platform1_rect.x += 10
    if move == 0 and hero_rect.x > 450:
        hero_rect.x -= 10
        wall1_rect.x -= 10
        wall2_rect.x -= 10
        wall3_rect.x -= 10
        wall4_rect.x -= 10
        wall5_rect.x -= 10
        wall6_rect.x -= 10
        ground_rect.x -= 10
        ladder1_rect.x -= 10
        platform_rect.x -= 10
        platform1_rect.x -= 10

    sc.blit(town, town_rect)
    sc.blit(ground, ground_rect)
    sc.blit(hero, hero_rect)
    sc.blit(wall1, wall1_rect)
    sc.blit(wall2, wall2_rect)
    sc.blit(wall3, wall3_rect)
    sc.blit(wall4, wall4_rect)
    sc.blit(wall5, wall5_rect)
    sc.blit(wall6, wall6_rect)
    sc.blit(ladder1, ladder1_rect)
    sc.blit(platform, platform_rect)
    sc.blit(platform1, platform1_rect)
    clock.tick(FPS)
    pygame.display.update()
