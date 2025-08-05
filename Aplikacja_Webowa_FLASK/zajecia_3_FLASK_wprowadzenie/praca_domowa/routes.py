from flask import Blueprint, render_template, request
from Prosty_sys_księgowy import _get_product_state, change_saldo, create_new_product, update_product


systemks_blueprint = Blueprint('strona_glowna', __name__)


@systemks_blueprint.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        form_type = request.form.get("form_type")
        match form_type:
            case "add_product":
                create_new_product(request.form)
            case "buy_product":
                update_product(request.form)
            case "update_saldo":
                change_saldo(float(request.form.get("saldo")))
            case _:
                pass
    stan = _get_product_state()
    return render_template("strona_glowna.html", **stan)

@systemks_blueprint.route('/historia', methods=['GET', 'POST'])
def historia():
    stan = _get_product_state()
    return render_template("historia.html", saldo=stan['saldo'], historia=stan['historia'])


