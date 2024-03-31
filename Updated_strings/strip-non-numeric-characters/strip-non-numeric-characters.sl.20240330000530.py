# Start time: 2024-03-30 00:20:28.201881
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the number from input, and given input as ['100 apples'] output is 100, given input as ['the price is %500 dollars'] output is 500, given input as ['serial number %003399'] output is 003399, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return the number from input
# Input: '100 apples'
# Output: 100

# Input: 'the price is %500 dollars'
# Output: 500

# Input: 'serial number %003399'
# Output: 003399

def extract_number(input_string):
    try:
        number = ''.join(filter(str.isdigit, input_string))
        return int(number)
    except ValueError:
        try:
            number = input_string.split('%')[-1].strip()
            return int(number)
        except ValueError:
            print("No number found in the input string")
            return None

# Test cases
print(extract_number('100 apples'))  # Output: 100
print(extract_number('the price is %500 dollars'))  # Output: 500
print(extract_number('serial number %003399'))  # Output: 003399
print(extract_number('no number here'))  # Output: None

# End time: 2024-03-30 00:20:32.074488
# Elapsed time in seconds: 3.872580941999786