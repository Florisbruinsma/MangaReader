from flask import render_template


htmlPage = 'mainPage.html'
title = "Main Page"

def render():
    user = {'username': 'Miguel'}
    return render_template(htmlPage, title=title, user=user)
