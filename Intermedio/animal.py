# herencia y polimorfismo en programacion orientada a objetros
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
    def sleep(self):
        print("I sleep")
animal = Animal('omar', 17, 'masculino')
animal.eat('some food')
print(animal.name)
print(animal.age)
print(animal.sexo)
print(animal.eat('svsvvs'))
print(animal.sleep)
print('=========')