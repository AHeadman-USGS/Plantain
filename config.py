import os


class Config:
    APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
    STATIC_DIR = os.path.join(APPLICATION_DIR, 'static')
    IMAGES_DIR = os.path.join(STATIC_DIR, 'images')
    SECRET_KEY = "TopSecret!"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/plantain.db' % APPLICATION_DIR
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
