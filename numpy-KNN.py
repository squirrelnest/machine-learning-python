#!/usr/bin/env python3

#************************************************#
# 1. Numpy Basics
#************************************************#

# The following line imports the numpy library
import numpy as np

# A. Use np.array to turn a_python_list into a numpy array
#    Store the result in the variable a_numpy_array
a_python_list = [[1,2,3], [4,5,6]]

a_numpy_array = np.array(a_python_list)

# Uncomment the "assert" statements below to test your code.
# If an error is thrown, your code is wrong. If nothing happens, the test is passing.
assert type(a_numpy_array) is np.ndarray
assert np.array_equal(a_numpy_array, a_python_list)


# B. Create a numpy array with shape (2,4,3).
#    Store the result in the variable array_243

a=1
b=2
c=3

array_243 = np.array(
                  [
                    [
                      [a,b,c],
                      [a,b,c],
                      [a,b,c],
                      [a,b,c],
                    ],
                    [
                      [a,b,c],
                      [a,b,c],
                      [a,b,c],
                      [a,b,c],
                    ]
                  ])

# Uncomment the "assert" statement below to test your code.
assert array_243.shape == (2,4,3)
# print(array_243.shape)

# C. Use array slicing to create a copy of the first two rows
# and the first two columns of `indexing_ex`. Store the result
# in the variable `subset_22`
indexing_ex = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

subset_22 = indexing_ex[0:2,0:2]

assert np.array_equal(subset_22, [[1,2],[4,5]])

# D. Use `np.zeros` to create an array of zeros with shape `(2,2)`
# Store the result in the variable arr_22

s=(2,2)
arr_22 = np.zeros(s)

# print(arr_22.shape)

# E. use np.random.uniform to create a numpy array with shape
# (5000,) filled with random values between -1 and 1
# Store the result to a variable, uniformly_random

random_shape = np.random.uniform(1,10,5000)
uniformly_random = np.array(random_shape)

# print(uniformly_random.shape)

# F. Use np.random.normal to create a numpy array with shape
# (5000,) filled with normally distributed random values with
# mean 0 and standard deviation 1. Save the result to a
# variable, normal_random. (for more info on normal distributions,
# see https://en.wikipedia.org/wiki/Normal_distribution)

normal_shape = np.random.normal(0,1,5000)
normal_random = np.array(normal_shape)

stdev = np.std(normal_random)

# print(normal_random.shape)
# print(stdev)

#************************************************#
# 2. Distance between points
#************************************************#

# The distance function accepts two parameters:
#     point_a: a numpy array with shape (2,)
#     point_b: a numpy array with shape (2,)
# We will think about point_a and point_b as if they are points in an (x,y) coordinate plane.
# The distance function will return a non-negative number that represents the distance between
# point_a and point_b.

def distance(point_a, point_b):
  # A. Use subtraction to find the "difference" between point_a and point_b.
  #    Save the result to the variable "diff"
  diff = np.subtract(point_a, point_b)

  # B. We need to measure the length of the vector "diff"
  #    Start by squaring each coordinate in diff. Save the result to "diff_squared"
  diff_squared = np.square(diff)


  # C. Now that we've squared each of the coordinates in diff, we have to add them up.
  #    Use np.sum to compute the sum of all of the coordinates in "diff_squared".
  #    Save the result to "squared_coord_sum"
  squared_coord_sum = np.sum(diff_squared)
  # D. Last, we need to compute the square root of "squared_coord_sum".
  #    Hint: look into np.sqrt
  #    save the result to the variable "dist"
  dist = np.sqrt(squared_coord_sum)
  # E. Now return the distance between point_a and point_b that we just calculated
  return dist
  # pass

# print(distance(np.array([0,0]), np.array([3,4])))
# uncomment the following assert statements to test your code
assert distance(np.array([0,0]), np.array([3,4])) == 5
assert distance(np.array([-3, -1]), np.array([-8, 11])) == 13

# Note: if you wrote your function using numpy operations and
# methods instead of for loops, you function should work for
# numpy vectors with shape (n,) for any number n!
# uncomment below to test:
# assert distance(np.array([0,0,0]), np.array([2,3,6])) == 7
# assert distance(np.array([6, -2, 3]), np.array([2, 2, 10])) == 9

#************************************************#
# 3. get_distances
#************************************************#

# get_distances will be similar to the distance function we created earlier.
# get_distances accepts two parameters:
#     points: a numpy array with shape (n, 2). You can think of points as a
#             list of points with shape (2,)
#     base_point: a numpy array with shape (2,).
# The goal of get_distances is to return a numpy array where each element
# the distance between one of the points in "points" and "base_point".
# Consider the example below:

ex_points = np.array([
  [3,4],
  [5,12],
  [9, 40]
])

ex_base_point = np.array([0,0])

# get_distances(ex_points, ex_base_point) should be equal to np.array([5, 13, 41])
# since the distance between [3,4] and [0,0] is 5; the distance between
# [5, 12] and [0,0] is 13; and the distance between [9, 40] and [0,0] is 41.

def get_distances(points, base_point):
  # A. Use subtraction to create an array of shape (n, 2) that holds a list of
  #    differences between the points in "points" and "base_point". Save the
  #    result to diffs.
  diffs = np.subtract(points, base_point)
  # print(diffs)
  # B. Square all the coordinates in diffs. Save the result to diffs_coords_squared.
  diffs_coords_squared = np.square(diffs)
  # print(diffs_coords_squared)
  # C. Use np.sum to sum all of the numbers IN EACH ROW of diffs_coords_squared.
  #    This should result in an array with shape (n,). If you aren't careful, you may
  #    end up summing every number in the whole array. Save the result to "sums"
  #    Hint: look up the numpy docs for np.sum. what does the keyword argument "axis" do?
  sums = np.sum(diffs_coords_squared, axis=1)
  # print(sums)
  # D. Use np.sqrt to find the square root of each number in sums. Save the result to "dists"
  dists = np.sqrt(sums)
  # E. Now return dists!
  return dists

# Test your code using the example provided before the function definition

# print(get_distances(ex_points, ex_base_point))

#************************************************#
# Extension: knn_predict
#************************************************#

# knn_predict will accept three parameters:
#     animal_data: a numpy array with shape (n, 2) that represents a dataset of animals.
#         Each row is a different animal. The first column is the animals domestication level
#         and the second column is the animal's size.
#     animal_types: a numpy array with shape (n,) that represents the type of animal each animal
#         in animal_data is. (E.g. if the first row in animal_data is a cat, then the first entry in
#         animal_types will be 'cat')
#     unknown_animal: a numpy array with shape (2,). The first number is its domestication level.
#         The second number is its size.
# The goal of knn_predict is to predict whether unknown animal is a cat or a dog. knn_predict
# should output either 'cat' or 'dog'.

def knn_predict(animal_data, animal_types, unknown_animal):
  # A. Use get_distances to find the distance between the unkown_animal and all of the
  #    animals in animal_data.
  distances_from_unknown = get_distances(unknown_animal, animal_data)

  # B. Find which type of animal the three closest animals in animal_data are.
  K = 3
  closest_indices = np.argpartition(distances_from_unknown,-K)[-K:]
  closest = np.array(animal_types[closest_indices])

  # C. Return 'cat' if at least two are cats. Return 'dog' if at least two are dogs.

  num_cats = (closest == 'cat').sum()
  num_dogs = (closest == 'dog').sum()

  if num_cats >= 2:
    print('cat')
    return 'cat'
  elif num_dogs >= 2:
    print('dog')
    return 'dog'


animal_data = np.array([
  [3,4],
  [5,12],
  [9, 40],
  [18, 3],
  [7, 23],
  [5, 6]
])

animals = ['cat', 'cat', 'cat', 'dog', 'dog', 'dog']

animal_types = np.array(animals, dtype=object)

unknown_animal = np.array([6, 14])

knn_predict(animal_data, animal_types, unknown_animal)
