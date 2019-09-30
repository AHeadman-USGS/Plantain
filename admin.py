from flask import g, url_for, request, redirect
from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.fileadmin import FileAdmin
from app import app, db
from models import Project, NationalRequired, User


class AdminAuthentication:
    def is_accessible(self):
        if g.user.is_authenticated and g.user.user_level() == 2:
            return True


class IndexView(AdminIndexView):
    @expose('/')
    def index(self):
        if not g.user.is_authenticated and g.user.user_level() == 2:
            return redirect(url_for('login', next=request.path))
        return self.render('admin/index.html')


admin = Admin(app, "Admin", index_view=IndexView())


class UserModelView(AdminAuthentication, ModelView):
    column_list = ['email', 'name', 'active', 'created_timestamp','group']


class BaseModelView(AdminAuthentication, ModelView):
    pass


class ProjectModelView(AdminAuthentication, ModelView):
    _status_choices = [(choice, label) for choice, label in [
        (Project.STATUS_SUBMITTED, 'Submitted'),
        (Project.STATUS_DRAFT, 'Draft'),
        (Project.STATUS_APPROVED, 'Approved'),
        (Project.STATUS_DELETED, 'Deleted')
    ]]

    column_choices = {
        'status': _status_choices,
    }


class StaticFileAdmin(AdminAuthentication, FileAdmin):
    pass


admin.add_view(UserModelView(User, db.session))
admin.add_view(BaseModelView(NationalRequired, db.session))
admin.add_view(ProjectModelView(Project, db.session))
admin.add_view(StaticFileAdmin(app.config['STATIC_DIR'], '/static/', name="Static Files"))