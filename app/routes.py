from app import app
from flask import render_template, redirect, url_for

@app.route('/')
def home():
    return redirect(url_for('ig.posts'))


@app.route('/about')
def iCanNameThisAnything():
    return render_template('about.html')

