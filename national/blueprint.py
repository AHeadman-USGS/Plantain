import os
from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from app import app, db
from flask_login import login_required
from models import ACCESS, require_access, National
from national.forms import NationalEntry, NationalMaster

natl = Blueprint('national', __name__, template_folder='templates')


def get_entry_or_404(slug, author=None):
    query = National.query.filter(National.slug == slug)
    return query.first_or_404()


@natl.route('/')
def index():
    entry = National.query.filter(National.id == 1).first_or_404()
    return render_template('national/index.html', NationalRequired=entry)


@natl.route('/<slug>/')
def detail(slug):
    entry = get_entry_or_404(slug)
    return render_template('national/detail.html', NationalRequired=entry)


@natl.route('/create/', methods=['GET', 'POST'])
@login_required
@require_access(ACCESS['ADMIN'])
def create():
    if request.method == 'POST':
        form = NationalMaster(request.form)
        if form.validate():
            entry = form.save_entry(National())
            db.session.add(entry)
            db.session.commit()
            flash('Entry "%s" created successfully.' % National.id, 'success')
            return redirect(url_for('index'))
    else:
        form = NationalMaster()

    return render_template('national/create.html', form=form)


@natl.route('/<slug>/edit', methods=['GET', 'POST'])
@login_required
@require_access(ACCESS['ADMIN'])
def edit(slug):
    entry = get_entry_or_404(slug)
    if request.method == 'POST':
        form = NationalMaster(request.form, obj=entry)
        entry = form.save_entry(entry)
        db.session.add(entry)
        db.session.commit()
        flash('Entry "%s" update.' % entry.title, 'success')
        return redirect(url_for('national.detail', slug=entry.slug))
    else:
        form = NationalMaster(obj=entry)

    return render_template('national/edit.html', NationalRequired=entry, form=form)