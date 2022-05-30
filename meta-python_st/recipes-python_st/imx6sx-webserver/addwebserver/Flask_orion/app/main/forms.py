# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from flask_babel import _, lazy_gettext as _l
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError,  Email, EqualTo, Length
from app.models import User

class EditProfileForm(FlaskForm):
    username = StringField(_l('Username'))
    password = PasswordField(_l('Password'))
    submit = SubmitField(_l('Submit'))

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

class IndexForm(FlaskForm):
    ip = StringField(_l('IP'), validators=[DataRequired()])
    mask = StringField(_l('Mask'), validators=[DataRequired()])
    gate = StringField(_l('Gate'), validators=[DataRequired()])
    ied = StringField(_l('IED'), validators=[DataRequired()])
    submit = SubmitField(_l('Submit'))

# class LangaugeForm(FlaskForm):
