def add_numbers(num1, num2):
  """Adds two numbers and returns the result."""
  return num1 + num2


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


sum = add_numbers(num1, num2)
print("The sum of", num1, "and", num2, "is":, sum)