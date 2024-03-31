# Start time: 2024-03-30 01:34:10.034910
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: take the first letter of the first input and add it to the front of the second input, then add "_" to the end, and then add the third input to the end, and given input as ['ayako', 'ogawa', 'acme.com'] output is aogawa_acme.com, given input as ['amy', 'johnson', 'google.com'] output is ajohnson_google.com, given input as ['tom', 'chang', 'upenn.edu'] output is tchang_upenn.edu, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: take the first letter of the first input and add it to the front of the second input, then add "_" to the end, and then add the third input to the end

def process_input(input_list):
    try:
        if len(input_list) != 3:
            raise ValueError("Input list must contain exactly 3 elements")
        
        first_letter = input_list[0][0]
        second_input = input_list[1]
        third_input = input_list[2]
        
        output = first_letter + second_input + "_" + third_input
        return output
    except IndexError:
        print("Input list must contain exactly 3 elements")
    except Exception as e:
        print("An error occurred:", e)

# Test cases
print(process_input(['ayako', 'ogawa', 'acme.com']))  # Output: aogawa_acme.com
print(process_input(['amy', 'johnson', 'google.com']))  # Output: ajohnson_google.com
print(process_input(['tom', 'chang', 'upenn.edu']))  # Output: tchang_upenn.edu

# End time: 2024-03-30 01:34:13.117143
# Elapsed time in seconds: 3.0821773260004193