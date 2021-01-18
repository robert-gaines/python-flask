#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    #
    return "<h3>This is the index</h3>"

@app.route('/info')

def info():
    #
    return "<h3> A page other than the index </h3>"

if(__name__ == '__main__'):
    #
    app.run()
