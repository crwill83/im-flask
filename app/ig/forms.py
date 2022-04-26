from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class CreatePostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    img_url = StringField('Image URL', validators=[DataRequired()])
    caption = StringField('Caption', validators=[])
    submit = SubmitField()

class UpdatePostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    img_url = StringField('Image URL', validators=[DataRequired()])
    caption = StringField('Caption', validators=[])
    submit = SubmitField()

#### add tool
class AddToolForm(FlaskForm):
    item_name = StringField('Item', validators=[DataRequired()])
    item_model = StringField('Model', validators=[DataRequired()])
    item_serial = StringField('Serial Number', validators=[DataRequired()])
    item_description = StringField('Description', validators=[])
    item_image = StringField('Image URL', validators=[])
    submit = SubmitField()

class EditToolForm(FlaskForm):
    item_name = StringField('Item', validators=[DataRequired()])
    item_model = StringField('Model', validators=[DataRequired()])
    item_serial = StringField('Serial Number', validators=[DataRequired()])
    item_description = StringField('Description', validators=[])
    item_image = StringField('Image URL', validators=[])
    submit = SubmitField()

class AddToCart(FlaskForm):
    submit = SubmitField()

