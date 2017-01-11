#!venv/bin/python
from flask import render_template
from flask_mail import Message

from .decorators import async
from config import ADMINS
from app import app, mail


def send_email(subject, sender, recipients, text, html):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text
    msg.html = html

    send_async_email(app, msg)


@async
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def follower_notification(followed, follower):
    send_email("[microblog] %s is now following you!" % follower.nickname,
               ADMINS[0],
               [followed.email],
               render_template('follower_email.txt',
                               user=followed, follower=follower),
               render_template('follower_email.html',
                               user=followed, follower=follower))
