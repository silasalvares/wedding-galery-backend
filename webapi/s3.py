import os
import boto3
from botocore.client import Config

class S3ImageHandler():

    def __init__(self):
        self.s3_client = boto3.client(
            's3', 
            region_name=os.environ.get('S3_REGION'),
            aws_access_key_id=os.environ.get('ACCESS_ID'),
            aws_secret_access_key=os.environ.get('ACCESS_KEY'))

    def upload_image(self, key, image):
        self.s3_client.put_object(Bucket=os.environ.get('IMAGE_BUCKET'), Key=key, Body=image)
        return True

    def get_image(self, key):
        return self.s3_client.get_object(Bucket=os.environ.get('IMAGE_BUCKET'), Key=key)