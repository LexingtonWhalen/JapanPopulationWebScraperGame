import numpy as np
import pandas as pd
import pygame as pg
import threading
import time
import os

from scraper import Scraper
import signal
from settings import *
from abe_player import AbePlayer
from sprites import Pop_Same,Pop_Dec,Pop_Inc,Streak,Load_Screen,History_Dict,Instructions,Streak_Counter

###Developed by Lex Whalen, Jan 14 2020
###DISCLAIMER: This is by no means a political statement.
###I just wanted to learn a bit of pygame and I was interested in webscraping.
###So this is the result. I am NOT saying that Shinzo Abe should be held in a negative light.
###I include videos of him as I recently saw a video where he tries many fruits, and I thought it was funny
###He says "juicy" quite often.
###Link: https://www.youtube.com/watch?v=f7wQUOjSqhc&ab_channel=%E3%83%86%E3%83%AC%E6%9D%B1NEWS

class Display():

    def __init__(self):
        self.CWD = os.getcwd()
        self.ABE_PLAYER = AbePlayer()
        self.AUDIO_FLDR = os.path.join(self.CWD,'audio')
        self.RUN = True
        self.SCRAPER = Scraper()

        pg.init()
        pg.mixer.init()
        pg.mixer.set_num_channels(8)
        self.INTRO_CHANNEL = pg.mixer.Channel(1)

        self.START_SND = os.path.join(self.AUDIO_FLDR,'race_start.mp3')
        self.MAIN_THEME = os.path.join(self.AUDIO_FLDR,'mario_kart_7.mp3')
        self.POW_UP = os.path.join(self.AUDIO_FLDR,'power_up.mp3')


        self.WIN = pg.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
        pg.display.set_caption(WIN_TITLE)
        self.SCRAPE = None

        self.FONT = pg.font.SysFont('comicsansms',30)
        self.LOADING_FONT = pg.font.SysFont('comicsansmc',70)

        self.NEW_NUMBERS = None
        self.OLD_NUMBERS = None
        self.NEW_STREAK = None
        self.OLD_STREAK = None
        

        self.INSTANCE_LIST = []
        self.POP_SAME = False
        self.POP_DEC = False
        self.POP_INC = False
        self.STREAK = False

        self.STREAK_DICT = {'same':0,'inc':0,'dec':0}
        self.HISTORY_DICT = {'Births':0,'Deaths':0}
        self.STREAK_CNT = {'Safe!':0,'Nice!':0,'Ouch!':0}



        self.Y_BOUND = WIN_HEIGHT//2 -75
        
    def timed_scrape(self):
        time.sleep(4.6)
        scrape = self.SCRAPER.getDict()
        #print(scrape)
        return scrape   

    def thread_function(self, should_stop):
        print('[Display] starting thread')
        
        # 'func' is wrapped in this wrapper function
        # the wrapper loops until the 'should_stop'-callback returns true
        def wrapper(should_stop):
            print('start doing something')
            while not should_stop():
                if self.NEW_NUMBERS != None:
                    self.OLD_NUMBERS = self.NEW_NUMBERS.copy()
                self.SCRAPE = self.timed_scrape()
                self.NEW_NUMBERS = self.getNumbers(self.SCRAPE)
                if(self.NEW_NUMBERS and self.OLD_NUMBERS != None):
                    self.checkDeathsBirths()
                    print(self.STREAK_DICT)

            print('stop doing something')
            
        x = threading.Thread(target = wrapper, args = [should_stop])
        x.start()
        return x
        
    def playTheme(self):
        pg.mixer.music.load(self.MAIN_THEME)
        pg.mixer.music.play(loops=-1)
    
    def getSND(self,f):
        snd = pg.mixer.Sound(f)
        return snd

    def checkDeathsBirths(self):
        if self.NEW_STREAK != None:
            self.OLD_STREAK = self.NEW_STREAK
        #if positive, more births / deaths
        birth_diff = self.NEW_NUMBERS['Births today'] - self.OLD_NUMBERS['Births today']
        death_diff = self.NEW_NUMBERS['Deaths today'] - self.OLD_NUMBERS['Deaths today']
        print("Current birthdifference:{}".format(birth_diff))
        print("Current deathdifference:{}".format(death_diff))

        #if pos, more birth
        total_diff = birth_diff-death_diff

        if total_diff > 0:
            self.NEW_STREAK = 'inc'
            self.populationIncrease(total_diff)

            self.HISTORY_DICT['Births'] +=1

        if total_diff < 0:
            self.NEW_STREAK = 'dec'
            self.populationDecrease(total_diff)

            self.HISTORY_DICT['Deaths'] +=1

        if total_diff == 0:
            self.NEW_STREAK = 'same'
            self.populationSame()

    def streakCondition(self):
        if self.NEW_STREAK != None:
            return self.NEW_STREAK == self.OLD_STREAK
        else:
            return False

    def killInstances(self):
        self.INSTANCE_LIST.clear()

    def populationDecrease(self,num):
        self.killInstances()
        self.STREAK_DICT['dec'] +=1
        self.POP_DEC = True
        self.ABE_PLAYER.play_vid()
        #show the decrease
        self.INSTANCE_LIST.append(Pop_Dec(self.WIN,WIN_WIDTH//2,self.Y_BOUND,num))

        if self.STREAK_DICT['dec'] %2 == 0 and self.streakCondition():
            streak_text = "{num} gone! Wow!".format(num =self.STREAK_DICT['dec'])
            self.STREAK_CNT['Ouch!'] +=1
            self.streaking(streak_text)
        self.clearStreaks('dec')

    def populationIncrease(self,num):
        self.killInstances()
        self.STREAK_DICT['inc'] +=1
        pow_up_snd = self.getSND(self.POW_UP)
        pow_up_snd.play()
        #show the increase
        self.POP_INC = True
        self.INSTANCE_LIST.append(Pop_Inc(self.WIN,WIN_WIDTH//2,self.Y_BOUND,num))
        if self.STREAK_DICT['inc'] %2 == 0 and self.streakCondition():
            streak_text = "{num} babies! Way to go!".format(num =self.STREAK_DICT['inc'])
            self.STREAK_CNT['Nice!'] +=1
            self.streaking(streak_text)
        self.clearStreaks('inc')

    def populationSame(self):
        self.killInstances()
        self.STREAK_DICT['same'] +=1
        self.POP_SAME = True
        self.INSTANCE_LIST.append(Pop_Same(self.WIN,WIN_WIDTH//2,self.Y_BOUND))

        if self.STREAK_DICT['same'] %3 == 0 and self.streakCondition():
            streak_text = "{num} safes! On a roll!".format(num =self.STREAK_DICT['same'])
            self.STREAK_CNT['Safe!'] +=1
            self.streaking(streak_text)
        self.clearStreaks('same')
        
    def clearStreaks(self,streak):
        #clears all streaks except 'streak'
        d = self.STREAK_DICT
        for k in d:
            if k != streak:
                d[k] = 0
        print(self.STREAK_DICT)
                
    def streaking(self,text):
        self.killInstances()
        self.STREAK = True
        self.INSTANCE_LIST.append(Streak(self.WIN,WIN_WIDTH//2,self.Y_BOUND,text))

    def getNumbers(self,d):
        new_d = d.copy()
        for k,v in new_d.items():
            new_d[k] = int(v.replace(',',''))
        return new_d

    def blitDict(self):
        #recall self.scrape is a dictionary
        blit_dict = {}
        label_dict = {}
        num_dict = {}
        label_x = 50
        num_x = 600
        for n, (k, v) in enumerate(self.SCRAPE.items()):
            y = (n+1)*40
            label_text = self.FONT.render(k,True,(94, 3, 163))
            label_rect = label_text.get_rect()
            label_rect.x,label_rect.y = label_x,y

            num_text = self.FONT.render(v,True,(255,0,102))
            num_rect = num_text.get_rect()
            num_rect.x, num_rect.y = num_x,y

            label_dict[label_text] = label_rect
            num_dict[num_text] = num_rect

        return label_dict, num_dict

    def initialize_display(self):
        # we keep a reference of the thread so we can wait
        # for it to finish once we told it to stop
        thread = self.thread_function(lambda: not self.RUN)
        # when the process should be killed (e.g. CTRL+C), stop thread
        def stop(sig, frame):
            print('[Display] got killed, stop thread')
            self.RUN = False
        
        signal.signal(signal.SIGINT, stop)
        clock = pg.time.Clock()

        #just to play at startup
        intro_snd = self.getSND(self.START_SND)
        self.INTRO_CHANNEL.play(intro_snd)
        #play main theme
        
        first = True

        LOADING_SPRITE = Load_Screen(self.WIN,WIN_WIDTH//2,WIN_HEIGHT//2 - 40)

        while self.RUN:

            if first:
                if not self.INTRO_CHANNEL.get_busy():
                    self.playTheme()
                    first= False

            if self.SCRAPE == None:
                self.WIN.fill(WHITE)
                LOADING_SPRITE.update()

                
            if self.SCRAPE != None:

                labels,nums = self.blitDict()
    
                self.WIN.fill(WHITE)
                
                for k,v in labels.items():
                    #keys are the text, v's are the rects
                    self.WIN.blit(k,v)

                for k,v in nums.items():
                    self.WIN.blit(k,v)

                history = History_Dict(self.WIN,WIN_WIDTH *0.8,WIN_HEIGHT * 3/4,
                self.HISTORY_DICT['Births'],self.HISTORY_DICT['Deaths'])
                history.update()

                counter = Streak_Counter(self.WIN,WIN_WIDTH * 0.8,WIN_HEIGHT*.3,self.STREAK_CNT['Safe!'],
                self.STREAK_CNT['Nice!'],self.STREAK_CNT['Ouch!'])
                counter.update()

                instructions = Instructions(self.WIN,WIN_WIDTH*.15,WIN_HEIGHT*.8)
                instructions.update()

                if self.POP_SAME:
                    for i in self.INSTANCE_LIST:
                        i.update()
                        if i.STOP:
                            self.POP_SAME = False

                if self.POP_DEC:
                    for i in self.INSTANCE_LIST:
                        i.update()
                        if i.STOP:
                            self.POP_DEC = False

                if self.POP_INC:
                    for i in self.INSTANCE_LIST:
                        i.update()
                        if i.STOP:
                            self.POP_INC = False

                if self.STREAK:
                    for i in self.INSTANCE_LIST:
                        i.update()
                        if i.STOP:
                            self.STREAK = False

                    
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    # setting 'run' to false will also stop the loop
                    # of the wrapper function
                    self.RUN = False
                    print('[Display] waiting for thread to finish')
                    # let's wait for the thread to finish
                    thread.join()
                    return
                    
            pg.display.update()
            clock.tick(60)
            
if __name__ == "__main__":
    display = Display()
    display.initialize_display()
    




