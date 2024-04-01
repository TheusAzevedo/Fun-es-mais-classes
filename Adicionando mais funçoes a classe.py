from datetime import datetime

class Funcionarios:
    
    def __init__(self, nome, sobrenome, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento
    
    def nome_completo(self):
        return (self.nome + ' ' + self.sobrenome)
    
    def idade_funcionario(self):
        ano_atual = datetime.now().year
        self.ano_nascimento = int(ano_atual - self.ano_nascimento)
        return self.ano_nascimento


#criar o objeto
usuario1 = Funcionarios('Jair', 'Santos', 1968)
usuario2 = Funcionarios('Solange', 'Dias', 1965)


print(Funcionarios.nome_completo(usuario1))
print(Funcionarios.idade_funcionario(usuario1))
print(Funcionarios.nome_completo(usuario2))
print(Funcionarios.idade_funcionario(usuario2))