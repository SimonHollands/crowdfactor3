# Importing all necessary libraries 
import cv2 
import os 
from s3pushpull2 import s3pushpull
import random 

class ReadVidz:

    def __init__(self,cam_link):
        self.cam_link=cam_link
        self.cam = cv2.VideoCapture(self.cam_link)
        self.frame_count= int(self.cam.get(cv2.CAP_PROP_FRAME_COUNT))

    def pull_frames_s3(self, how_many=1, s3key='S3:/data/breakwater/frame_last.jpg'):
                s3b=s3pushpull()
                self.cam.set(1, self.frame_count-random.randint(1, 1000) )
                res, frame = self.cam.read()

                name = 'data/breakwater/frame_last.jpg'
                print ('Creating...' + name) 
                # writing the extracted images
                crop_img = frame[100:100+325, 0:0+1280]
                crop_img = frame


                cv2.imwrite(name, crop_img)                         
                s3b.upload_aws(name, s3key)



#r=ReadVidz("https://camrewinds.cdn-surfline.com/live/wc-venicebeachclose.stream.20191027T211834705.mp4")#reader.pull_frames(how_many=10)
#r.pull_frames_s3()
#cam.release() 
#cv2.destroyAllWindows() 
