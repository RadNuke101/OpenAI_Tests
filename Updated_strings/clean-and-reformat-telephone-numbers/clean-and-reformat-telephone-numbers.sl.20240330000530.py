# Start time: 2024-03-30 00:07:01.302169
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: delete all "-", "<", ">", ".", and any spaces, and given input as ['801-456-8765'] output is 8014568765, given input as ['<978> 654-0299'] output is 9786540299, given input as ['978.654.0299'] output is 9786540299, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: delete all "-", "<", ">", ".", and any spaces
# Input: '801-456-8765'
# Output: 8014568765

def clean_phone_number(input_str):
    try:
        cleaned_str = input_str.replace("-", "").replace("<", "").replace(">", "").replace(".", "").replace(" ", "")
        return cleaned_str
    except AttributeError:
        return "Invalid input format, please provide a string."

# Test cases
print(clean_phone_number('801-456-8765'))  # Output: 8014568765
print(clean_phone_number('<978> 654-0299'))  # Output: 9786540299
print(clean_phone_number('978.654.0299'))  # Output: 9786540299

# End time: 2024-03-30 00:07:03.280548
# Elapsed time in seconds: 1.978324007000083