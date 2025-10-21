def convert_string_to_integer(parameter):
    # Handle empty string
    if not parameter:
        return 0

    # Check for invalid input using allowed characters
    if not parameter.lstrip('-').isdigit() or parameter.count('-') > 1 or parameter.find('-') > 0:
        raise ValueError("Invalid input: String contains invalid characters or format.")

    # Helper recursive function to process the string
    def recursive_convert(param, result=0):
        # Base case: if the string is empty, return the accumulated result
        if not param:
            return result

        # Take the first character, convert it to a digit, and add it to the result
        digit = ord(param[0]) - ord('0')  # Convert character to integer
        result = result * 10 + digit

        # Recur for the rest of the string
        return recursive_convert(param[1:], result) # Recursive calls 

    # Handle negative numbers
    is_negative = parameter[0] == '-'
    num = recursive_convert(parameter[1:] if is_negative else parameter)

    return -num if is_negative else num


# Test cases
try:
    print(convert_string_to_integer("123"))
    print(convert_string_to_integer("-456"))
    print(convert_string_to_integer("0"))
    print(convert_string_to_integer(""))

    # Raise an exception
    print(convert_string_to_integer("12a3"))  
except ValueError as e:
    print(e)

print()
input("Press Enter to terminate the program.")
