# Start time: 2024-03-30 01:44:45.872239
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the text before the last 3 numbers in inputted expression, and given input as ['Ducati100'] output is Ducati, given input as ['Honda125'] output is Honda, given input as ['Ducati250'] output is Ducati, given input as ['Honda250'] output is Honda, given input as ['Honda550'] output is Honda, given input as ['Ducati125'] output is Ducati, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return the text before the last 3 numbers in inputted expression
# Input: 'Ducati100', Output: 'Ducati'
# Input: 'Honda125', Output: 'Honda'
# Input: 'Ducati250', Output: 'Ducati'
# Input: 'Honda250', Output: 'Honda'
# Input: 'Honda550', Output: 'Honda'
# Input: 'Ducati125', Output: 'Ducati'

def extract_text(input_str):
    try:
        # Check if the input is a string
        if not isinstance(input_str, str):
            raise ValueError("Input must be a string")

        # Find the index of the last occurrence of a digit in the input string
        last_digit_index = len(input_str) - 1
        while last_digit_index >= 0 and input_str[last_digit_index].isdigit():
            last_digit_index -= 1

        # Find the index of the character before the last 3 numbers
        text_end_index = last_digit_index - 1
        while text_end_index >= 0 and input_str[text_end_index].isalpha():
            text_end_index -= 1

        # Extract and return the text before the last 3 numbers
        return input_str[:text_end_index + 1]

    except Exception as e:
        return str(e)

# Test cases
print(extract_text('Ducati100'))  # Output: Ducati
print(extract_text('Honda125'))   # Output: Honda
print(extract_text('Ducati250'))  # Output: Ducati
print(extract_text('Honda250'))   # Output: Honda
print(extract_text('Honda550'))   # Output: Honda
print(extract_text('Ducati125'))  # Output: Ducati

# End time: 2024-03-30 01:44:52.305029
# Elapsed time in seconds: 6.432663270000376