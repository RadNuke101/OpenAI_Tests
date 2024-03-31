# Start time: 2024-03-30 18:59:05.910763

# Content: Given that given input as ['  The shawshank'] output is The shawshank, given input as ['The    godfather'] output is The godfather, given input as ['    pulp   fiction'] output is pulp fiction, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test cases:
# input: '  The shawshank', output: 'The shawshank'
# input: 'The    godfather', output: 'The godfather'
# input: '    pulp   fiction', output: 'pulp fiction'

def clean_string(input_str):
    try:
        # Remove leading and trailing whitespaces
        clean_str = input_str.strip()
        
        # Replace multiple whitespaces with a single whitespace
        clean_str = ' '.join(clean_str.split())
        
        return clean_str
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Test the function with the provided test cases
print(clean_string('  The shawshank'))  # Output: The shawshank
print(clean_string('The    godfather'))  # Output: The godfather
print(clean_string('    pulp   fiction'))  # Output: pulp fiction

# End time: 2024-03-30 18:59:09.844797
# Elapsed time in seconds: 3.9339426750000257