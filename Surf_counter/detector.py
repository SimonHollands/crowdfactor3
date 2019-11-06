from Surf_counter.read_video import ReadVidz
from os import listdir
from os.path import isfile, join
import os, shutil 
from Surf_counter.spot_urls import SpotUrls
from Surf_counter.scrape_video_links import ScrapeVideoLinks
from s3pushpull2 import s3pushpull
import urllib.request
#import Surf_counter.analyze_history as History
#Something
s3=s3pushpull()

class Detect:

    def __init__(self, use_live):
        pass

    def pull_images_s3(self):
        '''Pull images from video'''
        r=ReadVidz(self.current_link)
        r.pull_frames_s3(1, s3key=self.s3key)
         
class DetectBreakwater(Detect):
    def __init__(self):
        self.scraper=ScrapeVideoLinks(surfbreak='breakwater')
        self.current_link=self.scraper.get_link()
        self.s3key='S3:/data/breakwater/frame_last.jpg'

    def detection(self):
        #Get prediction from the api
        response = urllib.request.urlopen('http://13.57.217.48/model/breakwater').read().decode('ASCII')
        return response

class DetectTopanga(Detect):
    def __init__(self):
        self.scraper=ScrapeVideoLinks(surfbreak='topanga')
        self.current_link=self.scraper.get_link()
        self.s3key='S3:/data/topanga/frame_last.jpg'

    def detection(self):
        #Get prediction from the api
        response = urllib.request.urlopen('http://13.57.217.48/model/topanga').read().decode('ASCII')
        return response

