from pygame import *
window = display.set_mode((700, 500))
display.set_caption('Escape from house')
background = transform.scale(image.load('wall.jpg'), (700, 500))
clock = time.Clock()
FPS = 50

win_width = 700
win_height = 500
score = 0

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

player = Player(('gg.png'), 50, 400, 80, 80, 4)

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


    



    display.update()
    clock.tick(FPS)