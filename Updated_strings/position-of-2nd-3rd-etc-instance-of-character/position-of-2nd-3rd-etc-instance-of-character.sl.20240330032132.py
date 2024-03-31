# Start time: 2024-03-30 03:35:09.827685
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the position of the first and third instance of the second input in the first input, and given input as ['100x15x50', 'x', '2'] output is 7, given input as ['cat-in-the-hat', '-', '3'] output is 11, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return the position of the first and third instance of the second input in the first input
# Input: '100x15x50', 'x', '2' 
# Output: 7
# Input: 'cat-in-the-hat', '-', '3'
# Output: 11

def find_positions(input_str, target_char, occurrence):
    try:
        first_index = input_str.index(target_char)
        second_index = input_str.index(target_char, first_index + 1)
        third_index = input_str.index(target_char, second_index + 1)
        
        if occurrence == '1':
            return first_index
        elif occurrence == '2':
            return second_index
        elif occurrence == '3':
            return third_index
        else:
            return -1
    except ValueError:
        return -1

# Test cases
print(find_positions('100x15x50', 'x', '2'))  # Output: 7
print(find_positions('cat-in-the-hat', '-', '3'))  # Output: 11

# End time: 2024-03-30 03:35:13.005062
# Elapsed time in seconds: 3.177298308999525