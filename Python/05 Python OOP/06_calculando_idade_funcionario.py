#Classes
    #utilizadas para criar objetos(instances)
    # objetos são partes dentro de uma classe (instancias)
    #classes são utilizadas para agrupar dados e funções, podendo reutlizar
    #Class: frutas
    #Object: Abacate, banana, ...


# criar a classe
from datetime import datetime


class Funcionarios:
    
    def __init__(self, nome, sobrenome, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento
    
    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome
    
    def idade_funcionario(self):
        ano_atual = datetime.now().year
        self.ano_nascimento = int(ano_atual - self.ano_nascimento)
        return self.ano_nascimento
        
    
#criando objeto    
usuario1 = Funcionarios('Elena', 'Cabral', 2009)
usuario2 = Funcionarios('Carol', 'Silva', 2005) 
usuario3 = Funcionarios('Stan', 'Napra', 1999)

# print
print(Funcionarios.idade_funcionario(usuario3))
