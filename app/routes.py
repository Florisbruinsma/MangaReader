from app import app
from flask import render_template
import sys
# sys.path.append('/pages')
from .pages import mainPage


@app.route('/')
@app.route('/index')
def index():
    return mainPage.render()