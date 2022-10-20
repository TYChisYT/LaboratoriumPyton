różnica= ord('a') - ord('A')
a =input('Podaj literę: ')
if 'a'<=a<='z':
    x = chr(ord(a) - różnica)
    print(x)
elif 'A' <=a<='z':
    x = chr(ord(a) + różnica)
    print(x)
else:
    print('To nie jest litera')