from pygame import *
window = display.set_mode((700, 500))
display.set_caption('Escape from house')
background = transform.scale(image.load('background.png'), (700, 500))
clock = time.Clock()
FPS = 50

x = 100
y = 300

game = True 
while game:
    window.blit(background,(0, 0))
    window.blit(sprite1, (x, y))


    keys_pressed = key.get_pressed()
    if keys_pressed[K_LEFT] and x > 5:
        x -= speed
    if keys_pressed[K_RIGHT] and x < 595:
        x += speed
    if keys_pressed[K_UP] and y > 5:
        y -= speed
    if keys_pressed[K_DOWN] and y < 395:
        y += speed



    display.update()
    clock.tick(FPS)