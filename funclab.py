def sum_to(num):
  sum = 0
  for n in range(1, num + 1):
    sum += n
  return sum

print(sum_to(6))




def largest_loop(nums):
    largest = 0
    for num in nums:
        if num > largest:
            largest = num
    return largest

def largest_sort(nums):
    nums.sort()
    return nums[-1]

numbers = [4, 9, 2, 7, 1, 10, 5]

result_loop = largest_loop(numbers)
result_sort = largest_sort(numbers)

print(f"Largest number (using loop): {result_loop}")
print(f"Largest number (using sort): {result_sort}")



