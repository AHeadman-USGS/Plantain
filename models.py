import datetime, re
from functools import wraps
from flask import redirect, url_for, g
from app import db, login_manager, bcrypt


def slugify(s):
    return re.sub('[^\w]+', '-', s).lower()


@login_manager.user_loader
def _user_loader(user_id):
    return User.query.get(int(user_id))


ACCESS = {
    'USER': 0,
    'WSC': 1,
    'ADMIN': 2
}


def require_access(access_level):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            user = g.user
            if not user.allowed(access_level):
                return redirect(url_for('index'))
            return f(*args, **kwargs)
        return decorated_function
    return decorator


class User(db.Model):
    END_USER = 0
    WSC_LEAD = 1
    ADMIN = 2

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True)
    password_hash = db.Column(db.String(255))
    name = db.Column(db.String(64), unique=True)
    slug = db.Column(db.String(64), unique=True)
    active = db.Column(db.Boolean, default=True)
    created_timestamp = db.Column(db.DateTime, default=datetime.datetime.now)
    projects = db.relationship('Project', backref='author', lazy='dynamic')
    group = db.Column(db.SmallInteger, default=END_USER)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.name:
            self.slug = slugify(self.name)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return self.active

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def user_level(self):
        return int(self.group)

    def allowed(self, access_level):
        return self.group >= access_level

    @staticmethod
    def make_password(plaintext):
        return bcrypt.generate_password_hash(plaintext).decode('utf-8')

    def check_password(self, raw_password):
        return bcrypt.check_password_hash(self.password_hash, raw_password)

    @classmethod
    def create(cls, email, password, **kwargs):
        name = email.split("@")[0]
        return User(email=email, password_hash=User.make_password(password), name=name,
                    **kwargs)

    @staticmethod
    def authenticate(email, password):
        user = User.query.with_entities(User.email).filter(User.email.ilike(email)).first()
        if user is not None:
            user = user[0]
            user = User.query.filter(User.email == user).first()
            if user and user.check_password(password):
                return user
        return False


class NationalRequired(db.Model):  # only admin can post in this level.
    STATUS_APPROVED = 0   # public - can only be set by admin
    STATUS_SUBMITTED = 1  # viewable by user/admin
    STATUS_DRAFT = 2  # viewable by user
    STATUS_DELETED = 3

    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(100), unique=True)
    title = db.Column(db.String(255), unique=True)
    intro = db.Column(db.Text)  # this is boilerplate
    scope = db.Column(db.Text)  # this is boilerplate
    org = db.Column(db.Text)  # this is boilerplate
    resp = db.Column(db.Text)  # this is boilerplate
    qa_workflow = db.Column(db.Text)  # boilerplate + form
    status = db.Column(db.SmallInteger, default=STATUS_DRAFT)
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    created_timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    #modified_timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        self.slug = ''
        if self.id:
            self.slug = slugify(self.title)

    def __repr__(self):
        return '<Entry: %s>' % self.id


class Project(db.Model):
    STATUS_APPROVED = 0   # public - can only be set by admin
    STATUS_SUBMITTED = 1  # viewable by user/admin
    STATUS_DRAFT = 2  # viewable by user
    STATUS_DELETED = 3  # Currently deleted can only be set in the admin panel.

    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(100), unique=True)
    title = db.Column(db.String(255), unique=True)
    intro = db.Column(db.Text)
    scope = db.Column(db.Text)
    org = db.Column(db.Text)
    resp = db.Column(db.Text)
    qa_workflow = db.Column(db.Text)
    tech = db.Column(db.Text)
    data = db.Column(db.Text)
    sysadmin = db.Column(db.Text)
    qa_intro = db.Column(db.Text)
    qa_workflow = db.Column(db.Text)
    qa_proposal = db.Column(db.Text)
    qa_plans = db.Column(db.Text)
    qa_review = db.Column(db.Text)
    dm_plan = db.Column(db.Text)
    status = db.Column(db.SmallInteger, default=STATUS_DRAFT)
    created_timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    modified_timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        self.slug = ''
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return '<Entry: %s>' % self.title


class Plan(db.Model):
    # Currently not in use, but is an anticipated use.

    STATUS_APPROVED = 0   # public - can only be set by admin
    STATUS_SUBMITTED = 1  # viewable by user/admin
    STATUS_DRAFT = 2  # viewable by user
    STATUS_DELETED = 3  # deleted - available to admin only

    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(100), unique=True)
    title = db.Column(db.String(128))
    intro = db.Column(db.Text)  # this is boilerplate from national
    scope = db.Column(db.Text)  # this is boilerplate from national
    org = db.Column(db.Text)  # this is boilerplate from national
    resp = db.Column(db.Text)  # this is boilerplate from national
    tech = db.Column(db.Text)  # fillable form.  Boilerplate from local?
    data = db.Column(db.Text)  # fillable form.  Boilerplate from local?
    sysadmin = db.Column(db.Text)  # fillable form.  Boilerplate from local?
    qa_intro = db.Column(db.Text)  # fillable form.  Boilerplate from local?
    qa_workflow = db.Column(db.Text)  # boilerplate + form
    qa_proposal = db.Column(db.Text)  # boilerplate + form
    qa_plans = db.Column(db.Text)  # boilerplate + form
    qa_review = db.Column(db.Text)  # boilerplate + form

    # TODO: once one thing works we'll add these columns.  Not now though.
    # dm_plan = db.Column(db.Text)  # form
    # dm_roles = db.Column(db.Text)  # form
    # dm_sharing = db.Column(db.Text)  # boilerplate + form
    # dm_mous = db.Column(db.Text)  # boilerplate + form
    # dm_access = db.Column(db.Text)  # boilerplate + form
    # dm_aqu = db.Column(db.Text) # boilerplate
    # dm_aqu_roles = db.Column(db.Text)  # form
    # dm_coll_pol = db.Column(db.Text)  # form
    # dm_pro_pol = db.Column(db.Text)  # form
    # dm_anal_pol = db.Column(db.Text)  #  form
    # dm_stand = db.Column(db.Text)  #  form
    # dm_temp = db.Column(db.Text)  #  form
    # dm_format = db.Column(db.Text)  #  form
    # dm_org = db.Column(db.Text)  #  form

    status = db.Column(db.SmallInteger, default=STATUS_DRAFT)
    created_timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    modified_timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        self.slug = ''
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return '<Entry: %s>' % self.title
