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