# Start time: 2024-03-30 04:09:09.321101
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the first input, followed by a space, and then the the first letter of the second input, followed by a period, and given input as ['Nancy', 'FreeHafer'] output is Nancy F., given input as ['Andrew', 'Cencici'] output is Andrew C., given input as ['Jan', 'Kotas'] output is Jan K., given input as ['Mariya', 'Sergienko'] output is Mariya S., , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return the first input, followed by a space, and then the first letter of the second input, followed by a period
# Input: ['Nancy', 'FreeHafer']
# Output: Nancy F.

def process_input(input_list):
    try:
        if len(input_list) != 2:
            raise ValueError("Input list must contain exactly 2 elements")
        
        first_input = str(input_list[0])
        second_input = str(input_list[1])
        
        if len(first_input) == 0 or len(second_input) == 0:
            raise ValueError("Input strings cannot be empty")
        
        output = first_input + " " + second_input[0].upper() + "."
        
        return output
    except (ValueError, TypeError) as e:
        return str(e)

# Test cases
print(process_input(['Nancy', 'FreeHafer']))  # Output: Nancy F.
print(process_input(['Andrew', 'Cencici']))    # Output: Andrew C.
print(process_input(['Jan', 'Kotas']))         # Output: Jan K.
print(process_input(['Mariya', 'Sergienko']))  # Output: Mariya S.
print(process_input(['John']))                 # Output: Input list must contain exactly 2 elements
print(process_input([]))                        # Output: Input list must contain exactly 2 elements
print(process_input(['', 'Surname']))           # Output: Input strings cannot be empty

# End time: 2024-03-30 04:09:11.828867
# Elapsed time in seconds: 2.5077075799999875