from pygame import *
mixer.init()
mixer.music.load('jungles.ogg')
font.init()
font= font.Font(None, 70)
win= font.render('YOU WIN!', True, (255,215,0))
lose= font.render('YOU LOSE!',True,(255,0,0))
class GameSprite(sprite.Sprite):
    def __init__(self,player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image=transform.scale(image.load(player_image),(65, 65))
        self.speed= player_speed
        self.rect= self.image.get_rect()
        self.rect.x= player_x
        self.rect.y= player_y
    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed= key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 685:
            self.rect.y += self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 785:
            self.rect.x += self.speed
        if keys_pressed[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed

class Enemy(GameSprite):
    def update(self):
        #self.direction= 'left'
        if self.rect.x <= 600:
            self.direction = 'right'
        if self.rect.x >= 800:
            self.direction = 'left'
        if self.direction =='left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self,color,width,height,x,y):
        super().__init__()
        self.color = color
        self.width= width
        self.height= height
        self.image = Surface((self.width, self.height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x= x
        self.rect.y= y
    def draw_wall(self):
        mw.blit(self.image,(self.rect.x, self.rect.y))

mw=display.set_mode((850,750))
background=transform.scale(image.load('background.jpg'),(850,750))
display.set_caption('Maze')
FPS= 60
clock= time.Clock()
game= True
finish=False
mixer.music.play()
kick= mixer.Sound('kick.ogg')
player= Player('hero.png',50,600,5)
enemy= Enemy('cyborg.png',600,350,5)
treasure= GameSprite('treasure.png',700,600,0)
money= mixer.Sound('money.ogg')
wall1=Wall((13,252,142),15,500,150,40 )
wall2=Wall((13,252,142),15,500,300,200)
wall3=Wall((13,252,142),15,500,450,40)
wall4=Wall((13,252,142),15,500,600,200)
wall5=Wall((13,252,142),660,15,150,40)
wall6=Wall((13,252,142),660,15,150,700)
while game==True:
    for evente in event.get():
        if evente.type == QUIT:
            game = False

    if finish != True:
        mw.blit(background,(0,0))
        if sprite.collide_rect(player, treasure):
            mw.blit(win, (200,200))
            finish= True
            money.play()
        if sprite.collide_rect(player,enemy) or sprite.collide_rect(player,wall1) or sprite.collide_rect(player,wall2) or sprite.collide_rect(player,wall3) or sprite.collide_rect(player,wall4) or sprite.collide_rect(player,wall5) or sprite.collide_rect(player,wall6):
            mw.blit(lose, (200,200))
            finish=True
            kick.play()
        player.update()
        player.reset()
        enemy.update()
        enemy.reset()
        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        wall4.draw_wall()
        wall5.draw_wall()
        wall6.draw_wall()
        treasure.reset()
        
    display.update()       
    clock.tick(FPS)