from flask import g, render_template, redirect, flash, url_for, request
from flask_bcrypt import check_password_hash
from flask_login import current_user, login_user, logout_user, login_required
import models
from models import require_access, ACCESS
from app import app, db, login_manager
from forms import LoginForm, RegisterForm


def get_NatlReq():
    query = models.NationalRequired.query.filter(models.NationalRequired.id == 1).first_or_404()
    return query



@login_manager.user_loader
def load_user(id):
    return models.User.query.get(int(id))


@app.before_request
def get_current_user():
    g.user = current_user


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/resources")
def resources():
    return render_template("resources.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/national/")
@login_required
def national():
    entry = models.National.query.filter(models.National.id == 1).first_or_404()
    return render_template("/national/index.html", NationalRequired=entry)


@app.route("/wsc/create")
@login_required
def create():
    return render_template("/wsc/create.html")


@app.route("/explore")
def explore():
    NatlReq = get_NatlReq()
    plans = models.Project.query.order_by(models.Project.created_timestamp.desc())
    return render_template('explore.html', plans=plans, National=NatlReq)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = models.User.create(email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("register_successful"))
    return render_template("register.html", form=form)


@app.route("/register_successful")
def register_successful():
    return render_template("register_successful.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        flash('You are already logged in.', 'info')
        return redirect(url_for('index'))

    if request.method == "POST":
        form = LoginForm()
        if form.validate_on_submit():
            email = request.form.get('email')
            password = request.form.get('password')
            existing_user = models.User.query.filter_by(email=email).first()
            if not (existing_user and existing_user.check_password(password)):
                flash("Invalid email or password", "danger")
                return render_template("login.html", form=form)
            login_user(existing_user)
            return redirect(request.args.get("next") or url_for("index"))

        if form.errors:
            flash(form.errors, "danger")
            return render_template("login.html", form=form)

    else:
        form = LoginForm()
    return render_template("login.html", form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))