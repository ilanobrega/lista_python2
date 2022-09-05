#Exercício 1

class Pessoa:
    def __init__(self, nome, cpf, idade, fuma):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.fuma = fuma
    
    def get_nome(self):
        return f'O nome da pessoa é {self.nome}'
    
    def get_cpf(self):
        return f'O cpf da pessoa é {self.cpf}'
    
    def check_fumante(self):
        if self.fuma == 'F':
            return f'Fumante'
        
        return f'Não fumante'
    
pessoa1 = Pessoa('Adamastor', '1234556', '34', 'N')
print(pessoa1.get_nome())
print(pessoa1.get_cpf())
print(pessoa1.check_fumante())
    
#Exercício 2

class Tipo_Pessoa(Pessoa):
    def __init__(self, nome, cpf, idade, fuma, tipo_pessoa):
        self.tipo_pessoa = tipo_pessoa

        super().__init__(nome, cpf, idade, fuma)


    def get_tipo_pessoa(self):
        if self.tipo_pessoa == 'Física':
            return f'O tipo de pessoa é Física'

        return f'Tipo de pessoa é Jurídica'

harry = Tipo_Pessoa('harry', '1221212', '12', 'F', 'Física')
print(harry.get_tipo_pessoa())

#Exercício 3

class Pessoa_Juridica(Tipo_Pessoa):
    def __init__(self, nome, cpf, idade, fuma, tipo_pessoa, cnpj):
        self.cnpj = cnpj

        super().__init__(nome, cpf, idade, fuma, tipo_pessoa)


    def get_cnpj(self):
        if self.tipo_pessoa != 'Física':
            return f'O cnpj é {self.cnpj}'
        
harry = Pessoa_Juridica('harry', '1221212', '12', 'F', 'Jurídica', 1234556)
print(harry.get_cnpj())

