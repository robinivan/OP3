from flask import Blueprint, jsonify
from app.services.user_service import get_all_users

bp = Blueprint('user_routes', __name__)

@bp.route('/users', methods=['GET'])
def get_users():
    users = get_all_users()
    print(users)
    return jsonify([user.username for user in users])
