from flask import Flask
from .extensions import db
from .models import user
from .routes import user_routes
from .services import user_service
from app.routes.image_routes import bp as image_routes_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)

    # Register blueprints (routes)
    app.register_blueprint(user_routes.bp)
    # Register the image routes blueprint
    app.register_blueprint(image_routes_bp)

    return app
