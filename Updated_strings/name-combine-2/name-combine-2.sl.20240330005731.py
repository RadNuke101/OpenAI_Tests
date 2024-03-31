# Start time: 2024-03-30 01:09:57.644077
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the first input, followed by a space, and then the the first letter of the second input, followed by a period, and given input as ['Nancy', 'FreeHafer'] output is Nancy F., given input as ['Andrew', 'Cencici'] output is Andrew C., given input as ['Jan', 'Kotas'] output is Jan K., given input as ['Mariya', 'Sergienko'] output is Mariya S., , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return the first input, followed by a space, and then the first letter of the second input, followed by a period
# Input: ['Nancy', 'FreeHafer'] 
# Output: Nancy F.

def format_names(input_list):
    try:
        first_name = str(input_list[0])
        last_name = str(input_list[1])
        
        if len(last_name) > 0:
            formatted_name = first_name + ' ' + last_name[0].upper() + '.'
            return formatted_name
        else:
            return "Invalid input: Last name cannot be empty."
    except IndexError:
        return "Invalid input: Input list must contain at least two elements."

# Test cases
print(format_names(['Nancy', 'FreeHafer']))  # Output: Nancy F.
print(format_names(['Andrew', 'Cencici']))    # Output: Andrew C.
print(format_names(['Jan', 'Kotas']))         # Output: Jan K.
print(format_names(['Mariya', 'Sergienko']))  # Output: Mariya S.

# End time: 2024-03-30 01:10:01.123553
# Elapsed time in seconds: 3.4793860459994903