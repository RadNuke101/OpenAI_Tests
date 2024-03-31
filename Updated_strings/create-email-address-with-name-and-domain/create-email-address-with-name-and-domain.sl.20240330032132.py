# Start time: 2024-03-30 03:22:57.673243
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: take the first letter of the first input and add it to the front of the second input, then add "_" to the end, and then add the third input to the end, and given input as ['ayako', 'ogawa', 'acme.com'] output is aogawa_acme.com, given input as ['amy', 'johnson', 'google.com'] output is ajohnson_google.com, given input as ['tom', 'chang', 'upenn.edu'] output is tchang_upenn.edu, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
def manipulate_inputs(input_str):
    try:
        # Prompt: take the first letter of the first input and add it to the front of the second input, then add "_" to the end, and then add the third input to the end
        input_list = input_str.split(',')
        first_input = input_list[0].strip()
        second_input = input_list[1].strip()
        third_input = input_list[2].strip()

        output = first_input[0] + second_input + '_' + third_input
        return output
    except Exception as e:
        return str(e)

# Input: ['ayako', 'ogawa', 'acme.com']
# Output: aogawa_acme.com
print(manipulate_inputs('ayako, ogawa, acme.com'))

# Input: ['amy', 'johnson', 'google.com']
# Output: ajohnson_google.com
print(manipulate_inputs('amy, johnson, google.com'))

# Input: ['tom', 'chang', 'upenn.edu']
# Output: tchang_upenn.edu
print(manipulate_inputs('tom, chang, upenn.edu'))

# End time: 2024-03-30 03:23:00.708165
# Elapsed time in seconds: 3.034820803000912