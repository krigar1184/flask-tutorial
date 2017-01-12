# -*- coding: utf-8 -*-

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_openid import OpenID
from flask_mail import Mail
from flask_babel import Babel
from config import basedir, ADMINS, MAIL_SERVER, MAIL_PORT, MAIL_USERNAME, MAIL_PASSWORD
from .momentjs import momentjs


app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

oid = OpenID(app, os.path.join(basedir, 'tmp'))

if not app.debug:
    import logging
    from logging.handlers import SMTPHandler, RotatingFileHandler

    file_handler = RotatingFileHandler('tmp/log', 'a', 1 * 1024 * 1024, 10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    credentials = None

    if MAIL_USERNAME or MAIL_PASSWORD:
        credentials = (MAIL_USERNAME, MAIL_PASSWORD)

    mail_handler = SMTPHandler((MAIL_SERVER, MAIL_PORT), 'no-reply@{}'.format(MAIL_SERVER), ADMINS, 'microblog failure', credentials)
    mail_handler.setLevel(logging.ERROR)

    app.logger.addHandler(file_handler)
    app.logger.addHandler(mail_handler)

mail = Mail(app)

app.jinja_env.globals['momentjs'] = momentjs

babel = Babel(app)

from app import views, models
