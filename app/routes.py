from app import app
from flask import render_template
import sys
# sys.path.append('/pages')
from .pages import mainPage, indexPage


@app.route('/')
@app.route('/home')
def home():
    return mainPage.render()


@app.route('/index')
def index():
    return indexPage.render()