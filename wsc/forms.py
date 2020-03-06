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

    facilities = CKEditorField(
        'Facilities',
        validators=[Optional()])

    labs = CKEditorField(
        'Laboratories',
        validators=[Optional()])

    dq_management = CKEditorField(
        'Data-Quality Management',
        validators=[Optional()])

    dq_planning = CKEditorField(
        'Data-Quality Planning',
        validators=[Optional()])

    dq_roles = CKEditorField(
        'Data-Quality Roles',
        validators=[Optional()])

    dq_workflows = CKEditorField(
        'Data-Quality Workflows',
        validators=[Optional()])

    dq_wf_pro = CKEditorField(
        'wf proposals',
        validators=[Optional()])

    dq_wf_workplan = CKEditorField(
        'wf workplans',
        validators=[Optional()])

    dq_wf_project_dmp = CKEditorField(
        'proj data management',
        validators=[Optional()])

    dq_wf_review = CKEditorField(
        'proj reviews',
        validators=[Optional()])

    dq_datasharing = CKEditorField(
        'Data Sharing Agreements',
        validators=[Optional()])

    dq_mous = CKEditorField(
        'Memoranda of Understands (MOUs)',
        validators=[Optional()])

    dq_access = CKEditorField(
        'Access Controls and Copyrights',
        validators=[Optional()])

    dq_aquisition = CKEditorField(
        'Data Acquisitions',
        validators=[Optional()])

    dq_aqu_roles = CKEditorField(
        'Data Acquisitions Roles',
        validators=[Optional()])

    dq_aqu_proc = CKEditorField(
        'Data Acquisitions Procedure',
        validators=[Optional()])

    dq_aqu_proc_coll = CKEditorField(
        'Data Acquisitions Collection Procedure',
        validators=[Optional()])

    dq_aqu_proc_proc = CKEditorField(
        'Data Acquisitions Processing Policies',
        validators=[Optional()])

    dq_aqu_proc_anal = CKEditorField(
        'Data Analysis and Policies',
        validators=[Optional()])

    dq_doc = CKEditorField(
        'Data Documentation',
        validators=[Optional()])

    dq_format = CKEditorField(
        'Data Formats',
        validators=[Optional()])

    dq_org = CKEditorField(
        'Organization of Files or Data',
        validators=[Optional()])

    dq_store = CKEditorField(
        'Data Storage',
        validators=[Optional()])

    dq_store_roles = CKEditorField(
        'Storage Roles',
        validators=[Optional()])

    dq_store_repo = CKEditorField(
        'Repositories',
        validators=[Optional()])

    dq_store_archive = CKEditorField(
        'Archiving',
        validators=[Optional()])

    dq_pubs = CKEditorField(
        'Publication and Sharing',
        validators=[Optional()])

    dq_pubs_roles = CKEditorField(
        'Publication Roles',
        validators=[Optional()])

    dq_pubs_workflow = CKEditorField(
        'Publication Workflow',
        validators=[Optional()])

    dq_pubs_prop = CKEditorField(
        'Publication Sensitive Data',
        validators=[Optional()])

    dq_pubs_release = CKEditorField(
        'Publication release',
        validators=[Optional()])

    dq_pubs_cite = CKEditorField(
        'Publication Citation',
        validators=[Optional()])

    dq_pubs_doi = CKEditorField(
        'Publication DOI',
        validators=[Optional()])

    dq_pubs_meta = CKEditorField(
        'Publication Meta',
        validators=[Optional()])

    dq_pubs_catalog = CKEditorField(
        'Publication Catalog',
        validators=[Optional()])

    qa_intro = CKEditorField(
        'Quality Assessment',
        validators=[Optional()])

    qa_field_data = CKEditorField(
        'Quality Assessment - Field Data',
        validators=[Optional()])

    qa_pro_ts = CKEditorField(
        'Quality Assessment - Time series Provisional',
        validators=[Optional()])

    qa_app_ts = CKEditorField(
        'Quality Assessment - Time Series Approved',
        validators=[Optional()])

    qa_discrete = CKEditorField(
        'Quality Assessment - Discrete Data Processing',
        validators=[Optional()])

    qa_db_integrity = CKEditorField(
        'Quality Assessment - Databases',
        validators=[Optional()])

    qa_records = CKEditorField(
        'Quality Assessment - records',
        validators=[Optional()])

    qa_interpretive = CKEditorField(
        'Quality Assessment',
        validators=[Optional()])

    qa_training = CKEditorField(
        'Quality Assessment',
        validators=[Optional()])

    qa_terms = CKEditorField(
        'Quality Assessment',
        validators=[Optional()])

    qa_resources = CKEditorField(
        'Quality Assessment',
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

    facilities = CKEditorField(
        'Facilities',
        validators=[Optional()])

    labs = CKEditorField(
        'Laboratories',
        validators=[Optional()])

    dq_management = CKEditorField(
        'Data-Quality Management',
        validators=[Optional()])

    dq_planning = CKEditorField(
        'Data-Quality Planning',
        validators=[Optional()])

    dq_roles = CKEditorField(
        'Data-Quality Roles',
        validators=[Optional()])

    dq_workflows = CKEditorField(
        'Data-Quality Workflows',
        validators=[Optional()])

    dq_wf_pro = CKEditorField(
        'wf proposals',
        validators=[Optional()])

    dq_wf_workplan = CKEditorField(
        'wf workplans',
        validators=[Optional()])

    dq_wf_project_dmp = CKEditorField(
        'proj data management',
        validators=[Optional()])

    dq_wf_review = CKEditorField(
        'proj reviews',
        validators=[Optional()])

    dq_datasharing = CKEditorField(
        'Data Sharing Agreements',
        validators=[Optional()])

    dq_mous = CKEditorField(
        'Memoranda of Understands (MOUs)',
        validators=[Optional()])

    dq_access = CKEditorField(
        'Access Controls and Copyrights',
        validators=[Optional()])

    dq_aquisition = CKEditorField(
        'Data Acquisitions',
        validators=[Optional()])

    dq_aqu_roles = CKEditorField(
        'Data Acquisitions Roles',
        validators=[Optional()])

    dq_aqu_proc = CKEditorField(
        'Data Acquisitions Procedure',
        validators=[Optional()])

    dq_aqu_proc_coll = CKEditorField(
        'Data Acquisitions Collection Procedure',
        validators=[Optional()])

    dq_aqu_proc_proc = CKEditorField(
        'Data Acquisitions Processing Policies',
        validators=[Optional()])

    dq_aqu_proc_anal = CKEditorField(
        'Data Analysis and Policies',
        validators=[Optional()])

    dq_doc = CKEditorField(
        'Data Documentation',
        validators=[Optional()])

    dq_format = CKEditorField(
        'Data Formats',
        validators=[Optional()])

    dq_org = CKEditorField(
        'Organization of Files or Data',
        validators=[Optional()])

    dq_store = CKEditorField(
        'Data Storage',
        validators=[Optional()])

    dq_store_roles = CKEditorField(
        'Storage Roles',
        validators=[Optional()])

    dq_store_repo = CKEditorField(
        'Repositories',
        validators=[Optional()])

    dq_store_archive = CKEditorField(
        'Archiving',
        validators=[Optional()])

    dq_pubs = CKEditorField(
        'Publication and Sharing',
        validators=[Optional()])

    dq_pubs_roles = CKEditorField(
        'Publication Roles',
        validators=[Optional()])

    dq_pubs_workflow = CKEditorField(
        'Publication Workflow',
        validators=[Optional()])

    dq_pubs_prop = CKEditorField(
        'Publication Sensitive Data',
        validators=[Optional()])

    dq_pubs_release = CKEditorField(
        'Publication release',
        validators=[Optional()])

    dq_pubs_cite = CKEditorField(
        'Publication Citation',
        validators=[Optional()])

    dq_pubs_doi = CKEditorField(
        'Publication DOI',
        validators=[Optional()])

    dq_pubs_meta = CKEditorField(
        'Publication Meta',
        validators=[Optional()])

    dq_pubs_catalog = CKEditorField(
        'Publication Catalog',
        validators=[Optional()])

    qa_intro = CKEditorField(
        'Quality Assessment',
        validators=[Optional()])

    qa_field_data = CKEditorField(
        'Quality Assessment - Field Data',
        validators=[Optional()])

    qa_pro_ts = CKEditorField(
        'Quality Assessment - Time series Provisional',
        validators=[Optional()])

    qa_app_ts = CKEditorField(
        'Quality Assessment - Time Series Approved',
        validators=[Optional()])

    qa_discrete = CKEditorField(
        'Quality Assessment - Discrete Data Processing',
        validators=[Optional()])

    qa_db_integrity = CKEditorField(
        'Quality Assessment - Databases',
        validators=[Optional()])

    qa_records = CKEditorField(
        'Quality Assessment - records',
        validators=[Optional()])

    qa_interpretive = CKEditorField(
        'Quality Assessment',
        validators=[Optional()])

    qa_training = CKEditorField(
        'Quality Assessment',
        validators=[Optional()])

    qa_terms = CKEditorField(
        'Quality Assessment',
        validators=[Optional()])

    qa_resources = CKEditorField(
        'Quality Assessment',
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
