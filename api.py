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
    n_surfers=det.detection()
    out=f'''There are {n_surfers} Surfers'''
    return render_template("breakwater_count.html", message=out)

@app.route('/breakwater_image')
def get_image():
    s3.download_aws('pred.jpg', 'S3:/current_prediction/pred.jpg')
    if request.args.get('type') == '1':
        filename = 'pred.jpg'
    else:
        filename = 'pred.jpg'
    return send_file(filename, mimetype='image/jpg')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cool_form', methods=['GET', 'POST'])
def cool_form():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('cool_form.html')


if __name__ == '__main__':
    app.run(threaded=False,use_reloader=False)