# Example 1:
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Division by zero!")

# Example 2:
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("Please enter a valid integer.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
except Exception as e:
    print("An error occurred:", e)

# Example 3:
try:
    file = open("nonexistent_file.txt", "r")
    data = file.read()
    file.close()
except FileNotFoundError:
    print("File not found!")
except IOError as e:
    print("Error reading file:", e)
finally:
    print("Cleanup code here, like closing files or database connections.")
