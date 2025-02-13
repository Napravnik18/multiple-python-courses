#Classes
    #utilizadas para criar objetos(instances)
    # objetos são partes dentro de uma classe (instancias)
    #classes são utilizadas para agrupar dados e funções, podendo reutlizar
    #Class: frutas
    #Object: Abacate, banana, ...


# criar a classe
class Funcionarios:
    
    def __init__(self, nome, sobrenome, data_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento
    
    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome
    
#criando objeto    
usuario1 = Funcionarios('Elena', 'Cabral', '12/01/2009')
usuario2 = Funcionarios('Carol', 'Silva', '15/10/2005') 

# print
print(usuario1.nome_completo())
print(Funcionarios.nome_completo(usuario1))
