
from pygame import *

class Gamesprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(Gamesprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

win_width = 700
win_height = 500
back = (200,255,255)
window = display.set_mode((win_width,win_height))
font.init()
font = font.Font(None,35)
lose1 = font.render('Player 1 lose',True,(180,0,0))
lose2 = font.render('Player 2 lose',True,(180,0,0))
speed_x = 3
speed_y = 3

FPS = 60
clock = time.Clock()

game = True
finish = False

racket1 = Player('Barretta_verde_Ping_Pong_1 (1) (1).png', 30, 200, 4, 50, 150) # при созданни спрайта добавляется еще два параметра
racket2 = Player('Barretta_verde_Ping_Pong_1 (1) (1).png', 520, 200, 4, 50, 150)
ball = Gamesprite('machik.png', 200, 200, 4, 50, 50)
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(back)
        racket1.update_r()
        racket2.update_l()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(racket1,ball) or sprite.collide_rect(racket2,ball):
            speed_x *= -1
            speed_y *= 1

        if ball.rect.y> win_height-50 or ball.rect.y <0:
            speed_y *= -1

        if ball.rect.x <0:
            finish = True
            window.blit(lose1,(280,280))
            game_over = True
        
        if ball.rect.x>win_width:
            finish = True
            window.blit(lose2,(280,280))
            game_over = True
            
        racket1.reset()
        racket2.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)