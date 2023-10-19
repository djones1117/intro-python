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