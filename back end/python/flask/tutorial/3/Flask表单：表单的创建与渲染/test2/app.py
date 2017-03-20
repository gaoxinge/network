#coding=utf-8
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)

class LoginForm(FlaskForm):
    email = StringField(u'邮箱', validators=[
                DataRequired(message=u'邮箱不能为空'), Length(1, 64),
                Email(message=u'请输入有效的邮箱地址，比如：username@domain.com')
                ])
    password = PasswordField(u'密码', validators=[
                DataRequired(message=u'密码不能为空')
                ])
    submit = SubmitField(u'登入')

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        result = u'邮箱: {email}\n密码: {password}'.format(
                    email=form.email.data,
                    password=form.password.data
                    )
        return result
    return render_template('login.html', form=form)
     
if __name__ == '__main__':
    app.run()