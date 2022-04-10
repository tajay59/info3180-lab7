# Add any form classes for Flask-WTF here

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired, DataRequired
from wtforms import Form, TextAreaField, FileField

class UploadForm(FlaskForm):
    photo        = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!') ])
    description  = TextAreaField('Description',validators=[DataRequired()])