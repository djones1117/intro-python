#Python Classes

nums = [1, 2, 3]

print(dir(nums))

class Dog():
    #initialize the attributes on the 
    #new object
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def bark(self):
        print(f'{self.name} say woof!' )

    def __str__(self):
        return f'Dog named {self.name} is {self.age} years old'
    

bo = Dog('Bo', 8)
nova = Dog('Nova')
print(bo.bark())
print(nova.age)
print(bo)
print(nova)

        