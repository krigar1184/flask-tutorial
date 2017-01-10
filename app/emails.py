#!venv/bin/python
from flask_mail import Message
from app import app, mail


def send_email(subject, sender, recipients, text, html):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text
    msg.html = html

    with app.app_context():
        mail.send(msg)
