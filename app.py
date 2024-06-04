from flask import Flask, request, render_template, make_response,send_from_directory, redirect, send_file, jsonify
import configparser
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField ,SubmitField
from wtforms.validators import InputRequired, Length
from datetime import datetime, timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

config = configparser.ConfigParser()
config.read('config.ini')

class RegisterForm(FlaskForm):
    username = StringField('Username', render_kw={"placeholder": "Your Name"}, validators=[InputRequired('Username required!'),
               Length(min=5, max=25, message='Username must be in 5 to 25 characters')])
    contact = StringField('Contact', render_kw={"placeholder": "Contact Email"}, validators=[InputRequired('Password required')])
    receive_updates = BooleanField('Monthly Updates', validators=[])
    receive_alerts = BooleanField('New Announcements', validators=[])
    submit = SubmitField('Submit')

def create_cookie():
    response=make_response()
    expires=datetime.now() + timedelta(days=7)
    response.set_cookie('downcharmed', 'test', expires=expires, domain='.pknw1.co.uk')
    return response

@app.route('/register', methods=['GET', 'POST'])
def register():
    form=RegisterForm()

    if request.method == 'GET':
        response=render_template('before.html')
        register_form=render_template('register.html', form=form)
        response=response+register_form+render_template('after.html')
        return response

    if request.method == 'POST':
        username=request.form['username']
        contact=request.form['contact']
        try:
            updates=request.form['receive_updates']
            updates='Newsletter'
        except:
            updates='No Newsletter'

        try:
            notifications=request.form['receive_alerts']
            notifications='Notifications'
        except:
            notifications='No Notifications'

        registration_details=str(request.remote_addr)+' - '+username+' - '+contact+' - '+updates+' - '+notifications+'  registered'
        print(registration_details)
        expires=datetime.now() + timedelta(days=7)
        response=make_response()
        response=thanks(username)
        response=make_response(response)
        response.set_cookie('downcharmed', 'test', samesite=lax, expires=expires, domain='.pknw1.co.uk')

        return response
        #return redirect("/thanks/"+username, code=302)

@app.route('/thanks/<username>')
@app.route('/registered/<username>')
def thanks(username):
    socials=''
    for site in config.sections():
        if site == 'Register':
            socials=socials
        else:
            link=config[site]['link']
            info=config[site]['info']
            entry=render_template('social.html', site=site, info=info, link=link)
            socials=socials+entry
        response=render_template('before.html')
        response=response+socials
        response=response+render_template('after.html')
    return response

@app.route('/')
def index():
    socials=''
    for site in config.sections():
        link=config[site]['link']
        info=config[site]['info']
        entry=render_template('social.html', site=site, info=info, link=link)
        socials=socials+entry
    response=render_template('before.html')
    response=response+socials
    response=response+render_template('after.html')
    return response



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
