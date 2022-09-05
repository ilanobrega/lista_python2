# 2. Escreva uma classe “PessoaFisica” e herde Pessoa, crie um método exclusivo para a classe e acesse-o

class Professor:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario

    def __get_salario_access(self):
        return f'Salário é {self.salario}'
    
    def access_salario(self, nome):
            if nome == 'magalu':
                return self.__get_salario_access()
        
            return 'Você não tem acesso a esse local'
    
pessoa = Professor('magalu', '35', '500')

access = pessoa.access_salario('Hermione')
print(access)

access =  pessoa.access_salario('magalu')
print(access)