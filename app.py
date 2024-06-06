from flask import Flask, request, render_template, make_response,send_from_directory, redirect, send_file, jsonify
import configparser
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField ,SubmitField
from wtforms.validators import InputRequired, Length
from datetime import datetime, timedelta
import json
import simplejson

data = {'apple': 'cat', 'banana':'dog', 'pear':'fish'}
data_json = "{'apple': 'cat', 'banana':'dog', 'pear':'fish'}"

data_json=simplejson.dumps(data)
print(str(simplejson.dumps(data))) # outputs data
print(data_json)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

config = configparser.ConfigParser()
config.read('config.ini')

cookie_name=config['DEFAULT']['cookie_name']
cookie_domain=config['DEFAULT']['cookie_domain']
cookie_lifespan=int(config['DEFAULT']['cookie_lifespan'])
cookie_expires=datetime.now() + timedelta(days=cookie_lifespan)

class RegisterForm(FlaskForm):
    username = StringField('Username', render_kw={"placeholder": "Your Name"}, validators=[InputRequired('Username required!'),
               Length(min=5, max=25, message='Username must be in 5 to 25 characters')])
    contact = StringField('Contact', render_kw={"placeholder": "Contact Email"}, validators=[InputRequired('Password required')])
    receive_updates = BooleanField('Monthly Updates', validators=[])
    receive_alerts = BooleanField('New Announcements', validators=[])
    submit = SubmitField('Submit')

def create_cookie(response,data=None):
    response=make_response(response)
    try:
        cookie_value=request.cookies.get(cookie_name)
        decoded_data=json.loads(cookie_value)
    except:
        decoded_data={'username':'','email':'','registered':'','default':'', 'updates': '', 'notifications': ''}
    if data == None:
        data=json.dumps(decoded_data)
    else:
        decoded_data.update(data)
        data=json.dumps(decoded_data)
    response.set_cookie(cookie_name, data, expires=cookie_expires, samesite='lax', domain=cookie_domain)
    return response

@app.route('/create_cookie')
def session():
    response=make_response()
    data = {'nana': 'nana'}
    response=create_cookie(response,data)
    return response

@app.route('/read_cookie/<key>')
@app.route('/read_cookie')
def read_cookie(key=None):
    try:
        cookie=request.cookies.get(cookie_name)
        value=json.loads(cookie)
    except:
        value={}
    if key == None:
        return value
    else:
        return value[key]

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
            updates='None'

        try:
            notifications=request.form['receive_alerts']
            notifications='Notifications'
        except:
            notifications='None'

        registration_details=str(request.remote_addr)+' - '+username+' - '+contact+' - '+updates+' - '+notifications+'  registered'
        print(registration_details)
        response=thanks(username)
        response=create_cookie(response,{'username': username, 'email': contact, 'registered': str(datetime.now()), 'updates': updates, 'notifications': notifications})
        return response

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
