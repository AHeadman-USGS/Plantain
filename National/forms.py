import wtforms
from wtforms import StringField
from wtforms.validators import DataRequired
from flask_ckeditor import CKEditorField
import bleach

from models import NationalRequired


class NationalEntry(wtforms.Form):

    title = StringField(
        'Introduction',
        validators=[DataRequired()])

    intro = CKEditorField(
        'Introduction',
        validators=[DataRequired()])

    scope = CKEditorField(
        'Scope',
        validators=[DataRequired()])

    org = CKEditorField(
        'Organization',
        validators=[DataRequired()])

    resp = CKEditorField(
        'Responsibilities',
        validators=[DataRequired()])

    status = wtforms.SelectField(
        'Status',
        choices=(
            (NationalRequired.STATUS_DRAFT, "Save Draft"),
            (NationalRequired.STATUS_SUBMITTED, "Submit for Review"),
            (NationalRequired.STATUS_APPROVED, "Approve and Publish")),
        coerce=int)

    def save_entry(self, NationalRequired):
        self.populate_obj(NationalRequired)
        NationalRequired.generate_slug()
        return NationalRequired

