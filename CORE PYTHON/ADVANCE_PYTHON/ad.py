class Mobile():
    def __init__(self,m):
        self.model = m
    def self_show(self,p):
        price = p
        print("Model:",self.model,"Price:",price)
realme = Mobile('realme')
realme.self_show(10000)
print(id(realme))
print()

redmi = Mobile('Redi 7s')
redmi.self_show(2000)
print(id(redmi))
print()

