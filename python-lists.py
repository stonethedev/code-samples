# Creating a List:
my_list = [1, 2, 3, 4, 5]

# Accessing Elements:
print(my_list[0])  # Accessing the first element
print(my_list[-1])  # Accessing the last element

# Slicing Lists:
print(my_list[1:4])  # Slicing from index 1 to index 3 (exclusive)

# Modifying Lists:
my_list.append(6)  # Adding an element to the end
my_list.insert(2, 10)  # Inserting element 10 at index 2
my_list.extend([7, 8, 9])  # Extending the list with another list

# Removing Elements:
my_list.remove(3)  # Removing specific element
popped_element = my_list.pop()  # Removing and returning the last element

# Iterating Over a List:
for item in my_list:
    print(item)

# List Comprehensions:
squares = [x**2 for x in my_list]  # Creating a new list with squares of elements

# Sorting a List:
my_list.sort()  # Sorts the list in ascending order
sorted_list = sorted(my_list)  # Returns a new sorted list

# Reversing a List:
my_list.reverse()  # Reverses the list in place
reversed_list = my_list[::-1]  # Creates a reversed copy of the list

# Finding the Length of a List:
list_length = len(my_list)

# Checking if an Element is in a List:
if 5 in my_list:
    print("5 is in the list")

# Copying a List:
copied_list = my_list.copy()  # Shallow copy

# Clearing a List:
my_list.clear()  # Removes all elements from the list
