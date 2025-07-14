# 10. Create a tuple and list of numbers and print out the sum of all the numbers in the tuple and list form.

numbers_list = [1, 2, 3, 4, 5]
numbers_tuple = (1, 2, 3, 4, 5)
total_sum_list= [sum(numbers_list)]
total_sum_tuple = [sum(numbers_tuple)]
print("Sum of numbers in the list:", total_sum_list)
print("Sum of numbers in the tuple:", tuple(total_sum_tuple))


