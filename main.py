num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
choice = input("Pick an operation to be done on these numbers: A, addition, S, Subtraction, M, Multiplication, D, Division ").strip().upper()
def divide_numbers(num1, num2):
    return num1/num2
def multiply_numbers(num1, num2):
    return num1*num2
def subtract_numbers(num1, num2):
    return num1 - num2
def add_numbers(num1, num2):
    return num1 + num2
if choice == "A":
    print(add_numbers(num1, num2))
elif choice == "S":
    print(subtract_numbers(num1, num2))
elif choice == "M":
    print(multiply_numbers(num1, num2))
elif choice == "D":
    print(divide_numbers(num1, num2))
else:
    print("Invalid")

