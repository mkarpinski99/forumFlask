from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, index=True, unique=True, nullable=False)
    password = db.Column(db.String)
    type = db.Column(db.String, db.CheckConstraint('type == \'Administrator\' or type == \'Moderator\' or type == \'Uzytkownik\''))

    def generatePassword(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return self.id, self.username, self.password


class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    details = db.Column(db.String, nullable=False)

    def __repr__(self):
        return self.id, self.name, self.details


class Thread(db.Model):
    __tablename__ = 'forumThread'
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String, nullable=False)
    visits = db.Column(db.Integer, default=0)
    date = db.Column(db.Date, nullable=False)
    category = db.Column(db.Integer, db.ForeignKey('category.id'))

    def __repr__(self):
        return self.id, self.subject, self.visits, self.date, self.category


class Post(db.Model):
    __tablename__ = 'thread'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=True)
    date = db.Column(db.DateTime, nullable=False)
    thread = db.Column(db.Integer, db.ForeignKey('thread.id'))
    user = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return self.id, self.content, self.date, self.thread, self.user


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

