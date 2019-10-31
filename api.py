import flask
from flask import request, jsonify
from flask import send_file
from os import listdir
from os.path import isfile, join
import os, shutil
from Surf_counter.detector import Detect
from Surf_counter.spot_urls import SpotUrls
from s3pushpull2 import s3pushpull
from flask import render_template
from flask import Flask, request, url_for, redirect, render_template


app = flask.Flask(__name__)
app.config["DEBUG"] = True

det=Detect()
s3=s3pushpull()

@app.route('/breakwater_count')
def breakwater_count():
    print ("In breakwater_count")
    n_surfers=det.detection()
    out=f'''There are {n_surfers} Surfers'''
    return render_template("breakwater_count.html", message=out)

@app.route('/breakwater_image')
def get_image(): 
    print("Downloading")
    s3.download_aws('pred.jpg', 'S3:/current_prediction/pred.jpg')
    print("Done Down")
    if request.args.get('type') == '1':
        filename = 'pred.jpg'
    else:
        filename = 'pred.jpg'
    return send_file(filename, mimetype='image/jpg')

@app.route('/')
def index():
    det.pull_images_s3()
    return render_template('index.html')

if __name__ == '__main__':
    app.run(threaded=False,use_reloader=False)