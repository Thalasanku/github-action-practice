#checking for Linter 2nd time by adding wrong details

import os  # Error 1: Unused import (F401)
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    unused_var = 42  # Error 2: Unused local variable (F841)
    return render_template('index.html')


@app.route('/health')
def health():
    x=1+2 # Error 3: Missing whitespace around operators (E225)
    print(undefined_variable)  # Error 4: Undefined name (F821)
    return 'Server is up and running'
