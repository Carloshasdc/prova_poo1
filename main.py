class Animal:
    def falar(self):
        return "Este animal faz um som."

class Cachorro(Animal):
    def falar(self):
        return "O cachorro late"

class Gato(Animal):
    def falar(self):
        return "O gato mia"
        
animal = Animal()
print (animal.falar())

cachorro = Cachorro()
print (cachorro.falar())

gato = Gato()
print (gato.falar())