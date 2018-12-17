from app import db
from datetime import datetime


class TimestampMixin(db.Model):
    __abstract__ = True
    created_at = db.Column(db.DateTime, default=datetime.now())
    modified_at = db.Column(
        db.DateTime, default=datetime.now(), onupdate=datetime.now())
