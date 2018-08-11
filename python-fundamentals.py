#!/usr/bin/env python3

# Welcome to Python for Machine Learning!
# Let's begin reviewing some features of python Below
# The instructions on the right contain additional information that may
# be helpful for completing the challenges

# We'll use this function to test our code
def test(challenge, val):
  assert val , "Challenge {i} failing".format(i=challenge)
  print("Challenge {i} passing".format(i=challenge))

# *************************************
# *************************************

# 1. Comments
# Comments in Python begin with a hash
# Comments allow us to explain our code
# The python interpreter ignores these lines

# *************************************
# *************************************

# 2. Variables
# An example of creating a variable:
my_number = 10

# Use the print function to display variables on the console below
print('my_number is: ', my_number)

# 2.1 Create a variable, another_number, that stores the value 11

another_number = 11
# Uncomment below to test 2.1
test('2.1', another_number == 11)

# 2.2 Use the print function to display the value of another_number below
# There's no test for 2.2


# 2.3 Reassign the variable another_number to the value 11.5

another_number = 11.5

# Uncomment below to test 2.3
test('2.3', another_number == 11.5)

# *************************************
# *************************************

# 3. Practice with strings and lists

# 3.1 Create a variable below, my_name, that holds
#     a string of either you or your partner's name (e.g. "Emily").

my_name = 'Mikka'
# Uncomment below to test 3.1
test('3.1', type(my_name) == str)


# 3.2 Create a variable below, our_names, that stores
#     an array with you and your coding parter's name
our_names = ['Mikka', 'ChubChub']
# Uncomment below to test 3.2
test('3.2', type(our_names) == list and type(our_names[0]) == str and type(our_names[1]) == str)


# 3.3 Create a variable, am_in_group, that stores a
#     boolean indicating if the string my_name is in
#     the list our_names (hint: use the keyword "in")

am_in_group = my_name in our_names
# Uncomment below to test 3.3
test('3.3', type(am_in_group) == bool)


# 3.4 Use the list method 'append' to add another name to our_names
# No test for 3.4 - use 'print' to figure out if it's working as expected

our_names.append('Foo')
print(our_names)
# 3.5 Use the list method 'pop' to remove the last name from the end of the list. Store the name you popped off in the variable "removed_from_group"
# No test for 3.5 - use 'print' to figure out if it's working as expected
removed_from_group = our_names.pop()
print(removed_from_group)
print(our_names)

# *************************************
# *************************************

# 4. Iteration
# 4.1 Create a variable my_list that holds the values 1, 18, -3, and 0
my_list = [1, 18, -3, 0]
# Uncomment to test Challenge 4.1
test('4.1', my_list == [1, 18, -3, 0])


# 4.2 Create a variable new_list and initialize it to an empty list

new_list = []
# Uncomment to test Challenge 4.2
test('4.2', new_list == [])

# 4.3 Create a variable named count and initialize it to zero.
count = 0
# Uncomment to test Challenge 4.3
test('4.3', count == 0)


# 4.4 Loop through the variable my_list. During each iteration:
#     1. print the value of count,
#     2. increment the value of count, and
#     3. append the current value of my_list to new_list
# After running the code, new_list should hold the same values as my_list
for element in my_list:
  print(count)
  count += 1
  new_list.append(my_list[count-1])
# Uncomment to test Challenge 4.4
test('4.4', my_list == new_list)


# 4.5 Repeat 4.4, but instead of using the variable count,
# use the built in python function enumerate
# No test for 4.4 - use 'print' to see if you are achieving the disired functionality
for (counter, value) in enumerate(my_list):
  print(counter, value)

# *************************************
# *************************************

# 5. Functions

# 5.1 Complete the function, times_two_v1, below.
# See the instructions to the right for details.

def times_two_v1(num_list):
  results = []
  for (counter, value) in enumerate(num_list):
    results.append(value * 2)
  return results

# We will test the functions in section 5 a little differently
# Uncomment the line beginning with 'assert' to test times_two_v1
# If nothing happens, the test is passing.
# If an error is thrown, the test isn't passing.
assert times_two_v1([10,-5, 0, 1]) == [20, -10, 0, 2]


# # 5.2 Complete the function zip_up.
# # See the instructions to the right for details.

# def zip_up(l_1, l_2):

#   combined = []
#   offset = 0
#   for counter, value in enumerate(l_1):
#     combined.append(value)
#   for counter, value in enumerate(l_2):
#     combined.insert(counter+1+offset, value)
#     offset += 1
#   return combined

# # Uncomment below to test your code
# assert zip_up([1,2,3], [4,5,6]) == [1,4,2,5,3,6]
# assert zip_up([1,2], [8,7,6,5]) == [1,8,2,7,6,5]

# 5.3 Complete the function unzip.
# See the instructions to the right for details.

def unzip(l):
  evens = l[0:len(l):2]
  odds = l[1:len(l):2]
  tuple = ()
  tuple = (evens, odds)
  print(tuple)
  return tuple

# Uncomment following lines to test your code
# assert unzip([1,2,3,4,5,6]) == ([1,3,5], [2,4,6])
# assert unzip([7,6,5,4,3,2,1]) == ([7,5,3,1], [6,4,2])

# 5.4 Complete the function mean.
# See the instructions to the right for details.

# def mean(l):
#   mean = sum(l)/len(l)
#   print(mean)
#   return sum(l)/len(l)

# # Uncomment below to test mean
# assert mean([5,5,5,5,5]) == 5
# assert mean([5,20,8,-1,0,0,2,16]) == 6.25

# 5.5 Complete the function std_dev.
# See the instructions to the right for details.
import statistics

def std_dev(l):
  stdev = statistics.stdev(l)
  print(stdev)
  return stdev


# Uncomment below to test std_dev
# assert std_dev([5,5,5,5,5]) == 0
# assert std_dev([5,20,8,-1,0,0,2,16]) == 7.905694150420948

# 5.6 Complete the function mode.
# See the instructions to the right for details.

import statistics
def modeOf(l):
  result = [statistics.mode(l)]

  print(result)
  return result

# Uncomment below to test mode
assert modeOf([5,5,5,5,5]) == [5]
assert modeOf([5,20,8,-1,0,0,2,16]) == [0]
assert modeOf([2,2,1,1,3]) == [1,2]

# *************************************
# *************************************

# Congrats on completing Python for Machine Learning part 1!
