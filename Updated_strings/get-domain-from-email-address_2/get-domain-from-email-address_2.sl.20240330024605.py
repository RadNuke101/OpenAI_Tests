# Start time: 2024-03-30 02:58:22.258939
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return everything before the "_" in the second input, and given input as ['ann chang', 'achang_maaker.com'] output is achang, given input as ['bobby smith', 'bobt_sphynx.uk.co'] output is bobt, given input as ['art lennox', 'art.lennox_svxn.com'] output is art.lennox, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return everything before the "_" in the second input
# Input: ['ann chang', 'achang_maaker.com']
# Output: achang

def extract_text(input_data):
    try:
        # Extracting the second input from the list
        second_input = input_data[1]
        
        # Finding the index of the underscore
        underscore_index = second_input.index('_')
        
        # Extracting the text before the underscore
        result = second_input[:underscore_index]
        
        return result
    except (IndexError, ValueError):
        return "Invalid input format"

# Test cases
print(extract_text(['ann chang', 'achang_maaker.com']))  # Output: achang
print(extract_text(['bobby smith', 'bobt_sphynx.uk.co']))  # Output: bobt
print(extract_text(['art lennox', 'art.lennox_svxn.com']))  # Output: art.lennox

# End time: 2024-03-30 02:58:25.216300
# Elapsed time in seconds: 2.9572567969989905