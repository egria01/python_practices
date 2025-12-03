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
        print("Invalid input. Please enter a valid integer for age.")

#output validation
print(f"Hello, {name}!")
print(f"You are {age} years old and {height} units tall.")