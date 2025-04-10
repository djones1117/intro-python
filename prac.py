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