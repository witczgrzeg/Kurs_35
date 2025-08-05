from flask import Blueprint, render_template, request
from Prosty_sys_księgowy import (
    _get_product_state,
    change_saldo,
    create_new_product,
    update_product
)

systemks_blueprint = Blueprint('strona_glowna', __name__)


@systemks_blueprint.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        match request.form.get("form_type"):
            case "add_product":
                create_new_product(request.form)
            case "buy_product":
                update_product(request.form)
            case "update_saldo":
                try:
                    change_saldo(float(request.form.get("saldo", 0)))
                except (ValueError, TypeError):
                    pass
    return render_template("strona_glowna.html", **_get_product_state())


@systemks_blueprint.route('/historia/', defaults={'start': None, 'koniec': None})
@systemks_blueprint.route('/historia/<int:start>/<int:koniec>')
def historia(start, koniec):
    stan = _get_product_state()
    historia = stan['historia']

    if start is not None and koniec is not None:
        historia = historia[max(0, start):min(len(historia), koniec)]

    return render_template("historia.html", saldo=stan['saldo'], historia=historia)
from flask import Blueprint, render_template, request
from Prosty_sys_księgowy import (
    _get_product_state,
    change_saldo,
    create_new_product,
    update_product
)

systemks_blueprint = Blueprint('strona_glowna', __name__)


@systemks_blueprint.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        match request.form.get("form_type"):
            case "add_product":
                create_new_product(request.form)
            case "buy_product":
                update_product(request.form)
            case "update_saldo":
                try:
                    change_saldo(float(request.form.get("saldo", 0)))
                except (ValueError, TypeError):
                    pass
    return render_template("strona_glowna.html", **_get_product_state())


@systemks_blueprint.route('/historia/', defaults={'start': None, 'koniec': None})
@systemks_blueprint.route('/historia/<int:start>/<int:koniec>')
def historia(start, koniec):
    stan = _get_product_state()
    pelna_historia = stan['historia']
    page_size = 10

    # Domyślne wartości, jeśli nie podano zakresu
    if start is None or koniec is None:
        start = 0
        koniec = page_size

    start = max(0, start)
    koniec = min(len(pelna_historia), koniec)

    fragment_historia = pelna_historia[start:koniec]

    # Przyciski nawigacji
    prev_start = max(0, start - page_size)
    prev_koniec = start

    next_start = koniec
    next_koniec = min(len(pelna_historia), koniec + page_size)

    has_prev = start > 0
    has_next = koniec < len(pelna_historia)

    return render_template(
        "historia.html",
        saldo=stan['saldo'],
        historia=fragment_historia,
        start=start,
        koniec=koniec,
        prev_start=prev_start,
        prev_koniec=prev_koniec,
        next_start=next_start,
        next_koniec=next_koniec,
        has_prev=has_prev,
        has_next=has_next
    )
