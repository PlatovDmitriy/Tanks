from pygame import *
from time import time as timer
x = 10
y = 10
x1 = 900
y1 = 900
font.init()
font1 = font.SysFont('Arial',75)
font2 = font.SysFont('Arial',30)
#BLACK = (0,0,0)
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, x_speed,y_speed):#добавила скорость по x и по y
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65,65))
        self.x_speed = x_speed #добавила скорость по x и по y
        self.y_speed = y_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        #движение по горизонтали
        self.rect.x += self.x_speed
        platforms_touched = sprite.spritecollide(self, wallsg, False)
        
        if self.x_speed > 0:
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left)
            
        elif self.x_speed < 0:
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right)
        platforms_touched2 = sprite.spritecollide(self, wscrg, False)
        if self.x_speed > 0:
            for p in platforms_touched2:
                self.rect.right = min(self.rect.right, p.rect.left)
            
        elif self.x_speed < 0:
            for p in platforms_touched2:
                self.rect.left = max(self.rect.left, p.rect.right)
        platforms_touched3 = sprite.spritecollide(self, wallsg2, False)
        if self.x_speed > 0:
            for p in platforms_touched3:
                self.rect.right = min(self.rect.right, p.rect.left)
            
        elif self.x_speed < 0:
            for p in platforms_touched3:
                self.rect.left = max(self.rect.left, p.rect.right)
        #движение по вертикали
        self.rect.y += self.y_speed    
        platforms_touched = sprite.spritecollide(self, wallsg, False)
        
        if self.y_speed > 0:
            for p in platforms_touched:
                self.rect.bottom = min(self.rect.bottom, p.rect.top)
        elif self.y_speed < 0:
            for p in platforms_touched:
                self.rect.top = max(self.rect.top, p.rect.bottom)
        platforms_touched2 = sprite.spritecollide(self, wscrg, False)
        if self.y_speed > 0:
            for p in platforms_touched2:
                self.rect.bottom = min(self.rect.bottom, p.rect.top)
        elif self.y_speed < 0:
            for p in platforms_touched2:
                self.rect.top = max(self.rect.top, p.rect.bottom)
        platforms_touched3 = sprite.spritecollide(self, wallsg2, False)
        if self.y_speed > 0:
            for p in platforms_touched3:
                self.rect.bottom = min(self.rect.bottom, p.rect.top)
        elif self.y_speed < 0:
            for p in platforms_touched3:
                self.rect.top = max(self.rect.top, p.rect.bottom)
    def shoot(self):
        bullet = Bullet('ener.png',self.rect.x,self.rect.y,30,30)
        bulls.add(bullet)
        bullets.append(bullet)
        
    def shoot2(self):
        bullet = Bullet('ener.png',self.rect.x,self.rect.y,30,30)
        bulls.add(bullet)
        bullets4.append(bullet)
 
    def shoot3(self):
        bullet = Bullet('ener.png',self.rect.x,self.rect.y,30,30)
        bulls.add(bullet)
        bullets2.append(bullet)

    def shoot4(self):
        bullet = Bullet('ener.png',self.rect.x,self.rect.y,30,30)
        bulls.add(bullet)
        bullets3.append(bullet)


class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.y_speed
        
    def update_2(self):
        self.rect.y -= self.y_speed
    
    def update_3(self):
        self.rect.x += self.x_speed
        
    def update_4(self):
        self.rect.x -= self.x_speed
class Player2(GameSprite):
    def update_45(self):
        self.rect.x += self.x_speed
        platforms_touched = sprite.spritecollide(self, wallsg, False)
        
        if self.x_speed > 0:
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left)
            
        elif self.x_speed < 0:
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right)
        platforms_touched2 = sprite.spritecollide(self, wscrg, False)
        if self.x_speed > 0:
            for p in platforms_touched2:
                self.rect.right = min(self.rect.right, p.rect.left)
            
        elif self.x_speed < 0:
            for p in platforms_touched2:
                self.rect.left = max(self.rect.left, p.rect.right)
        platforms_touched3 = sprite.spritecollide(self, wallsg2, False)
        if self.x_speed > 0:
            for p in platforms_touched3:
                self.rect.right = min(self.rect.right, p.rect.left)
            
        elif self.x_speed < 0:
            for p in platforms_touched3:
                self.rect.left = max(self.rect.left, p.rect.right)
        #движение по вертикали
        self.rect.y += self.y_speed    
        platforms_touched = sprite.spritecollide(self, wallsg, False)
        
        if self.y_speed > 0:
            for p in platforms_touched:
                self.rect.bottom = min(self.rect.bottom, p.rect.top)
        elif self.y_speed < 0:
            for p in platforms_touched:
                self.rect.top = max(self.rect.top, p.rect.bottom)
        platforms_touched2 = sprite.spritecollide(self, wscrg, False)
        if self.y_speed > 0:
            for p in platforms_touched2:
                self.rect.bottom = min(self.rect.bottom, p.rect.top)
        elif self.y_speed < 0:
            for p in platforms_touched2:
                self.rect.top = max(self.rect.top, p.rect.bottom)
        platforms_touched3 = sprite.spritecollide(self, wallsg2, False)
        if self.y_speed > 0:
            for p in platforms_touched3:
                self.rect.bottom = min(self.rect.bottom, p.rect.top)
        elif self.y_speed < 0:
            for p in platforms_touched3:
                self.rect.top = max(self.rect.top, p.rect.bottom)
    def shoot_2(self):
        bullet2 = Bullet2('ener.png',self.rect.x,self.rect.y,30,30)
        bulls2.add(bullet2)
        bullets_2.append(bullet2)
        
    def shoot2_2(self):
        bullet2 = Bullet2('ener.png',self.rect.x,self.rect.y,30,30)
        bulls2.add(bullet2)
        bullets4_2.append(bullet2)
 
    def shoot3_2(self):
        bullet2 = Bullet2('ener.png',self.rect.x,self.rect.y,30,30)
        bulls2.add(bullet2)
        bullets2_2.append(bullet2)

    def shoot4_2(self):
        bullet2 = Bullet2('ener.png',self.rect.x,self.rect.y,30,30)
        bulls2.add(bullet2)
        bullets3_2.append(bullet2)


class Bullet2(GameSprite):
    def update_2(self):
        self.rect.y += self.y_speed
        
    def update_2_2(self):
        self.rect.y -= self.y_speed
    
    def update_3_2(self):
        self.rect.x += self.x_speed
        
    def update_4_2(self):
        self.rect.x -= self.x_speed


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
bulls2 = sprite.Group()

#bullets2 = sprite.Group()
#bullets3 = sprite.Group()
#bullets4 = sprite.Group()
f = 1
wallsg = sprite.Group()
wscrg = sprite.Group()
wallsg2 = sprite.Group()

bullets = []
bullets2 = []
bullets3 = []
bullets4 = []
bullets_2 = []
bullets2_2 = []
bullets3_2 = []
bullets4_2 = []
sc = 0
rg = 0
rec_time = False
num_fire = 0
rg1 = 0
rec_time2 = False
num_fire2 = 0
game = True
clock = time.Clock()
FPS = 120
finish = True
start = False
w = 1900
h = 1000
health = 10
health2 = 10
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
background2 = transform.scale(image.load('background2_menu.png'),(w,h))
player_1 = Player(down,-500,-1000,0,0) #сюда добавили обе скорости по 0
player_2 = Player2('down.png',-500,-500,0,0)

wall1 = Walls('block.png',65,0)
wall2 = Walls('block.png',130,0)
wall3 = Walls('block.png',195,0)
wall4 = Walls('block.png',260,0)
wall5 = Walls('block.png',325,0)
wall6 = Walls('block.png',390,0)
wall7 = Walls('block.png',65,65)
wall8 = Walls('block.png',130,65)
wall9 = Walls('block.png',195,65)
wall10 = Walls('block.png',260,65)
wall11 = Walls('block.png',325,65)
wall12 = Walls('block.png',390,65)

wall1_1 = Walls('iron_block.png',455,130)
wall2_1 = Walls('iron_block.png',520,130)
wall3_1 = Walls('iron_block.png',585,130)
wall4_1 = Walls('iron_block.png',650,130)
wall5_1 = Walls('iron_block.png',715,130)
wall6_1 = Walls('iron_block.png',780,130)
wall7_1 = Walls('iron_block.png',845,130)
wall8_1 = Walls('iron_block.png',910,130)
wall9_1 = Walls('iron_block.png',975,130)
wall1_2 = Walls('iron_block.png',455,195)
wall2_2 = Walls('iron_block.png',520,195)
wall3_2 = Walls('iron_block.png',585,195)
wall4_2 = Walls('iron_block.png',650,195)
wall5_2 = Walls('iron_block.png',715,195)
wall6_2 = Walls('iron_block.png',780,195)
wall7_2 = Walls('iron_block.png',845,195)
wall8_2 = Walls('iron_block.png',910,195)
wall9_2 = Walls('iron_block.png',975,195)
wall1_3 = Walls('iron_block.png',455,260)
wall2_3 = Walls('iron_block.png',520,260)
wall1_4 = Walls('iron_block.png',455,325)
wall2_4 = Walls('iron_block.png',520,325)

wallw1 = Walls('water.png',1040,130)
wallw2 = Walls('water.png',1105,130)
wallw3 = Walls('water.png',1170,130)
wallw4 = Walls('water.png',1235,130)
wallw1_2 = Walls('water.png',1040,195)
wallw2_2 = Walls('water.png',1105,195)
wallw3_2 = Walls('water.png',1170,195)
wallw4_2 = Walls('water.png',1235,195)

wallw1_3 = Walls('water.png',325,260)
wallw2_3 = Walls('water.png',390,260)
wallw1_4 = Walls('water.png',325,325)
wallw2_4 = Walls('water.png',390,325)
wallw1_5 = Walls('water.png',325,390)
wallw2_5 = Walls('water.png',390,390)
wallw1_6 = Walls('water.png',325,455)
wallw2_6 = Walls('water.png',390,455)

block1 = Walls('block.png',1770,935) 
block2 = Walls('block.png',1705,935) 
block3 = Walls('block.png',1640,935) 
block4 = Walls('block.png',1575,935) 
block5 = Walls('block.png',1510,935) 
block6 = Walls('block.png',1445,935) 
block7 = Walls('block.png',1770,870) 
block8 = Walls('block.png',1705,870) 
block9 = Walls('block.png',1640,870) 
block10 = Walls('block.png',1575,870) 
block11 = Walls('block.png',1510,870) 
block12 = Walls('block.png',1445,870) 

iron_block = Walls('iron_block.png',1380,805)
iron_block2 = Walls('iron_block.png',1315,805)
iron_block3 = Walls('iron_block.png',1250,805)
iron_block4 = Walls('iron_block.png',1185,805)
iron_block5 = Walls('iron_block.png',1120,805)
iron_block6 = Walls('iron_block.png',1055,805)
iron_block7 = Walls('iron_block.png',990,805)
iron_block8 = Walls('iron_block.png',925,805)
iron_block9 = Walls('iron_block.png',860,805)
iron_block10 = Walls('iron_block.png',1380,740)
iron_block11 = Walls('iron_block.png',1315,740)
iron_block12 = Walls('iron_block.png',1250,740)
iron_block13 = Walls('iron_block.png',1185,740)
iron_block14 = Walls('iron_block.png',1120,740)
iron_block15 = Walls('iron_block.png',1055,740)
iron_block16 = Walls('iron_block.png',990,740)
iron_block17 = Walls('iron_block.png',925,740)
iron_block18 = Walls('iron_block.png',860,740)
iron_block1_2= Walls('iron_block.png',1380,675)
iron_block2_2 = Walls('iron_block.png',1315,675)
iron_block1_3 = Walls('iron_block.png',1380,610)
iron_block2_3 = Walls('iron_block.png',1315,610)



water_block = Walls('water.png',795,740)
water_block2 = Walls('water.png',795,805)
water_block3 = Walls('water.png',730,740)
water_block4 = Walls('water.png',730,805)
water_block5 = Walls('water.png',665,740)
water_block6 = Walls('water.png',665,805)
water_block7 = Walls('water.png',600,740)
water_block8 = Walls('water.png',600,805)

water_block1_2 = Walls('water.png',1510,675)
water_block2_2 = Walls('water.png',1445,675)
water_block1_3 = Walls('water.png',1510,610)
water_block2_3 = Walls('water.png',1445,610)
water_block1_4 = Walls('water.png',1510,545)
water_block2_4 = Walls('water.png',1445,545)
water_block1_5 = Walls('water.png',1510,480)
water_block2_5 = Walls('water.png',1445,480)



wscrg.add(water_block1_2)
wscrg.add(water_block2_2)
wscrg.add(water_block1_3)
wscrg.add(water_block2_3)
wscrg.add(water_block1_4)
wscrg.add(water_block2_4)
wscrg.add(water_block1_5)
wscrg.add(water_block2_5)

wscrg.add(water_block)
wscrg.add(water_block2)
wscrg.add(water_block3)
wscrg.add(water_block4)
wscrg.add(water_block5)
wscrg.add(water_block6)
wscrg.add(water_block7)
wscrg.add(water_block8)


wallsg2.add(iron_block)
wallsg2.add(iron_block2)
wallsg2.add(iron_block3)
wallsg2.add(iron_block4)
wallsg2.add(iron_block5)
wallsg2.add(iron_block6)
wallsg2.add(iron_block7)
wallsg2.add(iron_block8)
wallsg2.add(iron_block9)
wallsg2.add(iron_block10)
wallsg2.add(iron_block11)
wallsg2.add(iron_block12)
wallsg2.add(iron_block13)
wallsg2.add(iron_block14)
wallsg2.add(iron_block15)
wallsg2.add(iron_block16)
wallsg2.add(iron_block17)
wallsg2.add(iron_block18)
wallsg2.add(iron_block1_2)
wallsg2.add(iron_block2_2)
wallsg2.add(iron_block1_3)
wallsg2.add(iron_block2_3)


wallsg.add(block1)
wallsg.add(block2)
wallsg.add(block3)
wallsg.add(block4)
wallsg.add(block5)
wallsg.add(block6)
wallsg.add(block7)
wallsg.add(block8)
wallsg.add(block9)
wallsg.add(block10)
wallsg.add(block11)
wallsg.add(block12)



wallsg.add(wall1)
wallsg.add(wall2)
wallsg.add(wall3)
wallsg.add(wall4)
wallsg.add(wall5)
wallsg.add(wall6)
wallsg.add(wall7)
wallsg.add(wall8)
wallsg.add(wall9)
wallsg.add(wall10)
wallsg.add(wall11)
wallsg.add(wall12)

wallsg2.add(wall1_1)
wallsg2.add(wall2_1)
wallsg2.add(wall3_1)
wallsg2.add(wall4_1)
wallsg2.add(wall5_1)
wallsg2.add(wall6_1)
wallsg2.add(wall7_1)
wallsg2.add(wall8_1)
wallsg2.add(wall9_1)
wallsg2.add(wall1_2)
wallsg2.add(wall2_2)
wallsg2.add(wall3_2)
wallsg2.add(wall4_2)
wallsg2.add(wall5_2)
wallsg2.add(wall6_2)
wallsg2.add(wall7_2)
wallsg2.add(wall8_2)
wallsg2.add(wall9_2)
wallsg2.add(wall1_3)
wallsg2.add(wall2_3)
wallsg2.add(wall1_4)
wallsg2.add(wall2_4)

wscrg.add(wallw1)
wscrg.add(wallw2)
wscrg.add(wallw3)
wscrg.add(wallw4)
wscrg.add(wallw1_2)
wscrg.add(wallw2_2)
wscrg.add(wallw3_2)
wscrg.add(wallw4_2)
wscrg.add(wallw1_3)
wscrg.add(wallw2_3)
wscrg.add(wallw1_4)
wscrg.add(wallw2_4)
wscrg.add(wallw1_5)
wscrg.add(wallw2_5)
wscrg.add(wallw1_6)
wscrg.add(wallw2_6)


ws1 = 0
ws2 = 0
ws3 = 0
ws4 = 0
theal = 1
t2heal = 1
for i in range(30):
    wallscr = Walls('block.png',0+ws1,1000)
    wscrg.add(wallscr)
    ws1 += 65
for i in range(16):
    wallscr = Walls('block.png',1900,0+ws2)
    wscrg.add(wallscr)
    ws2 += 65
for i in range(30):
    wallscr = Walls('block.png',0+ws3,-65)
    wscrg.add(wallscr)
    ws3 += 65
for i in range(16):
    wallscr = Walls('block.png',-65,0+ws4)
    wscrg.add(wallscr)
    ws4 += 65




player_1_tank = 0
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                if num_fire < 1 and rec_time == False:
                    num_fire += 1
                    if e.key == K_SPACE and rg == 1:
                        player_1.shoot4()
                    elif e.key == K_SPACE and rg == 2:
                        player_1.shoot2()
                    elif e.key == K_SPACE and rg == 3:
                        player_1.shoot()
                    elif e.key == K_SPACE and rg == 4:
                        player_1.shoot3()
            if e.key == K_RSHIFT:
                if num_fire2 < 1 and rec_time2 == False:
                    num_fire2 += 1
                    if e.key == K_RSHIFT and sc == 1:
                        player_2.shoot4_2()
                    elif e.key == K_RSHIFT and sc == 2:
                        player_2.shoot2_2()
                    elif e.key == K_RSHIFT and sc == 3:
                        player_2.shoot_2()
                    elif e.key == K_RSHIFT and sc == 4:
                        player_2.shoot3_2()
                if num_fire2 >= 1 and rec_time2 == False:
                    last_time2 = timer()
                    rec_time2 = True
        #движение теперь вот тут        
            if e.key == K_a and player_1_tank == 1:
                player_1.x_speed = -15
                player_1.image = transform.scale(image.load(left),(65,65))
                rg = 2
            elif e.key == K_d and player_1_tank == 1:
                player_1.x_speed = 15
                player_1.image = transform.scale(image.load(right),(65,65))
                rg = 1
            elif e.key == K_w and player_1_tank == 1:
                player_1.y_speed = -15
                player_1.image = transform.scale(image.load(top),(65,65))
                rg = 4
            elif e.key == K_s and player_1_tank == 1:
                player_1.y_speed = 15
                player_1.image = transform.scale(image.load(down),(65,65))
                rg = 3
            elif e.key == K_LEFT and player_2_tank == 1:
                player_2.x_speed = -5
                player_2.image = transform.scale(image.load('left.png'),(65,65))
                sc = 2
            elif e.key == K_RIGHT and player_2_tank == 1:
                player_2.x_speed = 5
                player_2.image = transform.scale(image.load('right.png'),(65,65))
                sc = 1
            elif e.key == K_UP and player_2_tank == 1:
                player_2.y_speed = -5
                player_2.image = transform.scale(image.load('top.png'),(65,65))
                sc = 4
            elif e.key == K_DOWN and player_2_tank == 1:
                player_2.y_speed = 5
                player_2.image = transform.scale(image.load('down.png'),(65,65))
                sc = 3
            elif e.key == K_a and player_1_tank == 2:
                player_1.x_speed = -5
                player_1.image = transform.scale(image.load('left.png'),(65,65))
                rg = 2
            elif e.key == K_d and player_1_tank == 2:
                player_1.x_speed = 5
                player_1.image = transform.scale(image.load('right.png'),(65,65))
                rg = 1
            elif e.key == K_w and player_1_tank == 2:
                player_1.y_speed = -5
                player_1.image = transform.scale(image.load('top.png'),(65,65))
                rg = 4
            elif e.key == K_s and player_1_tank == 2:
                player_1.y_speed = 5
                player_1.image = transform.scale(image.load('down.png'),(65,65))
                rg = 3
            elif e.key == K_LEFT and player_2_tank == 2:
                player_2.x_speed = -15
                player_2.image = transform.scale(image.load(left),(65,65))
                sc = 2
            elif e.key == K_RIGHT and player_2_tank == 2:
                player_2.x_speed = 15
                player_2.image = transform.scale(image.load(right),(65,65))
                sc = 1
            elif e.key == K_UP and player_2_tank == 2:
                player_2.y_speed = -15
                player_2.image = transform.scale(image.load(top),(65,65))
                sc = 4
            elif e.key == K_DOWN and player_2_tank == 2:
                player_2.y_speed = 15
                player_2.image = transform.scale(image.load(down),(65,65))
                sc = 3
        elif e.type == KEYUP:
            if e.key == K_a:
                player_1.x_speed = 0
            elif e.key == K_d:
                player_1.x_speed = 0
            elif e.key == K_w:
                player_1.y_speed = 0
            elif e.key == K_s:
                player_1.y_speed = 0
        
            if num_fire >= 1 and rec_time == False:
                    last_time = timer()
                    rec_time = True 

        
        
            elif e.type == KEYUP:
                if e.key == K_LEFT:
                    player_2.x_speed = 0
                elif e.key == K_RIGHT:
                    player_2.x_speed = 0
                elif e.key == K_UP:
                    player_2.y_speed = 0
                elif e.key == K_DOWN:
                    player_2.y_speed = 0      
    if start != True:
        window.blit(background2,(0,0))
        if key.get_pressed()[K_s]:
            player_1_tank = 2
            player_1 = Player('down.png',0,0,0,0)
        if key.get_pressed()[K_d]:
            player_1_tank = 1
            player_1 = Player(down,0,0,0,0)
        if key.get_pressed()[K_i]:
            player_2_tank = 1
            player_2 = Player2('down.png',1835,935,0,0)
        if key.get_pressed()[K_p]:
            player_2_tank = 2
            player_2 = Player2(down,1835,935,0,0)
        if key.get_pressed()[K_l]: 
            start = True
            finish = False
        
    if finish != True:
        window.blit(background,(0,0))
        player_1.reset()
        player_1.update()
        player_2.update_45()
        player_2.reset()
        wallsg.draw(window)
        wscrg.draw(window)
        wallsg2.draw(window)
        bulls.draw(window)
        bulls2.draw(window)
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
        
        for bult in bullets_2:
            if bult.rect.y >= -65 and bult.rect.y <= h + 65:
                bult.update_2()
            #bulls.add(bul)
        for bult in bullets2_2:
            if bult.rect.y >= -65 and bult.rect.y <= h + 65:
                bult.update_2_2()
            #bulls.add(bul)
        for bult in bullets3_2:
            if bult.rect.x >= -65 and bult.rect.x <= w + 65:
                bult.update_3_2()
            #bulls.add(bul)
        for bult in bullets4_2:
            if bult.rect.x >= -65 and bult.rect.x <= w + 65:
                bult.update_4_2()
            #bulls.add(bul) 
        
        if rec_time == True:
            now_time = timer()
            if now_time - last_time < 1.5:
                pass
            else:
                num_fire = 0
                rec_time = False
        if rec_time2 == True:
            now_time2 = timer()
            if now_time2 - last_time2 < 1.5:
                pass
            else:
                num_fire2 = 0
                rec_time2 = False
        collides = sprite.groupcollide(bulls, wallsg, True,True)
        collides2 = sprite.groupcollide(bulls2, wallsg, True,True)
        collides3 = sprite.groupcollide(bulls2, wallsg2, True,False)
        collides4 = sprite.groupcollide(bulls, wallsg2, True,False)
        sprites_list3 = sprite.groupcollide(bulls,bulls2,True,True)
        if player_1_tank == 2 and theal == 1:
            health = 2
            theal = 0
        if player_1_tank == 1 and theal == 1:
            health = 1
            theal = 0
        if player_2_tank == 1 and t2heal == 1:
            health2 = 2
            t2heal = 0
        if player_2_tank == 2 and t2heal == 1:
            health2 = 1
            t2heal = 0
        if sprite.spritecollide(player_2,bulls,True):
            health2 -= 1
        if sprite.spritecollide(player_1,bulls2,True):
            health -= 1
        if health <=0:
            text_player2_win = font1.render('Player2 WIN',1,(0,200,200)) 
            window.blit(text_player2_win,(720,460))
            finish = True
        if health2 <=0:
            text_player1_win = font1.render('Player1 WIN',1,(0,200,200)) 
            window.blit(text_player1_win,(720,460))
            finish = True
        if health == 2:
            text_life = font2.render('2',1,(255,255,0)) 
            window.blit(text_life,(5,960))
        if health == 1:
            text_life = font2.render('1',1,(255,0,0)) 
            window.blit(text_life,(5,960))
        if health2 == 2:
            text_life = font2.render('2',1,(255,255,0)) 
            window.blit(text_life,(1870,960))
        if health2 == 1:
            text_life = font2.render('1',1,(255,0,0)) 
            window.blit(text_life,(1870,960))
        

    display.update() 
    clock.tick(FPS)
