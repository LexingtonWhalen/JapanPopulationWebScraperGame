import os
import cv2
import numpy as np
import pygame as pg
import random

###Developed by Lex Whalen, Jan 14 2020
###DISCLAIMER: This is by no means a political statement.
###I just wanted to learn a bit of pygame and I was interested in webscraping.
###So this is the result. I am NOT saying that Shinzo Abe should be held in a negative light.
###I include videos of him as I recently saw a video where he tries many fruits, and I thought it was funny
###He says "juicy" quite often.
###Link: https://www.youtube.com/watch?v=f7wQUOjSqhc&ab_channel=%E3%83%86%E3%83%AC%E6%9D%B1NEWS

class AbePlayer():

    def __init__(self):
        pg.init()
        pg.mixer.init()
        infoObject = pg.display.Info()
        self.display_w = infoObject.current_w
        self.display_h = infoObject.current_h
        self.CWD = os.getcwd()
        self.VID_DIR = os.path.join(self.CWD,'abe_videos')
        #folder is where the videos are held
        self.VID_LIST = [os.path.join(self.VID_DIR,i) for i in os.listdir(self.VID_DIR)]
        self.AUDIO_FOLDER = os.path.join(self.CWD,'audio')
        self.NOM_NOM = os.path.join(self.AUDIO_FOLDER,'NOM_NOM.mp3')
        self.temp_num = 0
    
    def play_audio(self,f):
        snd = pg.mixer.Sound(f)
        snd.play()

    def play_vid(self):
        rand_x = random.randint(self.display_w*.2,self.display_w*.6)
        rand_y = random.randint(self.display_h*.2,self.display_h*.6)

        win_title = 'He loves to nom!'


        if self.temp_num > len(self.VID_LIST)-1:
            self.temp_num =0
        #gets a video of abe, each iteration is the next video
        cap = cv2.VideoCapture(self.VID_LIST[self.temp_num])
        if(cap.isOpened()==False):
            print("error loading vid")
        else:
            self.play_audio(self.NOM_NOM)
            while(cap.isOpened()):
                ret,frame = cap.read()
                if ret == True:
                    cv2.imshow(win_title,frame)
                    cv2.moveWindow(win_title,rand_x,rand_y)

                    if cv2.waitKey(25) & 0xFF == ord('q'):
                        break
                else:
                    break
        self.temp_num +=1
        cap.release()
        cv2.destroyAllWindows()

