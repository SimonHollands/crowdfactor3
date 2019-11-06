import pytest

def test_s3():
    from s3pushpull2 import s3pushpull
    s3=s3pushpull()
    s3.upload_aws('api.py','S3:/api.py')