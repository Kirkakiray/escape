from pygame import *
from random import randint 
from time import time as timer



window = display.set_mode((700, 500))
display.set_caption('Escape from house')
background = transform.scale(image.load('wall.jpg'), (700, 500))
clock = time.Clock()
FPS = 50

win_width = 700
win_height = 500
score = 0
goal = 10


'''mixer.init()
mixer.music.load('space.mp3')
mixer.music.play()
sound = mixer.Sound('space.ogg')'''


font.init()
font2 = font.Font(None, 36)
font1 = font.Font(None, 36)
win = font1.render('ТЫ СБЕЖАЛ! ТЕПЕРЬ БЕГИ К МАМЕ!', True, (225, 255, 255))
lose = font1.render('О ЧЁРТ! ТЫ НЕ СБЕЖАЛ, ТЕБЯ СЪЕЛА БАБАЙКА!', True, (180, 0, 0))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 595:
            self.rect.x += self.speed
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 395:
            self.rect.y += self.speed




player = Player(('gg.png'), 50, 400, 80, 80, 3)
door = GameSprite(('door.png'), randint(20, 680), randint(20, 480), 100, 100, 0)

time = 20
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:       
        window.blit(background,(0, 0))
        player.update()
        player.reset()
        door.update()
        door.reset()



        if sprite.collide_rect(player, door):
            score = score + 1
            door = GameSprite(('door.png'), randint(20, 660), randint(20, 460), 100, 100, 0)
            '''sound.play()'''
        
        ''' window.blit(lose,(10, 50))'''
            

        if score >= goal:
            finish = True
            window.blit(win, (200, 200))
        text = font2.render('Score:' + str(score), 1, (225, 225, 255))
        window.blit(text, (10, 20))
       


    


    display.update()
    clock.tick(FPS)
