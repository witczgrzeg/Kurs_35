"""

   Aplikacja śledząca jakość powietrza dla danej lokalizacji:

   Wykorzystując API openAQ (https://openaq.org/), aplikacja prezentuje
   użytkownikowi dane o stężeniu zanieczyszczeń w wybranej lokalizacji.
   Użytkownik wprowadza nazwę miasta lub regionu, a aplikacja wyświetla tabelę z
   bieżącymi danymi o jakości powietrza oraz historyczny wykres zmian stężenia
   poszczególnych zanieczyszczeń.

   W wersji rozszerzonej aplikacja oferuje system powiadomień o przekroczeniach
   norm oraz możliwość porównywania danych pomiędzy różnymi miejscowościami.

"""

from openaq import OpenAQ

#import from API - Finding locations near a point
# """
# client = OpenAQ(api_key="YOUR-OPENAQ-API-KEY")
# client.locations.list(coordinates=[136.90610, 35.14942], radius=12000, limit=1000)
# client.close()
#
# """
client = OpenAQ(api_key= "9842cf2ba34018b9ff7e2f1593819e26e814a4f71f0001e65bf688f92e25c865")