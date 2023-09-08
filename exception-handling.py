#Exception Handling
#first try code will run
try:
    # Code that may raise an exception
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2

#if try code doesnot run it will check exception
except ZeroDivisionError as excep:
    # Handle the specific exception (division by zero)
    print(excep)

except ValueError:
    # Handle the specific exception (invalid input)
    print("Invalid input. Please enter a valid number.")

else:
    # Code to run if no exception occurred
    print(result)

finally:
    # Code that always runs, typically for cleanup
    print("Execution completed.")

########################################
#Customized Exception
try:
    value =int(input("Enter Number: "))
    if value < 0:
        raise Exception("Value must be non-negative")
except Exception as ve:
    print("Custom Exception Caught:" ,ve)
