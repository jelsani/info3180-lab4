from flask_wtf import FlaskForm
from app import app
from flask_wtf.file import FileField, FileRequired, FileAllowed

class UploadForm(FlaskForm):
    upload = FileField('image', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
