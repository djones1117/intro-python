8 > 8
# => False — 8 is not greater than 8.

8 >= 8
# => True — This checks if 8 is greater than or equal to 8, and they are equal.

8 < 8
# => False — 8 is not less than 8.

7 == 7
# => True — 7 is equal to 7.

7 == "7"
# => False — One is a number and the other is a string.

7 != 7
# => False — This checks if they aren't equal. Because does 7 equal 7, it's `False`.

6 != 7
# => True — 6 is not equal to 7.

True or False
# => True

False or True
# => True

'hello' or 0
# => 'hello'

0 or 'hello'
# => 'hello'

True and False
# => False

False and True
# => False

'hello' and 0
# => 0

0 and 'hello'
# => 0

'hello' and 'tacos'
# => 'tacos'

not True
# => False

not 123
# => False

not []
# => True

floor = "sticky"
walls = "clean"
if floor == "sticky":   # don't forget the colon
  print("Clean the floor! It's sticky!")
  # more lines of code in this code
  # block need to be indented as well
if walls == "sticky":
  print("Clean the walls! They're sticky!")
else:
  print("The walls are clean!")
color = ""

while color != 'quit':

    color = input('Enter "green", "yellow", "red": ').lower()
    print(f'The user entered {color}')
    
    if color == "green":
        print('Go!')
    elif color == "yellow":
        print('Slow Down!')
    elif color == "red":
        print('Stop!')
    else:
        print('bogus')

names = ["Tom", "Deborah", "Murray", "Axel"]

for name in names:
  print(name)
