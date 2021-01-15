# Japan Population Tracker & Game
Updated 1/15/21
## Video showing features:
* https://www.youtube.com/watch?v=qr1sP4v7Gak&t=16s&ab_channel=log1

## FEATURES:
* Grab live population data!
* Integrate the data into an animated screen!
* Show different animations based on updates to the data! (ie, if the population decreases or increases)
* Loop through a folder of videos based on updates to the data!
* Allow for streaks! (ie: 3 births in a row, 6 deaths in a row, etc [all multiples of 3])

## About:
I was interested in learning some webscraping. I figured I'd scrape some data from a population repository (https://countrymeters.info/en/Japan).
I also wanted to make it more interactive / interesting to watch than some inanimate graph. So I whipped-up some pygame / OpenCV stuff and here is what happened.

Please note that this is **BY NO MEANS A POLITICAL STATEMENT**. I just wanted to make this more interesting by throwing in some videos. I am learning Japanese,
and recently saw a video of Shinzo Abe eating some fruit (https://www.youtube.com/watch?v=f7wQUOjSqhc&ab_channel=%E3%83%86%E3%83%AC%E6%9D%B1NEWS). He said 
"juicy" a lot and I thought that was funny. This is BY NO MEANS a project meant to cast him in a bad light. I just did this so I had an excuse to 
work with pygame and cv.

## Modules Used:
1. pygame (https://www.pygame.org/news)
2. os (https://docs.python.org/3/library/os.html)
3. bs4 (https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
4. requests (https://requests.readthedocs.io/en/master/)
5. pandas (https://pandas.pydata.org/)
6. numpy (https://numpy.org/)
7. re (https://docs.python.org/3/library/re.html)
8. threading (https://docs.python.org/3/library/threading.html)
9. time (https://docs.python.org/3/library/time.html)
10. signal (https://docs.python.org/3/library/signal.html) 
11. cv2 (https://pypi.org/project/opencv-python/) 
12. random (https://docs.python.org/3/library/random.html)

## Music:
* Race Start Fanfare [Grand Prix & VS]
* Mario Kart 7 ~Main Titles~

###### TO DO:
Honestly I am likely done with this project. I just wanted a feel for bs4, pg, and cv. In hindsight I would not have used threading, 
since I believe pg has some functions that allow actions to take place after a certain time (I needed to wait a few seconds before accessing
the website that contained the population data so as not to be a nuisance). However, I do not regret looking into threading as I can see 
potential uses for that tool in the future.
