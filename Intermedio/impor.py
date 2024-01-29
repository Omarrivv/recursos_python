from animal import Animal
class Dog(Animal):
    def __init__(self, name: str, age: int, sexo: str, color:str):
        super().__init__(name, age, sexo)
        self.color = color  
        def sleep(self):
            print(f"I sleep 5 horas ")
class Cat(Animal):
    def __init__(self, name: str, age: int, sexo: str, lives:int):
        super().__init__(name, age, sexo)
        self.lives = lives
        def sleep(self):
            print("I sleep 9 horas")
dog1 = Dog("Florido", 2, "Macho", "negro")
dog1.eat('Chicken')
dog1.walk()
dog1.walk()
print(f'htis dog is {dog1.name} is {dog1.age} is {dog1.sexo} is {dog1.color}')
