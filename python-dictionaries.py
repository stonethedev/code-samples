# Creating a Dictionary:
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Accessing Values:
print(my_dict['name'])  # Accessing value by key

# Adding or Updating Key-Value Pairs:
my_dict['occupation'] = 'Engineer'  # Adding a new key-value pair
my_dict['age'] = 32  # Updating the value for an existing key

# Removing Key-Value Pairs:
del my_dict['city']  # Removing a key-value pair by key
popped_value = my_dict.pop('age')  # Removing and returning the value for a key

# Iterating Over a Dictionary:
for key, value in my_dict.items():
    print(key, value)

# Checking if a Key Exists:
if 'name' in my_dict:
    print("Name exists in the dictionary")

# Getting Keys or Values:
keys = my_dict.keys()  # Returns a view of all keys
values = my_dict.values()  # Returns a view of all values

# Copying a Dictionary:
copied_dict = my_dict.copy()  # Shallow copy

# Clearing a Dictionary:
my_dict.clear()  # Removes all items from the dictionary

# Dictionary Comprehensions:
squared_values = {x: x**2 for x in range(5)}  # Creating a new dictionary with squared values

# Merging Dictionaries (Python 3.9 and later):
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = {**dict1, **dict2}

# Accessing Values with .get():
age = my_dict.get('age')  # Retrieves the value for 'age', returns None if key doesn't exist

# Setting Default Values with .setdefault():
my_dict.setdefault('gender', 'Male')  # Sets the default value for 'gender' if key doesn't exist
