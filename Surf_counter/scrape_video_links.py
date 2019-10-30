from bs4 import BeautifulSoup
import requests
from Surf_counter.spot_urls import SpotUrls
from datetime import datetime
today=datetime.today().strftime('%Y%m%d')


class ScrapeVideoLinks:

    def __init__(self, camrewind_link,tofind_str=today+'T', occurance_n=3):
        self.main="https://camrewinds.cdn-surfline.com/live/wc-venicebeachclose.stream."
        self.camrewind_link=camrewind_link
        self.tofind_str =tofind_str
        self.page = requests.get(self.camrewind_link)
        self.soup = BeautifulSoup(self.page.content)
        self.soup_str=str(self.soup)



    def nth(self,Xstr):
        first_start = Xstr.find(self.tofind_str)
        first_end = first_start + len(self.tofind_str)
        
        second_start = first_end + Xstr[first_end:].find(self.tofind_str)
        second_end = second_start + len(self.tofind_str) 

        third_start = second_end + Xstr[second_end:].find(self.tofind_str)
        third_end = third_start + len(self.tofind_str) 
        print("Nth returning: ")
        print(Xstr[third_end:third_end+9])
        return Xstr[third_end:third_end+9]

    def get_link(self):
        self.end_of_link=self.tofind_str+self.nth(self.soup_str)+'.mp4'
        return self.main+self.end_of_link


# url=SpotUrls.lookup['venice_beach']
# v=ScrapeVideoLinks(url)
# print(v.get_link())

