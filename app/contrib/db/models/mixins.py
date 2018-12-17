from datetime import datetime

from app import db


class TimestampMixin(db.Model):
    __abstract__ = True
    created_at = db.Column(db.DateTime, default=datetime.now())
    modified_at = db.Column(
        db.DateTime, default=datetime.now(), onupdate=datetime.now())
