import pygame, math
from random import randint
from text_renderer import Text


class Game:

    def __init__(self, screen, scenes, im):
        self.screen = screen
        self.scenes = scenes
        self.im = im
        self.score = int()

        self.player = Player(screen)
        self.pipes = [Pipe(screen, 1000 - 500 * i) for i in range(2)]
        self.bg = Background(screen)

    def move_sprite(self):
        if self.im.pressed == pygame.K_UP:
            self.player.y_movement = self.player.jump_force

    def check_collision(self):
        sprite = self.player.sprite_rect

        for pipe in self.pipes:
            touching_top = sprite.colliderect(pipe.t_rect)
            touching_bottom = sprite.colliderect(pipe.b_rect)
            if touching_top or touching_bottom:
                self.scenes.swap_scene("Game_Over")

            touching_middle = sprite.colliderect(pipe.m_rect)
            if touching_middle and not pipe.scored:
                self.score += 1
                pipe.scored = True

    def update_pipe(self):
        for i, pipe in enumerate(self.pipes):
            pipe.update(self.score)
            if pipe.x + 100 < 0:
                self.pipes[i] = Pipe(self.screen, 1000)

    def draw_score(self):
        Text.draw(self.screen, f"SCORE: {self.score}", 40,
                    (0, 0, 0), (0, 20), background=True, center_x=True)

    def draw_menu_button(self):
        pass

    def update(self):
        if self.im.pressed:
            self.move_sprite()

        self.check_collision()

        self.bg.update()
        self.update_pipe()
        self.draw_score()
        self.draw_menu_button()
        self.player.update()

        self.im.pressed = str()


class Player:

    def __init__(self, screen):
        self.screen = screen

        self.pos = [150, 400]

        self.gravity = 1.1
        self.y_movement = int()
        self.jump_force = -17

        sprite_img = pygame.image.load("./resources/Fish256.png")
        self.sprite_default = pygame.transform.scale(sprite_img, (78, 78))

        self.sprite = self.sprite_default
        self.sprite_rect = self.sprite.get_rect()

    def move(self):
        def clamp(num, min_value, max_value):
            return max(min(num, max_value), min_value)

        self.y_movement += self.gravity
        self.pos[1] += self.y_movement

        if self.pos[1] > 800:
            self.pos[1] = 800

        if self.pos[1] < 0:
            self.pos[1] = 0

        clamped = clamp(-self.y_movement, -15, 15)
        self.sprite = pygame.transform.rotate(self.sprite_default, clamped)
        self.sprite_rect = self.sprite.get_rect()

        self.sprite_rect.center = self.pos

    def update(self):
        self.move()
        self.screen.blit(self.sprite, self.sprite_rect)


class Pipe:

    def __init__(self, screen, x):
        self.screen = screen

        self.scored = False

        self.x = x
        self.y = randint(30, 470)

        diff = 280

        self.t_rect = pygame.Rect(self.x, 0, 100, self.y)
        self.b_rect = pygame.Rect(self.x, self.y + diff, 100, 800 - self.y)
        self.m_rect = pygame.Rect(self.x, self.y, 100, diff)

        t_img = pygame.image.load("./resources/pipe2.png")
        b_img = pygame.image.load("./resources/pipe.png")
        self.t_pipe = pygame.transform.scale(t_img, (100, 800))
        self.b_pipe = pygame.transform.scale(b_img, (100, 800))

    def draw_pipe(self, score):
        self.x -= math.pow(math.log(score + 1), 1.5) + 2

        self.t_rect.left = self.x
        self.b_rect.left = self.x
        self.m_rect.left = self.x

        rect = self.t_pipe.get_rect()
        rect.center = self.t_rect.center
        rect.bottom = self.t_rect.bottom

        self.screen.blit(self.t_pipe, rect)
        self.screen.blit(self.b_pipe, self.b_rect)

    def update(self, score):
        self.draw_pipe(score)


class Background:

    def __init__(self, screen):
        self.screen = screen

        self.x = 2000
        self.bg_img = pygame.image.load("./resources/background.png")
        self.bg_rect = self.bg_img.get_rect()

    def cascade(self):
        self.x -= 1
        if self.x < 1000:
            self.x = 2000

        self.bg_rect.right = self.x
        self.screen.blit(self.bg_img, self.bg_rect)

    def update(self):
        self.cascade()
