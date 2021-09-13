# Write a function called `choose_func` which takes a list of nums and 2 callback functions.
# If all nums inside the list are positive, execute the first function on that list and return the result of it.
# Otherwise, return the result of the second one
def choose_func(nums:list):

   positive = [num for num in nums if num > 0]
   if nums == positive:
    return square_nums(nums)
   else:
    return remove_negatives(nums)

def square_nums(nums):
    return [num ** 2 for num in nums]
def remove_negatives(nums):
    return [num for num in nums if num > 0]

print(choose_func([1, 2, 3, 4, 5]))
print(choose_func([1, -2, 3, -4, 5]))
choose_func([1, 2, 3, 4, 5])
choose_func([1, -2, 3, -4, 5])

