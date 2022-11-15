class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def eat(self, eat):
        print("{} is eating {}".format(self.name, eat))

    def sing(self, song):
        print("{} is singing {}".format(self.name, song))


tiger = Animal("Shera",3)

tiger.eat("Deer")
tiger.sing("Happy")
