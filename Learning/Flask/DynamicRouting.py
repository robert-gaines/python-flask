#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    return "<h3> The Index Page </h3>"

@app.route('/info')

def info():
    return "<h3> The Info Page </h3>"

@app.route('/user/<name>')

def user(name):
    return "<h3> This is a page for: {} </h3>".format(name)

if(__name__ == '__main__'):
    app.run()
