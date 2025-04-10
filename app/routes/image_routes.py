from flask import Blueprint, jsonify, abort
from app.services.image_service import get_image_by_id
from uuid import UUID

bp = Blueprint('image_routes', __name__)

@bp.route('/image/<uuid:image_id>', methods=['GET'])
def get_image(image_id):
    # Ensure the image_id is a valid UUID
    try:
        # Check if it's a valid UUID
        image_id = UUID(str(image_id))
    except ValueError:
        abort(400, description="Invalid image ID format")

    # Fetch the image
    image = get_image_by_id(image_id)

    if not image:
        abort(404, description="Image not found")

    # Return the image URL as JSON
    return jsonify({"id": str(image.id), "url": image.url})
