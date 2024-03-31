# Start time: 2024-03-30 00:19:26.292840
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the first input, followed by a space, and then the second input, and given input as ['susan', 'chang'] output is susan chang, given input as ['aaron', 'kim'] output is aaron kim, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return the first input, followed by a space, and then the second input
# Input: ['susan', 'chang']
# Output: susan chang

def combine_inputs(input):
    try:
        if len(input) != 2:
            raise ValueError("Input must contain exactly 2 elements")
        
        return input[0] + " " + input[1]
    
    except ValueError as ve:
        return str(ve)

# Test cases
print(combine_inputs(['susan', 'chang']))  # Output: susan chang
print(combine_inputs(['aaron', 'kim']))    # Output: aaron kim
print(combine_inputs(['john']))            # Output: Input must contain exactly 2 elements
print(combine_inputs(['alice', 'bob', 'charlie']))  # Output: Input must contain exactly 2 elements

# End time: 2024-03-30 00:19:28.374543
# Elapsed time in seconds: 2.081699424999897