import pygame
from random import randrange as rnd
from sys import exit

WIDTH, HEIGHT = 1200, 800
fps = 60
# paddle settings
paddle_w = 330
paddle_h = 35
paddle_speed = 2
voltages = 0
distance = HEIGHT - 2 * paddle_h
paddle = pygame.Rect(WIDTH // 2 - paddle_w // 2, HEIGHT - paddle_h - 10, paddle_w, paddle_h)
paddle2 = pygame.Rect(WIDTH // 2 - paddle_w // 2, 10, paddle_w, paddle_h)
# ball settings

dx, dy = 1, -1
# blocks settings


pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
# background image
img = pygame.image.load('1.jpg').convert()
img = pygame.transform.scale(img, (WIDTH, HEIGHT))

f1 = pygame.font.Font(None, 30)

materials = {"Трансформаторное масло" : 115, 'Парафин' : 225, 'Эбонит' : 700,\
             'Резина' : 175, 'Стекло' : 125, 'Слюда' : 750,\
                 'Бумага, пропитанная маслом' : 175, 'Мрамор' : 40}

def breakdown(d, u, e):
    if u/d >= e: return True
    return False

mat = 'Мрамор'

while True:
    sc.blit(img, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
            if voltages < 1400: voltages += 20
            #print(voltages)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
            if voltages > 0: voltages -= 20
            #print(voltages)
            
    textU = f1.render('Разность потенциалов = ' + str(voltages) + 'kV', True,(70, 0, 130))
    placeU = textU.get_rect(center=(1000, 50))
    sc.blit(textU, placeU)
    
    
    pygame.draw.rect(sc, pygame.Color('red'), paddle)
    pygame.draw.rect(sc, pygame.Color('black'), paddle2)
    
    
    
    key = pygame.key.get_pressed()
    if key[pygame.K_UP] and paddle.top > 0 and paddle.top - paddle2.top > 100:
        paddle.top -= paddle_speed
        paddle2.top += paddle_speed
        distance = (paddle.top - paddle2.bottom) / 50
        print(distance)
    if key[pygame.K_DOWN] and paddle.bottom < HEIGHT:
        paddle.bottom += paddle_speed
        paddle2.bottom -= paddle_speed
        distance = (paddle.top - paddle2.bottom) / 50
        print(distance)
    textD = f1.render('Расстояние между анодами = ' + str(distance) + 'mm', True,(70, 0, 130))
    placeD = textD.get_rect(center=(200, 50))
    sc.blit(textD, placeD)
    
    if breakdown(distance, voltages, materials["Мрамор"]):
        stream = pygame.Rect(WIDTH/2-(30/distance)/2*voltages*0.01, paddle2.bottom, 30/distance*voltages*0.01, distance*50)
        pygame.draw.rect(sc, pygame.Color('blue'),stream)
        
    
    pygame.display.flip()
    clock.tick(fps)