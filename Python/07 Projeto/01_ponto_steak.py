
steak = int(input('Qual a temperatura da carne?'))

if steak < 48:
    print('a carne está crua')
elif 47 < steak < 54:
    print('a carne está mal passada') 
elif 53 < steak < 60:
    print('a carne está ao ponto para mal passada')
elif 59 < steak < 65:
    print('a carne está ao ponto')
elif 64 < steak < 71:
    print('a carne está bem passada')
else:
    print('você queimou a carne')

print(f'a temperatura da carne é {steak}C')