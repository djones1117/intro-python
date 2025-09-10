my_list = [1, 2, 3, 4, 5]
new_list = [x * 2 for x in my_list if x % 2 == 0]
print(new_list)

##whats the output?



#solution
#iterates over my_list to check if the number is even 
#and multiplies that number x 2
#[4, 8]

number = 0

# Simulated do...while loop
while True:
    print("Number is:", number)
    number += 1
    if number >= 3:
        break


### add more looping problems



correct_password = "secret"
attempts = 0

while True:
    guess = input("Enter password: ")
    attempts += 1
    if guess == correct_password:
        print("Access granted.")
        break
    elif attempts >= 3:
        print("Too many attempts. Access denied.")
        break
    else:
        print("Incorrect. Try again.")



n = 10
total = 0

for i in range(1, n + 1):
    total += i

print("Sum from 1 to", n, "is:", total)



n = 10
total = 0

for i in range(1, n + 1):
    if i % 3 == 0:
        continue  # Skip numbers divisible by 3
    total += i

print("Sum of numbers from 1 to", n, "excluding multiples of 3 is:", total)



my_list = [5, 8, 13, 21, 34]

for num in my_list:
    if num > 20:
        print("First number greater than 20 is:", num)
        break

for i in range(1, 4):
    for j in range(1, 4):
        print(i, "x", j, "=", i * j)


count = 5
while count > 0:
    print("Countdown:", count)
    count -= 1
print("Lift off!")


squares = [x**2 for x in range(1, 6)]
print("Squares:", squares)


odd_squares = [x**2 for x in range(1, 6) if x % 2 == 1]
print(odd_squares)


for num in range(5, 0, -1):
    print(num)


product = 1
for num in range(1, 6):
    product *= num
print("Product from 1 to 5 is:", product)


numbers = [1, 2, 3, 4, 5, 6]
tripled_odds = [x * 3 for x in numbers if x % 2 == 1]
print(tripled_odds)

total = 0
for i in range(1, 21):
    if i % 2 == 0:
        total += i
print("Sum of even numbers from 1 to 20 is:", total)

# Counting down with a custom message
countdown = 5

while countdown > 0:
    print("Counting down:", countdown)
    countdown -= 1

print("Blast off!")


my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = []

for num in my_list:
    if num not in unique_list:
        unique_list.append(num)

print("List without duplicates:", unique_list)


number = int(input("Enter a number: "))
if number % 2 == 0:
    print(number, "is even.")
else:
    print(number, "is odd.")


number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

for i in range(1, 21):
    output = ""
    if i % 3 == 0:
        output += "Fizz"
    if i % 5 == 0:
        output += "Buzz"
    print(output or i)


# Check if a number is prime
n = 7
for i in range(2, n):
    if n % i == 0:
        print(n, "is not prime")
        break
else:
    print(n, "is prime")


for num in range(2, 21):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, "is a prime number")
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"Fruit #{index + 1} is {fruit}")


text = "hello"
reversed_text = ""

for char in text:
    reversed_text = char + reversed_text

print("Reversed string:", reversed_text)

student_scores = {
    "Alice": 85,
    "Bob": 72,
    "Charlie": 90,
    "Diana": 95,
    "Evan": 67
}

# Print students who scored 80 or above
for student, score in student_scores.items():
    if score >= 80:
        print(f"{student} passed with a score of {score}")

numbers = [2, 4, 6, 8, 9, 10]

for num in numbers:
    if num % 2 != 0:
        print("Found an odd number:", num)
        break
else:
    print("All numbers are even")


##looping with zip
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

for i in range(10, 0, -2):
    print("Step:", i)

##looping through a 2d list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for item in row:
        print(item, end=" ")
    print()


age = int(input("Enter your age: "))
if age >= 18:
    print("You're eligible to vote.")
else:
    print("You're too young to vote.")


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

result = a + b
print("The sum is:", result)


word = input("Enter a word: ")

if "a" in word:
    print("The word contains the letter 'a'.")
else:
    print("The word does not contain the letter 'a'.")


def greet(name):
    print(f"Hello, {name}!")

greet("Alice")


def power(base, exponent=2):
    return base ** exponent

print(power(3))      # 9
print(power(2, 3))   # 8


set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

common = set1 & set2
print("Common elements:", common)


person = ("Alice", 30, "Engineer")

##tuple unpacking
name, age, profession = person
print(f"{name} is a {age}-year-old {profession}.")

# Dictionary of subjects and their list of scores
subject_scores = {
    "Math": [90, 85, 78],
    "Science": [88, 92, 80],
    "English": [75, 80, 72]
}

# Calculate average score for each subject
for subject, scores in subject_scores.items():
    average = sum(scores) / len(scores)
    print(f"Average score for {subject} is: {average:.2f}")


# Let the user input their own details
name = input("Enter your name: ")
age = input("Enter your age: ")
profession = input("Enter your profession: ")

intro = f"{name} is a {age}-year-old {profession}."
print(intro)


text = "Artificial Intelligence"
vowels = "aeiouAEIOU"

for char in text:
    if char in vowels:
        print(char, end=" ")       

sentence = input("Enter a sentence: ")
vowels = "aeiouAEIOU"
count = 0

for char in sentence:
    if char in vowels:
        count += 1

print("Number of vowels in the sentence:", count)


number = int(input("Enter a number to compute its factorial: "))
factorial = 1

if number < 0:
    print("Factorial is not defined for negative numbers.")
elif number == 0 or number == 1:
    print("Factorial of", number, "is 1")
else:
    for i in range(1, number + 1):
        factorial *= i
    print("Factorial of", number, "is", factorial)


rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print()

word = input("Enter a word: ")
letter = input("Enter a letter to count: ")

count = 0
for char in word:
    if char == letter:
        count += 1

print(f"The letter '{letter}' appears {count} time(s) in '{word}'.")


number = None

while number != 0:
    number = int(input("Enter a number (0 to stop): "))
    print("You entered:", number)

print("Done!")

print("Even numbers from 1 to 20:")

for num in range(1, 21):
    if num % 2 == 0:
        print(num)
secret_number = 7
guess = None

while guess != secret_number:
    guess = int(input("Guess the number (between 1 and 10): "))
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("You guessed it!")
word = input("Enter a word: ")

for letter in word:
    print(letter)


original = [1, 2, 3, 4, 5]
reversed_list = []

for i in range(len(original) - 1, -1, -1):
    reversed_list.append(original[i])

print("Original list:", original)
print("Reversed list:", reversed_list)


for number in range(1, 11):
    if number % 2 != 0:
        print(number)
total = 0
for number in range(1, 6):
    total += number

print("Total sum is:", total)
numbers = [1, 2, 3, 4, 5]
total = 0

for num in numbers:
    total += num

print("Sum is:", total)

numbers = [1, 2, 3, 4, 5]
print("Sum is:", sum(numbers))


numbers = [9, 2, 7, 1, 5]
smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest number is:", smallest)

text = input("Enter a word or sentence: ")
vowels = "aeiouAEIOU"
result = ""

for char in text:
    if char in vowels:
        result += "*"
    else:
        result += char

print("Modified text:", result)
size = int(input("Enter the size of the square: "))

for i in range(size):
    for j in range(size):
        print("#", end="")
    print()
word = input("Enter a word: ")

for index in range(len(word)):
    print(f"Character '{word[index]}' is at index {index}")
sentence = input("Enter a sentence: ")
words = sentence.split()

for word in words:
    print(word.capitalize())
nums = [2, 4, 6, 8]
total = 0

for num in nums:
    total += num
    print(f"Added {num}, running total is {total}")

sentence = input("Enter a sentence: ")
words = sentence.split()

for word in words:
    print(word.capitalize())


text = input("Enter a sentence: ")
new_text = ""

for char in text:
    if char == " ":
        new_text += "_"
    else:
        new_text += char

print("Modified text:", new_text)


numbers = [5, 12, 3, 18, 7, 21]
filtered = []

for num in numbers:
    if num > 10:
        filtered.append(num)

print("Numbers greater than 10:", filtered)


sentence = input("Enter a sentence: ")
words = sentence.split()
capital_count = 0

for word in words:
    if word[0].isupper():
        capital_count += 1

print("Words starting with a capital letter:", capital_count)


word = input("Enter a word: ")
is_palindrome = True

for i in range(len(word) // 2):
    if word[i] != word[-(i + 1)]:
        is_palindrome = False
        break

if is_palindrome:
    print("It's a palindrome!")
else:
    print("Not a palindrome.")


word = input("Enter a word: ")
built = ""

for letter in word:
    built += letter
    print(built)


size = int(input("Enter the size: "))

for i in range(size):
    for j in range(size):
        if i == j:
            print("X", end="")
        else:
            print(" ", end="")
    print()

    text = input("Enter a word or sentence: ").lower()
vowels = "aeiou"
switches = 0

for i in range(1, len(text)):
    if text[i-1].isalpha() and text[i].isalpha():
        prev = text[i-1] in vowels
        curr = text[i] in vowels
        if prev != curr:
            switches += 1

print("Number of vowel/consonant switches:", switches)

text = input("Enter a word or sentence: ").lower()
vowels = "aeiou"
switches = 0

for i in range(1, len(text)):
    if text[i-1].isalpha() and text[i].isalpha():
        prev = text[i-1] in vowels
        curr = text[i] in vowels
        if prev != curr:
            switches += 1

print("Number of vowel/consonant switches:", switches)