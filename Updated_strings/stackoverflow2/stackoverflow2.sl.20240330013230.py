# Start time: 2024-03-30 01:48:00.160499
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: remove the last word/phrase from input, and given input as ['india china japan'] output is india china, given input as ['indonesia korea'] output is indonesia, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: remove the last word/phrase from input
# Input: 'india china japan'
# Output: 'india china'

# Input: 'indonesia korea'
# Output: 'indonesia'

def remove_last_word(input_str):
    try:
        # Split the input string into words
        words = input_str.split()
        
        # Remove the last word
        words.pop()
        
        # Join the remaining words back into a string
        output_str = ' '.join(words)
        
        return output_str
    except:
        return "Invalid input"

# Test cases
print(remove_last_word('india china japan'))  # Output: india china
print(remove_last_word('indonesia korea'))     # Output: indonesia

# End time: 2024-03-30 01:48:05.343598
# Elapsed time in seconds: 5.183014962000016