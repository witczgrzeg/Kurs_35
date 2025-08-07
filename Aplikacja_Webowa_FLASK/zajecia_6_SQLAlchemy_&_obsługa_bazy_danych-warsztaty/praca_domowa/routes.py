from flask import Blueprint, render_template, request
from Prosty_sys_księgowy import (
    get_system_state,
    change_balance,
    create_new_product,
    buy_product,
    sell_product
)

systemks_blueprint = Blueprint('strona_glowna', __name__)

@systemks_blueprint.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        form_type = request.form.get("form_type")

        try:
            if form_type == "add_product":
                create_new_product(request.form)

            elif form_type == "buy_product":
                product_id = int(request.form.get("product_id"))
                ilosc = int(request.form.get("ilosc"))
                buy_product(product_id, ilosc)

            elif form_type == "sell_product":
                ilosc = int(request.form.get("ilosc"))

                product_id = request.form.get("product_id")
                new_nazwa = request.form.get("new_nazwa", "").strip()
                new_cena = request.form.get("new_cena")

                if product_id:
                    sell_product(product_id=int(product_id), ilosc=ilosc)
                elif new_nazwa and new_cena:
                    sell_product(product_id=None, ilosc=ilosc, new_nazwa=new_nazwa, new_cena=new_cena)
                else:
                    raise ValueError("Musisz wybrać istniejący produkt lub podać nazwę i cenę nowego produktu")

            elif form_type == "update_saldo":
                amount = float(request.form.get("saldo", 0))
                change_balance(amount)

        except (ValueError, TypeError) as e:
            # Tutaj możesz dodać logowanie błędów lub flashowanie wiadomości
            print(f"Błąd przetwarzania formularza: {e}")

    stan = get_system_state()
    return render_template("strona_glowna.html", **stan)


@systemks_blueprint.route('/historia/', defaults={'start': None, 'koniec': None})
@systemks_blueprint.route('/historia/<int:start>/<int:koniec>')
def historia(start, koniec):
    stan = get_system_state()
    pelna_historia = stan['historia']
    page_size = 10

    if start is None or koniec is None:
        start = 0
        koniec = page_size

    start = max(0, start)
    koniec = min(len(pelna_historia), koniec)

    fragment_historia = pelna_historia[start:koniec]

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
