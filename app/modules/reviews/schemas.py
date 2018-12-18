from flask_marshmallow.sqla import ModelSchema
from marshmallow import ValidationError, fields, validate, validates_schema

from app import ma

from .models import Review


class ReviewSchema(ModelSchema):
    score = fields.Integer(validate=validate.Range(min=1, max=5))
    id = fields.Integer(dump_only=True)

    class Meta:
        model = Review

    @validates_schema
    def validate_reviews(self, data):
        purchase = data['purchase']
        pk = data['id'] if data['id'] else None
        query = Review.query
        if pk:
            query = query.filter(Review.id != pk)
        exists = query.filter(Review.purchase == purchase).first()
        if exists:
            raise ValidationError('purchase already exist.')


class ReviewDetailSchema(ReviewSchema):
    id = fields.Integer()
