
funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa']
turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
turno_noite = ['Pedro', 'Sophia', 'Bruno']
tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']

set1 = set(funcionarios)
set2 = set(turno_dia)
set3 = set(turno_noite)
set4 = set(tem_carro)

lista1 = set3 & set4
print(f'estes funcionarios trabalham a noite e tem carro {lista1}')

lista2 = set2 & set4
print(f'estes funcionarios tem carro e trabalham durante o dia {lista2}')

lista3 = set1 - set4
print(f'estes funcionarios não tem carro {lista3}')