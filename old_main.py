import copy
import pygame
pygame.init()
import random
import sys
import threading
from pygame.locals import *

from map import Map
import demo_maps

random.seed()

demo_fn = demo_maps.build_demo53

screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption('TFT Sandbox')

wins_team_1 = 0
wins_team_2 = 0
draws = 0

def run_matches_in_background():
    global wins_team_2
    global wins_team_1
    global draws
    while True:
        current_map = demo_fn()
        time = 0.0
        while not current_map.winner:
            current_map.tick(time)
            time += 0.01
        if current_map.winner == 1:
            wins_team_1 += 1
        elif current_map.winner == 2:
            wins_team_2 += 1
        else:
            draws += 1

t = threading.Thread(target=run_matches_in_background, daemon=True)
t.start()

fps_clock = pygame.time.Clock()
FPS = 100
font = pygame.font.SysFont('Comic Sans MS', 30)

time = -0.5
def reset_show_map():
    return demo_fn()

map = reset_show_map()

i = 0
while True:
    i += 1
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYUP:
            if event.key in (K_SPACE, ):
                map = reset_show_map()
                time = -0.5

    if map.winner in (1, 2, 3):
        map = reset_show_map()
        time = -0.5

    if time >= 0:
        map.tick(time)
    if i % 10:
        screen.fill((255,255,255))
        map.draw(screen, time)
    time += 0.01
    if wins_team_2 + wins_team_1 + draws > 0:
        screen.blit(font.render(f'{100*wins_team_2/(wins_team_2+wins_team_1+draws):.2f}% ({wins_team_2})', False, (255, 0, 0)), (600, 50))
        screen.blit(font.render(f'{100*draws/(wins_team_2+wins_team_1+draws):.2f}% ({draws})', False, (0, 0, 0)), (600, 200))
        screen.blit(font.render(f'{100*wins_team_1/(wins_team_2+wins_team_1+draws):.2f}% ({wins_team_1})', False, (0, 255, 0)), (600, 350))
    pygame.display.update()
    fps_clock.tick(FPS)
