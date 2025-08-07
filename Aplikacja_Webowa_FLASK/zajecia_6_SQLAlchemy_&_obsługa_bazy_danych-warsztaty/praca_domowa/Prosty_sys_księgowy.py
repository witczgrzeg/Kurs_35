from datetime import datetime
from models import db, Products, Saldo, Historia

def get_system_state():
    saldo = Saldo.query.first()
    magazyn = Products.query.all()
    historia = Historia.query.order_by(Historia.data.desc()).limit(50).all()
    return {
        "saldo": saldo.amount if saldo else 0,
        "magazyn": magazyn,
        "historia": historia
    }

def _add_history(opis):
    db.session.add(Historia(opis=opis, data=datetime.now()))  # dodajemy datę

def change_balance(change):
    try:
        saldo = Saldo.query.first()
        if saldo is None:
            saldo = Saldo(amount=0)
            db.session.add(saldo)

        saldo.amount += change
        _add_history(f"Zmiana salda: {change:.2f} PLN")
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e

def create_new_product(product_form):
    try:
        nazwa = product_form.get("nazwa", "").strip()
        if not nazwa:
            raise ValueError("Nazwa produktu jest wymagana")

        try:
            cena = float(product_form.get("cena", 0))
            ilosc = int(product_form.get("ilosc", 0))
        except ValueError:
            raise ValueError("Nieprawidłowy format ceny lub ilości")

        produkt = Products.query.filter_by(nazwa=nazwa).first()
        if produkt:
            # Jeśli produkt istnieje, zwiększamy ilość i opcjonalnie aktualizujemy cenę
            produkt.ilosc += ilosc
            produkt.cena = cena  # jeśli chcesz zawsze aktualizować cenę
            _add_history(f"Zaktualizowano produkt: {nazwa}, cena: {cena:.2f} PLN, dodano ilość: {ilosc} szt.")
        else:
            # Dodajemy nowy produkt
            nowy_produkt = Products(nazwa=nazwa, cena=cena, ilosc=ilosc)
            db.session.add(nowy_produkt)
            _add_history(f"Dodano nowy produkt: {nazwa}, cena: {cena:.2f} PLN, ilość: {ilosc} szt.")

        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e

def buy_product(product_id, ilosc):
    try:
        produkt = Products.query.get(product_id)
        if not produkt:
            raise ValueError("Produkt nie istnieje")

        ilosc = int(ilosc)
        if ilosc <= 0:
            raise ValueError("Ilość musi być większa od zera")

        koszt = produkt.cena * ilosc
        saldo = Saldo.query.first()
        if saldo is None or saldo.amount < koszt:
            raise ValueError("Brak wystarczających środków na koncie")

        produkt.ilosc += ilosc
        saldo.amount -= koszt

        _add_history(f"Zakupiono {ilosc} szt. produktu '{produkt.nazwa}' za {koszt:.2f} PLN")
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e

def sell_product(product_id=None, ilosc=0, new_nazwa=None, new_cena=None):
    try:
        ilosc = int(ilosc)
        if ilosc <= 0:
            raise ValueError("Ilość musi być większa od zera")

        saldo = Saldo.query.first()
        if saldo is None:
            saldo = Saldo(amount=0)
            db.session.add(saldo)

        if product_id:
            produkt = Products.query.get(product_id)
            if not produkt:
                raise ValueError("Produkt nie istnieje")

            if produkt.ilosc < ilosc:
                raise ValueError("Brak wystarczającej ilości produktu w magazynie")

            koszt = produkt.cena * ilosc
            produkt.ilosc -= ilosc
            saldo.amount -= koszt  # saldo ujemne, bo wydajesz pieniądze

            _add_history(f"Sprzedano {ilosc} szt. produktu '{produkt.nazwa}' za {koszt:.2f} PLN (saldo zmniejszone)")

        else:
            if not new_nazwa or new_cena is None:
                raise ValueError("Brak nazwy lub ceny nowego produktu")

            new_cena = float(new_cena)
            if new_cena < 0:
                raise ValueError("Cena produktu musi być nieujemna")

            koszt = new_cena * ilosc
            saldo.amount -= koszt  # saldo ujemne, bo wydajesz pieniądze

            nowy_produkt = Products(nazwa=new_nazwa.strip(), cena=new_cena, ilosc=0)
            db.session.add(nowy_produkt)

            _add_history(f"Sprzedano {ilosc} szt. nowego produktu '{new_nazwa}' za {koszt:.2f} PLN (saldo zmniejszone)")

        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e

