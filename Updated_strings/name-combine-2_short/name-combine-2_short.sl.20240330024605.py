# Start time: 2024-03-30 02:59:43.138481
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the first input, followed by a space, and then the the first letter of the second input, followed by a period, and given input as ['Nancy', 'FreeHafer'] output is Nancy F., given input as ['Andrew', 'Cencici'] output is Andrew C., given input as ['Jan', 'Kotas'] output is Jan K., given input as ['Mariya', 'Sergienko'] output is Mariya S., , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return the first input, followed by a space, and then the first letter of the second input, followed by a period
# Input: ['Nancy', 'FreeHafer']
# Output: Nancy F.

def process_input(input_data):
    try:
        if len(input_data) != 2:
            raise ValueError("Input should contain exactly two elements")
        
        first_name = input_data[0]
        last_name = input_data[1]
        
        if not isinstance(first_name, str) or not isinstance(last_name, str):
            raise TypeError("Input elements should be strings")
        
        if len(first_name) == 0 or len(last_name) == 0:
            raise ValueError("Input elements should not be empty strings")
        
        return f"{first_name} {last_name[0]}."
    
    except (ValueError, TypeError) as e:
        return str(e)

# Test cases
print(process_input(['Nancy', 'FreeHafer']))  # Output: Nancy F.
print(process_input(['Andrew', 'Cencici']))    # Output: Andrew C.
print(process_input(['Jan', 'Kotas']))         # Output: Jan K.
print(process_input(['Mariya', 'Sergienko']))  # Output: Mariya S.
print(process_input(['John']))                  # Output: Input should contain exactly two elements
print(process_input(['', 'Doe']))               # Output: Input elements should not be empty strings
print(process_input([123, 'Doe']))              # Output: Input elements should be strings

# End time: 2024-03-30 02:59:50.470824
# Elapsed time in seconds: 7.33210829699965