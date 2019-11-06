#View an S3 bucket
from s3pushpull2 import s3pushpull
s3=s3pushpull()
surfbreak='breakwater'
s3.download_aws('check.jpg',"S3:/data/" + surfbreak + "/frame_last.jpg")