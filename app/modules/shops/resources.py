import logging

from flask_restplus import Namespace, Resource, fields, reqparse

log = logging.getLogger(__name__)
api = Namespace('shops', description="Shop Registry API v1 (Not Implemented)")

shop_model = api.model(
    'shop', {
        "name":
        fields.String(required=False, description="the shop name"),
        "url":
        fields.String(required=False, description="The shop url"),
        "jwt_public_key":
        fields.String(
            required=False,
            description="The shop JWT encrypt hash public key"),
        "jwt_private_key":
        fields.String(
            required=False,
            description="The shop JWT encrypt hash private key"),
    })

shop_model_response = api.model(
    'shop_response', {
        'created_at':
        fields.DateTime(required=False, description='The shop created date'),
        'modified_at':
        fields.DateTime(
            required=False, description='The shop last modified date'),
        "id":
        fields.Integer(
            readonly=True, description='The Shop unique identifier'),
        "name":
        fields.String(required=False, description="the shop name"),
        "url":
        fields.String(required=False, description="The shop url"),
        "jwt_public_key":
        fields.String(
            required=False,
            description="The shop JWT encrypt hash public key"),
        "jwt_private_key":
        fields.String(
            required=False,
            description="The shop JWT encrypt hash private key"),
    })

parser = reqparse.RequestParser()
parser.add_argument(
    'Authorization',
    type=str,
    location='headers',
    help='Bearer Access Token',
    required=True)


@api.route('/')
@api.route('/')
class ShopsList(Resource):
    """
    Manipulations with shopss.
    """

    @api.doc('list users', parser=parser)
    @api.marshal_list_with(shop_model)
    @api.response(409, 'message: <error>')
    @api.response(404, 'field: <error>')
    def get(self, *args):
        """
        List of shops instances (Not Implemented)
        
        """
        return "Not implemented"

    @api.doc('create user', parser=parser)
    @api.expect(shop_model, validate=True)
    @api.marshal_with(shop_model_response, code=201)
    @api.response(409, 'message: <error>')
    @api.response(404, 'field: <error>')
    def post(self, *args):
        """
        Create a new shop instance (Not Implemented)
        """
        return "Not Implemented"


@api.route('/<int:id>')
class ShopsDetail(Resource):
    """
        Manipulations of Shop.
    """

    @api.doc('detail shop', parser=parser)
    @api.marshal_with(shop_model_response)
    def get(self, id, *args):
        """
            Detail of Shop (Not Implemented)
        """

        return "Not implemented"

    @api.doc('update user', parser=parser)
    @api.expect(shop_model, validate=True)
    @api.marshal_with(shop_model_response, code=200)
    @api.response(409, 'message: <error>')
    @api.response(404, 'field: <error>')
    def put(self, id, *args):
        """
            Update a Shop instance (Not Implemented)
        """
        return "Not Implemented"

    @api.doc('delete shop', parser=parser)
    @api.response(204, 'no content.')
    @api.response(409, 'message: <error>')
    @api.response(404, 'field: <error>')
    def delete(self, id, *args):
        """
            Delete a Shop Instance (Not Implented)
        """
        return "Not implemented"

    @api.doc('patch shop', parser=parser)
    @api.response(409, 'message: <error>')
    @api.response(404, 'field: <error>')
    @api.response(200, 'No Implemented')
    def patch(self, id, *args):
        """
            Patch a Shop Instance column (Not implemented)
        """
        return 'No Implemented'
