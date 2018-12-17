import logging
import rq
import os

from logging.handlers import SMTPHandler, RotatingFileHandler
from flask import Flask, request, current_app
from flask_migrate import Migrate
from flask_restplus import Api
from flask_login import LoginManager
from flask_moment import Moment
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_babel import Babel, lazy_gettext as _
from flask_marshmallow import Marshmallow
from elasticsearch import Elasticsearch
from redis import Redis
from config import config

ma = Marshmallow()
db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'
login.login_message = _('Log in to get access.')
moment = Moment()
babel = Babel()
mail = Mail()
api = Api(
    version='1.0',
    title="Feedback-Microservice API",
    description=("""
    Welcome to **feedback** this is a simple **CRUD** Flask-app Rest-Plus API 
    to complete a personal challenge, it's writted in python 
    [Flask framework](http://flask.pocoo.org/ "Flask's official website") 
    with Flask Rest-Plus because it's cool for microservices. 
    to data storage I am using 
    [*postgreSQL*](https://www.postgresql.org/ "postgreSQL official website") 
    it's robust and great. 
    Thanks for read! 
    """))


def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    moment.init_app(app)
    babel.init_app(app)
    api.init_app(app)
    app.elasticsearch = Elasticsearch([app.config['ELASTICSEARCH_URL']]) \
        if app.config['ELASTICSEARCH_URL'] else None
    app.redis = Redis.from_url(app.config['REDIS_URL'])
    app.task_queue = rq.Queue('feedback-tasks', connection=app.redis)


    if not app.debug and not app.testing:
        if app.config['MAIL_SERVER']:
            auth = None
            if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
                auth = (app.config['MAIL_USERNAME'],
                        app.config['MAIL_PASSWORD'])
            secure = None
            if app.config['MAIL_USE_TLS']:
                secure = ()
            mail_handler = SMTPHandler(
                mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
                fromaddr='no-reply@' + app.config['MAIL_SERVER'],
                toaddrs=app.config['ADMINS'],
                subject='FeedBack App Failure',
                credentials=auth,
                secure=secure)
            mail_handler.setLevel(logging.ERROR)
            app.logger.addHandler(mail_handler)

        if app.config['LOG_TO_STDOUT']:
            stream_handler = logging.StreamHandler()
            stream_handler.setLevel(logging.INFO)
            app.logger.addHandler(stream_handler)
        else:
            if not os.path.exists('logs'):
                os.mkdir('logs')
            file_handler = RotatingFileHandler(
                'logs/feedback.log', maxBytes=10240, backupCount=10)
            file_handler.setFormatter(
                logging.Formatter('%(asctime)s %(levelname)s: %(message)s '
                                  '[in %(pathname)s:%(lineno)d]'))
            file_handler.setLevel(logging.INFO)
            app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info('Feedback is up!')

    # Start Modules!
    from . import modules

    modules.init_app(app)

    return app


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(current_app.config['LANGUAGES'])
