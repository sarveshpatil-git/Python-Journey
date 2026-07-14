class Factory:
    a = 12 #attribute

    def hello(self):      #method
        print("How are u?")
    print("I am getting initialized")

obj=Factory()

obj.hello()
print(obj.a)