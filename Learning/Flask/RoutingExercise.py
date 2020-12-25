#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    return "<h3> This is the index page </h3>"

@app.route('/invert/<name>')

def invert(name):
    i = len(name)-1
    inverted_name = ''
    while(i >= 0):
        value = name[i]
        inverted_name += value
        i -= 1
    return "<h3> Inverted Name: {} </h3>".format(inverted_name)

if(__name__ == '__main__'):
    #
    app.run()
