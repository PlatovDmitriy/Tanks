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
flag = 0
#sv = 0
#top1 = 'top.png'
#down1 = 'down.png'
#left1 = 'left.png'
window = display.set_mode((w,h))
background = transform.scale(image.load('background1.jpg'),(w,h))
background2 = transform.scale(image.load('background2_menu.png'),(w,h))
player_1 = Player(down,-500,-1000,0,0) #сюда добавили обе скорости по 0
player_2 = Player2('down.png',-500,-500,0,0)
wall = Walls('block.png',150,20)
wall1 = Walls('block.png',150,85)
wall2 = Walls('block.png',150,150)
wall3 = Walls('block.png',150,215)
wall4 = Walls('block.png',150,280)
wall5 = Walls('block.png',150,345)
wall6 = Walls('block.png',150,410)
wall7 = Walls('block.png',150,475)
wall8 = Walls('block.png',150,540)
wall9 = Walls('block.png',150,605)
wall10 = Walls('block.png',150,670)
wall11 = Walls('block.png',150,735)
wall12 = Walls('block.png',150,800)
wall13 = Walls('block.png',150,865)
wall14 = Walls('block.png',150,930)
wall15 = Walls('block.png',150,995)

wall_2 = Walls('block.png',215,20)
wall1_2 = Walls('block.png',215,85)
wall2_2 = Walls('block.png',215,150)
wall3_2 = Walls('block.png',215,215)
wall4_2 = Walls('block.png',215,280)
wall5_2 = Walls('block.png',215,345)
wall6_2 = Walls('block.png',215,410)
wall7_2 = Walls('block.png',215,475)
wall8_2 = Walls('block.png',215,540)
wall9_2 = Walls('block.png',215,605)
wall10_2 = Walls('block.png',215,670)
wall11_2 = Walls('block.png',215,735)
wall12_2 = Walls('block.png',215,800)
wall13_2 = Walls('block.png',215,865)
wall13_2 = Walls('block.png',215,865)
wall14_2 = Walls('block.png',215,930)
wall15_2 = Walls('block.png',215,995)


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
wallsg.add(wall)
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
wallsg.add(wall13)
wallsg.add(wall14)
wallsg.add(wall15)

wallsg.add(wall_2)
wallsg.add(wall1_2)
wallsg.add(wall2_2)
wallsg.add(wall3_2)
wallsg.add(wall4_2)
wallsg.add(wall5_2)
wallsg.add(wall6_2)
wallsg.add(wall7_2)
wallsg.add(wall8_2)
wallsg.add(wall9_2)
wallsg.add(wall10_2)
wallsg.add(wall11_2)
wallsg.add(wall12_2)
wallsg.add(wall13_2)
wallsg.add(wall14_2)
wallsg.add(wall15_2)

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
            if e.key == K_a:# and player_1_tank == 1:
                flag = 1
            if flag == 1 and flag != 2 and flag != 3 and flag != 4:
                player_1.x_speed = -15
                player_1.image = transform.scale(image.load(left),(65,65))
                rg = 2
            if e.key == K_d:# and player_1_tank == 1:
                flag = 2
            if flag == 2 and flag != 1 and flag != 3 and flag != 4:
                player_1.x_speed = 15
                player_1.image = transform.scale(image.load(right),(65,65))
                rg = 1
            if e.key == K_w:# and player_1_tank == 1:
                flag = 3
            if flag == 3 and flag != 1 and flag != 2 and flag != 4:
                player_1.y_speed = -15
                player_1.image = transform.scale(image.load(top),(65,65))
                rg = 4
            if e.key == K_s:# and# player_1_tank == 1:
                flag = 4
            if flag == 4 and flag != 1 and flag != 2 and flag != 3:
                player_1.y_speed = 15
                player_1.image = transform.scale(image.load(down),(65,65))
                rg = 3
            if e.key == K_LEFT and player_2_tank == 1:
                player_2.x_speed = -5
                player_2.image = transform.scale(image.load('left.png'),(65,65))
                sc = 2
            if e.key == K_RIGHT and player_2_tank == 1:
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

            #танк не должен двигаться по диагонали(НЕ ПОЛУЧАЕТСЯ!!!!!!!!!!!!!)
                
        elif e.type == KEYUP:
            if e.key == K_a:
                player_1.x_speed = 0
                #flag = 0
            if e.key == K_d:
                player_1.x_speed = 0
                #flag = 0
            if e.key == K_w:
                player_1.y_speed = 0
                #flag = 0
            if e.key == K_s:
                player_1.y_speed = 0
                #flag = 0
        
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
            player_1 = Player('down.png',10,10,0,0)
        if key.get_pressed()[K_d]:
            player_1_tank = 1
            player_1 = Player(down,1800,10,0,0)
        if key.get_pressed()[K_i]:
            player_2_tank = 1
            player_2 = Player2('down.png',1700,900,0,0)
        if key.get_pressed()[K_p]:
            player_2_tank = 2
            player_2 = Player2(down,1700,900,0,0)
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
