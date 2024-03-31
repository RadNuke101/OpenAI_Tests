# Start time: 2024-03-30 01:29:10.672435
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: remove the last word/phrase from input, and given input as ['india china japan'] output is india china, given input as ['indonesia korea'] output is indonesia, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: remove the last word/phrase from input
# Input: ['india china japan']
# Output: india china

def remove_last_word(input_str):
    try:
        # Split the input string into words
        words = input_str.split()
        
        # Remove the last word
        output_str = ' '.join(words[:-1])
        
        return output_str
    except:
        return "Invalid input"

# Test cases
print(remove_last_word('india china japan'))  # Output: india china
print(remove_last_word('indonesia korea'))     # Output: indonesia
print(remove_last_word('hello world'))         # Output: hello
print(remove_last_word('one'))                 # Output: 

# Additional test cases with invalid input
print(remove_last_word(123))                    # Output: Invalid input
print(remove_last_word(['apple', 'banana']))    # Output: Invalid input

# End time: 2024-03-30 01:29:14.043301
# Elapsed time in seconds: 3.370819819000644