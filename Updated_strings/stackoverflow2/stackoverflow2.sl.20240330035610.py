# Start time: 2024-03-30 04:09:11.918412
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: remove the last word/phrase from input, and given input as ['india china japan'] output is india china, given input as ['indonesia korea'] output is indonesia, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: remove the last word/phrase from input
# Input: ['india china japan']
# Output: india china

def remove_last_word(input_str):
    try:
        input_str = input_str.strip()  # Remove any leading or trailing whitespaces
        words = input_str.split()  # Split the input string into words
        
        if len(words) > 1:
            output_str = ' '.join(words[:-1])  # Join all words except the last one
        else:
            output_str = input_str  # If only one word, return the input as it is
        
        return output_str
    except Exception as e:
        return str(e)

# Test cases
print(remove_last_word('india china japan'))  # Output: india china
print(remove_last_word('indonesia korea'))  # Output: indonesia
print(remove_last_word('hello'))  # Output: hello
print(remove_last_word(''))  # Output: 

# End time: 2024-03-30 04:09:14.696268
# Elapsed time in seconds: 2.777791682998213