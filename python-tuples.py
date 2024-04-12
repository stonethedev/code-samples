# Creating a Tuple:
my_tuple = (1, 2, 3, 4, 5)

# Accessing Elements:
print(my_tuple[0])  # Accessing the first element
print(my_tuple[-1])  # Accessing the last element

# Slicing Tuples:
print(my_tuple[1:4])  # Slicing from index 1 to index 3 (exclusive)

# Tuples are immutable, so there are no examples for modifying tuples

# Iterating Over a Tuple:
for item in my_tuple:
    print(item)

# Tuple Packing and Unpacking:
a, b, c, d, e = my_tuple
print(a, b, c, d, e)

# Tuple Comprehensions are not directly supported in Python, so there's no example for that

# Finding the Length of a Tuple:
tuple_length = len(my_tuple)

# Checking if an Element is in a Tuple:
if 5 in my_tuple:
    print("5 is in the tuple")

# Copying a Tuple (Tuples are immutable, so no need to copy)

# Converting Tuple to List (if modification is needed):
my_list = list(my_tuple)

# Clearing a Tuple (Tuples are immutable, so no way to clear)
