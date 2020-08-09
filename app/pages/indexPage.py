from flask import render_template
from jikanpy import Jikan

htmlPage = 'indexPage.html'
title = "Index Page"
jikan = Jikan()

def render():
    animeIndex = jikan.user(username="florisb", request="animelist")
    return render_template(htmlPage, title=title, animeIndex=animeIndex["anime"])
