#!/usr/bin/env python3

from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'THE_SECRET_KEY'

class InformationForm(FlaskForm):
    #
    username = StringField("Username=> ")
    #
    password = StringField("Password=> ")
    #
    submit = SubmitField('Submit')

@app.route('/',methods=['GET','POST'])
def index():
    #
    username = False
    #
    password = False
    #
    form = InformationForm()
    #
    if(form.validate_on_submit()):
        #
        username = form.username.data
        #
        password = form.password.data
        #
    return render_template('index.html',form=form,username=username,password=password)

if(__name__ == '__main__'):
    #
    app.run(debug=True)
