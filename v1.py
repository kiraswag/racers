from pygame import *



clock = time.Clock()

class GameSprite(sprite.Sprite):
   #конструктор класса
    def __init__(self, player_image, player_x, player_y, player_speed, player_width, player_height):
        super().__init__()
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
       
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()

        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed 
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

back = (92, 92, 92)
win_width = 900
win_height = 600
window = display.set_mode((win_width, win_height))
display.set_caption("Race")


car1 = GameSprite('car1.png', 50, 100, 20, 150, 70)
car2 = GameSprite('car2.png', 50, 400, 20, 150, 170)
finish1 = GameSprite('finish.jpg', 750, 1, 5, 150, 600)
car1_win = GameSprite('car1_win.png', 0, 0, 5, 900, 600)
car2_win = GameSprite('car2_win.png', 0, 0, 5, 900, 600)


game = True
finish = False

clock = time.Clock()
FPS = 60
key_pressed = key.get_pressed()


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_a:
                car2.rect.x += car2.speed
            elif e.key == K_l:
                car1.rect.x += car1.speed
    if finish != True:

        window.fill(back)
        if sprite.collide_rect(car1, finish1):
            car1_win.reset()
            finish1.empty()

            finish = True


        if sprite.collide_rect(car2, finish1):
            finish = True


        car1.reset()
        car2.reset()
        finish1.reset()
        if sprite.collide_rect(car1, finish1):
            car1_win.reset()
            finish = True

        if sprite.collide_rect(car2, finish1):
            car2_win.reset()
            finish = True
        display.update()
        clock.tick(FPS)


       
