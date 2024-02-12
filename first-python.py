# python comment

# we dont have let or const and we use snake_case
# the variables act like let there is no const
first_name = 'dylan'
last_name = 'jones'


print(type(first_name))
print(type(1))
print(type(1.333333333))
print(type("kate"))
print(type([])) # List in python
print(type(True))
print(type(False))
print(type({})) # dictionary in python
# our console.log is print
print(first_name)
print(last_name)
print(len(first_name))

person = {
    'name': 'kate',
    'student': True,
    'pockets': ['fruit rollup', 'pen'],
}
# accessing a key
print(person['name']) # this would print the value kate
print(person['pockets'][1])
# accessing a key using a method
print(person.get('name'))
print(person.get('pockets')[1])
print(person.get('last_name')) # this will come out as none since there is no last-name key

# to find out the methods on an object (everything is an object)
# you can use the dir() method
print(dir(person))

print('hello my name is', first_name, last_name)
