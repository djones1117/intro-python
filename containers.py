# Python Containers
#Lists, Tuples & Dictionaries


student = {
    'name': 'Maria',
    'course': 'SEI',
    'current_week': 7
}

print(student['name'])
print(student['course'])
print(student['current_week'])
name = student['name']  #accessing the value attached to name key - output - maria. variable name doesnt matter it couldc be student_name = student['name']
print(name)
student['name'] = 'Tina' #updating the value 
print( student.get('skills', {'HTML': 5, 'JAVASCRIPT': 4}) )
#using get method - better practice than square brackets!
print(student.get('name'))

student['age'] = 25 #adding  to dictionary
print(student)
del student['course'] # makes else statement run/ how to delete item from dictionary

if 'course' in student:
  print( f"{student['name']} is enrolled in {student['course']}")
else:
  print( f"{student['name']} is not enrolled in a course")


##not best practice (anti pattern)
for person in student:
  print( f"{person} = {student[person]}")
  ### iterates through the student dictionary. represents the keys in the dictionary 
  ### so output would be name = maria current_week = 7 and age = 25. 
  ## the word "person" doesnt matter what matters it represents the key value pairs in the student dictionary
  ## you could write it for ---- "fish" in student: replace fish with person and itll run the same
print(student.items())


  ####same thing as above just better practice
for item_tuple in student.items():
  print( f"key = {item_tuple[0]} / value = {item_tuple[1]}" )


for key in student.keys():
  print(f"key  = {key}")


for value in student.values():
  print(f"value = {value}")

##BEST PRACT ---v-----
# Best practice 
for key, value in student.items():
  print( f"key = {key} / value = {value}" )
  
where_my_things_are = {
  'car': 'in the garage',
  'keys': 'in the dresser',
  'wallet': 'in the car'
}
for thing, location in where_my_things_are.items():
  print( f"My {thing} is kept {location}")

  ##nested dictionary

  student = {
    'name': 'Dylan',
    'details': {
      'course': 'sei',
      'current_week': 7
    }
  }
  print(student['details']['course'])
  ##looping through nested dic

for key, value in student['details'].items():
  print(f"key = {key} / value = {value}")

#convert the values of dictionary 'x' to a list 
#first prints out every value 4,8,16,32
# [2] accesses the third element in the list and prints out 16
x = {
  0: 4,
  1: 8,
  2: 16,
  3: 32
}
print(list(x.values()))
print(list(x.values())[2])

#Finished Dictionaries 



##Lists (like js arrays)

colors = ['red', 'green', 'blue']
print(len(colors))
colors[2] = 'brown' # updating list
colors.append('purple') # adding to a list
colors.extend(['orange', 'black']) # extend the list
colors.insert(1, 'yellow')  #inserts an item by index value
del colors[1] # deletes from list by idx num
colors.remove('orange') #removes by value ## you have to know the value
print(colors)

odds = [1, 3, 5]
evens = [2, 4, 6]
nums = odds + evens
print(nums)
##combines two list/ does not sort

#using list method to make a list of even numbers
even_numbers = list(range(2, 11, 2))
print(even_numbers)

numbers = range(1, 11)
odd_nums = []
for n in numbers:
  if n % 2 == 1:
    odd_nums.append(n)
print(f"odd nums = ", odd_nums)

#what if you need the index
#not best pract
players = ['messi', 'ronaldo', 'pele']

# idx = 0
# for player in players:
#   print( idx, player )
#   idx += 1

##beest practice if you need access
#to the index of the iteration
for idx, player in enumerate(players):
  print( idx, player )

#dictionary inside a list
scores = [
  {
    'name': 'dylan',
    'points': 25  # points the player scored
  }
]
scores.append({
  'name': 'justin',
  'points': 12
})
for player in scores:
  print(f"{player['name']} scored {player['points']} points")

#if you need to iterate through the dictionary inside the list to find the key values
for my_dict in scores:
  for key,value in my_dict.items():
    print(f"key = {key} / value = {value}")

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

##list comprehension 
squares = [num * num for num in nums]

even_squares = [n * n for n in nums if (n * n) % 2 == 0]


squares == even_squares
if squares == even_squares:
  print('true')
else:
  print('false')
print(even_squares)


list_one = [1, 2, 3]
list_two = [4, 5, 6]
both_lists = list_one + list_two
print(f"both lists = " + str(both_lists))
print(len(both_lists))
list_one.append(list_two)
print(list_one)
print(f"length of list one = " + str(len(list_one))) ## have to use the str method if you want to concatenate the two types together
print('length of list one is', len(list_one))  

##Finished Lists 



##Tuples 

##tuples are like python lists

##tuples cannot be modified unlike lists
##you can iterate over items in a tuple
##use tuples if you dont need to update that collection of data -
##more efficient and better pract


colors = ('red', 'green', 'blue')
print( colors )
print(len(colors))

#iterate through a tuple
for c in colors:
  print(f"{c} is a good color!")

#you could use -2 to start from green and achieve same result as below
for color in colors[1:]:
  print(color)

if 'purple' in colors:
  print('true')
else:
  print('false')

##unpack tuples
##naming does not matter could be tuna shark salmon = colors
r, g, b = colors
print(r)
print(g)
print(b)

##slicing 
short_name = 'Alexandria'[0:4] # output = x if Alexandria[3]
print(short_name)              # output = alex if Alexandria[0:4]
                               #represents starting index and ending index



colors = ('red', 'green', 'blue')
colors = colors[:2]  #creates and saves a new tuple output everything until blue
colors = colors[1:]  #creates a new tuple slices from the tuple created just above this line
print(colors)

##sets in python
fruits = {'apple', 'orange', 'banana'}
print(fruits)

fruits.add('grapes')

fruits.remove('banana')


if 'apple' in fruits:
  print('apple is in the set!')



# Set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print(set_a.union(set_b))  # Combine sets
print(set_a.intersection(set_b))  # Common items
print(set_a.difference(set_b))  # Unique to set_a

# Set comprehension
unique_squares = {n ** 2 for n in nums}
print(unique_squares)



# Removing duplicates from a list using a set
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print(f"Unique numbers: {unique_numbers}")  # {1, 2, 3, 4, 5}


# Checking if one set is a subset of another
small_set = {1, 2}
big_set = {1, 2, 3, 4, 5}
print(f"Is small_set a subset of big_set? {small_set.issubset(big_set)}")  # True


# Checking if one set is a superset of another
print(f"Is big_set a superset of small_set? {big_set.issuperset(small_set)}")  # True
