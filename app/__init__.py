from flask import Flask
from .extensions import db
from .models import user
from .routes import user_routes
from .services import user_service

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)

    # Register blueprints (routes)
    app.register_blueprint(user_routes.bp)

    return app
