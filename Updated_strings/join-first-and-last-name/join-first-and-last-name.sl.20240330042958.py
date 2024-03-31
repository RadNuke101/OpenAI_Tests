# Start time: 2024-03-30 04:44:19.823992
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the first input, followed by a space, and then the second input, and given input as ['susan', 'chang'] output is susan chang, given input as ['aaron', 'kim'] output is aaron kim, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return the first input, followed by a space, and then the second input
# Input: ['susan', 'chang'] 
# Output: susan chang

def combine_names(input):
    try:
        if len(input) != 2:
            raise ValueError("Input must contain exactly 2 elements")
        
        return input[0] + " " + input[1]
    
    except Exception as e:
        return "Error: " + str(e)

# Test cases
print(combine_names(['susan', 'chang']))  # Output: susan chang
print(combine_names(['aaron', 'kim']))    # Output: aaron kim
print(combine_names(['john']))             # Output: Error: Input must contain exactly 2 elements
print(combine_names(['alice', 'bob', 'charlie']))  # Output: Error: Input must contain exactly 2 elements
print(combine_names('invalid input'))      # Output: Error: 'str' object is not subscriptable

# End time: 2024-03-30 04:44:26.874005
# Elapsed time in seconds: 7.049997032998363