# Start time: 2024-04-05 17:55:57.839009

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the number of non-zero consecutive numbers, and input as ['7 0 0 5 4 4'] output is 3, input as ['0 0 2 3 3 0'] output is 3, input as ['5 6 4 6 0 7'] output is 4, input as ['0 4 5 0 0 2'] output is 2, input as ['3 0 3 0 1 2'] output is 2, input as ['5 3 2 5 6 1'] output is 6, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(input_string):
    # Split the input string into a list of numbers (as strings)
    numbers_as_strings = input_string.split()
    # Convert the list of strings to a list of integers
    numbers = [int(num) for num in numbers_as_strings]
    
    # Initialize variables to track the maximum length of consecutive non-zero numbers and the current length
    max_length = 0
    current_length = 0
    
    # Iterate through the list of numbers
    for num in numbers:
        # If the current number is not zero, increment the current length
        if num != 0:
            current_length += 1
            # Update the maximum length if the current length is greater
            if current_length > max_length:
                max_length = current_length
        else:
            # Reset the current length to zero if a zero is encountered
            current_length = 0
    
    # Return the maximum length of consecutive non-zero numbers
    return str(max_length)

# Test cases
print(generated_function('7 0 0 5 4 4'))  # Expected output: 3
print(generated_function('0 0 2 3 3 0'))  # Expected output: 3
print(generated_function('5 6 4 6 0 7'))  # Expected output: 4
print(generated_function('0 4 5 0 0 2'))  # Expected output: 2
print(generated_function('3 0 3 0 1 2'))  # Expected output: 2
print(generated_function('5 3 2 5 6 1'))  # Expected output: 6
print(generated_function("7 0 0 5 4 4"))  ## Output: 3
print(generated_function("0 0 2 3 3 0"))  ## Output: 3
print(generated_function("5 6 4 6 0 7"))  ## Output: 4
print(generated_function("0 4 5 0 0 2"))  ## Output: 2
print(generated_function("3 0 3 0 1 2"))  ## Output: 2
print(generated_function("5 3 2 5 6 1"))  ## Output: 6

# End time: 2024-04-05 17:56:07.625510
# Elapsed time in seconds: 9.785124087999975


# APPEND TEST SCRIPTS...
print(generated_function("7 0 0 5 4 4"))  ## Output: 3
print(generated_function("0 0 2 3 3 0"))  ## Output: 3
print(generated_function("5 6 4 6 0 7"))  ## Output: 4
print(generated_function("0 4 5 0 0 2"))  ## Output: 2
print(generated_function("3 0 3 0 1 2"))  ## Output: 2
print(generated_function("5 3 2 5 6 1"))  ## Output: 6


print(generated_function("8 7 1 6 0 3"))  ### Output: 4
print(generated_function("8 7 1 6 4 0"))  ### Output: 5
print(generated_function("9 0 1 0 1 3"))  ### Output: 2
print(generated_function("0 7 0 6 0 0"))  ### Output: 1
print(generated_function("9 0 1 5 4 4"))  ### Output: 4

# TEST SCRIPTS APPENDED!

