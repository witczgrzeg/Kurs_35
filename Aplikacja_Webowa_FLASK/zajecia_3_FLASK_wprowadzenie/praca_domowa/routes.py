from flask import Blueprint, render_template, request
from Prosty_sys_księgowy import _get_product_state

systemks_blueprint = Blueprint('strona_glowna', __name__)


@systemks_blueprint.route('/')
def index():
    stan = _get_product_state()
    return render_template("strona_glowna.html", **stan)


