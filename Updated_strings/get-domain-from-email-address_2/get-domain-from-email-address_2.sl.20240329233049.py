# Start time: 2024-03-29 23:43:12.728596
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return everything before the "_" in the second input, and given input as ['ann chang', 'achang_maaker.com'] output is achang, given input as ['bobby smith', 'bobt_sphynx.uk.co'] output is bobt, given input as ['art lennox', 'art.lennox_svxn.com'] output is art.lennox, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return everything before the "_" in the second input
# Input: ['ann chang', 'achang_maaker.com']
# Output: achang

def extract_before_underscore(input_data):
    try:
        # Extract the second input from the list
        second_input = input_data[1]
        
        # Find the index of the underscore
        underscore_index = second_input.index('_')
        
        # Extract the substring before the underscore
        result = second_input[:underscore_index]
        
        return result
    except (IndexError, ValueError):
        return "Invalid input format"

# Test cases
print(extract_before_underscore(['ann chang', 'achang_maaker.com']))  # Output: achang
print(extract_before_underscore(['bobby smith', 'bobt_sphynx.uk.co']))  # Output: bobt
print(extract_before_underscore(['art lennox', 'art.lennox_svxn.com']))  # Output: art.lennox

# End time: 2024-03-29 23:43:15.299059
# Elapsed time in seconds: 2.5703880290000143