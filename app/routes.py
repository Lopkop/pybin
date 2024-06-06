from urllib.parse import urlsplit
from uuid import uuid4

from flask import render_template, flash, redirect, url_for, request
import sqlalchemy as sa
from flask_login import current_user, login_user, logout_user, login_required

from app import app, db
from app.forms import LoginForm, PasteForm, RegistrationForm

# @todo: registration, login
from app.models import User, Paste


@app.route('/', methods=['GET', 'POST'])
def index():
    form = PasteForm()
    if form.validate_on_submit():
        paste_uuid = save_paste(paste=form.paste.data, line_count=form.line_count.data, user=current_user)
        return redirect(f'/{paste_uuid}')
    return render_template('index.html', form=form)


@app.post('/api/save_paste')
def save_paste(paste: str, line_count: str, user: User = None):
    paste_uuid = uuid4()
    p = Paste(id=paste_uuid, value=f"""{paste}""", line_count=line_count, author=user, user_id=user.id)
    db.session.add(p)
    db.session.commit()

    return f'{paste_uuid}'


@app.get('/<uuid:paste_url>')
def get_paste(paste_url):
    query = sa.select(Paste).where(Paste.id.like(paste_url))
    paste = db.session.scalar(query)
    return render_template('paste.html', paste=paste)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        login_user(user, remember=True)
        return redirect(url_for('index'))

    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data))
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/profile')
@login_required
def profile():
    pastes = db.session.execute(sa.select(Paste).where(Paste.user_id == current_user.id))
    print(pastes)
    return render_template('profile.html', pastes=pastes)
