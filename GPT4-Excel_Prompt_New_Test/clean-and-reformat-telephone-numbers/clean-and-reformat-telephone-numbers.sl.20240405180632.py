# Start time: 2024-04-05 18:10:56.020259

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: delete all "-", "<", ">", ".", and any spaces, and input as ['801-456-8765'] output is 8014568765, input as ['<978> 654-0299'] output is 9786540299, input as ['978.654.0299'] output is 9786540299, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(phone_number):
    # Define the characters to be removed
    chars_to_remove = "-<>. "
    # Use a generator expression to filter out unwanted characters
    cleaned_number = ''.join(char for char in phone_number if char not in chars_to_remove)
    return cleaned_number

# Test cases
print(generated_function('801-456-8765'))  # Expected output: 8014568765
print(generated_function('<978> 654-0299'))  # Expected output: 9786540299
print(generated_function('978.654.0299'))  # Expected output: 9786540299
print(generated_function("801-456-8765"))  ## Output: 8014568765
print(generated_function("<978> 654-0299"))  ## Output: 9786540299
print(generated_function("978.654.0299"))  ## Output: 9786540299

# End time: 2024-04-05 18:11:00.448563
# Elapsed time in seconds: 4.427722884000104


# APPEND TEST SCRIPTS...
print(generated_function("801-456-8765"))  ## Output: 8014568765
print(generated_function("<978> 654-0299"))  ## Output: 9786540299
print(generated_function("978.654.0299"))  ## Output: 9786540299


print(generated_function("801.456-8765"))  ### Output: 8014568765
print(generated_function("(978) 654-0299"))  ### Output: 9786540299
print(generated_function("978 654 0299"))  ### Output: 9786540299

# TEST SCRIPTS APPENDED!

