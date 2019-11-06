import flask
import random
from flask import request, jsonify
from flask import send_file
from os import listdir
from os.path import isfile, join
import os, shutil
from Surf_counter.detector import DetectTopanga, DetectBreakwater
from Surf_counter.spot_urls import SpotUrls
from s3pushpull2 import s3pushpull
from flask import render_template
from flask import Flask, request, url_for, redirect, render_template
#from flask_caching import Cache
use_live=True

app = flask.Flask(__name__)
app.config["DEBUG"] = True
#cache = Cache(app, config={'CACHE_TYPE': 'simple'})

det=DetectBreakwater()
det_topanga=DetectTopanga()

s3=s3pushpull()

@app.route('/topanga_count')
#@cache.cached(timeout=5)
def topanga_count():
    det_topanga=DetectTopanga()
    det_topanga.pull_images_s3()
    n_surfers=det.detection()
    out=f'''There are {n_surfers} Surfers at Topanga'''
    return render_template("topanga_count.html", message=out)

@app.route('/breakwater_count')
#@cache.cached(timeout=5)
def breakwater_count():
    n_surfers=det.detection()
    out=f'''There are {n_surfers} Surfers at the Breakwater'''
    return render_template("breakwater_count.html", message=out)

@app.route('/logo')
def logo(): 
    return send_file('cfLogo.png', mimetype='image/png')

@app.route('/breakwater_image')
def breakwater_image(): 
    s3.download_aws('breakwater_pred.jpg', 'S3:/data/breakwater/pred.jpg')
    return send_file('breakwater_pred.jpg', mimetype='image/jpg')

@app.route('/topanga_image')
def topanga_image(): 
    s3.download_aws('topanga_pred.jpg', 'S3:/data/topanga/pred.jpg')
    return send_file('topanga_pred.jpg', mimetype='image/jpg')

@app.route('/')
def index1():
    det_topanga=DetectTopanga()
    det=DetectBreakwater()
    det.pull_images_s3()
    return redirect(url_for('index'))

@app.route('/home')
def index():
    crowd1= f''' {random.randint(1,100)}% less crowded than normal '''
    crowd2= f''' {random.randint(1,100)}% less crowded than normal '''

    n_surfers=det.detection()
    n_surfers2=det_topanga.detection()

    return render_template('index.html',message1=str(n_surfers), message2=str(n_surfers2), crowd1=crowd1, crowd2=crowd2)

if __name__ == '__main__':
    app.run(threaded=False,use_reloader=False)

 #      <p style="text-align:center">Deep <img src="{{ url_for('logo') }}"  alt="Smiley face" align="middle"> Learning.</p></p>
 

