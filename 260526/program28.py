# Write a Python Program to Find Factorial of Number Using Recursion.
def factorial(n):
   varun= n * factorial(n - 1)
num = int(input("Enter a number to find its factorial: "))
print("Factorial of", num, "is", varun)
