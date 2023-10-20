#Python Classes

nums = [1, 2, 3]

print(dir(nums))

class Dog():
    #class attribute shared between all objects of this class
    next_id = 1
    #initialize the attributes on the 
    #new object
    def __init__(self, name, age=0):
        self.name = name
        self.age = age
        self.id = Dog.next_id
        Dog.next_id += 1

    def bark(self):
        print(f'{self.name} say woof!' )

    def __str__(self):
        return f'Dog ({self.id}) named {self.name} is {self.age} years old'
    
    @classmethod
    def get_total_dogs(cls):
        return cls.next_id - 1
    


bo = Dog('Bo', 8)
nova = Dog('Nova')
print(bo.bark())
print(nova.age)
print(bo)
print(nova)
print(Dog.get_total_dogs())
    #subclass of superclass DOG
class ShowDog(object):
    #Add additional parameters AFTER those of
    #the superclass (Dog)
    #we need the same properties from above first thing you should do for best practice
    def __init__(self, name, age=0, total_earnings=0):
        #always call the superclasses init method first
        Dog.__init__(self, name, age)
        #now its okay to specialize
        self.total_earnings = total_earnings

    def add_prize_money(self, amount):
        self.total_earnings += amount
        print(f'{self.name}\'s new total earnings are {self.total_earnings}')

    def __str__(self):
        return f'Dog ({self.id}) named {self.name} is {self.age} years old'
    
    def bark(self):
        print(f'{self.name} say woof!' )
        
chewi = ShowDog('chewi', 15, 3000)
winky = ShowDog('winky', 3, 1000)
print(winky)
print(winky.bark())
print(winky.add_prize_money(500))

class Vehicle():
    
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.running = False

    def start(self):
        self.running = True
        print('running')

    def stop(self):
        self.running = False
        print('stopped')

    def __str__(self):
        return f'Vehicle is a {self.make} model {self.model}'

car = Vehicle('BMW', 'I8')
van = Vehicle('Mercedes', 'G-Wagon')
print(car.stop())
print(car.start())
print(car)
print(van.make)
print(van)
        

        