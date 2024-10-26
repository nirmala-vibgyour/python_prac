import pygame
import random
import math
from pygame import mixer

# initalize pygame
pygame.init()

# creating game window
screen = pygame.display.set_mode((800, 600))

# background
background = pygame.image.load("background.png")

# music
mixer.music.load('background.wav')
mixer.music.play(-1)

# title and icon(32 px)
pygame.display.set_caption("Space Invasion")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# players
playerImg = pygame.image.load("shuttle.png")
playerX = 370
playerY = 480
playerX_change = 0

aliennImg = []
aliennX = []
aliennY = []
aliennX_change = []
aliennY_change = []
numOfEnemies = 6

for i in range(numOfEnemies):
    aliennImg.append(pygame.image.load("alienn.png"))
    aliennX.append(random.randint(0, 735))
    aliennY.append(random.randint(50, 150))
    aliennX_change.append(4)
    aliennY_change.append(40)

bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
    score = font.render("Score:" + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def player(x, y):
    screen.blit(playerImg, (x, y))

def alienn(x, y, i):
    screen.blit(aliennImg[i], (x, y))

def bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16, y+10))

def isCollision(aliennX, aliennY, bulletX, bulletY):
    distance = math.sqrt((math.pow(aliennX-bulletX, 2)) + (math.pow(aliennY-bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

# Main game loop
running = True
while running:

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # keystroke pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound('laser.wav')
                    bullet_sound.play()
                    bulletX = playerX
                    bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if (event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT):
                playerX_change = 0

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        # image size is 64, 800-64
        playerX = 736
    
    for i in range(numOfEnemies):
        if aliennY[i] > 440:
            for j in range(numOfEnemies):
                aliennY[i] = 2000
            game_over_text()
            break
        aliennX[i] += aliennX_change[i]
        if aliennX[i] <= 0:
            aliennX_change[i] = 4
            aliennY[i] += aliennY_change[i]
        elif aliennX[i] >= 736:
            aliennX_change[i] = -4 
            aliennY[i] += aliennY_change[i]

        collision = isCollision(aliennX[i], aliennY[i], bulletX, bulletY)
        if collision:
            explosion_Sound = mixer.Sound('explosion.wav')
            explosion_Sound.play()
            bulletY = 480
            bullet_State = "ready"
            score_value += 1
            print(score_value)
            aliennX[i] = random.randint(0, 735)
            aliennY[i] = random.randint(50, 150)

        alienn(aliennX[i], aliennY[i], i)

    if bulletY <= 0:
            bulletY = 480
            bullet_state = "ready"
        
    if bullet_state == "fire":
        bullet(playerX, bulletY)
        bulletY -= bulletY_change
    
    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()