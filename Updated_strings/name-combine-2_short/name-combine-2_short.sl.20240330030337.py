# Start time: 2024-03-30 03:17:45.456397
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the first input, followed by a space, and then the the first letter of the second input, followed by a period, and given input as ['Nancy', 'FreeHafer'] output is Nancy F., given input as ['Andrew', 'Cencici'] output is Andrew C., given input as ['Jan', 'Kotas'] output is Jan K., given input as ['Mariya', 'Sergienko'] output is Mariya S., , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return the first input, followed by a space, and then the first letter of the second input, followed by a period
# Input: ['Nancy', 'FreeHafer']
# Output: Nancy F.

def process_input(input_list):
    try:
        if len(input_list) != 2:
            raise ValueError("Input list must contain exactly 2 elements")
        
        first_input = input_list[0]
        second_input = input_list[1]
        
        if not isinstance(first_input, str) or not isinstance(second_input, str):
            raise ValueError("Both inputs must be strings")
        
        if len(first_input) == 0 or len(second_input) == 0:
            raise ValueError("Both inputs must have at least one character")
        
        output = first_input + " " + second_input[0].upper() + "."
        
        return output
    except ValueError as ve:
        return str(ve)

# Test cases
print(process_input(['Nancy', 'FreeHafer']))  # Output: Nancy F.
print(process_input(['Andrew', 'Cencici']))   # Output: Andrew C.
print(process_input(['Jan', 'Kotas']))        # Output: Jan K.
print(process_input(['Mariya', 'Sergienko'])) # Output: Mariya S.

# End time: 2024-03-30 03:17:51.958400
# Elapsed time in seconds: 6.501812164000512