<img src="https://i.imgur.com/a0edx5Q.png">

# Intro to Python

## Learning Objectives

| Students Will Be Able To: |
|---|
| Use the Python REPL |
| Execute Python scripts |
| Define and use variables |
| Create comments |
| Describe Python data types |
| Use and format Strings |

## Road Map

1. Intro to the Python Language
2. Using the Python Interpreter & REPL
3. Python's Conventions, Variables, Data Types, etc.
4. Essential Questions
5. Further Study

## 1. Intro to the Python Language

### History

Back in December 1989 a Dutch programmer named Guido van Rossum was looking for a hobby project to keep himself occupied during his Christmas break.

The result was the very popular Python programming language!

Python was first released to the public in 1991.

### Versions

Ten years after its release, Python 2.0 was introduced with many major new features and it started to gather a community dedicated to its development.

Python 3.0 was released in December 2008.

Version 3.0 introduced many enhancements, however, it included changes that made Python 3 incompatible with most existing version 2 applications.

### Type of Language

Python, like JavaScript, is a high-level, object-oriented, interpreted programming language.

*note*: It is necessary to note that many programming languages can be considered interpreted, compiled or scripting languages depending on their use. When we use javascript inside of modern web browser or when writing node.js your script will be ran through an interpreter making javascript behave as an interpreted language, but it is critical to remember, at its core, javascript is a scripting language even though in our current era of javascript development it is almost always used as an interpreted language. As we'll explain below, an interpreted language is a language that has an interpreter translate the script provided by the engineer into a optimize version that can be better acted on by machines. It is also helpful to consider that it is assumed an interpreted language is going to hand its interpreted code off to a compiler to compile that middle level interpreted code into machine code. Due to the variety of language architectures and framework designs as well as the inherent vagueness of the terms like 'interpreted' and 'compiled' it can often be confusing to determine exactly what any given programming language or framework is doing with in your project without considering the exact application and architecture of your project. For the purposes of this course, we'd recommend to just consider python and javascript interpreted languages and consider the alternative varieties later on when you've developed a more mature understanding of how our programming systems behave and how they were designed. 

<img src="https://i.imgur.com/i6N9fzx.jpg">

High-level means that Python is designed for writing applications vs. lower-level software such as operating systems and device drivers. It also means that programmers don't have to worry about things like memory management.

Also like JavaScript, Python is a dynamic scripting language that does not have to be compiled before it can be executed - it runs within an _interpreter_ that handles the conversion into machine code.

Python comes with a large standard library and is suitable for many types of programming tasks from web development to machine learning and data science.

However, if Python does not include functionality that you need, there is a huge repository, the [Python Package Index](https://pypi.org/), with third-party packages available for use.

### Syntax & Semantics

Python was designed to be an easy to read programming language.

Its formatting is visually uncluttered and it often uses English keywords where other languages use punctuation or symbols. For example, the equivalent to JS's `&&` operator in Python is `and`. 

Unlike many other languages, it does not use curly braces to define blocks of code, instead, it uses indentation.

## 2. Using the Python Interpreter & REPL

We'll be using **Python 3** at all times during SEI.

### Ensure `Python 3` is Installed

In terminal type: `python3`

If you receive an error, run `brew install python`, quit and re-open terminal, and try `python3` again.

Similar to what you saw with **Node.js**, Python comes with an interactive REPL (Read-Evaluate-Print-Loop) that provides a way to run Python code by typing in.

For now, type `exit()` or press `control + d` to exit the REPL.

### Running Python Scripts

In terminal, we can execute any python script like this:

```
python3 <filename>.py
```

Let's test this out by previewing a bit of Python by coding and running the infamous FizzBuzz function:

1. Move into your **~/code** folder:
    ```
    cd ~/code
    ```
2. Create a **fizzbuzz.py** script file:
    ```
    touch fizzbuzz.py
    ```
3. Open **fizzbuzz.py** in VS Code:
    ```
    code fizzbuzz.py
    ```
4. Code the `fizz_buzz()` function: 
    ```py
    # Functions are defined using the def keyword
    def fizz_buzz(max_num):
      # Code blocks are defined using 
      # indentation after a :
      '''
      Loops through 1 up to max_num and prints message depending on evaluation of the integer
      '''
      for num in range(1, max_num):
        if num % 3 == 0 and num % 5 == 0:
          # Using string format method
          print('{} is FizzBuzz'.format(num))
        elif num % 3 == 0:
          # Using newer f-string approach
          print(f'{num} is Fizz')
        elif num % 5 == 0:
          print(f'{num} is Buzz')
        else:
          print(num)

    fizz_buzz(31)
    ```

Now we can run the Python script as shown above by typing the following in Terminal:

```
python3 fizzbuzz.py
```

As you can see, Python's `print()` function outputs to the Terminal.

Unlike with Node.js, providing the file extension (`.py`) is required.

### REPL

During the remainder of this lesson, we'll be experimenting in the Python interpreter/REPL.

In terminal: `python3`

At the `>>>` prompt, type `help()`, then type `quit` to return to the REPL.

Cool, let's explore Python a bit in its REPL...

#### The Zen of Python

The Zen of Python is a simple import released with all versions of python and added by Tim Peters. It shares with you 20 lines of text detailing the guiding principles of python. This is an easter egg of sorts, but can be insightful for better understanding why python has been created in the way it has. 

You can view these 20 guiding principles in the python terminal by typing the following line of code into the terminal and hitting enter. 

```python
import this
```

This will then print out the guiding principles like follows. 

20 Guiding principles of python:
```
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

## 3. Python's Conventions, Variables, Data Types, etc.

### Comments

We use the `#` character to make a comment in Python:

```python
# This is a comment! Python will ignore it.
```

Anything after the `#` will not be run:

```python
total_guitars = 7  # Hope someone knows how to play guitar
```

To make multiline comments, we use triple quotes, `"""`, or the `#` on each line:

```python
"""
This is a
multiline comment
"""

# This is a
# multiline comment
```

Multiline comments are often used to document what a function or module does, therefore, they are sometimes referred to as _docstrings_.

### Python Variables

Variables in Python work in much the same way that variables work in JavaScript.

Variables hold the data an app needs when it runs.

#### Declaring

Here is how we declare a variable in Python:

```python
my_number = 15
```

Notice that there is no `var`, `let`, or `const` keyword in Python. We only need the name of the variable and then we can assign to it.

However, you cannot just declare a variable without assigning to it - there is no `undefined` in Python:

```python
# illegal syntax...
my_variable
NameError: name 'my_variable' is not defined
```

#### Naming Convention

Variables are case sensitive - variables named `my_number` and `My_Number` would be two different variables.

When you have a variable name with multiple words, the convention is to **snake_casing** the identifier:

```js
// In JavaScript we use camelCasing...
var myNumber = 10;
```

```python
# In Python we use snake_casing...
my_number = 10
```

#### Reassigning Variables

Just like in JavaScript, we can freely assign a new value to a variable after it is declared.

```python
my_number = 15
print(my_number)
my_number = -4
print(my_number)
```

Of course, reassignment replaces the current value and that previous value would no longer be available - just like in JS.

> 👀 The `print()` function works very much like `console.log()` does in JavaScript.

### Data Types

Python is a **very** object-oriented language.

In fact, pretty much everything in Python is an object that's been instantiated (created) by a particular _class_.

#### Checking the Data Type (class) of an Object

We use the `type()` function to obtain the class used to instantiate the data:

```python
>>> type(42)
<class 'int'>
>>> type('hello')
<class 'str'>
>>> type(True)
<class 'bool'>
```

Python's data types are similar to those available in JavaScript, there's just more of them...

#### Integer Numbers (`<class 'int'>`)

Unlike in JavaScript, Python distinguishes between integers (whole numbers) and floats (numbers with decimals).

When we don't follow a number literal with a decimal point, an integer is assumed:

```python
>>> some_int = 25
>>> type(some_int)
<class 'int'>
```

In JavaScript, we could use `Math.floor()` to truncate the decimal portion of a number.  In Python, we can convert non-integer numbers into integers using the `int()` function:

```python
>>> a_float = 1.7
>>> an_int = int(a_float)
>>> an_int
1
```

#### Floating-point Numbers (`<class 'float'>`)

Numbers with a decimal point are stored in variables as floating-point numbers, usually just called a `float`.

```python
# Certain built-in features need to be imported
>>> import math
>>> pi = math.pi
>>> pi
3.141592653589793
>>> type(pi)
<class 'float'>
>>> some_float = 25.
>>> type(some_float)
<class 'float'>
```

#### Complex Numbers (`<class 'complex'>`)

Python even has a data type for complex numbers, i.e., numbers with an "imaginary" component usually obtained by taking the square root of a negative number.

The imaginary portion is represented by the letter 'j':

```python
>>> my_complex = 3+4j
>>> type(my_complex)
<class 'complex'>
```

#### Booleans (`<class 'bool'>`)

Named after George Boole, these are the logical data types often used in conditional expressions.

Just like in JS, we have `true` and `false` except that their identifiers are capitalized:

```python
>>> my_bool = True
>>> my_other_bool = False
>>> type(my_bool)
<class 'bool'>
```

You must start them with capital letters in Python or they will not reflect the boolean values. 

#### Nothingness (`<class 'NoneType'>`)

Python's equivalent to JS's `null` & `undefined` is `None`:

```python
>>> my_nothing = None
>>> type(my_nothing)
<class 'NoneType'>
```

The value `None` in Python, with a capital N, provides the same meaning as `null` does in JavaScript.

### Math operations

Python has the normal math operators that you are used to from JavaScript:

- Addition `(+)`
- Subtraction `(-)`
- Multiplcation `(*)`
- Division `(/)`
- Modulo (remainder) `(%)`
- Exponentiation `(**)`

All work as you would expect. However, there few other things worth mentioning...

#### Integer Division

You can force the result to be an integer when dividing two integers using `//` instead of `/`:

```python
>>> quotient = 5 // 2
>>> quotient
2
# 2 is printed, because the decimal ".5" is truncated
```

#### Shortcut Assignment Operators

As we saw in JS, the operation of reassigning to a variable the result of adding, etc. to that variable is so common, there are a number of shortcut operators in the language that make it cleaner to write. 

Python has the very same operators, 

```python
# This line of code...
num = num + 1
# ...can be written with this shortcut operator:
num += 1

# It also works for any of the other math operations:
num = num / 5
# Rewrite like this:
num /= 5

# And this...
num = num * 3
# Can be written as this...
num *= 3
# And so on with the other operators.
```

> 👀 A couple of our favorites in JS, the Increment (`++`) and Decrement (`--`) operators, do not exist in Python. Use `+= 1` and `-= 1` instead.

### Ternary Expressions

In JS we used the ternary expression to concisely return one of two values depending upon a conditional expression, for example:

```js
// Using the ternary operator/expression
let beverage = age >= 21 ? 'Beer' : 'Milk';

// Without a ternary expression
let beverage;
if (age >= 21) {
  beverage = 'Beer';
} else {
  beverage = 'Milk';
}
```

Python, however, does not have a dedicated ternary operator.

Instead, Python uses a modified syntax of `if...else` which results in a ternary expression instead of a control flow construct.

The Python ternary expression equivalent to the JS example above is:

```python
beverage = 'Beer' if age >= 21 else 'Milk'
```

### Converting Between Data Types

One thing we kind of took for granted in JavaScript was that it usually performed automatic data type conversion for us - a process known as implicit type coercion.

```js
// JavaScript
let numTacos = 25;
let msg = 'There are ' + numTacos + ' tacos';
msg => There are 25 tacos
```

However, in Python we cannot do this - there is no type coercion. With few exceptions, variables must be the same type to perform an operation on them.

Luckily, doing math operations between integers and floats is allowed, but not much else.

When the time comes to convert one data type into another, Python provides us with several global functions or predefined classes to do so:

```python
str(item)        # Converts item to a string
int(item, base)  # Converts the provided item to an integer with the provided base
float(item)      # Converts the item to a floating-point number
hex(int)         # Converts an integer to a hexadecimal STRING
oct(int)         # Converts an integer to an octal STRING
tuple(item)      # Converts item to a tuple
list(item)       # Converts item to a list
dict(item)       # Converts item to a dictionary
```

### Working with Strings

Python also has strings for holding text, just like JavaScript:

```python
my_string = "A double quoted string"
your_string = 'A single quoted string'
```

You can also do some multi-line strings by using a triple quote (single or double):

```python
multiline_string = '''This is my string that
                        goes on multiple lines
                          for whatever reason'''
```

#### Concatenating Strings

One or more strings can be combined into a single string in the same way we do it in JS, by using the `+` operator:

```python
little_string = "bad"
medium_string = "super"
long_string = medium_string + little_string
print(long_string)
# prints "superbad"
```

#### String Interpolation using f-Strings

Something that Python has had much longer than JavaScript is a nice syntax for performing string interpolation (evaluating Python expressions and embedding the result within strings).

While we can always use the concatenation operators above, these get ugly when too many of them appear in a string.

Instead, we can use a syntax similar to ES2015's template literals.

You just need to remember to add an `f` before the string:

```python
state = "Hawaii"
year = 1959
message = f"{state} was the last state to join the U.S. in {year}."
```

When the `f` is placed directly before the opening quote (single, or double) of the string, it makes a formatted string or, **f-String**, for short.

Once we do this, we can put expressions into curly braces to "inject" the result of the expressions into the string.

f-Strings are awesome, but they've only been available since version 3.6 (released in December of 2016).

Prior to f-Strings, there were a couple of other options, one being the string `format` method:

```python
template = "My name is {} and I like {}"
print( template.format("Jim", "tacos") )
# prints 'My name is Jim and I like tacos'
```

#### Useful String Methods

Just like JS, Python has a number of string methods that we can use for string manipulation.

Some are familiar, like `split()` but others have different names:

```python
"ace of spades".split(" ")
# => ['ace', 'of', 'spades']

# However, this won't work as desired
"abcd".split("")
# Instead, use the list() function like this:
list("abcd")
# => ['a', 'b', 'c', 'd']

# Warning: Raises error if substring not found
"tesla".index("s")
# => 2

# Like index, but returns -1 if substring not found
"tesla".find("x")
# => -1

"foo".upper()
# => "FOO"

"WHY???".lower()
# => "why???"

"Then I went to the store I like".replace("I", "you")
# => 'Then you went to the store you like'
```

Want to know if a string contains a substring? You don't even need a function for that. You can use the most excellent `in` operator to quickly find out if one string appears in another.

```python
"eggs" in "green eggs and ham"
# => True
```

Use the built-in global `len()` function on a string to find its length.

```python
len("Tacos")
# => 5
```

### Python's Built-in Functions

Notice above that we did not call `len()` as a method on the string - we didn't do this: `"Tacos".len()`.

`len()` is just one of several [built-in functions](https://docs.python.org/3/library/functions.html) that exists in Python.

`len(arg)`, for example, is a function that returns the length (the number of items) of an object. The argument may be any sequence or collection (more on these soon).

Why does `len()` work on strings?  Because in Python, a string is a sequence of characters.

Because a string is a `sequence`, as we can in JS, we can use square brackets to access the characters in the string:

```python
course = 'SEI'
print( course[0] )
# => Prints 'S'

# We can use negative indexes!
last_letter = course[-1]
print( last_letter )
# => Prints 'I'
```

Later we'll see other fancy uses of square brackets.

Although we can access individual characters in a string, we cannot update the individual characters because stings are immutable (like JS):

```python
>>> s = 'Hello'
# I like Jello!
>>> s[0] = 'J'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

Let's wrap up with a few questions...

## 4. ❓ Essential Questions (1 min)

<details>
<summary>
(1) True or False: Every piece of data in Python is an object.
</summary>
<hr>

**True**

<hr>
</details>

```python
num = 25
msg = "There are " + num + " tacos"
```
<details>
<summary>
(2) Will the above code run without error in Python?
</summary>
<hr>

**No**, because Python doesn't convert the data types for us.

<hr>
</details>

<details>
<summary>
(3) String interpolation can be performed in Python by using __-Strings or a string's ________ method.
</summary>
<hr>

**f-strings** or a string's **`format()`** method

<hr>
</details>

## 5. Further Study

[Real Python Tutorials](https://realpython.com/)

## References

[Official Python Site](https://www.python.org/)

<img src="https://i.imgur.com/a0edx5Q.png">

# Control Flow in Python

## Learning Objectives

| Students Will Be Able To: |
|---|
| Describe what is truthy & falsy in Python |
| Perform multi-path branching using a `if...elif...else` statement |
| Perform looping using `while` statements |
| Use a **range** and a `for` statement to loop through a range of integers  |

## Road Map

1. Setup
2. Review of Control Flow
3. Conditional Expressions in Python
4. Branching
5. Looping
6. Python Ranges
7. Summary
8. Essential Questions

## 1. Setup

Create a Python-based repl in [https://replit.com/](https://replit.com/) - you can name it "Control Flow in Python".

## 2. Review of Control Flow

As you may recall, **control flow** refers to the order in which code executes in a program as determined by the use of constructs in the code.

In JavaScript, we saw how statements such as `if` and `switch` were used to perform **branching**.

We also used statements such as `for` and `while` to perform **looping**.

The good news is that most programming languages, including Python, share these same control flow constructs.

It's worth pointing out that programming concepts such as variables, data types, control flow, functions, etc. apply to programming languages in general thus making learning additional languages far easier than the first one!

## 3. Conditional Expressions in Python

Control flow typically comes down to different code paths executing according to the evaluation of **conditional expressions**.

In other words, if the **conditional expression** evaluates to _truthiness_, do this stuff, optionally, do something else.

Let's review some of the logic and fundamentals of conditional expressions.

### Boolean Values

Python has two logical boolean values: `True` and `False`.

Most logical operations result in one of these two values. They work exactly the same as in JS but are always written with a starting capital letter in Python.

### Truthy & Falsy in Python

Like JS, every expression in Python is considered to be either **truthy** or **falsy**.

Conditional expressions for `if` statements, etc., rely on an expression evaluating to `True`/**truthy** or `False`/**falsy** to determine which path the code will follow.

Just like in JavaScript, most things in Python are considered to be truthy.

Here's what is **falsy** in Python:

- `False`
- `None`
- Zero in any numeric type: `0`, `0.0` and `0j`
- Empty sequences or collections:
	- `''` (empty string)
	- `[]` (empty list)
	- `()` (empty tuple)
	- `{}` (empty dictionary)
	- `range(0)` (empty range)

> 👀 `[]` and `{}` in JavaScript are truthy, not falsy as in Python. 

### Comparison Operators

Python has all the same comparison operators as JavaScript:

- `<` - less than
- `>` - greater than
- `<=` - less than or equal
- `>=` - greater than or equal
- `==` - equal to
- `!=` - not equal to

Note that in Python, there's only one equality operator. The `==` in Python is the same as `===` in JavaScript.

#### Examples 

```python
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
```

### Logical Operators

Luckily, the amazing logical operators we used in JavaScript work the same way in Python except Python uses English words instead of symbols:

- `or` is the same as `||`
- `and` is the same as `&&`

Again, they work just like they did in JS, which means they always return either the **first** or the **second** operand as follows:

#### `or`

If the first operand is truthy, return it, otherwise return the second operand.

#### `and`

If this first operand is falsy, we will return its value, if the first operand is truthy, we will then return the value of the second operand. 

##### Examples

```python
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
```

#### `not`

"Flips" the truthiness/falsyness of its operand, and returns `True` or `False` 

```python
not True
# => False

not 123
# => False

not []
# => True
```

## 4. Branching

### Indentation!

Before we start looking at control flow, it's important to realize that **Python uses indentation to define blocks of code** - not curly braces.

It has always been recommended to use indentation in languages for readability purposes, however, in Python, proper indentation is mandatory!

### Branching with the `if` Statement

Just like in JavaScript, we can use an `if` statement to branch to one of several code paths depending upon the result of conditional expression(s).

Single path `if` statement:

```python
floor = "sticky"
walls = "clean"
if floor == "sticky":   # don't forget the colon
  print("Clean the floor! It's sticky!")
  # more lines of code in this code
  # block need to be indented as well
if walls == "sticky":
  print("Clean the walls! They're sticky!")
```

Yup, no parentheses are required around the conditional expression.

Dual path `if..else` statement:

```python
if condition:
  # do something
else:
  # do something else
  # do something else
```

Multi-path `if..elif..else` statement:

```python
if condition1:
  # do something
  # do something
elif condition2:
  # do something else
  # do something else
  # do something else
elif condition3 and condition4:
  # do another thing entirely
  # do another thing entirely
else:
  # else do this stuff
```

The `elif` is not a typo :)

As in JS, including an `else` is optional.

> 👀 There is no `switch` construct in Python

### 👉 You Do - Branching Exercise <small>(5 minutes)</small>

Copy/paste the following code that accepts text input from the user, converts it to lowercase and prints it:

```python
color = input('Enter "green", "yellow", "red": ').lower()
print(f'The user entered {color}')
```

<details>
<summary>
❓ What was the function we used in JavaScript to get input from the user?
</summary>
<hr>

`input()`

<hr>
</details>

Below that code, write an `if...elif...else` statement that prints out one of the following messages:

- If `green` is entered, print the message `Go!`
- If `yellow` is entered, print the message `Slow Down!`
- If `red` is entered, print the message `Stop!`
- If anything else is entered, print the message `Bogus!`

Test the code by running it in the repl.

## 5. Looping

### The `for` Statement

Python's `for` statement is not designed like the one you first used in JavaScript:

```js
// A JavaScript for loop
for (let i = 0; i < 10; i++) {
  // do stuff
}
```

Instead, the Python `for` loop always iterates over the items in a _sequence_, similar to JavaScript's `for...in` and `for...of` loops.

We'll learn about sequences soon, but here's a taste of how Python's `for` loop is used to loop through a **list** (Python's array):

```python
names = ["Tom", "Deborah", "Murray", "Axel"]

for name in names:
  print(name)
```

The above Python code is like the following ES2015 JS:

```js
const names = ["Tom", "Deborah", "Murray", "Axel"];

for (let name of names) {
  console.log(name);
}
```

### The `while` loop

Python also has a `while` loop construct that will continue to iterate **while a given condition is truthy** - just like in JavaScript.

Let's look at the syntax:

```python
while condition:
  # do some stuff
  # continue to do stuff
```

`while` loops are the go to when the number of times you will need to iterate is unknown.

> 👀 Beware of infinite loops! When using `while` loops, it's important to ensure that the condition will become falsy as some point so that the loop exits.

### The `break` and `continue` Statements

Just like in JavaScript...

The `break` statement is used to immediately exit `for` and `while` loops and continue executing any statements that may follow them.

The `continue` statement is used to immediately return to the top of the `for` or `while` loop.  In the case of a `while` loop, its conditional expression is once again evaluated to determine if the loop should continue.

### 👉 You Do - Looping Exercise <small>(3 minutes)</small>

Wrap the "color" code from the branching exercise in a `while` loop such that it continues to prompt for a color and print the response until the word `quit` is entered.

> Hint: Same gotcha as when you did this exercise in JS 😁  If you get an error, read it - you got this!

## 6. Python Ranges

### Purpose of Ranges

Python _**ranges**_ are a _sequence type_ like _lists_ and _tuples_.

The **range** type represents an immutable sequence of integers and is commonly used for looping a specific number of times in `for` loops.

_Ranges_ have a class (type) of `range`.

### Ranges - Basic Syntax

Ranges can be created by invoking the `range()` class:

```python
for num in range(5):
  print(num)
> 0
> 1
> 2
> 3
> 4
```

Notice that by default, the sequence starts at `0` and goes up to, but does not including the integer passed in.

Ranges can also generate sequences with a **start** and a **step**:

```python
for even in range(2, 10, 2):
  print(even)
> 2
> 4
> 6
> 8
```

When not passed in, the _start_ value defaults to `0` and the _step_ defaults to `1`.

Ranges can also be used to create _lists_ and _tuples_:

```python
nums = list(range(10))
print(nums)
> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
odds = tuple(range(1, 10, 2))
print(odds)
> (1, 3, 5, 7, 9)
```

### Ranges - Negative Step

If the _step_ is a negative integer, the _sequence_ counts down:

```python
for num in range(5, 0, -1):
  print(num)
> 5
> 4
> 3
> 2
> 1
```

## 7. Summary

As you have seen today so far, Python is not all that different than JavaScript.

Applying what we did in this lesson in the lab will provide you with some practice performing branching and looping in Python.

But first...

## 8.❓ Essential Questions <small>(1 minute)</small>

<details>
<summary>
(1) What are the two types of control flow discussed in this lesson.
</summary>
<hr>

**Branching** and **Looping**

<hr>
</details>

<details>
<summary>
(2) Name three things in Python that are considered to be falsy.
</summary>
<hr>

**Any three of the following:**

`False`, `None`,<br>
`0`, `0.0` and `0j` (zero)<br>
Empty sequences or collections:
- `''` (empty string)
- `[]` (empty list)
- `()` (empty tuple)
- `{}` (empty dictionary)
- `range(0)` (empty range)

<hr>
</details>

```python
25 or 50
```
<details>
<summary>
(3) What is returned by the above expression?
</summary>
<hr>

`25`

<hr>
</details>
	
```python
25 and 50
```
<details>
<summary>
(4) What is returned by the above expression?
</summary>
<hr>

`50`

<hr>
</details>

## References

[Official Docs for Control Flow in Python](https://docs.python.org/3/tutorial/controlflow.html#)

<img src="https://i.imgur.com/DPzk4Ok.png">

# Control Flow in Python - Lab

## Intro

Let's get some practice working with control flow and logic in Python!

#### This lab is a DELIVERABLE

## Setup and Instructions

1. Create a new Python-based repl in [Replit](https://replit.com) and name it "Python Control Flow Lab"

2. Copy and paste the prompts/hints from the exercises section below into the the repl.

3. After completing each exercise, you may comment out that exercise's code to ease completion of subsequent exercises.

4. Before submitting, please uncomment ALL solutions.

## Exercises

```python
# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z): 
# 2. Write the code that determines whether the letter entered is a vowel
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant

# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':





# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.





# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age like this:
#      Input a dog's age: 
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

# Hints:
# Use the int() function to convert the string returned from input() into an integer
# Start with an if that checks if the age is less than 3





# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equilateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - exactly two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle






# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hints:
# The next number is found by adding the two numbers before it
# Use a while loop with a looping variable, or look into Python ranges, e.g.:
#   for n in range(50):





# exercise-06 What's the Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
#   if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.



```

## Solutions

Possible solutions are [here](https://repl.it/@jim_clark/Python-Control-Flow-Lab), but do your best not to peek.

## Deliverable

This lab is a deliverable.

Please submit the link to your Python repl as directed. 

<img src="https://i.imgur.com/DPzk4Ok.png">

# Python Containers

## Learning Objectives

| Students will be able to: |
|---|
| Use **Lists**, **Tuples** & **Dictionaries** as Containers for Data |
| Use **List Comprehensions** to Create Lists |
| Create Subsets of a Sequence Using the **Slice Operator** |

## Road Map

1. Setup
2. General Purpose Containers
3. Dictionaries
4. Lists
5. List Comprehensions
6. Tuples
7. Slicing (Copying) Sequences
8. Python Containers Summary
9. Essential Questions

## 1. Setup

To test some of the examples and complete the exercises:
- Create a new Python-based [replit](https://replit.com/)
- Name it something like "Python Containers"

## 2. General Purpose Containers

As you've learned, applications frequently need to maintain collections of data.

We use a container data structures to hold these collections of data...

<details>
<summary>
❓ What did we use in JS to hold collections of data?
</summary>
<hr>

**`objects` and `arrays`** (although arrays are actually objects in JS)

<hr>
</details>

In this lesson, we're going to review the following Python built-in types commonly used as containers:

- [Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- [Tuples](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)

## 3. Dictionaries

### Purpose

**Dictionaries** are to Python as **objects** are to JS.

A **dictionary** provides a container for `key: value` pairs.

In Python, we commonly refer to `key: value` pairs as **items** vs. **properties** as in JS.

Dictionaries have a class (type) of `dict`.

### Basic Syntax

As with objects in JS, a **dictionary** is created literally using curly braces:

```python
student = {
  'name': 'Maria',
  'course': 'SEI',
  'current_week': 7
} 
```

Unlike in JS, when strings are used as keys, they must be quoted.

### Features

Dictionaries are mutable:

- The values assigned to a key can be changed
- Additional items can be added
- Existing items can be deleted
 
Any immutable type can be used as a key, including _numbers_ and _tuples_ (which we'll cover in a bit), for example:

```python
option = 3

d = {
  option: 'three'
}
```

The above dictionary, `d`, has 1 item with a key of `3` that holds the value of `'three'`.  Note that the value of the `option` variable is "copied" as the key - thus no "link" to the `option` variable is created.

> 👀 Only since version 3.6 does Python track the insertion order of items in a dictionary - so beware if you're relying on the order items are iterated upon.

### Getting and Setting Values

We always use **square bracket notation** to get and set an item's value:

```python
name = student['name']
print(name)
> Maria
student['name'] = 'Tina'
print(student['name'])
> Tina
```

Unlike JS, we can't access items in a Python dictionary using dot notation.

### The `get()` Method

When accessing a key that does not exist in a dictionary, a `KeyError` will be raised. 

<details>
<summary>
❓ What happens when we access a property that does not exist in a JS object? 
</summary>
<hr>

We'll receive a runtime exception called *keyError* and no value will be returned. 

<hr>
</details>

One option to avoid this error is to use the `get()` method:

```python
skills = student['skills']
> KeyError: 'skills'
print( student.get('skills') )
> None
# Provide a default value if key not in dictionary
print( student.get('skills', {'HTML': 5, 'JAVASCRIPT': 4}) )
> {'HTML': 5, 'JAVASCRIPT': 4}
```

The actual default value would of course depend on what makes sense for your app.

### The `in` Operator

Another way to avoid the `KeyError` is to use the `in` operator to check if the dictionary includes a certain key:

```python	
if 'course' in student:
  print( f"{student['name']} is enrolled in {student['course']}")
else:
  print( f"{student['name']} is not enrolled in a course")
```

The `in` operator always returns a boolean (`True` or `False`).

### Adding Items

Simply assigning to a key that does not exist will create a new item in the dictionary.

Let's add an item to `student`:

```python
student['age'] = 21
```

<details>
<summary>
❓ If an <code>'age'</code> item already existed, what would happen?
</summary>
<hr>

**It would be updated**

<hr>
</details>

### Deleting Items

The `del` statement is used to delete an item from a dictionary:

```python
del student['age']
# Verify that item was deleted
'age' in student
> False
```

> 👀 A `del` statement does not return a value

### Number of Items

Use the built-in `len()` function to retrieve the number of items in a dictionary:

```python
print( student )
> {'name': 'Tina', 'course': 'SEI'}
len(student)
> 2
len({})
> 0
```

### Dictionaries - Iterating Items

`for...in` loops are used to iterate over the items in a dictionary. 

However, accessing the value of an item as follows is considered to be a Python [anti-pattern](https://en.wikipedia.org/wiki/Anti-pattern):

```python
for key in student:
  print( f"{key} = {student[key]}" )
```
	
The preferred approach is to use the `items()` method to obtain a [dictionary view object](https://docs.python.org/3/library/stdtypes.html#dictionary-view-objects).

`student.items()` returns a wrapped list of (key, value) tuples:

```python
student.items()
> dict_items([('name', 'Tina'), ('course', 'SEI')])
```

Now we can use a `for...in` loop to iterate over the view object:

```python
for key, val in student.items():
  print( f"{key} = {val}" )
```

The `for` statement "unpacks" the tuples by assigning its values to multiple variables like with `key, val` above.

### 👉 You Do - Dictionary Practice Exercise <small>(10 mins)</small>

1. Define a Python dictionary named `where_my_things_are` containing a few items where:
	- the `keys` are things you have, and
	- the `values` are the locations you keep those things.

2. Write a `for...in` loop that iterates over the items in the dictionary and prints each one as<br>**_My [thing] is kept [location]_**

## 4. Lists

### Purpose

**Lists** are to Python as **arrays** are to JS.

A **list** provides a container for zero or more items (_elements_ in JS arrays).

**Lists** can contain items of different types, including dictionaries and nested lists.

**Lists** have a class (type) of `list`.

### Basic Syntax

Like arrays in JS, a **list** can be created literally with a set of **square brackets**:

```python
colors = ['red', 'green', 'blue']
```

The number of items in a list is returned using the built-in `len()` function:

```python
len(colors)
> 3
```

### Features

Lists are considered to be a _sequence_ type in Python. A _sequence_ is a generic term used for an **ordered** collection. Other _sequence_ types in Python include **strings** and **tuples**.

Lists are mutable:

- Existing items within a list can be updated
- Items can be added to a list
- Items can be removed from a list

### Accessing Items

Accessing the individual items of a list is much like accessing elements in a JS array, i.e., by using square bracket notation with an expression that evaluates to an integer:

```python
idx = 1
colors[idx + 1]
> blue
```

However, unlike in JS, we can use negative integers to index from the end of a list:

```python
colors[-1]
> blue
```

No need to write code like `colors[len(colors) - 1]` - yay!

### Assigning Items

We also use square brackets to target an item of a list for assignment:

```python
colors[-1] = 'brown'
print(colors)
> ['red', 'green', 'brown']
```

Unlike with JS arrays, assigning to a non-existing index results in an error:

```python
colors[10] = 'yellow'
> IndexError: list assignment index out of range
```

### Adding an Item

The equivalent to JS's `push()` method is `append()`:

```python
colors.append('purple')
```
	
However, unlike JS's `push()` method, `append()` can only add one item and does not return a value.

<details>
<summary>
❓ What does a JavaScript array's <code>push()</code> method return?
</summary>
<hr>

**The new length of the array**

<hr>
</details>
	
For adding multiple items, use the `extend()` method:

```python
colors.extend(['orange', 'black'])
```

or the `+=` operator:

```python
colors += ['orange', 'black']
```

The `+` operator can be used to create a **new list** by combining others:

```python
odds = [1, 3, 5]
evens = [2, 4, 6]
nums = odds + evens
print(nums)
> [1, 3, 5, 2, 4, 6]
```

### Inserting an Item

To add an item anywhere within a list, use the `insert()` method:

```python
print(colors)
> ['red', 'green', 'brown', 'purple', 'orange', 'black']
colors.insert(1, 'yellow')
> ['red', 'yellow', 'green', 'brown', 'purple', 'orange', 'black']
```

### Removing an Item

Yup, there's a `pop()` method, but it's more flexible in Python because you can specify the index of the item to remove and return:

```python
print(colors)
> ['red', 'yellow', 'green', 'brown', 'purple', 'orange', 'black']
green = colors.pop(2)
print(colors)
> ['red', 'yellow', 'brown', 'purple', 'orange', 'black']
```

If you don't care about the value returned by `pop()`, you can also use the `del` operator to delete an item:

```python
print(colors)
> ['red', 'yellow', 'brown', 'purple', 'orange', 'black']
del colors[1]
print(colors)
> ['red', 'brown', 'purple', 'orange', 'black']
```

Also there's a `remove()` method that removes the first item that matches what you pass in:

```python
print(colors)
> ['red', 'brown', 'purple', 'orange', 'black']
colors.remove('orange')
print(colors)
> ['red', 'brown', 'purple', 'black']
```

No value is returned by the `remove()` method.

### Clearing an Entire List

The `clear()` method does just what you'd think:

```python
print(colors)
> ['red', 'brown', 'purple', 'black']
colors.clear()
print(colors)
> []
```

### Iterating Over Items in a List

The `for...in` loop is used to iterate over the items in a list:

```python
colors = ['red', 'green', 'blue']
for color in colors:
  print(color)
> red
> green
> blue
```

If we need to access the index of the item while iterating over a list, we use the built-in `enumerate()` function to provide the index and the value to a `for...in` loop:

```python
for idx, color in enumerate(colors):
  print(idx, color)
> 0 red
> 1 green
> 2 blue
```

Please navigate to the next page where you will complete and submit the following exercise...

### 👉 You Do - Lists & Dictionary Practice Exercise <small>(10 mins)</small>

1. Define a list named `scores` that contains a dictionary with the following shape:
    ```python
    scores = [
      {
        'name': 'name of the player',
        'points': 25  # points the player scored
      }
    ]
    ```
2. Next, using `append()`, to add an additional "score" dictionary to the `scores` list.
3. Iterate over the items in the `scores` list and print a string with this format
    ```
    <name> scored <points> points
    ```
    for each dictionary item in the list.

## 5. List Comprehensions

### Purpose

[List comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions) are a powerful feature in Python.

They provide a concise way to create and work with lists.

They will seem confusing as first, but they certainly are a favorite of Pythonistas and you will probably come across them when googling.

### Numerical Example

Say we needed to square all of the numbers in a list and put them into a new list, we might use a for loop like this:

```python
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	
# I want 'n * n' for each 'n' in nums 
squares = []
for n in nums:
  squares.append(n * n)
print(squares)
> [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

<details>
<summary>
❓ What JS method would we use in this scenario?
</summary>
<hr>

**`map()`**

<hr>
</details>

A list comprehension can reduce this code:

```python
squares = []
for n in nums:
  squares.append(n * n)
```
To this:
	
```python
squares = [n * n for n in nums]
```

> 👀 Again, a list comprehension always returns a **new** list.

### Basic Syntax

Here's the basic syntax of a list comprehension:

```python
# [<expression> for <item> in <list>]
# This reads as: I want <expression> for each <item> in <list>
```

As you can see, a list comprehension is basically a modified `for...in` loop within square brackets that returns a new list.

### Filtering the Items

We just saw how list comprehensions are a nice way to map a list, but they can be used for **filtering** too.

Again, let's start with a non-comprehension approach by using a `for...in` loop to map and filter `nums`:

```python
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	
# I want 'n * n' for each 'n' in nums  if 'n * n' is even
even_squares = []
for n in nums:
  square = n * n 
  if square % 2 == 0:
    even_squares.append(square)
print(even_squares)
> [4, 16, 36, 64, 100]
```

Again list comprehensions reduce the above from:

```python
even_squares = []
for n in nums:
  square = n * n 
  if square % 2 == 0:
    even_squares.append(square)
```
To this one-liner:
	
```python
even_squares = [n * n for n in nums if (n * n) % 2 == 0]
```
Talk about less is more!

### ❓ List Comprehensions - Review Questions

<details>
<summary>
(1) What characters start and end a list comprehension?
</summary>
<hr>

A `[` starts the list comprehension and a `]` ends it

<hr>
</details>

<details>
<summary>
(2) True or False: A list comprehension creates a new list?
</summary>
<hr>

**True**

<hr>
</details>

## 6. Tuples

**Tuples** in Python are very similar to Python **lists**.

Tuples have a class (type) of `tuple`.

You may come across tuple's being "classified" based on how many items they contain, e.g., a **2-tuple** would contain two items such as `(some_key, some_value)`.

### Basic Syntax

Tuples can be defined in a few different ways.  Most basically, they are defined like this:

```python
colors = ('red', 'green', 'blue')
print(colors)
> ('red', 'green', 'blue')
print( len(colors) )
> 3
``` 

The parentheses are actually optional.  The following would work as well:

```python
colors = 'red', 'green', 'blue'
```

However, using parenthesis seems to be the convention.

If you need to create a 1-tuple (a tuple with one item), be aware that a comma is necessary:

```python
# Will not create a tuple
hello_tuple = ('Hello')
print( type(hello_tuple) )
>  <class 'str'>

hello_tuple = ('Hello',)
# or just the following (no parens required)
hello_tuple = 'Hello',
print( type(hello_tuple) )
> <class 'tuple'>
```
	
### Differences Between Tuples & Lists

The main difference between tuples and lists is that tuples are immutable.

Since tuples can't be changed after they are created, they are great for protecting data that you don't want to be changed.

Tuples internally are "lighter weight" than lists and Python iterates over tuples faster than lists.

Because they are immutable, tuples can even be used as keys for dictionaries.

Generally, you'll find that tuples are used to contain heterogeneous (different) data types and lists for homogeneous (similar) data types.

### Accessing Items

Although tuples can't be modified like lists, we retrieve their items in the same way using square brackets:

```python
colors = ('red', 'green', 'blue')
green = colors[1]
print(green)
> green
```

_Sequences_ (lists, tuples & strings) also have an `index()` method that returns the index of the first match:

```python
colors = ('red', 'green', 'blue')
blue_idx = colors.index('blue')
print(blue_idx)
> 2
```

### Iteration

The items in tuples are iterated over by using `for...in` loops as we saw previously with lists:

```python
colors = ('red', 'green', 'blue')
for idx, color in enumerate(colors):
  print(idx, color)
> 0 red
> 1 green
> 2 blue
```

### Unpacking Tuples

Tuples (and other sequences such as lists & strings) have a convenient feature, called **unpacking**, for performing multiple variable assignments in a single line of code:

```python
colors = ('red', 'green', 'blue')
r, g, b = colors
print(r, g, b)
> red green blue
```

Comma separated variables on the left-side of the assignment operator and a sequence of values on the right is what it takes.

FYI, we were seeing unpacking in action within the `for in` loops above, for example:
 
```python
for key, val in student.items():
  print( f"{key} = {val}" )
```

## 7. Slicing (Copying) Sequences

Slicing in Python is used to create "slices" (copies) of sequences.

However, instead of using a `slice` method like we did in JS, Python has a cool "slice" operator that uses this syntax:

```python
a_sequence[m:n]
```

Just like with indexing, slicing uses square brackets, but adds a colon:

```python
short_name = 'Alexandria'[0:4]
print(short_name)
> Alex
```

Note that the slice includes up to, **but not including** the index to the right of the colon.

<details>
<summary>
❓ Is this the same as with the ending index in JS's <code>slice()</code> method?
</summary>
<hr>

**Yes!**

<hr>
</details>

If the first index is omitted, a default starting index of `0` is used:

```python
colors = ('red', 'green', 'blue')
print( colors[:2] )
> ('red', 'green')
```
 
If the up to index is omitted, the slice copies the sequence all the way to the end:

```python
colors = ['red', 'green', 'blue']
print( colors[1:] )
> ['green', 'blue']
```

Assuming the following code:

```python
fruit = ('apples', 'bananas', 'oranges')
fruits = fruit[:]
```

<details>
<summary>
❓ What would the value of <code>fruits</code> be?
</summary>
<hr>

```python
('apples', 'bananas', 'oranges')
```
Yes, an entire copy of the source tuple!

<hr>
</details>

### Slice Assignment in Lists

Amazingly, we can use the slice operator to insert and/or remove items in a list - similar to how JavaScript's `splice()` method can be used.

For example, assume this list:

```python
chars = ['a', 'b', 'x', 'y', 'd']
```

We could replace the `'x'` and `'y'` characters with `'c'` like this:

```python
chars = ['a', 'b', 'x', 'y', 'd']
chars[2:4] = 'c'
print(chars)
> ['a', 'b', 'c', 'd']
```

Notice how our resulting list is smaller than our original list, this is due to python not changing each item within from our range, but instead, replacing the entire range provided(2-4) of our list with a single value, this means we removed items at index locations 2, 3, and 4 and replaced those three items with a single item, 'c'. 

## 8. Python Containers Summary

Python's **dictionary**, **list** and **tuple** are the most common data types used as containers for collections of data.

In addition, Python offers amazing power, convenience and readability with features such as list comprehensions and slicing.

However, as usual, it takes practice to become "comfortable" with these concepts, so on to the lab, but first...

## 9. ❓ Essential Questions <small>(1 minute)</small>

<details>
<summary>
(1) What is the practical difference between a list and a tuple.
</summary>
<hr>

**Unlike lists, tuples are immutable** (cannot be changed)

<hr>
</details> 

```python
fruit = {
  'apples': 'red',
  'bananas': 'yellow',
  'oranges': 'orange'
}

color_of_bananas = fruit.bananas
```

<details>
<summary>
(2) What's the problem with the above code?
</summary>
<hr>

On this line of code:
```python
color_of_bananas = fruit.bananas
```
The `fruit.bananas` won't work because we have to use square bracket notation, such as:
```python
color_of_bananas = fruit['bananas']
```

<hr>
</details>

```python
one, two, three = 'abc'
```
<details>
<summary>
(3) What concept is being used above to assign values to the variables and what would the value of <code>two</code> be?
</summary>
<hr>

The concept is known as **unpacking**.

The value of `two` would be `'b'`

<hr>
</details>

<img src="https://i.imgur.com/DPzk4Ok.png">

# Python Containers - Lab

**This lab is a DELIVERABLE**

## Setup and Instructions

- Create a Python-based [replit](https://replit.com) and name it "Python Containers Lab".
- Put a commented heading for each exercise in your repl.  For example:

  ```python
  # Exercise 1

  # your solution here


  # Exercise 2

  # your solution here

  # etc.....
  ```

- Complete the exercises below...

## Exercises


#### Exercise 1

- Create a list named `students` containing some student names (strings).
- Print out the second student's name.
- Print out the last student's name.

#### Exercise 2

- Create a tuple named `foods` containing the same number of foods (strings) as there are names in the `students` list.
- Use a `for` loop to print out the string "[_food goes here_] is a good food".

#### Exercise 3

- Using a `for` loop, print just the last two food strings from `foods`.

  > Hint:  Use the slice operator to select the last two foods

#### Exercise 4

- Create a dictionary named `home_town` containing the keys of `city`, `state` and `population`.
- Print a string with this format:<br>"I was born in _city_, _state_ - population of _population_"

#### Exercise 5

- Iterate over the _key: value_ pairs in `home_town` and print a string for each item, for example:<br>"city = Arcadia"<br>"state = California"<br>"population = 58000"

#### Exercise 6

- Create an empty list named `cohort`.
- Using a `for` loop to iterate over the `students` list.
  > Hint: Use the `enumerate` function to provide both the index & student
- Within the `for` loop, add a dictionary to the `cohort` list that combines the student's name and the food in the `foods` list at the same index. Each dictionary will have this shape:

	```python
	{
	  'student': 'Tina',
	  'fav_food': 'Cheeseburger'
	}
	```
- Iterate over the `cohort` list, printing out each item (it's not necessary to format the dictionaries).


#### Exercise 7

- Using the list of `students` and a list comprehension, assign to a variable named `awesome_students` a new list containing strings similar to this:<br>`["Tina is awesome!", "Fred is awesome!", "Wilma is awesome!"]`
- Iterate over the `awesome_students` list, printing out each string.

#### Exercise 8

- Use a `for` loop to iterate over a list comprehension that filters the  `foods` tuple to only include food strings that contains the letter `a`.
- Within the `for` loop, print each food string.

## Solutions

A solution can be found [here](https://repl.it/@jim_clark/Python-Containers-and-Ranges-Lab).

## Deliverable

**This lab is a deliverable.**

Please submit the link to your Python repl as directed.


<img src="https://i.imgur.com/uz3kC2P.jpg">

# Python Functions 

## Learning Objectives

| Students Will Be Able To: |
|---|
| Compare Python to JavaScript functions |
| Define functions in Python |
| Invoke functions in Python |
| Use `*args` and `**kwargs` parameters |

## Road Map

1. Setup
2. Review the Use Case of Functions - What & Why
3. Defining Functions in Python
4. A Minimal Function in Python
5. Key Differences Between Python & JS Functions
6. Calling Functions
7. Parameters & Arguments
8. Essential Questions

## 1. Setup

To practice with the code in this lesson:
- Create a new Python-based repl in [repl.it](https://repl.it)
- Name it something like "Python Functions"

## Review the Use Case of Functions - What & Why?

Let's review the use case of functions...

<details>
<summary>
❓ What is a function?
</summary>
<hr>

**A function is a block of code that can be called with inputs and optionally returns an output.**

<hr>
</details>

<details>
<summary>
❓ Why are functions necessary in development?
</summary>
<hr>

**Functions provide:**

- Code organization/modularization
- Code reusability
- Readability (when functions are appropriately named)

<hr>
</details>

Functions are the building blocks of programming and all programming languages have them, including Python...

## 3. Defining Functions in Python

Here's how we define a basic function in Python:

<img src="https://i.imgur.com/pixhxbF.png">

As you can see:

- The first line starts with the `def` keyword. This defines a function.
- The next word is the name (identifier) of the function.
- Following that is a parameter list inside parentheses.
- The first line ends with a colon.
- The first line is followed by an indented code block that we have become familiar with.
- Python functions, like JS, optionally return a value using a `return` statement.

## 4. A Minimal Function in Python

In JavaScript, we often would "stub up" an "empty" function temporarily:

```js
function someFunction() {

}
```

The following is how we would "stub up" a function in Python:

```python
def first_function():
  pass
```

The `pass` statement is simply a "do nothing" statement and is useful here to create a function that has at least one statement in its block, which is a requirement. 

<details>
<summary>
❓ What does a JS function return by default if it doesn't include a return statement?
</summary>
<hr>

**`undefined`**

<hr>
</details>

Let's see what a Python function returns by default:

```python
def first_function():
  pass

# Assign value returned by default
result = first_function()
print(result)
``` 

Good guess!

## 5. Key Differences Between Python & JS Functions

Besides the obvious syntactical differences, here are a few other things to be aware of...

#### Python functions are similar to function definitions in JS (not function expressions)

Functions in Python are defined using the `def` keyword.

Unlike JS's function expressions, they cannot be assigned to variables at the time they are being defined:

```python
# This will not work
my_function = def my_function():
  pass
```

However, after being defined, they can be assigned to variables, referenced by dictionaries/lists, etc.

For example, here's how you could dynamically "select" which function to call using a dictionary instead of a potentially huge `if...elif...else` statement:

```python
def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

math_operations = {
  '+': add,
  '-': subtract
}

selected_operation = '+'

math_operations[selected_operation](2, 4)
> 6
```

#### Python has `lambda` functions instead of arrow functions

Python `lambda` functions are very much like _Arrow Functions_ in JavaScript:  

- They implicitly return a single expression's value.
- They are expressions so they are commonly used as "inline" arguments.
- They can be assigned to a variable.

However, unlike arrow functions, they cannot have any code block - just a single expression that has its result implicitly returned.

For example:

```js
// JavaScript
const nums = [1, 3, 2, 6, 5];
let odds = nums.filter(num => num % 2);
```
	
```python
# Python
nums = [1, 3, 2, 6, 5]
odds = list( filter(lambda num: num % 2, nums) )
```

Lambda functions are nifty when using Python functions such as `map()` and `filter()` - just like how arrow functions are nifty when using array iterator methods.

#### Python does not "hoist" functions

A key difference between Python and JavaScript functions is that you cannot invoke a Python function before the code that defines it:

```python
# Will cause an error - must call function AFTER it has been defined
add(5, 10)

def add(a, b):
  return a + b
```

## 6. Calling Functions

In Python, calling functions is the same as it is in JavaScript:

```python
def add(a, b):
  return a + b
  
def sub(a, b):
  return a - b

def compute(a, b, op):
  return op(a, b)

print( compute(1, 2, add) )
```

Yup, functions in Python can be passed to other functions - **callbacks** exist in Python!

Let's learn more about Python's **parameters** & **arguments**...

## 7. Parameters & Arguments

Just like in JS, **parameters** are the placeholders for passing input to a function.

However, Python has more options when defining parameters.

```python
# a & b are parameters
def add(a, b):
  return a + b
```

Also like JS, the values/expressions passed to a function when calling it are known as **arguments**:

```python
num = 5

# num & 10 are arguments
add(num, 10)
```

However, unlike JavaScript, Python requires that the correct number of arguments be provided when calling a function. For example:

```python
def add(a, b):
  return a + b
  
add()
  
# Generates the following error:
# TypeError: add() missing 2 required positional arguments: 'a' and 'b'
```

### Accepting a varying number of arguments

In JavaScript, we were able to access "extra" arguments being passed in to a function by using the `arguments` keyword:

```js
// Using the arguments special variable
function sum() {
  let total = 0;
  for (arg of arguments) total += arg;
  return total;
}

console.log( sum(1, 5, 10) );  // -> 16
```

Or preferably by using ES2015's _rest parameters_:

```js
function sum(...nums) {
  return nums.reduce((sum, num) => sum + num, 0);
}

console.log( sum(1, 5, 10) );  // -> 16
```

#### Python's `*` Parameter Specifier (`*args`)

Using the `*` ("star") specifier in a parameter list allows us to pass in a varying number of **positional** arguments into a function:

```python
def fn(*args):
  print( type(args) )
  for arg in args:
    print(arg)

fn(1, 2, 'SEI')
''' Output:
<class 'tuple'>
1
2
SEI
'''
```

The identifier used with `*`, i.e., `args`, can be anything, however **by convention, use `args`**.

Always use the `*args` parameter **after** any **required** positional parameters. For example:

```python
def dev_skills(dev_name, *args):
  dev = {'name': dev_name, 'skills': []}
  # args will be a tuple
  for skill in args:
    dev['skills'].append(skill)
  return dev

print(dev_skills('Alex', 'HTML', 'CSS', 'JavaScript', 'Python'))
# -> {'name': 'Alex', 'skills': ['HTML', 'CSS', 'JavaScript', 'Python']}
```

Or, why not use the `list()` function to convert the args tuple into a list...

```python
def dev_skills(dev_name, *args):
  dev = {'name': dev_name, 'skills': list(args)}
  return dev
```

#### Python's `**` Parameter Specifier (`**kwargs`)

First, the reason we name the parameter `kwargs` is because it stands for **keyword arguments**.

A **keyword argument** is an argument with a _name_, and this is why keyword arguments are also referred to as **named arguments**.

For example, assume the following function:

```python
def divide(a, b):
  return f'{a} divided by {b} is {a / b}'
```

Not that it's recommended, but knowing how the function is defined above, we could invoke the function using keyword arguments where the order of the arguments doesn't matter:

```python
divide(b=25, a=100) # returns '100 divided by 25 is 4.0'
```

However, the above example is not how keyword arguments are commonly used...

First, we use the `**` specifier when defining a parameter named `**kwargs` (named by convention).

By adding `**kwargs` at the **end of the parameter list**, we can access any number of keyword arguments. 

For example:

```python
def dev_skills(dev_name, **kwargs):
  # kwargs will be a dictionary!
  dev = {'name': dev_name, 'skills': kwargs}
  return dev

print(dev_skills('Jackie', HTML=5, CSS=3, JavaScript=4, Python=2))
```

#### Combining Required Positional, Optional Positional (`*args`) & Keyword (`**kwargs`) Arguments

You can use all three types of parameters in the same function, but they have to be defined in the following order:

```python
def arg_demo(pos1, pos2, *args, **kwargs):
  print(f'Positional params: {pos1}, {pos2}')
  print('*args:')
  for arg in args:
    print(' ', arg)
  print('**kwargs:')
  for keyword, value in kwargs.items():
    print(f'  {keyword}: {value}')

arg_demo('A', 'B', 1, 2, 3, color='purple', shape='circle')
```

Output:

```
Positional params: A, B
*args:
  1
  2
  3
**kwargs:
  color: purple
  shape: circle
```

## 8. ❓ Essential Questions (2 minutes)

```python
def get_category(points):
  if points > 900:
    return 'Gold Member'
  elif points > 800:
    return 'Silver Member'
  else:
    return 'Bronze Member'

print( get_category(850) )
```

<details>
<summary>
(1) Which line of code within the above <code>get_category()</code> function will be the last to execute?
</summary>
<hr>

```python
    return 'Silver Member'
```

<hr>
</details>


```python
def add(a, b):
  return a + b
```

(2) Assuming the above function:

**Which of the following statements will result in an error?<br> (there could be more than one)**
	
A) `add(10, 100.)` <br>
B) `add(10, '10')` <br>
C) `add(100)` <br>
D) `add('abc', 'def')` <br>
E) `add(10, 20, 30)` <br>

<details>
<summary>
Answer to (2)
</summary>
<hr>

```
A) No error, because we can add integers and floats together
B) Error, because we cannot "add" an integer to a string
C) Error, because we need to provide two arguments
D) No error, because we can "add" strings together
E) Error, because there are too many arguments
```

<hr>
</details>

<details>
<summary>
(3) What "feature" in Python would allow the <code>add()</code> function above to accept any number of numbers to add together?
</summary>
<hr>

**`*args`**

<hr>
</details>

## References

[*args and **kwargs in python explained](https://pythontips.com/2013/08/04/args-and-kwargs-in-python-explained/)










<img src="https://i.imgur.com/Q5SFLV2.png">

# Python Functions Lab

## Intro

Time to practice some Python by writing functions that solve the four challenges below.

To test your functions, be sure to call each function at least once and `print` the returned value.

##### This Lab is NOT a Deliverable

## Setup

You may write the functions in a `.py` file or use a Python repl in repl.it

## Challenges

1. Write a function named `sum_to` that accepts a single integer, `n`, and returns the sum of the integers from 1 to `n`.
	
	For example:

	```python
	sum_to(6)  # returns 21
	sum_to(10) # returns 55
	```

2. Write a function named `largest` that takes a list of numbers as an argument and returns the largest number in that list.

	For example:
	
	```python
	largest([1, 2, 3, 4, 0])  # returns 4
	largest([10, 4, 2, 231, 91, 54])  # returns 231
	```

3. Write a function named `occurrences` that takes two string arguments as input and counts the number of occurrences of the second string inside the first string.

	For example:

	```python
	occurrences('fleep floop', 'e')   # returns 2
	occurrences('fleep floop', 'p')   # returns 2
	occurrences('fleep floop', 'ee')  # returns 1
	occurrences('fleep floop', 'fe')  # returns 0
	```

4. Write a function named `product` that takes an *arbitrary* number of numbers, multiplies them all together, and returns the product.<br>(HINT: Review your notes on `*args`).

	For example:
	
	```python
	product(-1, 4) # returns -4
	product(2, 5, 5) # returns 50
	product(4, 0.5, 5) # returns 10.0
	```

## Bonus Challenge

1. Write a function named `steps_to_zero` that accepts a non-negative integer as an argument, and returns the number of steps it took to reduce the integer to zero. If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
	
	For example:
	
	```python
	steps_to_zero(14) # returns 6
	```
	
	Explanation:
	```
	Step 1) 14 is even; divide by 2 and obtain 7. 
	Step 2) 7 is odd; subtract 1 and obtain 6.
	Step 3) 6 is even; divide by 2 and obtain 3. 
	Step 4) 3 is odd; subtract 1 and obtain 2. 
	Step 5) 2 is even; divide by 2 and obtain 1. 
	Step 6) 1 is odd; subtract 1 and obtain 0.
	```

## Solutions (do not peek unless you are stuck or finished)

<details>
  <summary><strong>Challenge 1</strong></summary>

  ```python
  def sum_to(num):
    sum = 0
    for n in range(1, num + 1):
      sum += n
    return sum
  ```
</details>

<details>
  <summary><strong>Challenge 2</strong></summary>

  ```python
  def largest(nums):
    largest = 0
    for num in nums:
      if num > largest:
        largest = num
    return largest
    
  # Sort the list approach
  def largest(nums):
    nums.sort()
    return nums[-1]
  ```
</details>

<details>
  <summary><strong>Challenge 3</strong></summary>

```python
def occurrences(string, substr):
  # remove each occurrence of substr
  stripped_string = string.replace(substr, '')
  # compute based on length of the strings
  return (len(string) - len(stripped_string)) // len(substr)
	
# Python actually has a method to solve this too!
def occurrences(string, substr):
  return string.count(substr)
```
	
</details>

<details>
  <summary><strong>Challenge 4</strong></summary>

  ```python
  def product(*args):
    product = 1
    for arg in args:
      product *= arg
    return product
  ```
</details>