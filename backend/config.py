import os

basedir =os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'A-VERY_:ONG_SECRET-KEY'
    
    SQLALCHEMY_DATABASE_URI = os.environ.get(('DATABASE_URL')) or 'sqlite:///' + os.path.join(basedir, 'site.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False