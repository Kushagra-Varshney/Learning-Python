try:
    # Code that may raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Exception handling for ZeroDivisionError
    print("Cannot divide by zero!")
except ValueError as e:
    # Exception handling for ValueError
    print("Invalid value:", str(e))
except Exception as e:
    # Exception handling for all other exceptions
    print("An error occurred:", str(e))
else:
    # Code to be executed if no exception is raised
    print("Division successful!")
finally:
    # Code that will always be executed, regardless of exceptions
    print("End of exception handling")