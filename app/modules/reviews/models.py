# -*- coding: utf-8 -*-
from app import db
from app.contrib.db.models.mixins import TimestampMixin
from app.contrib.db.models.queries import SoftDeleteQuery


class Review(TimestampMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(254), index=True, nullable=False)
    shop = db.Column(db.String(254), index=True, nullable=False)
    purchase = db.Column(
        db.String(254), index=True, unique=True, nullable=False)
    score = db.Column(db.Integer(), default=1, index=True)
    description = db.Column(db.Text(), nullable=True)
    deleted = db.Column(db.Boolean(), default=False)

    query_class = SoftDeleteQuery

    def __repr__(self):
        return "<Review:{}> ".format(self.id)

    def has_swearwords(self):
        raise NotImplementedError

    @db.validates('score')
    def validate_score(self, key, value):
        if value < 1 or value > 5:
            raise ValueError('Score must be between 1..5')
        return value
