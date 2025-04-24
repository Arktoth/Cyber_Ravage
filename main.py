from pygame.math import Vector2
from math import atan2, degrees, pi

import pygame
clock = pygame.time.Clock()

pygame.init()

#характеристики дисплея
screen = pygame.display.set_mode((1920, 1080))
bg_x= 0
bg = pygame.image.load('images/bg.png').convert_alpha()

#заглавие
pygame.display.set_caption('Legend Of Legend')
lable = pygame.font.Font('Roboto-Black.ttf', 90)

#игрок
class Player():
    count = 1
    #перемещение
    def __init__(self):
        self.walk_left_anim = [
            pygame.image.load('images/char/left1.png').convert_alpha(),
            pygame.image.load('images/char/left2.png').convert_alpha(),
            pygame.image.load('images/char/left3.png').convert_alpha(),
            pygame.image.load('images/char/left4.png').convert_alpha(),
            pygame.image.load('images/char/left5.png').convert_alpha(),
            pygame.image.load('images/char/left6.png').convert_alpha(),
            pygame.image.load('images/char/left7.png').convert_alpha(),
            pygame.image.load('images/char/left8.png').convert_alpha()
        ]
        self.walk_right_anim = [
            pygame.image.load('images/char/right1.png').convert_alpha(),
            pygame.image.load('images/char/right2.png').convert_alpha(),
            pygame.image.load('images/char/right3.png').convert_alpha(),
            pygame.image.load('images/char/right4.png').convert_alpha(),
            pygame.image.load('images/char/right5.png').convert_alpha(),
            pygame.image.load('images/char/right6.png').convert_alpha(),
            pygame.image.load('images/char/right7.png').convert_alpha(),
            pygame.image.load('images/char/right8.png').convert_alpha()
        ]
        self.afk = pygame.image.load('images/char/right1.png').convert_alpha()
        self.anim_count = 0
        self.speed =25
        #координаты
        self.position = Vector2(200, 600)
        #прыжок
        self.is_jump = False
        self.jump_count = 12
        self.rect = self.afk.get_rect(topleft=self.position)

    def walk(self):
        if keys[pygame.K_a] and keys[pygame.K_d]:
            screen.blit(self.afk, self.position)
        elif keys[pygame.K_a]:
            screen.blit(self.walk_left_anim[self.anim_count], self.position)  # вывод игрока
        elif keys[pygame.K_d]:
            screen.blit(self.walk_right_anim[self.anim_count], self.position)  # вывод игрока
        elif not (keys[pygame.K_a] or keys[pygame.K_d]):
            screen.blit(self.afk, self.position)
        if keys[pygame.K_a] and self.position[0] > 50:
            self.position[0] -= self.speed
        if keys[pygame.K_d] and self.position[0] < 1780:
            self.position[0] += self.speed
        self.anim_count = (self.anim_count + 1) % 7
        self.rect = self.afk.get_rect(topleft=self.position)

    def jump(self):
        if not self.is_jump:
            if keys[pygame.K_SPACE]:
                self.is_jump = True
        else:
            if self.jump_count >= -12:
                if self.jump_count > 0:
                    self.position[1] -= self.jump_count * 5
                else:
                    self.position[1] += abs(self.jump_count) * 5
                self.jump_count -= 1
            else:
                self.is_jump = False
                self.jump_count = 12

    def attack(self):
        bullet.all.append(bullet())








#враг
class Enemy():
    enemy_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(enemy_timer, 1000)
    list_in_game = []
    model = pygame.image.load('images/enemy.png').convert_alpha()

    @staticmethod
    def spawn_enemy():
        Enemy.list_in_game.append(Enemy().model.get_rect(topleft=(2000, 600)))




#пули
class bullet():
    model = pygame.image.load('images/char/bullet.png')
    all = []

    def __init__(self):
        self.position = Vector2((player.position[0], player.position[1]))
        self.speed = 50
        __mouse_position = pygame.mouse.get_pos()
        dx = __mouse_position[0] - self.position[0]
        dy = __mouse_position[1] - self.position[1]
        rads = atan2(dy, dx)
        rads %= 2 * pi
        self.angel = degrees(rads)
        self.direction = Vector2(1, 0).rotate(self.angel)
        self.rect = bullet.model.get_rect(topleft=self.position)



    def move(self):
        screen.blit(self.model, self.position)
        self.position += self.direction * self.speed
        self.rect = bullet.model.get_rect(topleft=self.position)


#text
label = pygame.font.Font('Roboto-Black.ttf', 40)
#рестарт
restart_label = label.render('Начать заново', False, (255, 255, 255))
restart_label_rect = restart_label.get_rect(topleft=(800, 400))
#выход
exit_label = label.render('выйти из игры', False, (255, 255, 255))
exit_label_rect = exit_label.get_rect(topleft=(800, 500))
#управление_меню
move_label = label.render('управление', False, (255, 255, 255))
move_label_rect = move_label.get_rect(topleft=(830, 600))
#управление
jump_label = label.render('прыжок - space', False, (255, 255, 255))
attak_label = label.render('атака - ЛКМ', False, (255, 255, 255))
walk_label = label.render('движение влево/вправо - a/d', False, (255, 255, 255))
#вернуться
return_label = label.render('обратно', False, (255, 255, 255))
return_label_rect = return_label.get_rect(topleft=(800, 800))

player = Player()
done = True
gameplay = False
moves_menu = False
while done:
    if gameplay:
        screen.blit(bg, (0, 0))
        keys = pygame.key.get_pressed()

        #ходьба
        player.walk()

        #прыжок
        player.jump()

        # атака
        if bullet.all:
            for (i, el1) in enumerate(bullet.all):
                el1.move()
                if el1.position[0] < 0 or el1.position[0] > 2000 or el1.position[1] < -40 or el1.position[1] > 1100 :
                    bullet.all.pop(i)
                if Enemy.list_in_game:
                    for (j, el2) in enumerate(Enemy.list_in_game):
                        if el1.rect.colliderect(el2):
                                Enemy.list_in_game.pop(j)
                                bullet.all.pop(i)









        #враг
        if Enemy.list_in_game:
            for (i, el) in enumerate(Enemy.list_in_game):
                screen.blit(Enemy().model, el)
                el.x -= 20

                if el.x < -300:
                    Enemy.list_in_game.pop(i)

                if player.rect.colliderect(el):
                    gameplay = False

    else:
        screen.fill((0,0,0))
        screen.blit(restart_label, restart_label_rect)
        screen.blit(exit_label, exit_label_rect)
        screen.blit(move_label, move_label_rect)
        mouse = pygame.mouse.get_pos()
        if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay = True
            player.is_jump = False
            player.jump_count = 12
            player.position = Vector2(200, 600)
            Enemy.list_in_game.clear()
            bullet.all.clear()
            pygame.time.set_timer(Enemy.enemy_timer, 1000)
        if exit_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            done = False
            pygame.quit()
        if move_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            moves_menu = True
    if moves_menu:
        screen.fill((0, 0, 0))
        screen.blit(walk_label, (800, 400))
        screen.blit(jump_label, (800, 500))
        screen.blit(attak_label, (800, 600))
        screen.blit(return_label, return_label_rect)
        if return_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            moves_menu = False





    pygame.display.update()
    for event in pygame.event.get():
        #враги
        if event.type == Enemy.enemy_timer:
            Enemy.spawn_enemy()
        #выстрел
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            player.attack()
        #выход
        if event.type == pygame.QUIT:
            done = False
            pygame.quit()
    clock.tick(30)