import pygame, pygame.font


class Text:

    @staticmethod
    def draw(screen, text, size, colour, pos=(0, 0), background=False,
        bg_colour=(255, 255, 255), center_x=False, center_y=False):

        font = pygame.font.Font("./resources/Messiri.ttf", size)
        text_surface = font.render(text, True, colour)
        text_width = text_surface.get_width()
        text_height = text_surface.get_height()

        pos = list(pos)

        if center_x:
            pos[0] = 500 - text_width // 2
        if center_y:
            pos[1] = 400 - text_height // 2

        if background:
            rect = pygame.Rect(pos[0] - 5, pos[1] - 3,
                        text_width + 7, text_height)
            pygame.draw.rect(screen, bg_colour, rect, 0, 20)

        screen.blit(text_surface, pos)
