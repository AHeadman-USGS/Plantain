from app import app, db
import admin
import views
import models

from National.blueprint import natl
from wsc.blueprint import wsc

app.register_blueprint(natl, url_prefix='/national')

app.register_blueprint(wsc, url_prefix='/wsc')

if __name__ == '__main__':
    app.run()