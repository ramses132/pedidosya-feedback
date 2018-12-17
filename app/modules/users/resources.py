import logging

from flask_restplus import Namespace, Resource, fields, reqparse

log = logging.getLogger(__name__)
api = Namespace('users', description="Reviews API v1 (Not Implemented)")

permission_model = api.model(
    'permission',
    {"name": fields.String(required=True, description="Permission name")})

group_model = api.model(
    'group', {"name": fields.String(required=True, description="Group name")})

user_model = api.model(
    'user', {
        "username":
        fields.String(required=False, description="the user username"),
        "password_hash":
        fields.String(
            required=False, description="The user password secret hash"),
        "access_token":
        fields.String(
            required=False,
            description="The user actual JWT hash access Token"),
        "refresh_token":
        fields.String(
            required=False,
            description="The user actual JWT hash Refresh Token"),
        "email":
        fields.String(required=False, description="The user email address"),
        "first_name":
        fields.String(required=False, description="The user first name"),
        "last_name":
        fields.String(required=False, description="The user last name"),
        "is_superuser":
        fields.Boolean(
            required=False,
            description="The user is superuser flag to allow all privileges"),
        "is_staff":
        fields.Boolean(
            required=False,
            description=
            "The user is staff flag to allow enter to future api html interface"
        ),
        "is_active":
        fields.Boolean(
            required=False,
            description="The User is active flag to allow operations"),
        "last_login":
        fields.DateTime(
            required=False, description="The user last login date"),
        "date_joined":
        fields.DateTime(
            required=False, description="The User microservice joined date"),
        "groups":
        fields.Nested(group_model, as_list=True, allow_null=True),
        "permissions":
        fields.Nested(permission_model, as_list=True, allow_null=True),
        "shop":
        fields.String(description="shop identifier", required=False)
    })

user_model_response = api.model(
    'user', {
        'created_at':
        fields.DateTime(required=False, description='The User created date'),
        'modified_at':
        fields.DateTime(
            required=False, description='The User last modified date'),
        "id":
        fields.Integer(
            readonly=True, description='The User unique identifier'),
        "username":
        fields.String(required=False, description="the user username"),
        "password_hash":
        fields.String(
            required=False, description="The user password secret hash"),
        "access_token":
        fields.String(
            required=False,
            description="The user actual JWT hash access Token"),
        "refresh_token":
        fields.String(
            required=False,
            description="The user actual JWT hash Refresh Token"),
        "email":
        fields.String(required=False, description="The user email address"),
        "first_name":
        fields.String(required=False, description="The user first name"),
        "last_name":
        fields.String(required=False, description="The user last name"),
        "is_superuser":
        fields.Boolean(
            required=False,
            description="The user is superuser flag to allow all privileges"),
        "is_staff":
        fields.Boolean(
            required=False,
            description=
            "The user is staff flag to allow enter to future api html interface"
        ),
        "is_active":
        fields.Boolean(
            required=False,
            description="The User is active flag to allow operations"),
        "last_login":
        fields.DateTime(
            required=False, description="The user last login date"),
        "date_joined":
        fields.DateTime(
            required=False, description="The User microservice joined date"),
        "groups":
        fields.Nested(group_model, as_list=True, allow_null=True),
        "permissions":
        fields.Nested(permission_model, as_list=True, allow_null=True),
        "shop":
        fields.String(description="shop identifier", required=False)
    })

parser = reqparse.RequestParser()
parser.add_argument(
    'Authorization',
    type=str,
    location='headers',
    help='Bearer Access Token',
    required=True)


@api.route('/')
class UsersList(Resource):
    """
    Manipulations with users.
    """

    @api.doc('list users', parser=parser)
    @api.marshal_list_with(user_model)
    @api.response(409, 'message: <error>')
    @api.response(404, 'field: <error>')
    def get(self, *args):
        """
        List of users instances (Not Implemented)
        
        """
        return "Not implemented"

    @api.doc('create user', parser=parser)
    @api.expect(user_model, validate=True)
    @api.marshal_with(user_model_response, code=201)
    @api.response(409, 'message: <error>')
    @api.response(404, 'field: <error>')
    def post(self, *args):
        """
        Create a new user instance (Not Implemented)
        """
        return "Not Implemented"


@api.route('/<int:id>')
class UsersDetail(Resource):
    """
        Manipulations of User.
    """

    @api.doc('detail user', parser=parser)
    @api.marshal_with(user_model_response)
    def get(self, id, *args):
        """
            Detail of User (Not Implemented)
        """

        return "Not implemented"

    @api.doc('update user', parser=parser)
    @api.expect(user_model, validate=True)
    @api.marshal_with(user_model_response, code=200)
    @api.response(409, 'message: <error>')
    @api.response(404, 'field: <error>')
    def put(self, id, *args):
        """
            Update a User instance (Not Implemented)
        """
        return "Not Implemented"

    @api.doc('delete user', parser=parser)
    @api.response(204, 'no content.')
    @api.response(409, 'message: <error>')
    @api.response(404, 'field: <error>')
    def delete(self, id, *args):
        """
            Delete a User Instance (Not Implented)
        """
        return "Not implemented"

    @api.doc('patch user', parser=parser)
    @api.response(409, 'message: <error>')
    @api.response(404, 'field: <error>')
    @api.response(200, 'No Implemented')
    def patch(self, id, *args):
        """
            Patch a User Instance column (Not implemented)
        """
        return 'No Implemented'
