import pygame as pg
from settings import *
import os

###Developed by Lex Whalen, Jan 14 2020
###DISCLAIMER: This is by no means a political statement.
###I just wanted to learn a bit of pygame and I was interested in webscraping.
###So this is the result. I am NOT saying that Shinzo Abe should be held in a negative light.
###I include videos of him as I recently saw a video where he tries many fruits, and I thought it was funny
###He says "juicy" quite often.
###Link: https://www.youtube.com/watch?v=f7wQUOjSqhc&ab_channel=%E3%83%86%E3%83%AC%E6%9D%B1NEWS

class Pop_Same():

    def __init__(self,surf,start_x,end_y):
        self.SURF=surf
        self.FONT = pg.font.SysFont('comicsansmc',100)
        self.TEXT_SURF = self.FONT.render("Safe!",True,(0,0,255))
        self.TEXT_RECT = self.TEXT_SURF.get_rect()
        self.END_Y = end_y
        self.TEXT_RECT.centerx = start_x
        self.TEXT_RECT.bottom = WIN_HEIGHT + 100
        self.SPEEDY = -10
        self.SPEEDX = +10
        self.STOP = False

        
    def draw(self):
        self.SURF.blit(self.TEXT_SURF,self.TEXT_RECT)

    def update(self):
        if not self.STOP:
            if self.TEXT_RECT.y > self.END_Y:
                self.draw()
                self.TEXT_RECT.y += self.SPEEDY
            else:
                if self.TEXT_RECT.x < WIN_WIDTH + 100:
                    self.draw()
                    self.TEXT_RECT.x += self.SPEEDX
                else:
                    self.STOP = True

class Pop_Dec():

    def __init__(self,surf,start_x,end_y,num):
        self.SURF=surf
        self.FONT = pg.font.SysFont('comicsansmc',100)
        self.TEXT_SURF = self.FONT.render("Ouch! {}!".format(num),True,(255,0,0))
        self.TEXT_RECT = self.TEXT_SURF.get_rect()
        self.END_Y = end_y
        self.TEXT_RECT.centerx = start_x
        self.TEXT_RECT.bottom = WIN_HEIGHT + 100
        self.SPEEDY = -10
        self.SPEEDX = +10
        self.STOP = False

        
    def draw(self):
        self.SURF.blit(self.TEXT_SURF,self.TEXT_RECT)

    def update(self):
        if not self.STOP:
            if self.TEXT_RECT.y > self.END_Y:
                self.draw()
                self.TEXT_RECT.y += self.SPEEDY
            else:
                if self.TEXT_RECT.x < WIN_WIDTH + 100:
                    self.draw()
                    self.TEXT_RECT.x += self.SPEEDX
                else:
                    self.STOP = True
            
class Pop_Inc():

    def __init__(self,surf,start_x,end_y,num):
        self.SURF=surf
        self.FONT = pg.font.SysFont('comicsansmc',100)
        self.TEXT_SURF = self.FONT.render("Nice! +{}!".format(num),True,(0,255,0))
        self.TEXT_RECT = self.TEXT_SURF.get_rect()
        self.END_Y = end_y
        self.TEXT_RECT.centerx = start_x
        self.TEXT_RECT.bottom = WIN_HEIGHT + 100
        self.SPEEDY = -10
        self.SPEEDX = +10
        self.STOP = False

        
    def draw(self):
        self.SURF.blit(self.TEXT_SURF,self.TEXT_RECT)

    def update(self):
        if not self.STOP:
            if self.TEXT_RECT.y > self.END_Y:
                self.draw()
                self.TEXT_RECT.y += self.SPEEDY
            else:
                if self.TEXT_RECT.x < WIN_WIDTH + 100:
                    self.draw()
                    self.TEXT_RECT.x += self.SPEEDX
                else:
                    self.STOP = True

class Streak():

    def __init__(self,surf,start_x,end_y,text):
        self.SURF=surf
        self.FONT = pg.font.SysFont('comicsansmc',100)
        self.TEXT_SURF = self.FONT.render(text,True,(255,0,255))
        self.TEXT_RECT = self.TEXT_SURF.get_rect()
        self.END_Y = end_y
        self.TEXT_RECT.centerx = start_x
        self.TEXT_RECT.bottom = -100
        self.SPEEDY = 5
        self.SPEEDX = +8
        self.STOP = False

    def draw(self):
        self.SURF.blit(self.TEXT_SURF,self.TEXT_RECT)

    def update(self):
        if not self.STOP:
            if self.TEXT_RECT.y < self.END_Y:
                self.draw()
                self.TEXT_RECT.y += self.SPEEDY
            else:
                if self.TEXT_RECT.x < WIN_WIDTH + 100:
                    self.draw()
                    self.TEXT_RECT.x += self.SPEEDX
                else:
                    self.STOP = True
            
class Load_Screen():

    def __init__(self,surf,x,y):
        self.SURF = surf
        self.CWD = os.getcwd()
        self.IMGS = os.path.join(self.CWD,'imgs')
        self.IMG = os.path.join(self.IMGS,'flag.png')

        self.IMG = pg.image.load(self.IMG)
        self.IMG_RECT = self.IMG.get_rect()
        self.IMG_RECT.centerx = x
        self.IMG_RECT.centery = y

        text_A = 'Population Decline:'
        text_B = 'The Simulation!'

        color_A = (94, 3, 163)
        color_B = (255,0,102)


        self.FONT = pg.font.SysFont('comicsansmc',100)

        self.TEXT_A_SURF = self.FONT.render(text_A,True,color_A)
        self.TEXT_A_RECT = self.TEXT_A_SURF.get_rect()
        self.TEXT_A_RECT.centerx = x
        self.TEXT_A_RECT.centery = y

        self.TEXT_B_SURF = self.FONT.render(text_B,True,color_B)
        self.TEXT_B_RECT = self.TEXT_B_SURF.get_rect()
        self.TEXT_B_RECT.centerx = x
        self.TEXT_B_RECT.centery = y + 80

        self.SPEED_X = 5
        self.SPEED_Y = 5

    def draw(self):
        self.SURF.blit(self.IMG,self.IMG_RECT)
        self.SURF.blit(self.TEXT_A_SURF,self.TEXT_A_RECT)
        self.SURF.blit(self.TEXT_B_SURF,self.TEXT_B_RECT)
        

    def update(self):
        if not self.SURF.get_rect().contains(self.TEXT_A_RECT):
            self.SPEED_X *=-1

        if not self.SURF.get_rect().contains(self.IMG_RECT):
            self.SPEED_Y *=-1

        self.draw()
        self.TEXT_A_RECT.x += self.SPEED_X
        self.TEXT_B_RECT.x += self.SPEED_X
        self.IMG_RECT.y += self.SPEED_Y
        self.IMG_RECT.x += self.SPEED_X

class History_Dict:

    def __init__(self,surf,x,y,birth_num,death_num):
        self.SURF = surf
        self.x = x
        self.y = y
        self.BIRTH_NUM =birth_num
        self.DEATH_NUM = death_num

        self.FONT = pg.font.SysFont('comicsansmc',100)
        self.BIRTH_TEXT = self.FONT.render('Births: {}'.format(self.BIRTH_NUM),True,(255, 201, 5))
        self.DEATH_TEXT = self.FONT.render('Deaths: {}'.format(self.DEATH_NUM),True,(255, 201, 5))

        self.BIRTH_RECT = self.BIRTH_TEXT.get_rect()
        self.DEATH_RECT = self.DEATH_TEXT.get_rect()
        
        self.BIRTH_RECT.center = (x,y)
        self.DEATH_RECT.center = (x,y+100)

    def draw(self):
        self.SURF.blit(self.BIRTH_TEXT,self.BIRTH_RECT)
        self.SURF.blit(self.DEATH_TEXT,self.DEATH_RECT)

    def update(self):
        self.draw()

class Instructions():
    
    def __init__(self,surf,x,y):
        self.SURF = surf
        self.x = x
        self.y = y

        SAFE = 'Safe: Births = Deaths'
        NICE = 'Nice: Births > Deaths'
        OUCH = 'Ouch: Deaths > Births'

        self.FONT = pg.font.SysFont('comicsansmc',50)

        self.SAFE_TEXT = self.FONT.render(SAFE,True,(0,185,255))
        self.NICE_TEXT = self.FONT.render(NICE,True,(0,228,46))
        self.OUCH_TEXT = self.FONT.render(OUCH,True,(238,6,6))

        self.SAFE_RECT = self.SAFE_TEXT.get_rect()
        self.NICE_RECT = self.NICE_TEXT.get_rect()
        self.OUCH_RECT = self.OUCH_TEXT.get_rect()

        self.SAFE_RECT.center = (x,y)
        self.NICE_RECT.center = (x,y+50)
        self.OUCH_RECT.center = (x,y+100)

    def draw(self):
        self.SURF.blit(self.SAFE_TEXT,self.SAFE_RECT)
        self.SURF.blit(self.NICE_TEXT,self.NICE_RECT)
        self.SURF.blit(self.OUCH_TEXT,self.OUCH_RECT)

    def update(self):
        self.draw()

class Streak_Counter:

    def __init__(self,surf,x,y,safe,nice,ouch):
        self.SURF = surf
        self.x = x
        self.y = y

        self.SAFE = safe
        self.NICE = nice
        self.OUCH = ouch

        self.FONT = pg.font.SysFont('comicsansmc',75)

        self.SAFE_TEXT = self.FONT.render('Safe! streak: {}'.format(self.SAFE),True,(1, 126, 203 ))
        self.NICE_TEXT = self.FONT.render('Nice! streak: {}'.format(self.NICE),True,(3, 178, 24 ))
        self.OUCH_TEXT = self.FONT.render('Ouch! streak: {}'.format(self.OUCH),True,(198, 0, 0 ))

        self.SAFE_RECT = self.SAFE_TEXT.get_rect()
        self.NICE_RECT = self.NICE_TEXT.get_rect()
        self.OUCH_RECT = self.OUCH_TEXT.get_rect()

        self.SAFE_RECT.center = (x,y)
        self.NICE_RECT.center = (x,y+50)
        self.OUCH_RECT.center = (x,y+100)

    def draw(self):
        self.SURF.blit(self.SAFE_TEXT,self.SAFE_RECT)
        self.SURF.blit(self.NICE_TEXT,self.NICE_RECT)
        self.SURF.blit(self.OUCH_TEXT,self.OUCH_RECT)

    def update(self):
        self.draw()