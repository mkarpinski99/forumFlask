from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, EqualTo, Length
from app.models import User, Category


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw={"placeholder": "Username"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder": "Password"})
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')


class PostForm(FlaskForm):
    post = TextAreaField('Say something', validators=[
        DataRequired(), Length(min=1, max=500)], render_kw={"placeholder": "Add your post here"})
    submit = SubmitField('Submit')


class EditPostForm(FlaskForm):
    post = TextAreaField('Say something', validators=[
        DataRequired(), Length(min=1, max=500)], render_kw={"placeholder": "Edit post here"})
    submit = SubmitField('Edit')


class CategoryForm(FlaskForm):
    category = TextAreaField('New category', validators=[
        DataRequired(), Length(min=1, max=30)], render_kw={"placeholder": "New category"})
    details = TextAreaField('New category', validators=[
        DataRequired(), Length(min=1, max=50)], render_kw={"placeholder": "Details"})
    submit = SubmitField('Submit')

    def validate_category(self, category):
        category = Category.query.filter_by(name=category.data).first()
        if category is not None:
            raise ValidationError('Category already exists!')


class ThreadForm(FlaskForm):
    thread = TextAreaField('New thread', validators=[
        DataRequired(), Length(min=1, max=30)], render_kw={"placeholder": "New thread"})
    submit = SubmitField('Submit')


