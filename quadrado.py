#Escreva uma classe “Quadrado”, crie dois métodos que retornem a
#área do quadrado e o perímetro, não crie a instância nesse exercício.

class Quadrado:
    def __init__(self, lado):
        self.lado = lado
        
    def area(self):
        area = (self.lado)**2
        return area
    
    def perimetro(self):
        perimetro = (self.lado)*4
        return perimetro