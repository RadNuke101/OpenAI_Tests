# Start time: 2024-03-30 04:08:26.404042
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: remove second input from first input, and given input as ['zx66448', 'z'] output is x66448, given input as ['zx66448', 'x'] output is z66448, given input as ['zx66448', '6'] output is zx448, given input as ['zx66448', '4'] output is zx668, given input as ['zx66448', '8'] output is zx6644, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: remove second input from first input
# Input: ['zx66448', 'z']
# Output: x66448

def remove_second_input(input_str, char):
    try:
        input_str = str(input_str)
        char = str(char)
        
        if len(char) != 1:
            raise ValueError("Second input must be a single character")
        
        output = input_str.replace(char, "", 1)
        
        return output
    
    except Exception as e:
        return str(e)

# Test cases
print(remove_second_input('zx66448', 'z'))  # Output: x66448
print(remove_second_input('zx66448', 'x'))  # Output: z66448
print(remove_second_input('zx66448', '6'))  # Output: zx448
print(remove_second_input('zx66448', '4'))  # Output: zx668
print(remove_second_input('zx66448', '8'))  # Output: zx6644

# End time: 2024-03-30 04:08:29.559649
# Elapsed time in seconds: 3.155539458999556