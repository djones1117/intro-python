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
name = student['name']
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
# Best practice "unpack" the tuples just like destructuring
for key, value in student.items():
  print( f"key = {key} / value = {value}" )
  