import flask
from flask import request, jsonify
from flask import send_file
from os import listdir
from os.path import isfile, join
import os, shutil
#from s3pushpull import s3pushpull
#ddd
from Surf_counter.detector import Detect
from Surf_counter.spot_urls import SpotUrls
#from Surf_counter.scrape_video_links import ScrapeVideoLinks
#FF

app = flask.Flask(__name__)
app.config["DEBUG"] = True

det=Detect()
#det.pull_images_s3(SpotUrls.venice_static)

@app.route('/api/v1/breakwater/count')
def api_surfercount():
    #det.clear_data_dir()
    #Find the video
    #url=SpotUrls.lookup['venice_beach']
    #v=ScrapeVideoLinks(url)
    #link=v.get_link()
    #det.pull_images_s3(SpotUrls.venice_static)
    print("Made it herrrrre")
    n_surfers=det.detection()
    #print ("THERE ARE N SURFERS ", n_surfers)
    return str(n_surfers)
    #return str(23)
    
    #output=f'''There are currently {surfer_count} surfers at the Breakwater'''
    #return jsonify(n_surfers)



# s3=s3pushpull()
# d=list(s3.get_matching_s3_keys(prefix='S3:/data/'))
# print("List of keys:")
# print(d)
# pics = [p for p in d if '.jpg' in p]
# print('pics')
# print(pics)
# print ("downloading")
# s3.download_aws('MyPic.jpg', pics[0])

# @app.route('/get_image')
# def get_image():
#     if request.args.get('type') == '1':
#         filename = 'data/MyPic.jpg'
#     else:
#         filename = 'MyPic.jpg'
#     return send_file(filename, mimetype='image/jpg')


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


if __name__ == '__main__':
    app.run(threaded=False,use_reloader=False)