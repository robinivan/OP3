from app import create_app
from app.extensions import db

# Create the Flask app
app = create_app()

# Create tables (this step creates the database and tables)
with app.app_context():
    db.create_all()
