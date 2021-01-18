#/usr/bin/env python3

from flask import Flask , render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    rand_ints = []
    for i in range(0,10):
        var = random.randint(0,100)
        rand_ints.append(var)

    return render_template('basic.html',rand_list=rand_ints)

if(__name__ == '__main__'):
    app.run()
