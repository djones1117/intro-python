#Python Functions

def first_function():
    pass

result = first_function()
print(result)

def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

math_operations = {
  '+': add,
  '-': subtract
}

selected_operation = '+'

print(math_operations[selected_operation](2, 4))



nums = [1, 3, 2, 6, 5]
odds = list(filter(lambda num: num % 2, nums))
print(odds)

def fn(*args):
  print( type(args) )
  for arg in args:
    print(arg)

fn(1, 2, 'SEI')

def dev_skills(dev_name, *args):
  dev = {'name': dev_name, 'skills': list()}
  for skill in args:
    dev['skills'].append(skill)
  return dev

print(dev_skills('Alex', 'HTML', 'CSS', 'Javascript', 'Python'))

def divide(a, b):
  return f'{a} divided by {b} is {a / b }'

print(divide(100, 25))

def dev_skills(dev_name, **kwargs):
  dev = {'name': dev_name, 'skills': kwargs}
  return dev
print(dev_skills('Jackie', HTML=5, CSS=3, JavaScript=4, Python=5))


def arg_demo(pos1, pos2, *args, **kwargs):
  print(f'Positional params: {pos1}, {pos2}')
  print('*args:')
  for arg in args:
    print(' ', arg)
  print('**kwargs:')
  for keyword, value in kwargs.items():
    print(f'  {keyword}: {value}')

arg_demo('A', 'B', 1, 2, 3, color='purple', shape='circle')
  
  