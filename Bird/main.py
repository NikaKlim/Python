import time
import pygame
import random

h, w = 1200, 700
x, y = h * 0.5, w * 0.85
flag = True
black, white, green, blue, red = (0, 0, 0), (255, 255, 255),(0, 255, 0), (0, 0, 128), (255, 30, 70)
score, record = 0,0
xmove,ymove = 0, 0
x_eat, y_eat = 500,300
color = green

time_of_click = time.time()

# initialization of screen
pygame.init()
screen = pygame.display.set_mode((h, w))
pygame.display.set_caption("MyGame")

# load image
img = pygame.image.load('bird.png').convert_alpha()
rect = img.get_rect()
img = pygame.transform.scale(img, (60, 60))

# add text score
def add_text_score():
    global score
    text = "Score: {}".format(score)
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(text, True, black)
    textRect = text.get_rect()
    textRect.center = (75, 24)
    # add case for text
    score_case = pygame.Rect(0, 0, 163, 45) #position x,y / w,h
    screen.blit(text, textRect)
    pygame.draw.rect(screen, black, score_case, 4)

def add_best_record():
    get_record()
    text = "Record: {}".format(record)
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(text, True, black)
    textRect = text.get_rect()
    textRect.center = (255, 24)
    # add case for text
    score_case = pygame.Rect(167, 0, 200, 45) #position x,y / w,h
    screen.blit(text, textRect)
    pygame.draw.rect(screen, black, score_case, 4)

def get_record():
    global record
    file = open('record.txt')
    lines = file.read()
    lines = lines.split("-")
    del lines[-1]
    lines = [int(i) for i in lines]
    record = max(lines)


def add_time():
    times = round((time.time() - time_of_click))
    text = "Time: {}".format(times)
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(text, True, black)
    textRect = text.get_rect()
    textRect.center = (485, 24)
    # add case for text
    score_case = pygame.Rect(372, 0, 220, 45) #position x,y / w,h
    screen.blit(text, textRect)
    pygame.draw.rect(screen, black, score_case, 4)

def img_position(x, y):
    rect.center = x, y
    screen.fill(white)
    screen.blit(img, rect)

def add_eat(x, y):
    global x_eat, y_eat, score, color
    if (x-120<=x_eat<=x-80) and (y-120<=y_eat<=y-80): # create new food
        color = random.choice([black, green, blue, red])
        x_eat = random.randint(121,1170)
        y_eat = random.randint(131,660)
        eat = pygame.Rect(x_eat, y_eat, 10, 10) #position x,y / w,h
        pygame.draw.rect(screen, color, eat)
        score +=1

def add_start_button():
    global record
    text = "Start".format(record)
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(text, True, black)
    textRect = text.get_rect()
    textRect.center = (1100, 24)
    # add case for text
    score_case = pygame.Rect(1025, 0, 150, 45) #position x,y / w,h
    screen.blit(text, textRect)
    pygame.draw.rect(screen, black, score_case, 4)


def remember_record():
    f = open('record.txt', 'a')
    f.write(str(score))
    f.write("-")
    f.close()

def new_game():
    global score, x,y, x_eat, y_eat
    score = 0
    x, y = h * 0.5, w * 0.85
    x_eat, y_eat = 500, 300


while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            remember_record()

            flag = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                xmove = 2
            elif event.key == pygame.K_LEFT:
                xmove = -2
            elif event.key == pygame.K_DOWN:
                ymove = 2
            elif event.key == pygame.K_UP:
                ymove = -2

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT\
                    or event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                xmove = 0
                ymove = 0

        if event.type == pygame.MOUSEBUTTONDOWN:
            if 1025 <= mouse[0] <= 1175 and 0 <= mouse[1] <= 45:
                time_of_click = time.time()
                remember_record()
                new_game()

    mouse = pygame.mouse.get_pos()
    if x>1271:
        xmove = 0
        x = 1270
    elif x<120:
        xmove = 0
        x = 121
    elif y>761:
        ymove = 0
        y = 760
    elif y<130:
        ymove = 0
        y = 131

    x +=xmove
    y += ymove

    img_position(x, y)

    add_eat(x,y)
    add_eat(x,y)
    eat = pygame.Rect(x_eat, y_eat, 10, 10) #position x,y / w,h
    pygame.draw.rect(screen, color, eat)
    add_best_record()
    add_start_button()
    add_text_score()
    add_time()

    pygame.display.update()
