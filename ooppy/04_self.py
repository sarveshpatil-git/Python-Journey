class Factory:
    def __init__(self,material,zips,pockets):
        self.material=material
        self.zips=zips
        self.pockets=pockets
    def show(self):
        print(f"Your object details are {self.material},{self.zips},{self.pockets}")  

reebok=Factory("Leather",3,2)

campus=Factory("Nylon",3,3)

reebok.show()

print(reebok.material)

print(campus.pockets)