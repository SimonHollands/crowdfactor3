import boto3
from botocore.exceptions import NoCredentialsError
import os


class s3pushpull:
    # is_prod = os.environ.get('IS_HEROKU', None)

    # if is_prod:
    #     os.environ.get('AWS_IAM_ACCESS_KEY')
    #     os.environ.get('AWS_IAM_SECRET_KEY')

    ACCESS_KEY = os.environ.get('AWS_IAM_ACCESS_KEY')
    SECRET_KEY =os.environ.get('AWS_IAM_SECRET_KEY')

    #ACCESS_KEY = os.environ['AWS_IAM_ACCESS_KEY'] #I think this is the EKC
    #SECRET_KEY =os.environ['AWS_IAM_SECRET_KEY'] #I think this is the admnin?
    
    def __init__(self):
        self.s3=boto3.client('s3', aws_access_key_id=self.ACCESS_KEY,
                            aws_secret_access_key=self.SECRET_KEY)
        self.bucket='surfcounter14367'

    def upload_aws(self, local_file, s3_file):
        bucket=self.bucket
        try:
            self.s3.upload_file(local_file, bucket, s3_file)
            print("Upload Successful")
            return True
        except FileNotFoundError:
            print("The file was not found")
            return False
        except NoCredentialsError:
            print("Credentials not available")
            return False

    def upload_aws_obj(self, local_file, s3_file):
        bucket=self.bucket
        try:
            self.s3.upload_fileobj(local_file, bucket, s3_file)
            print("Upload Successful")
            return True
        except FileNotFoundError:
            print("The file was not found")
            return False
        except NoCredentialsError:
            print("Credentials not available")
            return False

    def download_aws(self, local_file, s3_file):
        bucket=self.bucket
        print("Herteee")
        print(s3_file)
        try:
            self.s3.download_file(bucket, s3_file, local_file)
            print("Download Successful 666")
            return True
        except FileNotFoundError:
            print("The file was not found")
            return False
        except NoCredentialsError:
            print("Credentials not available")
            return False

    def download_aws_obj(self, local_file, s3_file):
        bucket=self.bucket
        print("Herteee")
        print(s3_file)

        try:
            self.s3.download_fileobj(bucket, s3_file, local_file)
            print("Download Successful 69")
            return True
        except FileNotFoundError:
            print("The file was not found")
            return False
        except NoCredentialsError:
            print("Credentials not available")
            return False

    def delete_files(self,Key):
        self.s3.delete_object(Bucket=self.bucket, Key=Key)

    def get_matching_s3_keys(self, prefix='', suffix=''):
        """
        Generate the keys in an S3 bucket.

        :param bucket: Name of the S3 bucket.
        :param prefix: Only fetch keys that start with this prefix (optional).
        :param suffix: Only fetch keys that end with this suffix (optional).
        """
        bucket=self.bucket
        s3 = self.s3
        kwargs = {'Bucket': bucket}

        # If the prefix is a single string (not a tuple of strings), we can
        # do the filtering directly in the S3 API.
        if isinstance(prefix, str):
            kwargs['Prefix'] = prefix

        while True:

            # The S3 API response is a large blob of metadata.
            # 'Contents' contains information about the listed objects.
            resp = s3.list_objects_v2(**kwargs)
            for obj in resp['Contents']:
                key = obj['Key']
                if key.startswith(prefix) and key.endswith(suffix):
                    yield key

            # The S3 API is paginated, returning up to 1000 keys at a time.
            # Pass the continuation token into the next response, until we
            # reach the final page (when this field is missing).
            try:
                kwargs['ContinuationToken'] = resp['NextContinuationToken']
            except KeyError:
                break


