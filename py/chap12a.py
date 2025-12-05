
try:
    number = int(input("Enter an integer: "))
    result = 10/number
    print(f"Result is {result}")
except ValueError:
    print("Invalid input! Please enter a valid integer.")
except ZeroDivisionError:
    print("Error! Division by zero is not allowed.")


try:
    file = open("data.txt","r")
except FileNotFoundError:
    print("Error! The file 'data.txt' was not found.")  
else:
    content = file.read()
    print(content)
    print("File read successfully.")
finally:
    if 'file' in locals() and not file.closed:
        file.close()
    print("clean up completed.")

    def validate_age(age):
        if age < 0:
            raise ValueError("Age cannot be negative.")
        if age > 150:
            raise ValueError("Age seems unrealistic.")
        return True
    
    try:
        validate_age(-5)
    except ValueError as e:
        print(f"Validation Error: {e}")