# Start time: 2024-03-30 03:31:46.316989
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return everything after the last ".' in the inputted expression, and given input as ['www.domain.com'] output is com, given input as ['mail.net'] output is net, given input as ['www.amaon.co.uk'] output is uk, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return everything after the last '.' in the inputted expression
# Input: 'www.domain.com', Output: 'com'
# Input: 'mail.net', Output: 'net'
# Input: 'www.amaon.co.uk', Output: 'uk'

def get_last_extension(input_str):
    try:
        # Split the input string by '.'
        parts = input_str.split('.')
        
        # Get the last part after the last '.'
        last_extension = parts[-1]
        
        return last_extension
    except:
        return "Invalid input"

# Test cases
print(get_last_extension('www.domain.com'))  # Output: com
print(get_last_extension('mail.net'))  # Output: net
print(get_last_extension('www.amaon.co.uk'))  # Output: uk

# End time: 2024-03-30 03:31:48.444219
# Elapsed time in seconds: 2.1271725360002165