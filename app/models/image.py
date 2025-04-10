from app.extensions import db
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Image(db.Model):
    __tablename__ = 'images'

    # Use the correct UUID type from the PostgreSQL dialect
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    url = db.Column(db.String, nullable=False, unique=True)

    def __repr__(self):
        return f"<Image id={self.id}, url={self.url}>"
