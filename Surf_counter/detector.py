from Surf_counter.read_video import ReadVidz
from os import listdir
from os.path import isfile, join
import os, shutil 
from Surf_counter.spot_urls import SpotUrls
from Surf_counter.scrape_video_links import ScrapeVideoLinks
from s3pushpull2 import s3pushpull
import urllib.request
#Something
s3=s3pushpull()

class Detect:
    scraper=ScrapeVideoLinks()
    def __init__(self):
        self.current_link=self.scraper.get_link()
    
    #ScrapeVideoLinks
    def grab_frames(self):
        '''Pull images from video'''
        r=ReadVidz(self.current_link)
        r.pull_frames(5)

    def pull_images_s3(self):
        '''Pull images from video'''
        r=ReadVidz(self.current_link)
        r.pull_frames_s3(5)

    def detection(self):
        #Get prediction from the api
        response = urllib.request.urlopen('https://cfmodelserver.herokuapp.com/model').read().decode('ASCII')

        return response


