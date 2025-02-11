class Parrot:
    species="Bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
parrot1=Parrot("Polly",2)
parrot2=Parrot("Brandon",4)
print(f"Species :{Parrot.species}")
print(f"Name :{parrot1.name},Age: {parrot1.age}")
print(f"Name :{parrot2.name},Age: {parrot2.age}")