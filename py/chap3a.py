name = input("Enter your name: ")
height = float(input("Enter your height: "))

# input validation
while True:
    try:
        age = int(input("Enter your age: "))
        if age > 0:
            break
        else:
            print("Age must be a positive integer. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

#output validation
print(f"Hello, {name}!")
print(f"You are {age} years old and {height} units tall.")

# Exercise 3b
while True:
    try:
        num1 = int(input("Enter 1st number "))
        num2 = int(input("Enter 2nd number "))
        if num1 > 0 and num2 > 0:
            ans1 = num1 + num2
            break
        else:
            print("Input must be a positive integer. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid integer for age.")

print(f"The sum of {num1} and {num2} is {ans1}")