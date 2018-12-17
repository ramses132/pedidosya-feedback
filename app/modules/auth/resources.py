import logging
from flask_restplus import Resource, Namespace, fields, reqparse

log = logging.getLogger(__name__)
api = Namespace('auth-jwt', description="Authorization JWT API v1 (Not Implemented)")

auth_model = api.model(
    'auth_jwt', {

        "message": fields.String(required=False, description="Message login for [username]"),
        "access_token": fields.String(required=False, description="The JWT Hash Token"),
        "refresh_token": fields.String(required=False, description="The JWT hash Refresh Token")
    })
token_model = api.model(
    'token_jwt', {
        "access_token": fields.String(required=False, description="The JWT Hash Token"),
    }
)
login_model = api.model(
    'login', {
        "username": fields.String(required=True, description="The User username"),
        "password": fields.String(required=True, description="The User password")
    }
)
parser = reqparse.RequestParser()
parser.add_argument('Authorization', type=str, location='headers', help='Bearer Access Token', required=True)

@api.route('/login')
class UserLogin(Resource):
    """
    Login with user
    """
    @api.expect(login_model)
    @api.marshal_with(auth_model)
    @api.response(404, 'username/password invalid.')
    @api.response(409, 'message: Something went wrong')
    def post(self, *args):
        """
            Create a new JWT Access and Refresh Token from user (Not Implemented)
        """
        return "Not Implemented"

@api.route('/refresh')
class UserRefreshToken(Resource):
    """
        Refresh Token for user
    """
    @api.doc("Refresh User JWT refresh token (Not Implemented)")
    @api.doc(parser=parser)
    @api.marshal_with(token_model)
    @api.response(409, 'message: Something went wrong')
    def post(self, *args):
        """
            Refresh JWT Access Token from user (Not Implemented)
        """
        return "Not Implemented"

@api.route('/logout/refresh')
class UserLogoutRefresh(Resource):
    """
        Revoke Refresh Token from user
    """
    @api.doc(parser=parser)
    @api.response(200, 'message: JWT refresh token has been revoked')
    @api.response(409, 'message: Something went wrong')
    def post(self, *args):
        """
            Revoke JWT Refresh Token from user (Not Implemented)
        """
        return 'Not Implemented'

@api.route('/logout')
class UserLogout(Resource):
    """
        Revoke Refresh Token from user
    """
    @api.doc(parser=parser)
    @api.response(200, 'message: JWT access token has been revoked')
    @api.response(409, 'message: Something went wrong')
    def post(self, *args):
        """
            Revoke JWT Access Token from user (Not Implemented)
        """
        return 'Not Implemented'
