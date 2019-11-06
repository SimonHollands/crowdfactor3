# CrowdFactor [![CircleCI](https://circleci.com/gh/SimonHollands/crowdfactor3.svg?style=svg)](https://circleci.com/gh/SimonHollands/crowdfactor3)

![image](https://user-images.githubusercontent.com/22828446/68315875-52def480-006d-11ea-8f59-48ffc1b16ec0.png)


Crowdfactor is an app for real-time crowd surfbreak crowd prediction. It is powered by a custum Yolo deep learning computer vision model. 
* [CrowdFactor](https://crowdfactor.herokuapp.com/) - Deployed on Heroku
* [HitModel](https://crowdfactor.herokuapp.com/) - Deep learning model api, deployed on Heroku

* [ModelserverGithub](https://github.com/SimonHollands/cfmodelserver) - Repo for the flask api which serves the Yolo model


## Install
```
git clone https://github.com/SimonHollands/crowdfactor3
git clone https://github.com/SimonHollands/cfmodelserver 
```

## Useage
Each surf break should be instantiated with a ```dector.py``` class. Detectors are instantiated with a link to the relevent surf break mp4. 
```read_video.py``` and ```scrape_video_links.py``` methods are used to pull images into the S3 folders used by the model API. 
```dector.py``` class can  call the model api for crowd counts, and the predicted images (with bounding boxes) behind the counts.

## Deploying on Heroku
```
1. Create new app
2. connect it to github branch for deployment.
3. Need procfile, and requirements
```

## License
Copyright (c) 2019 Simon Hollands  
Licensed under the MIT license.