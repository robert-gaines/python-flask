#!/usr/bin/env python3

from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('base.html')

@app.route('/home/<integer>')

def squared(integer):
    integer = int(integer)
    if(type(integer) == int):
        result = integer * integer
    else:
        result = 'Not an integer!'
    return render_template('squared.html',result=result)

if(__name__ =='__main__'):
    app.run()
