class Factory:
    a=12 #attribute

    def hello(self):      #method
        print("How are u?")
    print("I am getting initialized")

print(Factory().a)  
Factory().hello()  