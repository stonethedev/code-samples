# Example 1:
import math

print(math.sqrt(16))

# Example 2:
import random

random_number = random.randint(1, 10)
print("Random number between 1 and 10:", random_number)

# Example 3:
from datetime import datetime

current_time = datetime.now()
print("Current date and time:", current_time)

# Example 4:
import os.path

file_path = "example.txt"
if os.path.exists(file_path):
    print(f"File '{file_path}' exists.")
else:
    print(f"File '{file_path}' does not exist.")
