import flask
from flask import request, jsonify
from flask import send_file
from os import listdir
from os.path import isfile, join
import os, shutil
from Surf_counter.detector import Detect
from Surf_counter.spot_urls import SpotUrls
from s3pushpull2 import s3pushpull
#i

app = flask.Flask(__name__)
app.config["DEBUG"] = True

det=Detect()
s3=s3pushpull()

@app.route('/breakwater_count')
def api_surfercount():
    n_surfers=det.detection()
    out=f'''There are {n_surfers} Surfers'''
    return out

@app.route('/breakwater_image')
def get_image():
    s3.download_aws('pred.jpg', 'S3:/current_prediction/pred.jpg')
    if request.args.get('type') == '1':
        filename = 'pred.jpg'
    else:
        filename = 'pred.jpg'
    return send_file(filename, mimetype='image/jpg')

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


if __name__ == '__main__':
    app.run(threaded=False,use_reloader=False)