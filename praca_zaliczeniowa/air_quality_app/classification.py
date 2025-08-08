def classify_air_quality(parameter, value):
    if value is None:
        return "Brak danych"

    param = parameter.lower()

    if param == "pm25":
        if value <= 12:
            return "GOOD ✅"
        elif value <= 35.4:
            return "MEDIUM ⚠️"
        else:
            return "BAD ❌"

    elif param == "pm10":
        if value <= 50:
            return "GOOD ✅"
        elif value <= 100:
            return "MEDIUM ⚠️"
        else:
            return "BAD ❌"

    elif param == "co":
        co_mg_m3 = value / 1000
        if co_mg_m3 <= 10:
            return "GOOD ✅"
        elif co_mg_m3 <= 30:
            return "MEDIUM ⚠️"
        else:
            return "BAD ❌"

    elif param == "no2":
        if value <= 40:
            return "GOOD ✅"
        elif value <= 100:
            return "MEDIUM ⚠️"
        else:
            return "BAD ❌"

    elif param == "o3":
        if value <= 100:
            return "GOOD ✅"
        elif value <= 180:
            return "MEDIUM ⚠️"
        else:
            return "BAD ❌"

    elif param == "so2":
        if value <= 20:
            return "GOOD ✅"
        elif value <= 75:
            return "MEDIUM ⚠️"
        else:
            return "BAD ❌"

    elif param == "bc":
        if value <= 1:
            return "GOOD ✅"
        elif value <= 3:
            return "MEDIUM ⚠️"
        else:
            return "BAD ❌"

    elif param == "no":
        if value <= 10:
            return "GOOD ✅"
        elif value <= 20:
            return "MEDIUM ⚠️"
        else:
            return "BAD ❌"

    else:
        return "Brak danych"
