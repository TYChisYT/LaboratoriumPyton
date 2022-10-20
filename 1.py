x = (int)(input('Wprowadż wiek klienta: ' ))
if x < 4:
    print("Wstęp jest bezpłatny")
elif x<=18:
    print('Cena biletu: 10 zł')
else:
    print('Cena biletu: 20 zł')