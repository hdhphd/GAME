from pygame import *

win_wight = 1500
win_height = 700
window = display.set_mode((win_wight,win_height))
display.set_caption('Шутер')
background = transform.scale(image.load('fre.jpg'), (win_wight, win_height))

x1 = 100
y1 = 500

x2 = 700
y2 = 400



class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65,65))
        self.speed = player_speed

        self.rect = self.image.get_rect()   
        self.rect.x = player_x
        self.rect.y = player_y

    def recet(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
    def move_up(self):
        self.rect.y -= self.speed
        
    def move_down(self):
        self.rect.y += self.speed
    def move_left(self):
        self.rect.x -= self.speed
    def move_right(self):
        self.rect.x += self.speed

class Player(GameSprite):

    def update(self):
        keys = key.get_pressed()
        if (keys[K_a] or keys[K_LEFT]) and self.rect.x >5 :
            self.rect.x += self.speed
    
    def fire(self):
        keys = key.get_pressed()
        if keys[K_W] and flag == False:
            go_x = self.rect.x
            flag = True
        if flag == True:
            self.rect.y -= self.speed
        else:
            self.rect.x = go_x

        



game = True
while game:

    
    #if keys_pressed[K_UP] and y1 > 5:

        #y1 -= 10
    #if keys_pressed[K_DOWN] and y1 < 600:

        #y1 += 10

    #if keys_pressed[K_LEFT] and x1 > 5:

        #x1 -= 10

    #if keys_pressed[K_RIGHT] and x1 < 1200:

        #x1 += 10

    #if keys_pressed[K_w] and y2 > 5:

        #y2 -= 10
    #if keys_pressed[K_s] and y2 < 600:

        #y2 += 10

    #if keys_pressed[K_a] and x2 > 5:

        #x2 -= 10

    #if keys_pressed[K_d] and x2 < 1200:

       # x2 += 10






    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(background,(0,0))
    display.update()
    time.delay(60)
