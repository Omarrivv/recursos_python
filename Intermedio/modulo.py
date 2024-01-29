# Metodos
class Animal:
    # constructor
    def __init__(self, name: str, age: int, sexo:str): # hace referencia a que lo que pongamos en la parentesis va aser luego referenciado al propio objeto de la clase
        self.name= name  # primero ponemos el self luego el punto y llamando a los parametros bueno a si es como yo lo llame i que le igualemos a el mismo parametro de cada uno como self.name = name , etc
        self.age= age
        self.sexo= sexo
    def eat(self, food):
        print(f'{self.name} is eating {food} .')
    def walk(self):
        print(f'{self.name} is walking')
dog = Animal("Vovi", 3, "Macho")
print(f'The name of this dog is {dog.name} y su age es {dog.age} es un {dog.sexo}')
dog.eat('Pollo')
dog.walk()