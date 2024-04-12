# Example 1: List Comprehension
squared_numbers = [x ** 2 for x in range(5)]
print(squared_numbers)

# Example 2: List Comprehension with Conditional
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)

# Example 3: Set Comprehension
squared_set = {x ** 2 for x in range(5)}
print(squared_set)

# Example 4: Dictionary Comprehension
squared_dict = {x: x ** 2 for x in range(5)}
print(squared_dict)

# Example 5: Tuple Comprehension (Generator Expression)
squared_tuple = tuple(x ** 2 for x in range(5))
print(squared_tuple)

# Example 6: Nested List Comprehension
matrix = [[j for j in range(3)] for i in range(3)]
print(matrix)
