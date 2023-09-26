def fizz_buzz(max_num):
    # code blocks are defined using indentation
    # after a :
    '''
    Docstring - Multi-line string/comment
    '''
    for num in range(1, max_num):
        if num % 3 == 0 and num % 5 == 0:
            print('{} is FizzBuzz'.format(num))
        elif num % 3 == 0:
            print(f'{num} is Fizz')
        elif num % 5 == 0:
            print(f'{num} is Buzz')
        else:
            print(num)

fizz_buzz(31)

my_number = 15
print(my_number)
my_number = 4
print(my_number)

type(42)
# <class 'int'>

type('hello')
# <class 'str'>

type(True)
# <class 'bool'>
