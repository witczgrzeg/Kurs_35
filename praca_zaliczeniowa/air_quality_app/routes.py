from flask import Blueprint, render_template

main_page = Blueprint('main_page', __name__)

@main_page.route('/')
def index():
    return render_template("main_page.html")



@main_page.route('/historia')
def historia():
    return render_template("historia.html")
