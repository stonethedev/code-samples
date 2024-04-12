# Example 1:
def greet(name):
    print("Hello, " + name + "!")
    
greet("Alice")

# Example 2:
def add_numbers(a, b):
    return a + b

result = add_numbers(3, 5)
print("The sum is:", result)

# Example 3:
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial of 5 is:", factorial(5))

# Example 4:
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

print("Is 17 a prime number?", is_prime(17))
