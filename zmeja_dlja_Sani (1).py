import pygame
import random
pygame.init()
W = 1000
H = 1000
sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("События от клавиатуры")
WHITE = (255, 255, 255)
BLUE = (0, 191, 255)
PURPLE = (199, 21, 133)
GREEN = (124, 252, 0)
RED = (139, 0, 0)
SUPERRED = (255, 69, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
GRAY = (105, 105, 105)

speed = 5
x = 450
y = 450

a = 100
food = False
listx = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 450]
listy = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 450]

jopa = 1

FPS = 60  # число кадров в секунду
clock = pygame.time.Clock()

sc.fill(GRAY)
s = 0
while s == 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[0] > 100 and event.pos[0] < 451 and event.pos[1] > 100 and event.pos[1] < 451:
                colour_snake = PURPLE
                colour_earth = BLUE
                colour_food = WHITE
                colour_eyes = WHITE
                s = 1
            if event.pos[0] > 550 and event.pos[0] < 901 and event.pos[1] > 100 and event.pos[1] < 451:
                colour_snake = YELLOW
                colour_earth = SUPERRED
                colour_food = WHITE
                colour_eyes = WHITE
                s = 1
            if event.pos[0] > 100 and event.pos[0] < 451 and event.pos[1] > 550 and event.pos[1] < 901:
                colour_snake = GREEN
                colour_earth = WHITE
                colour_food = RED
                colour_eyes = WHITE
                s = 1
            if event.pos[0] > 550 and event.pos[0] < 901 and event.pos[1] > 550 and event.pos[1] < 901:
                colour_snake = WHITE
                colour_earth = BLACK
                colour_food = WHITE
                colour_eyes = BLACK
                s = 1


    theme1 = pygame.Surface((350, 350))
    theme1.fill(BLUE)
    pygame.draw.rect(theme1, WHITE, (50, 50, 100, 100))
    pygame.draw.rect(theme1, PURPLE, (150, 200, 200, 100))
    pygame.draw.rect(theme1, WHITE, (170, 220, 20, 20))
    pygame.draw.rect(theme1, WHITE, (170, 260, 20, 20))
    sc.blit(theme1, (100, 100))

    theme2 = pygame.Surface((350, 350))
    theme2.fill(SUPERRED)
    pygame.draw.rect(theme2, WHITE, (50, 50, 100, 100))
    pygame.draw.rect(theme2, YELLOW, (150, 200, 200, 100))
    pygame.draw.rect(theme2, WHITE, (170, 220, 20, 20))
    pygame.draw.rect(theme2, WHITE, (170, 260, 20, 20))
    sc.blit(theme2, (550, 100))

    theme3 = pygame.Surface((350, 350))
    theme3.fill(WHITE)
    pygame.draw.rect(theme3, RED, (50, 50, 100, 100))
    pygame.draw.rect(theme3, GREEN, (150, 200, 200, 100))
    pygame.draw.rect(theme3, WHITE, (170, 220, 20, 20))
    pygame.draw.rect(theme3, WHITE, (170, 260, 20, 20))
    sc.blit(theme3, (100, 550))

    theme4 = pygame.Surface((350, 350))
    theme4.fill(BLACK)
    pygame.draw.rect(theme4, WHITE, (50, 50, 100, 100))
    pygame.draw.rect(theme4, WHITE, (150, 200, 200, 100))
    pygame.draw.rect(theme4, BLACK, (170, 220, 20, 20))
    pygame.draw.rect(theme4, BLACK, (170, 260, 20, 20))
    sc.blit(theme4, (550, 550))

    pygame.display.update()
    pygame.display.flip()
    clock.tick(FPS)


eyes_up = pygame.Surface((50, 50))
eyes_up.fill(colour_earth)
pygame.draw.rect(eyes_up, colour_snake, (0, 20, 50, 30))
pygame.draw.rect(eyes_up, colour_eyes, (10, 30, 10, 10))
pygame.draw.rect(eyes_up, colour_eyes, (30, 30, 10, 10))
pygame.draw.rect(eyes_up, colour_snake, (10, 0, 30, 20))

eyes_down = pygame.Surface((50, 50))
eyes_down.fill(colour_earth)
pygame.draw.rect(eyes_down, colour_snake, (0, 0, 50, 30))
pygame.draw.rect(eyes_down, colour_eyes, (10, 10, 10, 10))
pygame.draw.rect(eyes_down, colour_eyes, (30, 10, 10, 10))
pygame.draw.rect(eyes_down, colour_snake, (10, 30, 30, 20))

eyes_left = pygame.Surface((50, 50))
eyes_left.fill(colour_earth)
pygame.draw.rect(eyes_left, colour_snake, (20, 0, 30, 50))
pygame.draw.rect(eyes_left, colour_eyes, (30, 10, 10, 10))
pygame.draw.rect(eyes_left, colour_eyes, (30, 30, 10, 10))
pygame.draw.rect(eyes_left, colour_snake, (0, 10, 20, 30))

eyes_right = pygame.Surface((50, 50))
eyes_right.fill(colour_earth)
pygame.draw.rect(eyes_right, colour_snake, (0, 0, 30, 50))
pygame.draw.rect(eyes_right, colour_eyes, (10, 10, 10, 10))
pygame.draw.rect(eyes_right, colour_eyes, (10, 30, 10, 10))
pygame.draw.rect(eyes_right, colour_snake, (30, 10, 20, 30))

tail_up = pygame.Surface((50, 50))
tail_up.fill(colour_earth)
pygame.draw.rect(tail_up, colour_snake, (0, 30, 50, 30))
pygame.draw.rect(tail_up, colour_snake, (10, 10, 30, 20))
pygame.draw.rect(tail_up, colour_snake, (20, 0, 10, 10))

tail_senja = pygame.Surface((50, 50))
tail_senja.fill(colour_earth)
pygame.draw.rect(tail_senja, colour_snake, (0, 0, 50, 20))
pygame.draw.rect(tail_senja, colour_snake, (10, 20, 30, 20))
pygame.draw.rect(tail_senja, colour_snake, (20, 40, 10, 10))

tail_left = pygame.Surface((50, 50))
tail_left.fill(colour_earth)
pygame.draw.rect(tail_left, colour_snake, (0, 20, 10, 10))
pygame.draw.rect(tail_left, colour_snake, (10, 10, 20, 30))
pygame.draw.rect(tail_left, colour_snake, (30, 0, 20, 50))

tail_right = pygame.Surface((50, 50))
tail_right.fill(colour_earth)
pygame.draw.rect(tail_right, colour_snake, (0, 0, 20, 50))
pygame.draw.rect(tail_right, colour_snake, (20, 10, 20, 30))
pygame.draw.rect(tail_right, colour_snake, (40, 20, 10, 10))
surf = pygame.Surface((50, 50))
surf.fill(colour_snake)

while s != 0:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            exit()
    keys = pygame.key.get_pressed()
    sc.fill(colour_earth)
    if keys[pygame.K_LEFT]:
        jopa = 1
    elif keys[pygame.K_RIGHT]:                                                                                           
        jopa = 2
    elif keys[pygame.K_UP]:
        jopa = 3
    elif keys[pygame.K_DOWN]:
        jopa = 4
    if jopa == 1:
        x -= speed
        if x < 0:
            x = 990
        listx.append(x)
        listy.append(listy[-1])
        listx.pop(0)
        listy.pop(0)
    elif jopa == 2:
        x += speed
        if x > 1000:
            x = -10
        listx.append(x)
        listy.append(listy[-1])
        listx.pop(0)
        listy.pop(0)
    elif jopa == 3:
        y -= speed
        if y < 0:
            y = 990
        listy.append(y)
        listx.append(listx[-1])
        listx.pop(0)
        listy.pop(0)
        sc.blit(eyes_up, (listx[-1], listy[-1]))
    elif jopa == 4:
        y += speed
        if y > 1000:
            y = -10
        listy.append(y)
        listx.append(listx[-1])
        listx.pop(0)
        listy.pop(0)

    for f in range(len(listx) - 1):
        if listx[f] == listx[-1] and listy[f] == listy[-1]:
            sc.fill(BLACK)
            pygame.display.update()
            s = 0

    if a > 0 and food == False:
        foodx = random.randint(0, 900)
        foody = random.randint(0, 900)
        eat = pygame.Surface((a, a))
        eat.fill(colour_food)
        a += -1
        food = True

    if listx[-1] + 50 > foodx and listx[-1] + 50 < foodx + 100 and listy[-1]  > foody and listy[-1] < foody + 100:
        listx.insert(0, listx[0] - speed)
        listy.insert(0, listy[0] - speed)
        sc.blit(eat, (foodx, foody))
        eat.fill(colour_earth)
        food = False
        speed += 0.2
    if listx[-1] + 50  > foodx and listx[-1] + 50  < foodx + 100 and listy[-1] + 50  > foody and listy[-1] + 50  < foody + 100:
        listx.insert(0, listx[0] - speed)
        listy.insert(0, listy[0] - speed)
        sc.blit(eat, (foodx, foody))
        eat.fill(colour_earth)
        food = False
        speed += 0.2
    if listx[-1] > foodx and listx[-1] < foodx + 100 and listy[-1]  > foody and listy[-1] < foody + 100:
        listx.insert(0, listx[0] - speed)
        listy.insert(0, listy[0] - speed)
        sc.blit(eat, (foodx, foody))
        eat.fill(colour_earth)
        food = False
        speed += 0.2
    if listx[-1] > foodx and listx[-1]  < foodx + 100 and listy[-1] + 50  > foody and listy[-1] + 50  < foody + 100:
        listx.insert(0, listx[0] - speed)
        listy.insert(0, listy[0] - speed)
        sc.blit(eat, (foodx, foody))
        eat.fill(colour_earth)
        food = False
        speed += 0.2
    for i in range(len(listx) - 2, 0, -1):
        sc.blit(surf, (listx[i], listy[i]))
    if listy[-1] > listy[-2]:
        sc.blit(eyes_down, (listx[-1], listy[-1]))
    if listy[-1] < listy[-2]:
        sc.blit(eyes_up, (listx[-1], listy[-1]))
    if listx[-1] < listx[-2]:
        sc.blit(eyes_left, (listx[-1], listy[-1]))
    if listx[-1] > listx[-2]:
        sc.blit(eyes_right, (listx[-1], listy[-1]))
    if listx[0] < listx[1]:
        sc.blit(tail_left, (listx[0], listy[0]))
    if listx[0] > listx[1]:
        sc.blit(tail_right, (listx[0], listy[0]))
    if listy[0] < listy[1]:
        sc.blit(tail_up, (listx[0], listy[0]))
    if listy[0] > listy[1]:
        sc.blit(tail_senja, (listx[0], listy[0]))
    sc.blit(eat, (foodx, foody))
    pygame.display.update()
    pygame.display.flip()
    clock.tick(FPS)
   
    


   
