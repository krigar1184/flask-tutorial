import os


WTF_CSRF_ENABLED = True
SECRET_KEY = 'noko-du-aldri-kjem-til-aa-gjette'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com/a/FFA.S9AAk56RWwEQqk7Jx0RyDCuVgGp_6mH.BoSAN9O85.dPAXCHzzrt53S3oGbim8CKag4-'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://flickr.com/<username>'},
    {'name': 'MyOpenId', 'url': 'http://myopenid.com'}
]

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'migrations')
SLQALCHEMY_TRACK_MODIFICATIONS = False

MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USERNAME = None
MAIL_PASSWORD = None

ADMINS = ['krigar1184@gmail.com']

POSTS_PER_PAGE = 2

WHOOSH_BASE = os.path.join(basedir, 'search.db')
MAX_SEARCH_RESULTS = 50
