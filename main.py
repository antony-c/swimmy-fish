import pygame, pygame.time, sys, GUI, game_over
from scenes import Scene_Manager
from input_manager import Input_Manager

pygame.init()

screen = pygame.display.set_mode([1000, 800])
clock = pygame.time.Clock()

scenes = Scene_Manager()
im = Input_Manager()

GAME = GUI.Game(screen, scenes, im)
GAME_OVER = game_over.Game_Over(screen, scenes)

scenes.add_scene("Game", GAME)
scenes.add_scene("Game_Over", GAME_OVER)

scenes.swap_scene("Game")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            im.pressed = event.key

    scenes.current_scene.update()

    clock.tick(60)
    pygame.display.flip()
