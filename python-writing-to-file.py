# Example 1:
with open("output.txt", "w") as file:
    file.write("Hello, world!")

# Example 2:
file_path = "output.txt"
try:
    with open(file_path, "w") as file:
        file.write("This is line 1\n")
        file.write("This is line 2\n")
        file.write("This is line 3\n")
except IOError as e:
    print(f"Error writing to file '{file_path}': {e}")

# Example 3:
file_path = "output.txt"
lines_to_write = ["Line 1\n", "Line 2\n", "Line 3\n"]
try:
    with open(file_path, "w") as file:
        file.writelines(lines_to_write)
except IOError as e:
    print(f"Error writing to file '{file_path}': {e}")
