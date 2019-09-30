import os
from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from app import app, db
from flask_login import login_required
from models import NationalRequired, ACCESS, require_access
from National.forms import NationalEntry

natl = Blueprint('National', __name__, template_folder='templates')


def get_entry_or_404(slug, author=None):
    query = NationalRequired.query.filter(NationalRequired.slug == slug)
    return query.first_or_404()


@natl.route('/')
def index():
    entry = NationalRequired.query.filter(NationalRequired.id == 1).first_or_404()
    return render_template('National/index.html', NationalRequired=entry)


@natl.route('/<slug>/')
def detail(slug):
    entry = get_entry_or_404(slug)
    return render_template('National/detail.html', NationalRequired=entry)


@natl.route('/create/', methods=['GET', 'POST'])
@login_required
@require_access(ACCESS['ADMIN'])
def create():
    if request.method == 'POST':
        form = NationalEntry(request.form)
        if form.validate():
            entry = form.save_entry(NationalRequired())
            db.session.add(entry)
            db.session.commit()
            flash('Entry "%s" created successfully.' % NationalRequired.id, 'success')
            return redirect(url_for('index'))
    else:
        form = NationalEntry()

    return render_template('National/create.html', form=form)


@natl.route('/<slug>/edit', methods=['GET','POST'])
@login_required
@require_access(ACCESS['ADMIN'])
def edit(slug):
    entry = get_entry_or_404(slug)
    if request.method == 'POST':
        form = NationalEntry(request.form, obj=entry)
        entry = form.save_entry(entry)
        db.session.add(entry)
        db.session.commit()
        flash('Entry "%s" update.' % entry.title, 'success')
        return redirect(url_for('wsc.detail', slug=entry.slug))
    else:
        form = NationalEntry(obj=entry)

    return render_template('National/edit.html', NationalRequired=entry, form=form)