#Napisz skrypt działający jak prosty kalkulator, który potrafi dodawać, odejmować, mnożyć, dzielić oraz obliczać potęgę.
print ('''
Jaką operację chcesz wykonać?
1) dodawanie
2) odejmowanie
3) mnożenie
4) dzielenie
5) potęgowanie
''')
a=int(input('Podaj operację: '))
d=int(input('Podaj argument 1: '))
b=int(input('Podaj argument 2: '))
if a == 1:
    x=d +b
elif a == 2:
    x= d-b
elif a == 3:
    x = d * b
elif a == 4:
    if b == 0:
        print('Nie można dzielić przez 0')
        exit()
    x = d / b
elif a == 5:
    x= d**b
else:
    Print('Niepoprawną operacja')

print('Wynik: ', x)