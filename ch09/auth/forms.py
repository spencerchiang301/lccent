from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('帳密', validators=[DataRequired()])
    password = PasswordField('密碼', validators=[DataRequired()])
    submit = SubmitField('登入')

class EditForm(FlaskForm):
    password = PasswordField("新密碼", validators=[DataRequired(), Length(min=4)])
    submit = SubmitField('更新密碼')