import os
import uuid
import boto3

from .s3 import S3ImageHandler
from .models import WeddingImage

class WeddingImageService():
    
    def save_image(self, image):
        image_key = str(uuid.uuid1())        
        S3ImageHandler().upload_image(image_key, image)

        image = WeddingImage()
        image.s3_key = image_key
        image.url = os.environ.get('API_URL') + image_key + '/'
        image.save()
        return image

    def list_images(self):
        return WeddingImage.objects(approved=True)

    def list_pending_images(self):
        return WeddingImage.objects(approved=False)

    def approve_image(self, s3_key):
        wedding_image = WeddingImage.objects(s3_key=s3_key).get()
        wedding_image.approved = True
        wedding_image.save()
        return wedding_image

    def get_image(self, s3_key):
        images = WeddingImage.objects(s3_key=s3_key, approved=True)
        if len(images) > 0:
            return S3ImageHandler().get_image(s3_key)

        return None
