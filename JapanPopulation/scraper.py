from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import re

###Developed by Lex Whalen, Jan 14 2020
###DISCLAIMER: This is by no means a political statement.
###I just wanted to learn a bit of pygame and I was interested in webscraping.
###So this is the result. I am NOT saying that Shinzo Abe should be held in a negative light.
###I include videos of him as I recently saw a video where he tries many fruits, and I thought it was funny
###He says "juicy" quite often.
###Link: https://www.youtube.com/watch?v=f7wQUOjSqhc&ab_channel=%E3%83%86%E3%83%AC%E6%9D%B1NEWS

class Scraper():

    def __init__(self):
        self.url = r"https://countrymeters.info/en/Japan"
    
    def getData(self):
        
        self.page = requests.get(self.url,timeout=10)
        self.soup = BeautifulSoup(self.page.text,'html.parser')
        data = self.soup.find_all('td',class_='counter')
        rows = self.soup.find_all('td',class_="data_name")
        return data, rows

    def getDict(self):
        data_pattern = re.compile("(?<=>)-?\d.*(?=</d)")
        row_pattern = re.compile("[A-Z].*\w(?=\s?<)")
        data,rows = self.getData()
        table_dict = {}
        for n,i in enumerate(rows):
            val = row_pattern.findall(str(i))[0]
            num = ("").join(data_pattern.findall(str(data[n])))
            table_dict[val] = num

        return table_dict

#print('starting')
#test = Scraper().getDict()
#for n, (k,v) in enumerate(test.items()):
#    print(n)
#    print("{}:{}".format(k,v))
