# Start time: 2024-03-30 00:06:27.711426
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: take the first letter of the first input and add it to the front of the second input, then add "_" to the end, and then add the third input to the end, and given input as ['ayako', 'ogawa', 'acme.com'] output is aogawa_acme.com, given input as ['amy', 'johnson', 'google.com'] output is ajohnson_google.com, given input as ['tom', 'chang', 'upenn.edu'] output is tchang_upenn.edu, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: take the first letter of the first input and add it to the front of the second input, then add "_" to the end, and then add the third input to the end
# Input: ['ayako', 'ogawa', 'acme.com']
# Output: aogawa_acme.com

def process_input(inputs):
    try:
        if len(inputs) != 3:
            raise ValueError("Input should contain exactly 3 elements")
        
        first_letter = inputs[0][0]
        second_input = inputs[1]
        third_input = inputs[2]
        
        result = first_letter + second_input + "_" + third_input
        return result
    except Exception as e:
        return str(e)

# Test cases
print(process_input(['ayako', 'ogawa', 'acme.com']))  # Output: aogawa_acme.com
print(process_input(['amy', 'johnson', 'google.com']))  # Output: ajohnson_google.com
print(process_input(['tom', 'chang', 'upenn.edu']))  # Output: tchang_upenn.edu

# End time: 2024-03-30 00:06:30.579797
# Elapsed time in seconds: 2.8682932680003432