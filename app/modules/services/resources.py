import logging

from flask_restplus import Namespace, Resource, fields, reqparse

log = logging.getLogger(__name__)
api = Namespace(
    'services', description="Shop Registry API v1 (Not Implemented)")

service_model = api.model(
    'service', {
        "name":
        fields.String(required=False, description="service name name"),
        "request_url":
        fields.String(required=False, description="The service request url"),
        "jwt_public_key":
        fields.String(
            required=False,
            description="The service JWT encrypt hash public key"),
        "jwt_private_key":
        fields.String(
            required=False,
            description="The service JWT encrypt hash private key"),
        "headers":
        fields.String(
            required=False, description="The service request headers"),
        "request_body_schema":
        fields.String(
            required=False,
            description="The service request body structure schema"),
        "request_type":
        fields.String(
            required=False, description="The service request data type"),
        "response_body_schema":
        fields.String(
            required=False,
            description="The service response body structure schema"),
        "response_type":
        fields.String(
            required=False, description="The service response data type"),
        "method":
        fields.String(required=False, description="service request method"),
        "cookies":
        fields.String(
            required=False, description="the service request cookies"),
        "verbose":
        fields.String(required=False, description="Level logger verbose"),
    })

service_model_response = api.model(
    'service_response', {
        'created_at':
        fields.DateTime(required=False, description='The shop created date'),
        'modified_at':
        fields.DateTime(
            required=False, description='The shop last modified date'),
        "id":
        fields.Integer(
            readonly=True, description='The Shop unique identifier'),
        "name":
        fields.String(required=False, description="service name name"),
        "request_url":
        fields.String(required=False, description="The service request url"),
        "jwt_public_key":
        fields.String(
            required=False,
            description="The service JWT encrypt hash public key"),
        "jwt_private_key":
        fields.String(
            required=False,
            description="The service JWT encrypt hash private key"),
        "headers":
        fields.String(
            required=False, description="The service request headers"),
        "request_body_schema":
        fields.String(
            required=False,
            description="The service request body structure schema"),
        "request_type":
        fields.String(
            required=False, description="The service request data type"),
        "response_body_schema":
        fields.String(
            required=False,
            description="The service response body structure schema"),
        "response_type":
        fields.String(
            required=False, description="The service response data type"),
        "method":
        fields.String(required=False, description="service request method"),
        "cookies":
        fields.String(
            required=False, description="the service request cookies"),
        "verbose":
        fields.String(required=False, description="Level logger verbose"),
    })

parser = reqparse.RequestParser()
parser.add_argument(
    'Authorization',
    type=str,
    location='headers',
    help='Bearer Access Token',
    required=True)


@api.route('/')
class ServicesList(Resource):
    """
    Manipulations with services.
    """

    @api.doc('list external services', parser=parser)
    @api.marshal_list_with(service_model)
    @api.response(409, 'message: <error>')
    @api.response(404, 'field: <error>')
    def get(self, *args):
        """
        List of shops instances (Not Implemented)
        
        """
        return "Not implemented"

    @api.doc('create user', parser=parser)
    @api.expect(service_model, validate=True)
    @api.marshal_with(service_model_response, code=201)
    @api.response(409, 'message: <error>')
    @api.response(404, 'field: <error>')
    def post(self, *args):
        """
        Create a new service instance (Not Implemented)
        """
        return "Not Implemented"


@api.route('/<int:id>')
class ServicesDetail(Resource):
    """
        Manipulations of Service.
    """

    @api.doc('detail service', parser=parser)
    @api.marshal_with(service_model_response)
    def get(self, id, *args):
        """
            Detail of Service (Not Implemented)
        """

        return "Not implemented"

    @api.doc('update service', parser=parser)
    @api.expect(service_model, validate=True)
    @api.marshal_with(service_model_response, code=200)
    @api.response(409, 'message: <error>')
    @api.response(404, 'field: <error>')
    def put(self, id, *args):
        """
            Update a Service instance (Not Implemented)
        """
        return "Not Implemented"

    @api.doc('delete service', parser=parser)
    @api.response(204, 'no content.')
    @api.response(409, 'message: <error>')
    @api.response(404, 'field: <error>')
    def delete(self, id, *args):
        """
            Delete a Service Instance (Not Implented)
        """
        return "Not implemented"

    @api.doc('patch service', parser=parser)
    @api.response(409, 'message: <error>')
    @api.response(404, 'field: <error>')
    @api.response(200, 'No Implemented')
    def patch(self, id, *args):
        """
            Patch a Service Instance column (Not implemented)
        """
        return 'No Implemented'


@api.route('/tasks')
class TasksList(Resource):
    """
        Async Task Celery Schedules (Not implented)
    """

    @api.response(200,
                  "list of tasks with cron and schedule (not implemented)")
    def get(self, *args):
        """
        List of Async Task with cron and schedules (Not Implemented)
        """
        return "Not implemented"
