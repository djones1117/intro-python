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


#what if you need the index
#not best pract
players = ['messi', 'ronaldo', 'pele']

idx = 0
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
for score in scores:
  print(f"{score['name']} scored {score['points']} points")

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = [num * num for num in nums]

even_squares = [n * n for n in nums if (n * n) % 2 == 0]

squares == even_squares
if squares == even_squares:
  print('true')
else:
  print('false')
print(even_squares)

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


#see if this pushes testing github access token authorization on multiple repos