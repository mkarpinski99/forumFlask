from app import app, db
from app.forms import LoginForm, RegistrationForm, PostForm, ThreadForm, CategoryForm, EditPostForm
from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user
from app.models import User, Post, Category, Thread
from datetime import date, datetime


@app.route('/', methods=['GET', 'POST'])
def index():
    form = CategoryForm()
    if form.validate_on_submit():
        category = Category(name=form.category.data, details=form.details.data)
        db.session.add(category)
        db.session.commit()
        flash('Category created successfully')
        return redirect(url_for('index'))
    categories = db.session.query(Category)
    return render_template("index.html", title='ForumFlask', categories=categories, form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='SingIn', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, type='Uzytkownik')
        user.generatePassword(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('signup.html', title='Register', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/thread/<id>', methods=['GET', 'POST'])
def thread(id):
    form = ThreadForm()
    if current_user.is_authenticated & form.validate_on_submit():
        thread = Thread(subject=form.thread.data, date=date.today(), category=id)
        db.session.add(thread)
        db.session.commit()
        flash('Thread created successfully!')
        return redirect(url_for('post', id=thread.id))
    threads = db.session.query(Thread).filter_by(category=id)
    return render_template('threads.html', threads=threads, form=form)


@app.route('/post/<id>', methods=['GET', 'POST'])
def post(id):
    form = PostForm()
    editForm = EditPostForm()
    if form.validate_on_submit():
        post = Post(content=form.post.data, user=current_user.id, date=datetime.now(), thread=id)
        db.session.add(post)
        db.session.commit()
        flash('Your post is now live!')
        return redirect(url_for('post', id=id))
    # posts = db.session.query(Post.id, Post.content, Post.date, User.username).filter_by(thread=id).group_by(Post.id)
    posts = db.session.query(Post, User).filter(Post.thread == id).join(User, User.id==Post.user)
    db.session.query(Thread).filter(Thread.id == id).update({'visits': Thread.visits + 1})
    db.session.commit()
    return render_template('post.html', posts=posts, form=form, editForm=editForm)


@app.route('/delete_post<id>', methods=['POST'])
def delete_post(id):
    post = db.session.query(Post).filter(Post.id == id).first()
    thread = post.thread
    if current_user.type != 'Uzytkownik' or current_user.id == post.user:
        db.session.delete(post)
        db.session.commit()
        flash('Post deleted!')
        return redirect(url_for('post', id=thread))
    flash('Chicen face, something went wrong!')
    return redirect(url_for('post', id=thread))


@app.route('/delete_thread<id>', methods=['POST'])
def delete_thread(id):
    thread = db.session.query(Thread).filter(Thread.id == id).first()
    category = thread.category
    if current_user.type != 'Uzytkownik':
        db.session.delete(thread)
        db.session.commit()
        flash('Thread deleted!')
        return redirect(url_for('thread', id=category))
    flash('Chicen face, something went wrong!')
    return redirect(url_for('thread', id=category))


@app.route('/update_post<id>', methods=['POST'])
def update_post(id):
    post = db.session.query(Post).filter(Post.id == id).first()
    thread = post.thread
    form = EditPostForm()
    if current_user.type != 'Uzytkownik' or current_user.id == post.user:
        db.session.query(Post).filter(Post.id == id).update({'content': form.post.data})
        db.session.commit()
        flash('Post updated!')
        return redirect(url_for('post', id=thread))
    flash('Chicen face, something went wrong!')
    return redirect(url_for('post', id=thread))
