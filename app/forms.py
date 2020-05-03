from app import app
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed


class UploadForm(FlaskForm):
    pictures = FileField('pictures', validators = [FileRequired(), FileAllowed(['jpg', 'png', 'Images only!'])])