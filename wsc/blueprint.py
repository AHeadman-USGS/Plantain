from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from flask_login import login_required
from app import app, db
from models import Project, National, ACCESS, require_access
from wsc.forms import ProjectEntry, ProjectApprove

wsc = Blueprint('wsc', __name__, template_folder='templates')


def get_NatlReq():
    query = National.query.filter(National.id == 1).first_or_404()
    return query


NatlReq = get_NatlReq()


def object_list(template_name, query, **context):
    object_list = query
    return render_template(template_name, object_list=object_list, **context)


def plan_list(template, query, **context):
    valid_statuses = (Project.STATUS_APPROVED, Project.STATUS_DRAFT, Project.STATUS_SUBMITTED)
    query = query.filter(Project.status.in_(valid_statuses))
    if request.args.get('q'):
        search = request.args['q']
        query = query.filter(
            (Project.body.contains(search)) |
            (Project.title.contains(search)))
    return object_list(template, query, **context)


def filter_status_by_user(query):
    if not g.user.is_authenticated:
        return query.filter(Project.status == Project.STATUS_APPROVED)
    else:
        # Allow user to view their own drafts.
        query = query.filter(
            (Project.status == Project.STATUS_APPROVED) |
            ((Project.author_id == g.user) & (Project.status != Project.STATUS_DELETED)))
        return query


def get_entry_or_404(slug, author=None):
    query = Project.query.filter(Project.slug == slug)
    return query.first_or_404()


@wsc.route('/')
def index():
    plans = Project.query.order_by(Project.created_timestamp.desc())
    return render_template('/wsc/index.html', plans=plans, National=NatlReq)


@wsc.route('/<slug>/')
def detail(slug):
    entry = get_entry_or_404(slug)
    return render_template('wsc/detail.html', Project=entry, NationalRequired=NatlReq)


@wsc.route('/create/', methods=['GET', 'POST'])
@require_access(ACCESS['WSC'])
@login_required
def create():
    if request.method == 'POST':
        form = ProjectEntry(request.form)
        if form.validate():
            entry = form.save_entry(Project(author=g.user))
            db.session.add(entry)
            db.session.commit()
            flash('Entry "%s" created successfully.' % entry.title, 'success')
            return redirect(url_for('wsc.detail', slug=entry.slug))
    else:
        form = ProjectEntry()

    return render_template('wsc/create.html', form=form, NationalRequired=NatlReq)


@wsc.route('/<slug>/edit/', methods=['GET', 'POST'])
@login_required
@require_access(ACCESS['WSC'])
def edit(slug):
    entry = get_entry_or_404(slug)
    if request.method == 'POST':
        form = ProjectEntry(request.form, obj=entry)
        entry = form.save_entry(entry)
        db.session.add(entry)
        db.session.commit()
        flash('Entry "%s" update.' % entry.title, 'success')
        return redirect(url_for('wsc.detail', slug=entry.slug))
    else:
        form = ProjectEntry(obj=entry)

    return render_template('wsc/edit.html', Project=entry, form=form, NationalRequired=NatlReq)


@wsc.route('/<slug>/approve/', methods=['GET', 'POST'])
@login_required
@require_access(ACCESS['ADMIN'])
def approve(slug):
    entry = get_entry_or_404(slug)
    if request.method == 'POST':
        form = ProjectApprove(request.form, obj=entry)
        entry = form.save_entry(entry)
        db.session.add(entry)
        db.session.commit()
        flash('Entry "%s" update.' % entry.title, 'success')
        return redirect(url_for('wsc.detail', slug=entry.slug))
    else:
        form = ProjectApprove(obj=entry)

    return render_template('wsc/approve.html', Project=entry, form=form, NationalRequired=NatlReq)
