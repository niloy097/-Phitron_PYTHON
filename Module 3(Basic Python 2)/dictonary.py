#key value pari
#dictonary
#object
#hash table
#overlap with set

#{key : value, kye : value}
person = {
    
    'name': 'kala pakhi',
    'address': 'Bangla',
    'job' : 'sweeper'
}

print(person)
print(person['job'])
print(person.keys())
print(person.values())

person['language'] = 'python'


print(person)

person['name'] = 'Sada pakhi'

print(person)


#special dictonary loopint
for key, value in person.items():
    print(key, value)