################################################################################
#########################   Setting up forms for posts  ########################
################################################################################

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from flask_ckeditor import CKEditorField

class BlogPostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    #text = TextAreaField('Text', validators=[DataRequired()])
    text = CKEditorField('Text', validators=[DataRequired()])
    submit = SubmitField('Post')
