# Start time: 2024-03-29 23:57:42.191644
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the text before the last 3 numbers in inputted expression, and given input as ['Ducati100'] output is Ducati, given input as ['Honda125'] output is Honda, given input as ['Ducati250'] output is Ducati, given input as ['Honda250'] output is Honda, given input as ['Honda550'] output is Honda, given input as ['Ducati125'] output is Ducati, given input as ['Acura100'] output is Acura, given input as ['Acura125'] output is Acura, given input as ['Ferrari250'] output is Ferrari, given input as ['Ferrari250'] output is Ferrari, given input as ['Honda550'] output is Honda, given input as ['Ducati125'] output is Ducati, given input as ['Ducati100'] output is Ducati, given input as ['Honda125'] output is Honda, given input as ['Ducati250'] output is Ducati, given input as ['Honda250'] output is Honda, given input as ['Honda550'] output is Honda, given input as ['Ducati125'] output is Ducati, given input as ['Acura100'] output is Acura, given input as ['Acura125'] output is Acura, given input as ['Ferrari250'] output is Ferrari, given input as ['Ferrari250'] output is Ferrari, given input as ['Honda550'] output is Honda, given input as ['Ducati125'] output is Ducati, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return the text before the last 3 numbers in inputted expression
# Input: 'Ducati100', Output: 'Ducati'
# Input: 'Honda125', Output: 'Honda'
# Input: 'Ducati250', Output: 'Ducati'
# Input: 'Honda250', Output: 'Honda'
# Input: 'Honda550', Output: 'Honda'
# Input: 'Ducati125', Output: 'Ducati'
# Input: 'Acura100', Output: 'Acura'
# Input: 'Acura125', Output: 'Acura'
# Input: 'Ferrari250', Output: 'Ferrari'

def get_text_before_last_3_numbers(input_str):
    try:
        if input_str[-3:].isdigit():
            for i in range(len(input_str)-1, -1, -1):
                if not input_str[i].isdigit():
                    return input_str[:i+1]
        else:
            raise ValueError("Input does not end with 3 numbers")
    except ValueError as e:
        return str(e)

# Test cases
print(get_text_before_last_3_numbers('Ducati100'))  # Output: Ducati
print(get_text_before_last_3_numbers('Honda125'))  # Output: Honda
print(get_text_before_last_3_numbers('Ducati250'))  # Output: Ducati
print(get_text_before_last_3_numbers('Honda250'))  # Output: Honda
print(get_text_before_last_3_numbers('Honda550'))  # Output: Honda
print(get_text_before_last_3_numbers('Ducati125'))  # Output: Ducati
print(get_text_before_last_3_numbers('Acura100'))  # Output: Acura
print(get_text_before_last_3_numbers('Acura125'))  # Output: Acura
print(get_text_before_last_3_numbers('Ferrari250'))  # Output: Ferrari

# End time: 2024-03-29 23:57:54.071305
# Elapsed time in seconds: 11.879303228000026