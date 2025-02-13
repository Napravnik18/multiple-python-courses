
altura = float(input('Qual é sua altura? '))
peso = float(input('Qual é seu peso? '))

def calculo_imc():
    imc = peso / (altura * altura)
    print(f'Seu indice de massa corporal é {imc}')
    
    if imc < 18.5:
        print('Você está magro')
    elif 18.4 < imc < 25:
        print('Você está normal')
    elif 24.9 < imc < 30:
        print('Você está gordo')
    elif 29.9 < imc < 40:
        print('Você está obeso')
    else:
        print('Você está proximo da morte')

calculo_imc()
    