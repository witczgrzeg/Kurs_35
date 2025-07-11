users = [
    {
        "name": "Jan Kowalski",
        "age": 30,
        "email": "jan.kowalski@gmail.com",
        "address": "Warszawa, Polska",
        "zip_code": "00-001",
        "city": "Warszawa",
        "country": "Polska",

    },
    {
        "name": "Anna Nowak",
        "age": 25,
        "email": "anna.nowak@gmail.com",
        "address": "Kraków, Polska",
        "zip_code": "31-001",
        "city": "Kraków",
        "country": "Polska",
    },
    {
        "name": "Piotr Wiśniewski",
        "age": 40,
        "email": "piotr.wisniewski@gmail.com",
        "address": "Wrocław, Polska",
        "zip_code": "50-001",
        "city": "Wrocław",
        "country": "Polska",
    }
]

def address_parser_for_users(users):
    parsed_users = []
    for user in users:
        parsed_users.append(
            {
                "name": user.get("name"),
                "age": user.get("age"),
                "email":user.get("email"),
                "full_address": user.get("address") + "," + user.get("zip_code") + "," + user.get("city") + "," + user.get("country")
            }
        )
    return parsed_users
users_in_our_system = address_parser_for_users(users)
print(users_in_our_system)

def address_parser_for_users_generator(users):
    for user in users:
        yield {
                "name": user.get("name"),
                "age": user.get("age"),
                "email":user.get("email"),
                "full_address": user.get("address") + "," + user.get("zip_code") + "," + user.get("city") + "," + user.get("country")
            }

generator = address_parser_for_users_generator(users)
print(generator)
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))