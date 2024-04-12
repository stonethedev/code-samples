# Example 1:
with open("example.txt", "r") as file:
    data = file.read()
    print(data)

# Example 2:
file_path = "example.txt"
try:
    with open(file_path, "r") as file:
        for line in file:
            print(line.strip())  # Strip newline characters
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except IOError as e:
    print(f"Error reading file '{file_path}': {e}")

# Example 3:
file_path = "example.txt"
try:
    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())  # Strip newline characters
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except IOError as e:
    print(f"Error reading file '{file_path}': {e}")
