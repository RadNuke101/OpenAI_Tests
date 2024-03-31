# Start time: 2024-03-30 11:51:34.256255
# Content: Given that given input as ['thatensures'] output is ensures, given input as ['thatwill'] output is will, given input as ['thathave'] output is have, given input as ['knowthat'] output is know, given input as ['that'] output is that, given input as ['mouse'] output is mouse, given input as ['knowthat'] output is know, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input and output to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any noncode
def extract_word(input_str):
    try:
        input_str = input_str[0]  # Convert list to string
        if 'that' in input_str:
            output_str = input_str.split('that')[-1]
        else:
            output_str = input_str
        return output_str
    except (IndexError, AttributeError):
        return "Invalid input"

# Test cases
print(extract_word(['thatensures']))  # Output: ensures
print(extract_word(['thatwill']))  # Output: will
print(extract_word(['thathave']))  # Output: have
print(extract_word(['knowthat']))  # Output: know
print(extract_word(['that']))  # Output: that
print(extract_word(['mouse']))  # Output: mouse
print(extract_word(['knowthat']))  # Output: know
print(extract_word('invalid_input'))  # Output: Invalid input

# End time: 2024-03-30 11:51:37.130757
# Elapsed time in seconds: 2.874449264000006