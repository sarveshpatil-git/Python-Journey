class Factorymumbai: #parent class / superclass
    a = "I am an attribute mentioned inside Factory"
def hello(self):
    print("hello I am a method mentioned inside Factory")

class Factorypune(Factorymumbai):   #child class /subclass
    pass

obj = Factorymumbai()

obj2 = Factorypune()
obj2.hello()
