dict = {}
print(type(dict))

person = {'first_name':'John','last_name':'Doe','age':25,'favorite_color':['blue','green'],'active':True}  #Dictonary

print(person['first_name'])  #print first name using key
print(person['last_name'])

ssn = person.get('ssn','00000000000')  #using get method to avoid error
print(ssn)

person['gender'] = 'male'  #Adding new key to the dictonary
print(person)

person['age'] =26  #updating value of keys
print(person)

del person['age'] #deleting key
print(person)

print(person.items()) #return an object as tuple

for key,value in person.items():#iterating using for loop
    print(f"{key}:{value}")

for key in person.keys():#only keys
    print(key)
for value in person.values():#only values
    print(value)