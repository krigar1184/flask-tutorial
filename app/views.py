from datetime import datetime
from app import app
from flask import render_template, flash, redirect, \
    session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from app.forms import LoginForm, EditForm
from app.models import User, Post
from app import login_manager, db, oid


@app.before_request
def before_request():
    g.user = current_user

    if g.user.is_authenticated:
        g.user.last_seen = datetime.utcnow()

        db.session.add(g.user)
        db.session.commit()


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


@oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == '':
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))

    user = User.query.filter_by(email=resp.email).first()

    if user is None:
        nickname = resp.nickname

        if nickname is None or nickname == '':
            nickname = resp.email.split('@')[0]

        nickname = User.make_unique_nickname(nickname)
        user = User(nickname=nickname, email=resp.email)

        db.session.add(user)
        db.session.commit()

        db.session.add(user.follow(user))
        db.session.commit()

    remember_me = False
    if remember_me in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)

    login_user(user, remember=remember_me)
    return redirect(request.args.get('next') or url_for('index'))


@app.errorhandler(404)
def not_found_error(*args, **kwargs):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(*args, **kwargs):
    db.session.rollback()
    return render_template('500.html'), 500


@app.route('/')
@app.route('/index')
@login_required
def index():
    user = g.user
    posts = [
        {
            'author': 'John',
            'body': 'Beautiful day in Bergen!'
        },
        {
            'author': 'Susan',
            'body': 'The Avengers movie was so cool!'
        }
    ]

    posts = user.followed_posts()
    return render_template(
        'index.html',
        title='Home',
        posts=posts,
        user=user)


@app.route('/login', methods=['GET', 'POST'])
@oid.loginhandler
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()

    if form.validate_on_submit():
        session.remember_me = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])

    return render_template(
        'login.html',
        title='Sign in',
        form=form,
        providers=app.config['OPENID_PROVIDERS'])


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/user/<string:nickname>')
@login_required
def user(nickname):
    user = User.query.filter_by(nickname=nickname).first()

    if user is None:
        flash('User %s not found.' % nickname)
        return redirect(url_for('index'))

    posts = Post.query.filter_by(user_id=user.id)

    return render_template(
        'user.html',
        user=user,
        posts=posts)


@app.route('/edit', methods=['GET', 'POST'])
@login_required
def edit():
    form = EditForm(g.user.nickname)

    if form.validate_on_submit():
        g.user.nickname = form.nickname.data
        g.user.about_me = form.about_me.data

        db.session.add(g.user)
        db.session.commit()

        flash('Your changes have been saved')
        return redirect(url_for('index'))
    else:
        form.nickname.data = g.user.nickname
        form.about_me.data = g.user.about_me

        return render_template('edit.html',
                               form=form)


@app.route('/follow/<string:nickname>')
@login_required
def follow(nickname):
    followed = User.query.filter_by(nickname=nickname).first()
    if followed is None:
        flash('User %s not found' % nickname)
        return redirect(url_for('index'))
    elif followed == g.user:
        flash('You can\'t follow yourself!')
        return redirect(url_for('index'))

    u = g.user.follow(followed)
    db.session.add(u)
    db.session.commit()

    flash('You are now following %s!' % nickname)
    return redirect(url_for('user', nickname=nickname))


@app.route('/unfollow/<string:nickname>')
@login_required
def unfollow(nickname):
    followed = User.query.filter_by(nickname=nickname).first()
    if followed is None:
        flash('User %s not found' % nickname)
        return redirect(url_for('index'))
    elif followed == g.user:
        flash('You can\'t follow yourself!')
        return redirect(url_for('index'))
    u = g.user.unfollow(followed)
    db.session.add(u)
    db.session.commit()

    flash('You have stopped following %s' % nickname)
    return redirect(url_for('user', nickname=nickname))
