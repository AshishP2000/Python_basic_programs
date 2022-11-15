class Parrot:
    species = "bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age


blu = Parrot("Blue", 10)
woo = Parrot("Purple", 15)

print("blu is a", blu.__class__.species)
print("woo is also a", woo.__class__.species)


print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(woo.name, woo.age))
