import wtforms
from wtforms import StringField
from wtforms.validators import DataRequired, Optional
from flask_ckeditor import CKEditorField
from models import Project


class ProjectEntry(wtforms.Form):

    title = StringField(
        'Title',
        validators=[DataRequired()])

    intro = CKEditorField(
        'Introduction',
        validators=[Optional()])

    scope = CKEditorField(
        'Scope',
        validators=[Optional()])

    org = CKEditorField(
        'Organization',
        validators=[Optional()])

    resp = CKEditorField(
        'Responsibilities',
        validators=[Optional()])

    status = wtforms.SelectField(
        'Status',
        choices=(
            (Project.STATUS_DRAFT, "Save Draft"),
            (Project.STATUS_SUBMITTED, "Submit for Review")),
        coerce=int)

    def save_entry(self, Project):
        self.populate_obj(Project)
        Project.generate_slug()
        return Project


class ProjectApprove(wtforms.Form):

    title = StringField(
        'Title',
        validators=[DataRequired()])

    intro = CKEditorField(
        'Introduction',
        validators=[Optional()])

    scope = CKEditorField(
        'Scope',
        validators=[Optional()])

    org = CKEditorField(
        'Organization',
        validators=[Optional()])

    resp = CKEditorField(
        'Responsibilities',
        validators=[Optional()])

    status = wtforms.SelectField(
        'Status',
        choices=(
            (Project.STATUS_DRAFT, "Save Draft"),
            (Project.STATUS_APPROVED, "Approve and Publish")),
        coerce=int)

    def save_entry(self, Project):
        self.populate_obj(Project)
        Project.generate_slug()
        return Project
