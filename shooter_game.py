#Создай собственный Шутер!


from pygame import * 
from random import randint
from time import time as timer 
window=display.set_mode((1000,700)) 
display.set_caption('Deep Rock Galactic') 
clock=time.Clock() 
fon=transform.scale(image.load('galaxy.jpg'),(1000,700))

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire_music = mixer.Sound('fire.ogg')
font.init()
font = font.SysFont('Arial',35)
score = 0
miss = 0
class drg(sprite.Sprite):
    def __init__(self,hero_image,hero_x,hero_y,size_x,size_y,hero_speed):
        super().__init__()
        self.image=transform.scale(image.load(hero_image),(size_x,size_y))
        self.rect=self.image.get_rect()
        self.rect.x=hero_x
        self.rect.y=hero_y

        self.speed=hero_speed
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class hhhh(drg):
    def control(self):
        control = key.get_pressed()
        if control[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if control[K_d] and self.rect.x < 920:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet('bullet.png',self.rect.x+50,self.rect.y,15,20,15)
        Bullets.add(bullet)
class Enemy(drg):
    def update(self):
        self.rect.y +=self.speed
        global miss
        if self.rect.y>700:
            miss += 1
            self.rect.y = 0
            self.rect.x = randint(0,920)
class Enemy_1(drg):
    def update(self):
        self.rect.y +=self.speed
        if self.rect.y>700:
            self.rect.y = 0
            self.rect.x = randint(0,920)
class Bullet(drg):
    def update(self):
        self.rect.y -=self.speed
        if self.rect.y <0:
            self.kill()
game = True
Finish = False
clock = time.Clock()
scout = hhhh('rocket.png',460,600,80,100,10)
asteroids = sprite.Group()
for i in range(1,3):
    asteroid = Enemy_1('asteroid.png',randint(80,920),0,80,80,randint(1,3))
    asteroids.add(asteroid)
monsters = sprite.Group()
Bullets = sprite.Group()
for i in range(1,5):
    monster = Enemy('ufo.png',randint(0,920),0,80,80,randint(2,7))
    monsters.add(monster)
kol_bullets = 0
r = False
while  game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                if kol_bullets <= 5 and r == False :
                    kol_bullets += 1
                    fire_music.play()
                    scout.fire()
                if kol_bullets >= 5 and r == False:
                    start_t = timer() 
                    r = True
    if Finish !=True:
        window.blit(fon,(0,0))
        score_text = font.render('Счет:'+str(score),True,(255,255,255))
        miss_text = font.render('Пропуски:'+str(miss),True,(255,255,255))
        window.blit(score_text,(10,10))
        window.blit(miss_text,(10,55))
        scout.reset()
        scout.control()
        monsters.draw(window)
        monsters.update()
        Bullets.draw(window)
        Bullets.update()
        asteroids.draw(window)
        asteroids.update()
        if r == True:
            end_t = timer()
            if end_t-start_t < 2:
                text_r = font.render('перезардка ',True,(255,255,255))
                window.blit(text_r,(500,350))
            else:
                r = False
                kol_bullets = 0
        if sprite.spritecollide(scout,monsters,False) or sprite.spritecollide(scout,asteroids,False)or miss>=5:
            Finish = True
            text_lose = font.render('украине так же конец ',True,(255,255,255))
            window.blit(text_lose,(500,350))
        piu = sprite.groupcollide(Bullets,monsters,True,True)
        for i in piu:
            score  +=1
            monster = Enemy('ufo.png',randint(80,920),0,80,80,randint(1,5))
            monsters.add(monster)
        if score >=50:
            Finish=True
            text_win = font.render('ТЫ РУССКИЙ!!! ',True,(255,255,255))
            window.blit(text_цшт,(500,350))


        display.update()
    clock.tick(60)