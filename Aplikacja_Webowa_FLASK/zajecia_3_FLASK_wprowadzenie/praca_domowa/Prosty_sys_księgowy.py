from FileHandler import file_handler, save_temporary_data

def get_products():
    return file_handler.produkty

def _get_product_state():
    return {
        "saldo": file_handler.saldo,
        "historia": file_handler.historia,
        "magazyn": get_products(),
    }

def create_new_product(product_form: dict):
    nazwa = product_form.get("nazwa")
    cena = float(product_form.get("cena"))
    ilosc = int(product_form.get("ilosc"))

    koszt = cena * ilosc

    produkt = next((produkt for produkt in file_handler.produkty if produkt["nazwa"] == nazwa), None)
    if produkt:
        produkt["ilosc"] += ilosc
    else:
        file_handler.produkty.append({
            "nazwa": nazwa,
            "cena": cena,
            "ilosc": ilosc,
        })

    file_handler.saldo -= koszt
    file_handler.historia.append(f"Sprzedaż: {nazwa}, cena: {cena}, ilość: {ilosc}, wpływ: {koszt} zł")

    save_temporary_data(file_handler, file_handler.produkty, file_handler.saldo, file_handler.historia)


def update_product(product_form: dict):
    nazwa = product_form.get("nazwa")
    ilosc = int(product_form.get("ilosc"))

    produkt = next((produkt for produkt in file_handler.produkty if produkt["nazwa"] == nazwa), None)
    if not produkt:
        raise ValueError("Produkt nie istnieje w magazynie")

    koszt = produkt["cena"] * ilosc
    if file_handler.saldo < koszt:
        raise ValueError("Saldo niewystarczające na zakup")

    produkt["ilosc"] -= ilosc
    file_handler.saldo += koszt
    file_handler.historia.append(f"Zakup: {nazwa}, cena: {produkt['cena']}, ilość: {ilosc}, koszt: {koszt} zł")

    save_temporary_data(file_handler, file_handler.produkty, file_handler.saldo, file_handler.historia)


def change_saldo(amount: float):
    if file_handler.saldo + amount < 0:
        raise ValueError("Wartość nie może być ujemna")
    file_handler.saldo += amount
    save_temporary_data(file_handler, file_handler.produkty, file_handler.saldo, file_handler.historia)
