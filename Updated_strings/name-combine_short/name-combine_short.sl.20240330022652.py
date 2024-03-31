# Start time: 2024-03-30 02:39:24.537241
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return first input followed by a space, and then the second input, and given input as ['Launa', 'Withers'] output is Launa Withers, given input as ['Lakenya', 'Edison'] output is Lakenya Edison, given input as ['Brendan', 'Hage'] output is Brendan Hage, given input as ['Bradford', 'Lango'] output is Bradford Lango, given input as ['Rudolf', 'Akiyama'] output is Rudolf Akiyama, given input as ['Lara', 'Constable'] output is Lara Constable, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Input: ['Launa', 'Withers']
# Output: Launa Withers
# Prompt: return first input followed by a space, and then the second input

def combine_names(input_list):
    try:
        if len(input_list) != 2:
            raise ValueError("Input list must contain exactly 2 elements")
        
        return input_list[0] + ' ' + input_list[1]
    
    except (TypeError, ValueError, IndexError) as e:
        return "Invalid input"

# Test cases
print(combine_names(['Launa', 'Withers']))  # Output: Launa Withers
print(combine_names(['Lakenya', 'Edison']))  # Output: Lakenya Edison
print(combine_names(['Brendan', 'Hage']))  # Output: Brendan Hage
print(combine_names(['Bradford', 'Lango']))  # Output: Bradford Lango
print(combine_names(['Rudolf', 'Akiyama']))  # Output: Rudolf Akiyama
print(combine_names(['Lara', 'Constable']))  # Output: Lara Constable

# End time: 2024-03-30 02:39:28.705816
# Elapsed time in seconds: 4.168489847999808