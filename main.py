
from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (60, 60))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))





window = display.set_mode((700, 500))
display.set_caption('Pipl')
background = transform.scale(image.load("background.jpg"), (700, 500))


player = GameSprite("player_image.png", 100, 100, 5)  


mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

game = True
while game:
    for a in event.get():
        if a.type == QUIT:
            game = False
    
window.blit(background, (0, 0))

    

display.update()
