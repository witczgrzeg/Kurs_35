a = 10
b = 10
print(a is b)  # True – Python cache’uje małe liczby (-5 do 256)

a = 1000
b = 1000
print(a is b)  # może być False – dla dużych liczb Python tworzy nowe obiekty
