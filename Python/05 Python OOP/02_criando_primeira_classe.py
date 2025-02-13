#Classes
    #utilizadas para criar objetos(instances)
    # objetos são partes dentro de uma classe (instancias)
    #classes são utilizadas para agrupar dados e funções, podendo reutlizar
    #Class: frutas
    #Object: Abacate, banana, ...


class Funcionarios:
    nome = 'Helena'
    sobrenome = 'Cabral'
    data_nascimento = '12/01/2009'
    
usuario1  = Funcionarios()

print(usuario1.nome)
print(usuario1.sobrenome)
print(usuario1.data_nascimento)