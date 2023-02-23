from flask import request, render_template, url_for, abort
from app.main import bp


@bp.route('/')
def index():
    return render_template('index.html')
