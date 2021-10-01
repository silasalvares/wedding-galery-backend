from flask import Blueprint, request, jsonify, make_response
from threading import Thread

from .service import WeddingImageService
from .schemas import WeddingImageSchema

api = Blueprint('api', __name__, url_prefix="/api")

@api.route('/', methods=['POST'])
def upload():
    images = request.files.getlist('images[]')
    image_service = WeddingImageService()
    for image in images:
        Thread(target=image_service.save_image, args=(image.read(),)).start()
    
    return jsonify({})

@api.route('/', methods=['GET'])
def list_images():
    images = WeddingImageService().list_images()
    return jsonify(WeddingImageSchema(many=True).dump(images))

@api.route('/<key>/', methods=['GET'])
def get_image(key):
    image = WeddingImageService().get_image(key)
    response = make_response(image.get('Body').read())
    response.headers.set('Content-Type', 'image/jpeg')
    response.headers.set(
        'Content-Disposition', '', filename='%s.jpg' % key)
    return response

@api.route('/approve', methods=['GET'])
def list_pedding_images():
    images = WeddingImageService().list_pending_images()
    return jsonify(WeddingImageSchema(many=True).dump(images))

@api.route('/<key>/approve', methods=['POST'])
def approve(key):
    image = WeddingImageService().approve_image(key)
    return jsonify(WeddingImageSchema().dump(image))

   