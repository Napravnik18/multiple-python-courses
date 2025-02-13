#Classes
    #utilizadas para criar objetos(instances)
    # objetos são partes dentro de uma classe (instancias)
    #classes são utilizadas para agrupar dados e funções, podendo reutlizar
    #Class: frutas
    #Object: Abacate, banana, ...


# criar a classe
class Funcionarios:
    pass

#criando objeto    
usuario1 = Funcionarios()
usuario2 = Funcionarios() 

#criando parametros do usuario 1
usuario1.nome = 'Helena'
usuario1.sobrenome = 'Cabral'
usuario1.data_nascimento = '12/01/2009'

#criando parametros do usuario 1
usuario2.nome = 'Carol'
usuario2.sobrenome = 'Silva'
usuario2.data_nascimento = '11/08/2000'

# print
print(usuario1.nome)
print(usuario2.data_nascimento)