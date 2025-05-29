import re

regex_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

wiersz_o_emailach = """
W cyfrowym świecie, gdzie dane fruwają,
Maile codziennie skrzynki zalewają.
Pisze Ada z rana – ada.nowak@poczta.pl,
A potem wiadomość – od Marka sygnał.

marek123@onet.eu – w tytule "Pilne",
Choć treść jak zwykle: "Spotkajmy się w Wilnie".
zosia.kwiat@firma.com przysyła fakturę,
A admin@bezpiecznie.net – alert o strukturze.

Na koniec robot7@gmail.com pisze: "Hello!",
Choć nikt nie wie, czy to człowiek, czy AI zgoła...
"""

def is_valid_email(email: str) -> bool:
    valid_email = re.match(regex_pattern, email)
    print(valid_email)
    return valid_email is not None


def is_valid_email_in_text(text: str) -> list:
    # text = text.split(" ")
    # for word in text:
    #     emails = re.findall(regex_pattern, word)
    #     print(emails)
    emails = re.findall(regex_pattern, text)
    print(emails)

validation1 = is_valid_email("<EMAIL>")
print(validation1)
is_valid_email("michal@gmail.com")

emails = is_valid_email_in_text(wiersz_o_emailach)
