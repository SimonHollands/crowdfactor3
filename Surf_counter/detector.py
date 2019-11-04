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
    def __init__(self, use_live):
        if use_live:
            self.current_link=self.scraper.get_link()
        else:
            self.current_link=SpotUrls.venice_morning_good

    def pull_images_static(self):
        '''Pull images from video'''
        print ("In:pull_images_s3")
        r=ReadVidz(self.current_link)
        r.pull_frames_s3(1, s3key='S3:/data/breakwater_static/frame_last.jpg')

    def pull_images_s3(self):
        '''Pull images from video'''
        print ("In:pull_images_s3")
        r=ReadVidz(self.current_link)
        print("pass ReadVidz")
        r.pull_frames_s3(1)

    def detection(self):
        #Get prediction from the api
        response = urllib.request.urlopen('http://13.57.217.48/model').read().decode('ASCII')

        return response


