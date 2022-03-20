import pygame
from text_renderer import Text


class Game_Over:

    def __init__(self, screen, scenes):
        self.screen = screen
        self.scenes = scenes

    def draw(self):
        self.screen.fill([255, 255, 255])
        Text.draw(self.screen, "Game Over!", 40, [0, 0, 0],
                    center_x=True, center_y=True)

    def update(self):
        self.draw()
