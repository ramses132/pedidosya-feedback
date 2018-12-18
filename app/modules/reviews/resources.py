import logging

import sqlalchemy
from flask_restplus import Namespace, Resource, abort, fields, inputs, reqparse
from flask_restplus._http import HTTPStatus
from marshmallow import ValidationError

from app import db

from . import schemas
from .models import Review

log = logging.getLogger(__name__)
api = Namespace('reviews', description="reviews API v1")

review_model = api.model(
    'review', {
        'created_at':
        fields.DateTime(required=False, description='The Review created date'),
        'modified_at':
        fields.DateTime(
            required=False, description='The Review last modified date'),
        'user':
        fields.String(required=True, description='External User identifier'),
        'purchase':
        fields.String(
            required=True, description='external Purchase identifier'),
        'shop':
        fields.String(required=True, description='external Shop identifier'),
        'score':
        fields.Integer(required=True, description='The Review score (1..5)'),
        'description':
        fields.String(required=False, description='The Review description')
    })
review_model_response = api.model(
    'review_response', {
        'created_at':
        fields.DateTime(required=False, description='The Review created date'),
        'modified_at':
        fields.DateTime(
            required=False, description='The Review last modified date'),
        'id':
        fields.Integer(
            readonly=True, description='The Review unique identifier'),
        'user':
        fields.String(required=True, description='External User identifier'),
        'purchase':
        fields.String(
            required=True, description='external Purchase identifier'),
        'shop':
        fields.String(required=True, description='external Shop identifier'),
        'score':
        fields.Integer(required=True, description='The Review score (1..5)'),
        'description':
        fields.String(required=False, description='The Review description')
    })


@api.route('/')
class ReviewsList(Resource):
    """
    Manipulations with reviews.
    """
    model_class = Review
    schema_class = schemas.ReviewSchema
    arg_filters = (('created_at__lte', 'date'), ('created_at__gte', 'date'))

    def filter_query(self, query):
        def build_filter(arg, lookup, value, operator=sqlalchemy.or_):
            
            column = getattr(self.model_class, arg, None)
            if not column:
                raise abort(
                    code=HTTPStatus.BAD_REQUEST,
                    message='invalid filter argument: %s' % arg)
            if value == 'null':
                value = None

            if lookup == 'lte' and value:

                return operator(column <= value)
            elif lookup == 'gte' and value:
                return operator(column >= value)
            return operator(column == value)

        parser = reqparse.RequestParser()

        for arg, type_arg in self.arg_filters:
            if type_arg == 'date':
                input_type = inputs.date
            else:
                input_type = None

            if input_type:
                parser.add_argument(arg, type=input_type)

        args = parser.parse_args()

        for __arg, __value in args.items():
            __arg, *__lookups = __arg.split('__')
            if __lookups:
                __filter = (build_filter(__arg, __lookup, __value)
                            for __lookup in __lookups)
            else:
                __filter = build_filter(
                    __arg,
                    __lookups,
                    __value,
                )
            try:
                query = query.filter(*__filter)
            except Exception as err:
                abort(
                    code=HTTPStatus.BAD_REQUEST,
                    message='invalid filter argument lookup %s' % err)
        return query

    def get_query(self):
        """
        return query object
        """
        return self.model_class.query

    @api.doc('list reviews')
    @api.marshal_list_with(review_model_response)
    @api.doc(
        params={
            'created_at__lte': 'filter by date less than or equal...',
            'created_at__gte':
            'filter by created date greater than or equal...'
        })
    @api.response(409, 'message: <error>')
    @api.response(404, 'field: <error>')
    def get(self, *args):
        """
        List of reviews instances
        
        """
        query = self.get_query()
        schema = self.schema_class(many=True)
        query = self.filter_query(query)
        return schema.dump(self.get_query())

    @api.doc('create review')
    @api.expect(review_model, validate=True)
    @api.marshal_with(review_model_response, code=201)
    @api.response(409, 'message: <error>')
    @api.response(404, 'field: <error>')
    def post(self, *args):
        """
        Create a new review instance.
        """
        schema = self.schema_class()
        try:
            data = schema.load(api.payload, )

        except ValidationError as err:
            return abort(
                code=HTTPStatus.BAD_REQUEST,
                message='Failed to create review...',
                **err.messages)
        try:
            # review = Review(**data)
            db.session.add(data)
            db.session.commit()
        except (ValueError, sqlalchemy.exc.IntegrityError) as err:
            print(err)
            log.info(
                "Database transaction was rolled back due to: {}".format(err))
            return abort(
                code=HTTPStatus.CONFLICT, message='Failed to create review...')

        return data, 201


@api.route('/<int:id>')
class ReviewsDetail(Resource):
    """
        Manipulations of review.
    """
    model_class = Review
    schema_class = schemas.ReviewDetailSchema

    @api.doc('detail review')
    @api.marshal_with(review_model_response)
    def get(self, id, *args):
        """
            Detail of Review
        """
        schema = self.schema_class()
        try:
            instance = self.model_class.query.get_or_404(id)
        except Exception as err:
            print(err)
            abort(code=HTTPStatus.BAD_REQUEST, message="%s" % err)

        return schema.dump(instance), 200

    @api.doc('update review')
    @api.expect(review_model, validate=True)
    @api.marshal_with(review_model_response, code=200)
    @api.response(409, 'message: <error>')
    @api.response(404, 'field: <error>')
    def put(self, id, *args):
        """
            Update a Review instance
        """

        Review.query.get_or_404(id)
        schema = self.schema_class()
        try:
            api.payload['id'] = id
            instance = schema.load(api.payload)
        except ValidationError as err:
            return abort(
                code=HTTPStatus.BAD_REQUEST,
                message='Failed to create review...',
                **err.messages)

        try:

            db.session.commit()

        except (ValueError, sqlalchemy.exc.IntegrityError) as err:
            print(err)
            log.info(
                "Database transaction was rolled back due to: {}".format(err))
            return abort(
                code=HTTPStatus.CONFLICT, message='Failed to update review...')

        return schema.dump(instance), 200

    @api.doc('delete review')
    @api.response(204, 'no content.')
    @api.response(409, 'message: <error>')
    @api.response(404, 'field: <error>')
    def delete(self, id, *args):
        """
        Delete Review instance
        """
        schema = self.schema_class()
        instance = Review.query.get_or_404(id)
        try:

            instance.deleted = True
            db.session.commit()

        except (ValueError, sqlalchemy.exc.IntegrityError) as err:
            print(err)
            log.info(
                "Database transaction was rolled back due to: {}".format(err))
            return abort(
                code=HTTPStatus.CONFLICT, message='Failed to update review...')

        return schema.dump(instance), 204

    @api.doc('patch review')
    @api.response(409, 'message: <error>')
    @api.response(404, 'field: <error>')
    @api.response(200, 'No Implemented')
    def patch(self, id, *args):
        """
            Patch a Review Instance column
        """
        return 'No Implemented'


@api.route('/purchase/<string:purchase_id>')
class ReviewDetailByPurchase(Resource):
    """
        Manipulations of review by purchase identifier.
    """
    model_class = Review
    schema_class = schemas.ReviewSchema

    @api.doc('detail review by purchase identifier')
    @api.marshal_with(review_model_response)
    def get(self, purchase_id, *args):
        """
            Detail of Review purchase identifier
        """
        schema = self.schema_class()
        try:
            instance = self.model_class.query.filter(
                self.model_class.purchase == purchase_id).first_or_404()
        except Exception as err:
            print(err)
            abort(code=HTTPStatus.BAD_REQUEST, message="%s" % err)

        return schema.dump(instance), 200
