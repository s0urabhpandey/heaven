class Person:
    def __init__(self,name,age,gender='female',iq=90):
        self.name=name
        self.age=age
        self.gender=gender
        self.iq=iq

    def eat(self,food='bread'):
        print(f'{self.name}eats{food}')

    def info(self):
        print('name',self.name)
        print('age',self.age)
        print('gender',self.gender)
        print('iq',self.iq)
    
    def sleeps(self,hrs=6):
        print(f'{self.name} sleeps {hrs}hrs')
if __name__ == "__main__":
    p1=Person('Ram',7,'male')
    p2=Person('shyam',17,'male')
    p3=Person('riya',20,'female')
    p4=Person('priya',18,iq=110)

    p1.info()
    p2.info()
    p3.sleeps(100)
    p4.eat("maggi")
    p3.info()
    p4.info()
