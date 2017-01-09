import os


WTF_CSRF_ENABLED = True
SECRET_KEY = 'noko-du-aldri_kjem-til-aa-gjette'

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
