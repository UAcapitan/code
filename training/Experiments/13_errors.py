
errors = [
    SyntaxError, # When some syntax mistakes in code
    ZeroDivisionError, # When you try number divide by 0
    ImportError, # Module or some functional from module is not existed
    NameError, # Error if there is no variable with its name
    TypeError, # When user give variable with wrong type to function
    ValueError, # When user give variable with right type, but with wrong value to function
    IndexError, # If user try to take element with index which out from list
    KeyError, # If there is no needed key in dict
    MemoryError, # If memory is out
]

counter = 0

for error in errors:
    try:
        raise error
    except:
        counter += 1
        print(f"Errors: {str(counter)}")