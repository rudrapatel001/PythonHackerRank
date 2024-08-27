# Loops are control structures that iterate over a range to perform a certain task. They can work with any iterable type, such as lists and dictionaries. To control the loop in this problem, use the range function (see below for a description).

# There are two kinds of loops in Python.

# A for loop:

# for i in range(0, 5):
#     print i
# And a while loop:

# i = 0
# while i < 5:
#     print i
#     i += 1
# When using a for loop, the next value from the iterator is automatically taken at the start of each loop. When using a while loop, the iterator must be initialized prior to the loop, and the value updated within the loop.

# Note Be careful about indentation in Python. Read more

# The range() function

# The range function is a built in function that returns a series of numbers. At a minimum, it needs one integer parameter.

# Given one parameter, , it returns integer values from  to . For example, range(5) returns the numbers  through  in sequence.
# To start at a value other than , call range with two arguments. For example, range(1,5) returns the numbers  through .
# Finally, you can add an increment value as the third argument. For example, range(5, -1, -1) produces the descending sequence from  through  and range(0, 5, 2) produces , , . If you are going to provide a step value, you must also include a start value.

if __name__ == '__main__':
    n = int(input())

for i in range(n):
    print(i*i)
