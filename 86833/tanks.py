from pygame import *
x = 10
y = 10
x1 = 900
y1 = 900
BLACK = (0,0,0)
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= 15
            global y 
            y -= 15
        elif keys_pressed[K_s] and self.rect.y < 920:
            self.rect.y += 15
            y += 15
        elif keys_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= 15
            global x 
            x -= 15
        elif keys_pressed[K_d] and self.rect.x < 1800:
            self.rect.x += 15
            x += 15
    def shoot(self):
        bullet = Bullet('ener.png',x,y,20)
        bulls.add(bullet)
        bullets.append(bullet)
        
    def shoot2(self):
        bullet = Bullet('ener.png',x,y,20)
        bulls.add(bullet)
        bullets4.append(bullet)
 
    def shoot3(self):
        bullet = Bullet('ener.png',x,y,20)
        bulls.add(bullet)
        bullets2.append(bullet)

    def shoot4(self):
        bullet = Bullet('ener.png',x,y,20)
        bulls.add(bullet)
        bullets3.append(bullet)


class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        
    def update_2(self):
        self.rect.y -= self.speed
    
    def update_3(self):
        self.rect.x += self.speed
        
    def update_4(self):
        self.rect.x -= self.speed
        
class Walls(sprite.Sprite):
    def __init__(self,name,cor_x, cor_y ):
        super().__init__ ()
        self.image = transform.scale(image.load(name),(65,65))
        self.rect = self.image.get_rect()
        self.rect.x = cor_x
        self.rect.y = cor_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        

                

shooot = 'shot.jpg'
bulls = sprite.Group()
#bullets2 = sprite.Group()
#bullets3 = sprite.Group()
#bullets4 = sprite.Group()
f = 1
wallsg = sprite.Group()

bullets = []
bullets2 = []
bullets3 = []
bullets4 = []

sc = 0
rg = 0

rg1 = 0
game = True
clock = time.Clock()
FPS = 120
finish = False
w = 1900
h = 1000
top = 'tank_player_1_top.png'
down = 'tank_player_1_down.png'
left = 'tank_player_1_left.png'
right = 'tank_player_1_right.png'
#sv = 0
#top1 = 'top.png'
#down1 = 'down.png'
#left1 = 'left.png'
window = display.set_mode((w,h))
background = transform.scale(image.load('background1.jpg'),(w,h))
player_1 = Player(down,10,10,10)
wall1 = Walls('block.png',150,150)
wall2 = Walls('block.png',150,85)
wall3 = Walls('block.png',150,215)
wall4 = Walls('block.png',150,280)
wall5 = Walls('block.png',150,345)
wall6 = Walls('block.png',150,410)
wall7 = Walls('block.png',150,475)
wall8 = Walls('block.png',150,540)
wallsg.add(wall1)
wallsg.add(wall2)
wallsg.add(wall3)
wallsg.add(wall4)
wallsg.add(wall5)
wallsg.add(wall6)
wallsg.add(wall7)
wallsg.add(wall8)
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE and rg == 1:
                player_1.shoot4()
            if e.key == K_SPACE and rg == 2:
                player_1.shoot2()
            if e.key == K_SPACE and rg == 3:
                player_1.shoot()
            if e.key == K_SPACE and rg == 4:
                player_1.shoot3()
                
       
    if finish != True:
        window.blit(background,(0,0))
        player_1.reset()
        player_1.update()
        wallsg.draw(window)
        bulls.draw(window)
        for bul in bullets:
            if bul.rect.y >= -65 and bul.rect.y <= h + 65:
                bul.update()
            #bulls.add(bul)
        for bul in bullets2:
            if bul.rect.y >= -65 and bul.rect.y <= h + 65:
                bul.update_2()
            #bulls.add(bul)
        for bul in bullets3:
            if bul.rect.x >= -65 and bul.rect.x <= w + 65:
                bul.update_3()
            #bulls.add(bul)
        for bul in bullets4:
            if bul.rect.x >= -65 and bul.rect.x <= w + 65:
                bul.update_4()
            #bulls.add(bul) 
        collides = sprite.groupcollide(bulls, wallsg, True,True)
        
        if key.get_pressed()[K_w]:
            player_1 = Player(top,x,y,10)
            rg = 4

        if key.get_pressed()[K_s]:
            player_1 = Player(down,x,y,10)
            rg = 3

        if key.get_pressed()[K_a]:
            player_1 = Player(left,x,y,10)
            rg = 2   

        if key.get_pressed()[K_d]:
            player_1 = Player(right,x,y,10)
            rg = 1
        

        display.update()
    clock.tick(FPS)
