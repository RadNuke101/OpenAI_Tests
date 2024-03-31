# Start time: 2024-03-30 02:55:19.856559
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the numbers from first input, and given input as ['80v', '3'] output is 80, given input as ['10hrs', '3'] output is 10, given input as ['7h', '2'] output is 7, given input as ['500m', '4'] output is 500, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return the numbers from first input
# Input: ['80v', '3']
# Output: 80

def extract_number(input_str):
    try:
        num = ''
        for char in input_str:
            if char.isdigit():
                num += char
            else:
                break
        return int(num)
    except:
        return None

# Test cases
print(extract_number('80v'))  # Output: 80
print(extract_number('10hrs'))  # Output: 10
print(extract_number('7h'))  # Output: 7
print(extract_number('500m'))  # Output: 500

# End time: 2024-03-30 02:55:22.061197
# Elapsed time in seconds: 2.2044358189996274