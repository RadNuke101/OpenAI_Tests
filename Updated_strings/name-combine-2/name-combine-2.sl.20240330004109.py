# Start time: 2024-03-30 00:52:39.600626
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the first input, followed by a space, and then the the first letter of the second input, followed by a period, and given input as ['Nancy', 'FreeHafer'] output is Nancy F., given input as ['Andrew', 'Cencici'] output is Andrew C., given input as ['Jan', 'Kotas'] output is Jan K., given input as ['Mariya', 'Sergienko'] output is Mariya S., , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return the first input, followed by a space, and then the the first letter of the second input, followed by a period
# Input: ['Nancy', 'FreeHafer']
# Output: Nancy F.

def process_input(input_data):
    try:
        if len(input_data) != 2:
            raise ValueError("Input should contain exactly two elements")
        
        first_name = input_data[0]
        last_name = input_data[1]
        
        if not isinstance(first_name, str) or not isinstance(last_name, str):
            raise ValueError("Input elements should be strings")
        
        if len(first_name) == 0 or len(last_name) == 0:
            raise ValueError("Input strings should not be empty")
        
        return f"{first_name} {last_name[0]}."
    
    except ValueError as ve:
        return str(ve)

# Test cases
print(process_input(['Nancy', 'FreeHafer']))  # Output: Nancy F.
print(process_input(['Andrew', 'Cencici']))    # Output: Andrew C.
print(process_input(['Jan', 'Kotas']))         # Output: Jan K.
print(process_input(['Mariya', 'Sergienko']))  # Output: Mariya S.

# End time: 2024-03-30 00:52:43.286609
# Elapsed time in seconds: 3.68589364699983