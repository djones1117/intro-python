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
