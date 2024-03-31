# Start time: 2024-03-30 01:52:17.511745
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: take the first letter of the first input and add it to the front of the second input, then add "_" to the end, and then add the third input to the end, and given input as ['ayako', 'ogawa', 'acme.com'] output is aogawa_acme.com, given input as ['amy', 'johnson', 'google.com'] output is ajohnson_google.com, given input as ['tom', 'chang', 'upenn.edu'] output is tchang_upenn.edu, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: take the first letter of the first input and add it to the front of the second input, then add "_" to the end, and then add the third input to the end
# Input: ['ayako', 'ogawa', 'acme.com']
# Output: aogawa_acme.com

# Input: ['amy', 'johnson', 'google.com']
# Output: ajohnson_google.com

# Input: ['tom', 'chang', 'upenn.edu']
# Output: tchang_upenn.edu

def combine_inputs(input_list):
    try:
        first_letter = input_list[0][0]
        second_input = input_list[1]
        third_input = input_list[2]
        
        result = first_letter + second_input + "_" + third_input
        return result
    except IndexError:
        print("Input list should contain three elements.")
    except Exception as e:
        print("An error occurred:", e)

# Test cases
print(combine_inputs(['ayako', 'ogawa', 'acme.com']))  # Output: aogawa_acme.com
print(combine_inputs(['amy', 'johnson', 'google.com']))  # Output: ajohnson_google.com
print(combine_inputs(['tom', 'chang', 'upenn.edu']))  # Output: tchang_upenn.edu

# End time: 2024-03-30 01:52:20.494032
# Elapsed time in seconds: 2.982268159999876