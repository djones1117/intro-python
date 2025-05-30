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
