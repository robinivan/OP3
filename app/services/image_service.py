from app.models.image import Image
from app import db

def get_image_by_id(image_id):
    # Query the image by its ID
    image = Image.query.get(image_id)
    return image
